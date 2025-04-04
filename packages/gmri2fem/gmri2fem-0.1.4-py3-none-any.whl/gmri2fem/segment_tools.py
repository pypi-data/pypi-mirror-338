import contextlib
import dataclasses
import itertools
import json
import os
import re
from pathlib import Path
from typing import Optional

import click
import matplotlib as mpl
import numpy as np
import pandas as pd
import scipy
import skimage
import tqdm
from simple_mri import SimpleMRI, load_mri, save_mri


def inverse_dict(index):
    inverse = {}
    for k, v in index.items():
        for x in list(v):
            inverse.setdefault(x, []).append(k)
    return inverse


@contextlib.contextmanager
def temp_seed(seed):
    state = np.random.get_state()
    np.random.seed(seed)
    try:
        yield
    finally:
        np.random.set_state(state)


def canonical_lut(
    segments: list[str], cmap: str, permute_colors: Optional[int] = None
) -> pd.DataFrame:
    n_segments = len(segments)
    colormap = mpl.colormaps[cmap]

    # Zero is added manually below
    color_list = colormap([(i + 1) / n_segments for i in range(n_segments)])

    if permute_colors is not None:
        with temp_seed(permute_colors):
            np.random.shuffle(color_list)
    records = [
        {
            "label": idx + 1,
            "description": desc,
            **{"RGBA"[i]: val for i, val in enumerate(color_list[idx])},
        }
        for idx, desc in enumerate(segments)
    ] + [{"label": 0, "description": "unknown", "R": 0, "G": 0, "B": 0, "A": 0}]
    return pd.DataFrame.from_records(sorted(records, key=lambda x: x["label"]))


def listed_colormap(lut_table: pd.DataFrame) -> mpl.colors.ListedColormap:
    # Norm need sorted labels
    sorted_table = lut_table.sort_values("label").reset_index(drop=True)
    colors = sorted_table[["R", "G", "B", "A"]].values
    labels = sorted_table["label"].values
    norm = mpl.colors.BoundaryNorm(
        boundaries=list(labels) + [labels[-1] + 1], ncolors=len(colors), clip=False
    )
    return {"cmap": mpl.colors.ListedColormap(colors), "norm": norm}


def write_lut(filename: Path | str, table: pd.DataFrame):
    newtable = table.copy()
    for col in "RGBA":
        newtable[col] = (newtable[col] * 255).astype(int)
    newtable.to_csv(filename, sep="\t", index=False, header=False)


def lut_record(match: re.Match) -> dict[str, str | float]:
    groupdict = match.groupdict()
    return {
        "label": int(groupdict["label"]),
        "description": groupdict["description"],
        "R": float(groupdict["R"]) / 255,
        "G": float(groupdict["G"]) / 255,
        "B": float(groupdict["B"]) / 255,
        "A": 1.0 - float(groupdict["A"]) / 255,
    }


def read_lut(filename: Path | str | None) -> pd.DataFrame:
    if filename is None:
        filename = Path(os.environ["FREESURFER_HOME"]) / "FreeSurferColorLUT.txt"
    lut_regex = re.compile(
        r"^(?P<label>\d+)\s+(?P<description>[_\da-zA-Z-]+)\s+(?P<R>\d+)\s+(?P<G>\d+)\s+(?P<B>\d+)\s+(?P<A>\d+)"
    )
    with open(filename, "r") as f:
        records = [lut_record(m) for m in map(lut_regex.match, f) if m is not None]
    return pd.DataFrame.from_records(records)


def write_relabeling(
    filename: Path | str, relabeling: dict[str, list[int]], indent: int = 2
):
    json_object = json.dumps(relabeling, indent=indent)
    with open(filename, "w") as outfile:
        outfile.write(json_object)


def read_relabeling(filename: Path | str) -> dict[str, list[int]]:
    with open(filename, "r") as openfile:
        json_object = json.load(openfile)
    return json_object


def collapse_segmentation(
    input: Path,
    output: Path,
    relabeling: dict[str, list[int]],
    cmap: Optional[str] = None,
):
    if cmap is None:
        cmap = "gist_ncar"
    aseg_mri = load_mri(input, dtype=np.int16)
    aseg = aseg_mri.data
    newseg = collapse(aseg, relabeling)
    new_mri = SimpleMRI(newseg, aseg_mri.affine)
    save_mri(new_mri, output, dtype=np.int16)
    lutname = Path(output).parent / f"{Path(output).name.split('.')[0]}_LUT.txt"
    write_lut(lutname, canonical_lut(list(relabeling), cmap))


def assert_valid_relabeling(relabeling: dict[str, list[int]]):
    inverse = inverse_dict(relabeling)
    for label, description in inverse.items():
        if len(description) != 1:
            raise ValueError(
                f"Entry {label} found in multiple descriptions {description}."
            )


def collapse(seg: np.ndarray, relabeling: dict[str, list[int]]) -> np.ndarray:
    assert_valid_relabeling(relabeling)
    newseg = np.zeros_like(seg)
    for new_label, old_labels in enumerate(relabeling.values(), start=1):
        segment_mask = np.isin(seg, old_labels)
        newseg[segment_mask] = new_label
    return newseg


def inclusions(seg: np.ndarray, old: int, new: int) -> np.ndarray:
    np.where(old)
    return seg


@click.command(name="collapse")
@click.option("--input", type=Path, required=True)
@click.option("--output", type=Path, required=True)
@click.option("--relabeling", type=Path, required=True)
@click.option("--cmap", type=str)
def collapse_segmentation_cli(*a, **kw):
    collapse_segmentation(*a, **kw)


if __name__ == "__main__":
    collapse_segmentation_cli()
