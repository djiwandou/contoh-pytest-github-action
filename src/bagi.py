def bagi(x: int, y: int) -> float:
    """Return the result of a division operation between two numbers.

    Args:
        x (int): pembilang.
        y (int): penyebut.

    Returns:
        float: hasil pembagian.

    Raises:
        ZeroDivisionError: If y is zero.
    """
    if y == 0:
        raise ZeroDivisionError("Tidak dapat membagi dengan nol!")
    return x / y