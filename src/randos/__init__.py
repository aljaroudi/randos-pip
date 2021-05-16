from random import randint


def randoms(length, minimum=0, maximum=100):
    return list([randint(minimum, maximum) for _ in range(length)])


