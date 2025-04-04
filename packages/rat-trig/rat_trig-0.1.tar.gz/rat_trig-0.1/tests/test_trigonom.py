from rat_trig.trigonom import archimedes
from fractions import Fraction


def test_archimedes():
    """Test Archimedes' formula"""
    q_1 = 2
    q_2 = 4
    q_3 = 6
    assert archimedes(q_1, q_2, q_3) == 32

    q_1 = 2.0
    q_2 = 4.0
    q_3 = 6.0
    assert archimedes(q_1, q_2, q_3) == 32

    q_1 = Fraction(1, 2)
    q_2 = Fraction(1, 4)
    q_3 = Fraction(1, 6)
    assert archimedes(q_1, q_2, q_3) == Fraction(23, 144)
