#!/usr/bin/env python3
"""
id-gen CLI tool - A simple ID generator with various options
"""

import argparse
import sys

# Import from the main package
from id_gen import DEFAULT_LENGTH, MIN_LENGTH, create_id_generator, generate_ids


def parse_args() -> tuple[int, int, bool, bool, bool, bool]:
    """
    Parse command line arguments.

    Returns:
        tuple of (length, count, uppercase, special, left_hand, cvcv)
    """
    parser = argparse.ArgumentParser(
        description="Generate random IDs with various options",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "length_or_pattern",
        nargs="?",
        default=str(DEFAULT_LENGTH),
        help=f"Length of IDs to generate (min {MIN_LENGTH})",
    )

    parser.add_argument(
        "-n", "--count", type=int, default=1, help="Number of IDs to generate"
    )

    parser.add_argument(
        "-u", "--uppercase", action="store_true", help="Include uppercase letters"
    )

    parser.add_argument(
        "-s", "--special", action="store_true", help="Include special characters"
    )

    parser.add_argument(
        "-f",
        "--fast",
        action="store_true",
        help="Use only left-hand characters for fast typing",
    )

    args = parser.parse_args()

    # Check if CVCV pattern is requested
    cvcv = args.length_or_pattern.lower() == "cvcv"

    # Determine length
    if cvcv:
        length = 4
    else:
        try:
            length = int(args.length_or_pattern)
        except ValueError:
            print(
                f"Error: '{args.length_or_pattern}' is not a valid length or pattern",
                file=sys.stderr,
            )
            sys.exit(1)

    # Validate length
    if length < MIN_LENGTH and not cvcv:
        print(f"Error: Length must be at least {MIN_LENGTH}", file=sys.stderr)
        sys.exit(1)

    # Check for incompatible options with CVCV
    if cvcv and (args.uppercase or args.special or args.fast):
        print(
            "Error: CVCV pattern cannot be combined with other options", file=sys.stderr
        )
        sys.exit(1)

    return length, args.count, args.uppercase, args.special, args.fast, cvcv


def main():
    """Main entry point for the CLI tool."""
    length, count, uppercase, special, left_hand, cvcv = parse_args()

    generator = create_id_generator(
        include_uppercase=uppercase,
        include_special=special,
        left_hand_only=left_hand,
        cvcv_pattern=cvcv,
    )

    ids = generate_ids(generator, length, count)

    for id_str in ids:
        print(id_str)
        print(f"[id-gen] Generated ID: {id_str}", file=sys.stderr)


if __name__ == "__main__":
    main()
