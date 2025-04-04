from typing import TypeVar
from fractions import Fraction

T = TypeVar("T", int, float, Fraction)


def archimedes(q_1: T, q_2: T, q_3: T) -> T:
    temp = q_1 + q_2 - q_3
    return 4 * q_1 * q_2 - temp * temp


def test1():
    q_1 = 20000
    q_2 = 40000
    q_3 = 60000
    print(archimedes(q_1, q_2, q_3))


def test2():
    q_1 = 2.0
    q_2 = 4.0
    q_3 = 6.0
    print(archimedes(q_1, q_2, q_3))


def test3():
    q_1 = Fraction(1, 2)
    q_2 = Fraction(1, 4)
    q_3 = Fraction(1, 6)
    print(archimedes(q_1, q_2, q_3))


if __name__ == "__main__":
    test1()
    test2()
    test3()
