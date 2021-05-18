from src.randos import *
from pytest import mark


@mark.parametrize('length,minimum,maximum', [(10, 7, 95), (145, 53, 483)])
def test_random_ints(length, minimum, maximum):

    output = random_ints(length, minimum, maximum)
    # correct length?
    assert len(output) == length
    # correct min?
    assert min(output) >= minimum
    # correct max?
    assert max(output) < maximum


def test_random_city():

    output = random_city()
    # not null?
    assert output
    # has length?
    assert len(output)

