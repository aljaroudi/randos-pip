from randos import *
from pytest import mark
from random import choice, randint


@mark.xfail(raises=ValueError)
@mark.parametrize('length,minimum', [(randint(1, 9999), randint(0, 9999)) for _ in range(1000)])
def test_random_ints(length: int, minimum: int):

    output = random_ints(length, minimum, minimum - randint(0, 9999))
    # correct length?
    assert len(output) == length
    # correct min?
    assert min(output) >= minimum


@mark.parametrize('length,minimum', [(randint(1, 9999), randint(0, 9999)) for _ in range(1000)])
def test_random_ints(length: int, minimum: int):

    output = random_ints(length, minimum, minimum + randint(0, 9999))
    # correct length?
    assert len(output) == length
    # correct min?
    assert min(output) >= minimum


@mark.parametrize('include_country', [randint(0, 100) % 2 == 0 for _ in range(1000)])
def test_random_city(include_country: bool):
    output = random_city(include_country)
    # not null?
    assert output
    # correct length?
    assert len(output) == 2 if include_country else len(output)
    # correct type?
    assert isinstance(
        output, tuple) if include_country else isinstance(output, str)


@mark.parametrize('include_abbr', [randint(0, 100) % 2 == 0 for _ in range(1000)])
def test_random_country(include_abbr: bool):
    output = random_country(include_abbr)
    # not null?
    assert output
    # has length?
    assert len(output)


@mark.parametrize('include_desc', [randint(0, 100) % 2 == 0 for _ in range(1000)])
def test_random_emoji(include_desc: bool):
    output = random_emoji(include_desc)
    # not null?
    assert output
    # has length?
    assert len(output)


@mark.parametrize(
    'file_path',
    [f'randos/data/{choice(["CITIES", "COUNTRIES", "EMOJIS"])}.txt' for _ in range(1000)])
def test_random_emoji(file_path: str):
    output = random_line(file_path, ',' if random_bool() else None)
    # not null?
    assert output
    # has length?
    assert len(output)


@mark.parametrize('_', list(range(1000)))
def test_random_bool(_):
    output = random_bool()
    assert output is True or output is False
