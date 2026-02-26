from typing import Tuple

def _find_base(a: int, b: int) -> int:
    digits = max(len(str(abs(a))), len(str(abs(b))))
    return 10 ** digits


def nikhilam_multiply(a: int, b: int) -> int:
    base = _find_base(a, b)
    a_diff = base - a
    b_diff = base - b

    left = a - b_diff
    right = a_diff * b_diff

    return left * base + right