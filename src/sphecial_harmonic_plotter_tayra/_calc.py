"""Calculates the sphecial harmonic funtions."""
import numpy as np
from scipy.special import sph_harm_y
from typing import Any

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
type _Float3D = np.ndarray[
    tuple[int, int, int],
    np.dtype[np.float64]
]
type _Float2D = _Array2D[np.float64]
type _Int3D = np.ndarray[
    tuple[int, int, int],
    np.dtype[np.integer[Any]]
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
    phi = np.linspace(0, 2 * np.pi, 100)
    m_l = np.arange(-l, l + 1)
    m: _Int3D
    t: _Float3D
    p: _Float3D
    t, m, p = np.meshgrid(theta, m_l, phi)
    print('m_l =', m)
    print('Theta =', t)
    print('Phi =', p)
    harms: _Complex3D = sph_harm_y(l, m, t, p)
    points: list[
        _Coord
    ] = []
    t2: _Float2D
    p2: _Float2D
    p2, t2 = np.meshgrid(phi, theta)
    print('Theta =', t2)
    print('Phi =', p2)
    x_coeff = np.sin(t2) * np.cos(p2)
    y_coeff = np.sin(t2) * np.sin(p2)
    z_coeff = np.cos(t2)
    for i in range(l + 1):
        ps: list[_Coord] = list()
        if i == 0:
            harm_real: _Float2D = harms.real[i + l]
            harm_real **= 2
            x = RADIUS * x_coeff * harm_real
            y = RADIUS * y_coeff * harm_real
            z = RADIUS * z_coeff * harm_real
            point = x, y, z
            ps.append(point)
        else:
            harm_real1: _Complex2D = harms.real[i + l]
            harm_real2: _Complex2D = harms.real[l - i]
            for s in (-1, 1):
                harm_r = (harm_real1 + s * harm_real2) / np.sqrt(2)
                harm_r = harm_r.real
                harm_r **= 2
                x = RADIUS * x_coeff * harm_r
                y = RADIUS * y_coeff * harm_r
                z = RADIUS * z_coeff * harm_r
                ps.append(
                    (
                        x,
                        y,
                        z,
                    )
                )
        points += ps
    return tuple(points)
