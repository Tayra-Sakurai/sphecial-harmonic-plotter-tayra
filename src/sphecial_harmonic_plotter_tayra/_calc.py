"""Calculates the sphecial harmonic funtions."""
import numpy as np
from scipy.special import sph_harm_y
from typing import Any, Iterable

# Constants
RADIUS = 10.0

__all__ = ["generate_harmonics_2d"]

type _Array2D[T: np.number[Any, Any]] = np.ndarray[
    tuple[int, int],
    np.dtype[T]
]
type _Complex3D = np.ndarray[
    tuple[int, int, int],
    np.dtype[np.complex128]
]
type _Complex2D = _Array2D[np.complex128]
type _Coord = tuple[
    _Array2D[np.float64],
    _Array2D[np.float64],
    _Array2D[np.float64]
]


def generate_harmonics_2d(
    l: int
) -> tuple[
    _Coord,
    ...
]:
    """Generates the surface data of the atomic orbitals.

    Parameters
    ----------
    l : int
        The azimuthal quantum number.

    Returns
    -------
    points : Tuple[Coord]
        The coordinates of the surface of the AOs.
    """
    theta = np.linspace(0, np.pi)
    phi = np.linspace(0, 2 * np.pi)
    m_l = np.arange(-l, l + 1)
    harms: _Complex3D = sph_harm_y(l, m_l, theta, phi)
    points: list[
        _Coord
    ] = []
    t_x, p_x = np.meshgrid(
        np.sin(theta),
        np.cos(phi)
    )
    x_coeff = t_x * p_x
    t_y, p_y = np.meshgrid(
        np.sin(theta),
        np.sin(phi)
    )
    y_coeff = t_y * p_y
    for i in range(l + 1):
        fs: Iterable[_Array2D[np.float64]]
        if i == 0:
            harm: _Complex2D = harms[l]
            f = harm.real
            fs = (f,)
        else:
            harm: _Complex2D = (harms[l - i] + harms[l + i]) / np.sqrt(2)
            f1 = harm.real
            harm2: _Complex2D = (harms[l + i] - harms[l - i]) / np.sqrt(2)
            f2 = harm2.real
            fs = f1, f2
        for fval in fs:
            x: _Array2D[
                np.float64
            ] = RADIUS * fval * x_coeff
            y: _Array2D[
                np.float64
            ] = RADIUS * fval * y_coeff
            z: _Array2D[
                np.float64
            ] = RADIUS * fval * np.cos(theta)
            point: _Coord = x, y, z
            points.append(point)
    return tuple(points)
