"""Plotting tools."""
import matplotlib.pyplot as plt
from ._calc import *
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from os import PathLike
from typing import Any

type _Array1D[T: np.generic[Any]] = np.ndarray[
    tuple[int],
    np.dtype[T]
]


def plot(
    l: int,
    save_to: str | PathLike[Any] | None = None
) -> None:
    """Plots the sphecial harmonic functions.

    Parameters
    ----------
    l : int
        The azimuthal quantum number
    save_to : StrOrPath, optional
        The function saves the file if this parameter is handled.
    """
    axset: _Array1D[Any]
    (_, axset) = plt.subplots(
        2 * l + 1,
        subplot_kw={
            'projection': '3d',
        }
    )
    pointsset = generate_harmonics_2d(l)
    ax: Axes3D
    for ax, (point_x, point_y, point_z) in zip(axset, pointsset):
        ax.set_aspect('equal', adjustable='box')
        ax.plot_wireframe(point_x, point_y, point_z)
    if save_to is not None:
        plt.savefig(save_to)
    else:
        plt.show()
