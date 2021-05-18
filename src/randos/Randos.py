from __future__ import annotations
from random import randint
from linecache import getline

FILE_CITIES = 'src/randos/data/CITIES.txt'
FILE_CITIES_LINES = 1100

FILE_COUNTRIES = 'src/randos/data/CITIES.txt'
FILE_COUNTRIES_LINES = 1100

FILE_EMOJIS = 'src/randos/data/EMOJIS.txt'
FILE_EMOJIS_LINES = 806


def random_ints(length: int, minimum: int = 0, maximum: int = 100):
    return list([randint(minimum, maximum) for _ in range(length)])


def random_line(file_name: str, separator: str = None, number_of_lines: int = 0):
    if not number_of_lines:
        number_of_lines = sum(1 for i in open(file_name, 'rb'))

    random_line_number = randint(0, number_of_lines)

    line = getline(file_name, random_line_number).strip()

    return line.split(separator) if separator else line


def random_city(include_country: bool = False):
    line = random_line(FILE_CITIES, ',', FILE_CITIES_LINES)
    city, country = line
    return (city, country) if include_country else city


def random_country(include_abbr: bool = False):
    country, abbr = random_line(FILE_COUNTRIES, ',', FILE_COUNTRIES_LINES)
    return (country, abbr) if include_abbr else country


def random_emoji(include_desc: bool = False):
    emoji, desc = random_line(FILE_EMOJIS, ',', FILE_EMOJIS_LINES)
    return (emoji, desc) if include_desc else emoji


def random_bool() -> bool:
    return randint(0, 100) % 2 == 0
