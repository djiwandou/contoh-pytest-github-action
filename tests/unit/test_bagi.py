from src.bagi import bagi
import pytest

def test_bagi_angka_positif_benar():
    """Test that divide returns the correct result when given two numbers."""
    assert bagi(1, 2) == 0.5

def test_bagi_angka_positif_salah():
    assert not bagi(1, 2) == 0.6

def test_bagi_angka_negatif_benar():
    """
    Test that divide returns the correct result when given a positive and
    a negative number.
    """
    assert bagi(5, -2) == -2.5
    assert bagi(-2, 5) == -0.4

def test_bagi_nol():
    """Test that divide raises a ZeroDivisionError when the denominator is zero."""
    with pytest.raises(ZeroDivisionError, match="Tidak dapat membagi dengan nol!"):
        bagi(1, 0)


