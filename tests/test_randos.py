from src.randos import *
from pytest import mark
from random import choice


@mark.parametrize('length,minimum,maximum', [(10, 7, 95), (145, 53, 483)])
def test_random_ints(length: int, minimum: int, maximum: int):
    output = random_ints(length, minimum, maximum)
    # correct length?
    assert len(output) == length
    # correct min?
    assert min(output) >= minimum
    # correct max?
    assert max(output) <= maximum


@mark.parametrize('include_country', [True, False, None])
def test_random_city(include_country: bool):
    output = random_city(include_country)
    # not null?
    assert output
    # correct length?
    assert len(output) == 2 if include_country else len(output)
    # correct type?
    assert isinstance(output, tuple) if include_country else isinstance(output, str)


@mark.parametrize('include_abbr', [True, False, None])
def test_random_country(include_abbr: bool):
    output = random_country(include_abbr)
    # not null?
    assert output
    # has length?
    assert len(output)


@mark.parametrize('include_desc', [True, False, None])
def test_random_emoji(include_desc: bool):
    output = random_emoji(include_desc)
    # not null?
    assert output
    # has length?
    assert len(output)


@mark.parametrize(
    'file_path',
    [f'../src/randos/data/{choice(["CITIES", "COUNTRIES", "EMOJIS"])}.txt' for _ in range(100)])
def test_random_emoji(file_path: str):
    output = random_line(file_path, ',' if random_bool() else None)
    # not null?
    assert output
    # has length?
    assert len(output)


def test_random_bool():
    output = random_bool()
    assert output is True or output is False
