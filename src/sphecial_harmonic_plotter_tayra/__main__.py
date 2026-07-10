"""Main running module."""
from ._plot import plot
import argparse
from pathlib import Path

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Plots AOs for l."
    )
    parser.add_argument(
        'l',
        nargs='?',
        type=int,
        help='The azimuthal quantum number.'
    )
    parser.add_argument(
        '--save',
        '-s',
        type=Path,
        required=False,
        default=None,
        help='If you would like to save the image, please set this argument an effective path.'
    )
    ns = parser.parse_args()
    l: int = ns.l if ns.l else int(input('l = '))
    save_to: Path | None = ns.save
    plot(l, save_to)


if __name__ == '__main__':
    main()
