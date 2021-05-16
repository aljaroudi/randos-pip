from random import randint


def randoms(length: int, min: int = 0, max: int = 100) -> list[int]:
    return list([randint(min, max) for _ in range(length)])
