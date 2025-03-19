"""
id-gen - A simple ID generator with various options.

This package provides functions for generating random IDs with various options:
- Basic IDs (lowercase letters and numbers)
- IDs with uppercase letters
- IDs with special characters
- IDs with left-hand-only characters for fast typing
- IDs with consonant-vowel-consonant-vowel pattern

The package can be used as a library or as a command-line tool.
"""

__version__ = "0.1.1"

import random
from functools import partial, reduce
from itertools import cycle
from typing import Callable

# Constants
MIN_LENGTH = 5
DEFAULT_LENGTH = 5
CONSONANTS = "bcdfghjklmnpqrstvwyz"
VOWELS = "aeiou"
LEFT_HAND_CHARS = "1234qwerasdfcv!@#$QWERASDFCV"
ASCII = "abcdefghijklmnopqrstuvwyz"
DIGITS = "0123456789"
PUNCTUATION = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""

# Type aliases
CharacterPool = str
Generator = Callable[[int], str]


def compose(*functions):
    """Compose multiple functions from right to left."""
    return reduce(lambda f, g: lambda x: f(g(x)), functions)


def get_char_pool(
    include_uppercase: bool = False,
    include_special: bool = False,
    left_hand_only: bool = False,
) -> CharacterPool:
    """
    Get the character pool based on options.

    Args:
        include_uppercase: Whether to include uppercase letters
        include_special: Whether to include special characters
        left_hand_only: Whether to use only left-hand characters

    Returns:
        Character pool as a string
    """
    chars = ASCII + DIGITS

    if include_uppercase:
        chars += ASCII.upper()

    if include_special:
        chars += PUNCTUATION

    if left_hand_only:
        chars = "".join(filter(lambda c: c in LEFT_HAND_CHARS, chars))

    return chars


def ensure_first_letter_alpha(id_str: str, char_pool: CharacterPool) -> str:
    """Ensure the first character is a letter."""
    if not id_str[0].isalpha():
        chars = list(id_str)
        # Replace first char with a random letter
        chars[0] = random.choice("".join(filter(lambda c: c.isalpha(), char_pool)))
        return "".join(chars)
    return id_str


def ensure_has_digit(id_str: str, char_pool: CharacterPool) -> str:
    """Ensure the ID contains at least one digit."""
    if not any(c.isdigit() for c in id_str):
        # Replace a random character (not the first) with a digit
        chars = list(id_str)
        pos = random.randint(1, len(chars) - 1)
        chars[pos] = random.choice("".join(filter(lambda c: c.isdigit(), char_pool)))
        return "".join(chars)
    return id_str


def generate_random_id(length: int, char_pool: CharacterPool) -> str:
    """
    Generate a random ID from the given character pool.

    Args:
        length: Length of the ID to generate
        char_pool: set of characters to use

    Returns:
        Generated ID
    """
    return "".join(random.choice(list(char_pool)) for _ in range(length))


def generate_cvcv_id(length: int) -> str:
    """
    Generate an ID with consonant-vowel-consonant-vowel pattern.

    Args:
        length: Length of the ID to generate

    Returns:
        Generated CVCV ID
    """
    pattern = cycle([CONSONANTS, VOWELS])
    return "".join(random.choice(next(pattern)) for _ in range(length))


def create_id_generator(
    include_uppercase: bool = False,
    include_special: bool = False,
    left_hand_only: bool = False,
    cvcv_pattern: bool = False,
) -> Generator:
    """
    Create an ID generator function based on options.

    Args:
        include_uppercase: Whether to include uppercase letters
        include_special: Whether to include special characters
        left_hand_only: Whether to use only left-hand characters
        cvcv_pattern: Whether to use CVCV pattern

    Returns:
        A function that generates IDs of specified length
    """
    if cvcv_pattern:
        return generate_cvcv_id

    char_pool = get_char_pool(include_uppercase, include_special, left_hand_only)
    base_generator = partial(generate_random_id, char_pool=char_pool)

    # Define constraints to be applied to the generated IDs
    constraints = [
        ensure_first_letter_alpha,
        ensure_has_digit,
    ]
    constraints = [partial(f, char_pool=char_pool) for f in constraints]

    # Compose transformations to ensure constraints are met
    return compose(*constraints, base_generator)


def generate_ids(generator: Generator, length: int, count: int) -> list[str]:
    """
    Generate multiple IDs using the provided generator.

    Args:
        generator: ID generator function
        length: Length of each ID
        count: Number of IDs to generate

    Returns:
        list of generated IDs
    """
    return [generator(length) for _ in range(count)]


# Convenience functions for common use cases
def generate_basic_id(length: int) -> str:
    """Generate a basic ID with lowercase letters and numbers."""
    generator = create_id_generator()
    return generator(length)


def generate_complex_id(
    length: int, uppercase: bool = True, special_chars: bool = True
) -> str:
    """Generate a complex ID with uppercase and special characters."""
    generator = create_id_generator(
        include_uppercase=uppercase, include_special=special_chars
    )
    return generator(length)


def generate_fast_typing_id(length: int) -> str:
    """Generate an ID optimized for fast typing with left hand."""
    generator = create_id_generator(left_hand_only=True)
    return generator(length)


def generate_multiple_ids(
    length: int,
    count: int,
    uppercase: bool = False,
    special_chars: bool = False,
    left_hand_only: bool = False,
    cvcv_pattern: bool = False,
) -> list[str]:
    """Generate multiple IDs with the specified options."""
    generator = create_id_generator(
        include_uppercase=uppercase,
        include_special=special_chars,
        left_hand_only=left_hand_only,
        cvcv_pattern=cvcv_pattern,
    )
    return generate_ids(generator, length, count)
