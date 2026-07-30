import math


def gcd(a: int, b: int) -> int:
    """Euclidean algorithm - Beginner Level.

    Compute the Greatest Common Divisor of a and b using the
    classic Euclidean algorithm (repeated subtraction variant).

    Time complexity: O(log(min(a,b))) in the number of steps.
    Space complexity: O(1).

    Examples:
        >>> gcd(48, 18)
        6
        >>> gcd(17, 5)
        1
        >>> gcd(0, 5)
        5
    """
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a


def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    """Extended Euclidean algorithm - Intermediate Level.

    Returns (g, x, y) such that a*x + b*y = g = gcd(a, b).

    This is critical in Shor's algorithm for computing modular
    inverses and for the continued fractions step.

    Time complexity: O(log(min(a,b))).
    Space complexity: O(1).

    Examples:
        >>> extended_gcd(48, 18)
        (6, -1, 3)   # because 48*(-1) + 18*3 = 6
        >>> extended_gcd(17, 5)
        (1, -2, 7)   # because 17*(-2) + 5*7 = 1
    """
    a, b = abs(a), abs(b)
    if b == 0:
        return (a, 1, 0)
    g, x1, y1 = extended_gcd(b, a % b)
    return (g, y1, x1 - (a // b) * y1)


def gcd_with_steps(a: int, b: int) -> list[dict]:
    """GCD with full step-by-step trace - Advanced / Debugging.

    Returns a list of steps showing the computation, useful
    for understanding and teaching.

    Each step is a dict with keys:
        'a', 'b', 'quotient', 'remainder', 'equation'

    Examples:
        >>> steps = gcd_with_steps(48, 18)
        >>> len(steps)
        3
        >>> steps[0]['equation']
        '48 = 2 * 18 + 12'
    """
    a, b = abs(a), abs(b)
    steps = []
    while b != 0:
        q = a // b
        r = a % b
        steps.append({
            'a': a,
            'b': b,
            'quotient': q,
            'remainder': r,
            'equation': f'{a} = {q} * {b} + {r}',
        })
        a, b = b, r
    steps.append({
        'a': a,
        'b': 0,
        'quotient': None,
        'remainder': 0,
        'equation': f'gcd = {a}',
    })
    return steps


def lcm(a: int, b: int) -> int:
    """Least Common Multiple using gcd.

    Examples:
        >>> lcm(4, 6)
        12
        >>> lcm(7, 5)
        35
    """
    return abs(a * b) // gcd(a, b)
