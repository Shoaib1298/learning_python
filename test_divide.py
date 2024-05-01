from calculator import divide


def test_divide_unique():
    assert divide(3, 2) == 1.5
    assert divide(4, 2) == 2


def test_divide_identical():
    assert divide(2, 2) == 1
    assert divide(3, 3) == 1
