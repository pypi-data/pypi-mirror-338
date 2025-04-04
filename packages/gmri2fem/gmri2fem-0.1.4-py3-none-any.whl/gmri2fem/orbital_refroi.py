import itertools
from pathlib import Path

import click
import matplotlib.pyplot as plt
import nibabel
import numpy as np
import scipy
import skimage
from scipy.stats import multivariate_normal

from gmri2fem.utils import largest_island


@click.command()
@click.option("--T1w_dir", type=Path, required=True)
@click.option("--segmentation", type=Path, required=True)
@click.option("--output", type=Path, required=True)
@click.option("--side", type=str, default="left")
def orbital_refroi(t1w_dir, segmentation, output, side):
    image_paths = sorted(t1w_dir.glob("*T1w*"))
    vols = [
        nibabel.nifti1.load(path).get_fdata(dtype=np.single) for path in image_paths
    ]
    vols = np.array(vols)
    seg_nii = nibabel.nifti1.load(segmentation)
    seg_data = seg_nii.get_fdata().astype(np.uint16)

    assert seg_data.shape == vols[0].shape

    # LUT-values of regions to look for to find slice in R,A,S-directions respectively
    if side == "left":
        axes_seg_indices = [1012, 1027, 18]
    else:
        axes_seg_indices = [2012, 2027, 54]
    centers = [
        [np.rint(x.mean()).astype(int) for x in np.where(seg_data == label)][idx]
        for idx, label in enumerate(axes_seg_indices)
    ]
    cov_scale = [3, 1.5, 6]
    cov = [
        cov_scale[idx] * [x.var() for x in np.where(seg_data == label)][idx]
        for idx, label in enumerate(axes_seg_indices)
    ]
    G = multivariate_normal(mean=centers, cov=cov)

    pos = np.fromiter(
        itertools.product(
            *(
                np.arange(ci - 3 * np.sqrt(di), ci + 3 * np.sqrt(di))
                for ci, di in zip(centers, cov)
            )
        ),
        dtype=np.dtype((int, 3)),
    )
    I, J, K = pos.T

    binary = np.ones(vols[0].shape, dtype=bool)
    image = np.zeros_like(vols[0])
    for idx, vol in enumerate(vols):
        image[I, J, K] = vol[I, J, K] * G.pdf(pos)
        thresh = skimage.filters.threshold_otsu(image)
        binary *= image > thresh

    binary = skimage.morphology.binary_erosion(
        binary, footprint=skimage.morphology.ball(3)
    )
    binary = largest_island(binary)
    temporal_std = (
        vols[:, binary] / np.median(vols[:, binary], axis=1, keepdims=1)
    ).std(axis=0)
    binary[binary] = (
        np.abs(vols[0, binary] / np.median(vols[0, binary]) - 1) < 0.25
    ) * (temporal_std < 0.1)
    refroi_nii = nibabel.nifti1.Nifti1Image(
        binary.astype(np.uint8),
        affine=seg_nii.affine,
    )
    nibabel.nifti1.save(refroi_nii, output)


if __name__ == "__main__":
    orbital_refroi()
