#! /usr/bin/env python3
"""
A script to verify the calculations for bric.stairs.total_run.
"""

import argparse

import bricoleur as bric


def main():
    parser = argparse.ArgumentParser(description="total run")
    parser.add_argument(
        "-nr",
        "--number_risers",
        default=14,
        type=int,
        required=False,
        help="Provide the number of risers",
    )
    parser.add_argument(
        "-td",
        "--tread_depth",
        default=11,
        type=float,
        required=False,
        help="Provide the tread depth",
    )
    args = parser.parse_args()
    total_run = bric.total_run(
        number_risers = args.number_risers,
        tread_depth = args.tread_depth
    )
    print(total_run)


if __name__ == "__main__":
    main()
