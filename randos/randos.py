from __future__ import annotations
from random import randint
from linecache import getline

FILE_CITIES = 'data/CITIES.txt'
FILE_CITIES_LINES = 1100

FILE_COUNTRIES = 'data/CITIES.txt'
FILE_COUNTRIES_LINES = 245

FILE_EMOJIS = 'data/EMOJIS.txt'
FILE_EMOJIS_LINES = 806


def random_ints(length: int, minimum: int = 0, maximum: int = 100):
    """Generates a list of random integers

    Args:
        length (int): number of elements in output list
        minimum (int, optional): minimum possible value, inclusive. Defaults to 0.
        maximum (int, optional): maximum possible value, inclusive. Defaults to 100.

    Raises:
        ValueError: If maximum < minimum

    Returns:
        list[int]: list of random int values
    """
    # make sure length is > 0, default to 1 if not
    length = length if length > 0 else 1
    try:
        return [randint(minimum, maximum) for _ in range(length)]
    except ValueError:
        raise ValueError(
            f'maximum ({maximum}) cannot be lower than minimum ({minimum})')


def random_line(file_name: str, separator: str = None, number_of_lines: int = None):
    """Returns a random line from a file

    Args:
        file_name (str): the relative path of the file
        separator (str, optional): Specify to split the line. Defaults to None.
        number_of_lines (int, optional): Number of lines in the file. Defaults to None.

    Raises:
        ValueError: If maximum < minimum

    Returns:
        str or tuple[str,]: a random line's value
    """

    try:
        if not number_of_lines:
            number_of_lines = sum(1 for i in open(file_name, 'rb'))

        random_line_number = randint(1, number_of_lines-1)
        line = getline(file_name, random_line_number).strip()

        return line.split(separator) if separator else line

    except FileNotFoundError:
        FileNotFoundError(f'random_line() file not found: {file_name}')


def random_city(include_country: bool = False):
    """Returns the name of one of world's +1,000 largest cities, randomly.

    Args:
        include_country (bool, optional): Return the country name too. Defaults to False.

    Returns:
        str or tuple[str,str]: random city name
    """
    line = random_line(FILE_CITIES, ',', FILE_CITIES_LINES)
    city, country = line
    return (city, country) if include_country else city


def random_country(include_abbr: bool = False):
    """Returns the name of a randomly-selected country (reference: UN).

    Args:
        include_abbr (bool, optional): Return the country's abbreviation too. Defaults to False.

    Returns:
        str or tuple[str,str]: random country name
    """
    country, abbr = random_line(FILE_COUNTRIES, ',', FILE_COUNTRIES_LINES)
    return (country, abbr) if include_abbr else country


def random_emoji(include_desc: bool = False):
    """Returns a randomly-selected emoji

    Args:
        include_desc (bool, optional): Return emoji's description too. Defaults to False.

    Returns:
        str or tuple[str,str]: random emoji
    """
    emoji, desc = random_line(FILE_EMOJIS, ',', FILE_EMOJIS_LINES)
    return (emoji, desc) if include_desc else emoji


def random_bool() -> bool:
    """Returns either True or False, randomly

    Returns:
        bool: True or False
    """
    return randint(0, 100) % 2 == 0
