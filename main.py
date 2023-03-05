"""
test
"""

print("test")

j = [1, 2, 3]


def test(param: int) -> int:
    """
    add func
    """
    return param + 1


def test_answer():
    """
    test func
    """
    assert test(3) == 5
