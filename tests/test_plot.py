import pytest
from src.sphecial_harmonic_plotter_tayra import plot


def test_plotter_type():
    plot(3)
    assert True