from random import randint
from linecache import getline

FILE_CITIES = 'CITIES'
FILE_CITIES_LINES = 1100

FILE_COUNTRIES = 'CITIES'
FILE_COUNTRIES_LINES = 1100

FILE_EMOJIS = 'EMOJIS'
FILE_EMOJIS_LINES = 806

def random_ints(length, minimum=0, maximum=100):
    return list([randint(minimum, maximum) for _ in range(length)])


def random_line(file_name, separator = None, number_of_lines = 0):
    if not number_of_lines:
        number_of_lines = sum(1 for i in open(file_name, 'rb'))
    
    random_line_number = randint(0, number_of_lines)

    line = getline(file_name, random_line_number).strip()

    return line.split(separator) if separator else line


def random_city():
    city = random_line(FILE_CITIES, ',', FILE_CITIES_LINES)[0]
    return city


def random_city_w_country():
    city, country = random_line(FILE_CITIES, ',', FILE_CITIES_LINES)
    return city, country


def random_country():
    country = random_line(FILE_COUNTRIES, ',', FILE_COUNTRIES_LINES)[0]
    return country


def random_country_abbr():
    abbr = random_line(FILE_COUNTRIES, ',', FILE_COUNTRIES_LINES)[1]
    return abbr


def random_country_w_abbr():
    country, abbr = random_line(FILE_COUNTRIES, ',', FILE_COUNTRIES_LINES)
    return country, abbr


def random_emoji():
    emoji = random_line(FILE_EMOJIS, ',', FILE_EMOJIS_LINES)[0]
    return emoji


def random_emoji_w_desc():
    emoji, desc = random_line(FILE_EMOJIS, ',', FILE_EMOJIS_LINES)
    return emoji, desc
