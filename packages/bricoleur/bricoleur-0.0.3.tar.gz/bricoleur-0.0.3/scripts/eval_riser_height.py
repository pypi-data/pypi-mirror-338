#! /usr/bin/env python3
"""
A script to verify the calculations for bric.stairs.riser_height.
"""

import argparse

import bricoleur as bric


def main():
    parser = argparse.ArgumentParser(description="riser height")
    parser.add_argument(
        "-tr",
        "--total_rise",
        default=100,
        type=float,
        required=False,
        help="Provide the total rise",
    )
    parser.add_argument(
        "-nr",
        "--number_risers",
        default=14,
        type=int,
        required=False,
        help="Provide the number of risers",
    )
    args = parser.parse_args()
    riser_height = bric.riser_height(
        total_rise = args.total_rise,
        number_risers = args.number_risers
    )
    print(riser_height)


if __name__ == "__main__":
    main()
