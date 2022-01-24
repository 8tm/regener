import argparse
from pathlib import Path


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-p', '--path', action='store', required=True, type=Path,
        help='Path to folder with files (json, images, fonts)',
    )

    parser.add_argument(
        '-o', '--output', action='store', required=False, type=Path,
        help='Path to the pdf file or to directory where that pdf file will be generated',
    )

    return parser.parse_args()
