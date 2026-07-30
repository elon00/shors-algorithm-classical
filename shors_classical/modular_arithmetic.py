from .gcd import extended_gcd, gcd


def modular_exponentiate(base: int, exp: int, mod: int) -> int:
    """Modular exponentiation via binary exponentiation - Beginner Level.

    Compute (base^exp) % mod efficiently in O(log exp) time,
    without computing the huge intermediate number.

    This is the computational backbone of Shor's algorithm.
    We need to compute a^x mod N for very large x (up to Q ~ N^2).

    Args:
        base: The base integer.
        exp: The exponent (non-negative).
        mod: The modulus.

    Returns:
        (base^exp) % mod

    Examples:
        >>> modular_exponentiate(2, 10, 1000)
        24
        >>> modular_exponentiate(3, 5, 7)
        5
        >>> modular_exponentiate(7, 0, 11)
        1
    """
    if mod == 1:
        return 0
    result = 1 % mod
    base = base % mod
    while exp > 0:
        if exp & 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp >>= 1
    return result


def modular_inverse(a: int, m: int) -> int:
    """Modular multiplicative inverse - Intermediate Level.

    Find x such that (a * x) % m = 1.
    Uses the Extended Euclidean algorithm.
    Only exists if gcd(a, m) = 1.

    In Shor's algorithm, this is used when computing
    candidates for the period from convergents.

    Args:
        a: The number to invert.
        m: The modulus.

    Returns:
        The inverse of a modulo m.

    Raises:
        ValueError: If the inverse does not exist.

    Examples:
        >>> modular_inverse(3, 7)
        5    # because 3*5 = 15 = 1 mod 7
        >>> modular_inverse(2, 5)
        3    # because 2*3 = 6 = 1 mod 5
    """
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise ValueError(f"Inverse of {a} mod {m} does not exist (gcd={g})")
    return x % m


def modular_exponentiate_with_steps(base: int, exp: int, mod: int) -> dict:
    """Step-by-step modular exponentiation - Advanced / Teaching.

    Returns result and a list of steps showing binary expansion
    and each squaring/multiplication step.

    Examples:
        >>> r = modular_exponentiate_with_steps(3, 5, 7)
        >>> r['result']
        5
    """
    if mod == 1:
        return {'result': 0, 'steps': [], 'binary': []}
    result = 1 % mod
    base_mod = base % mod
    binary = []
    e = exp
    while e > 0:
        binary.append(e & 1)
        e >>= 1
    binary.reverse()
    steps = [{
        'step': 0,
        'bit': None,
        'base_squared': base_mod,
        'result': result,
        'action': 'initial',
    }]
    for i, bit in enumerate(binary):
        if bit == 1:
            result = (result * base_mod) % mod
            action = f'multiply by {base_mod}'
        else:
            action = 'skip multiplication'
        steps.append({
            'step': i + 1,
            'bit': bit,
            'base_squared': base_mod,
            'result_after': result,
            'action': action,
        })
        base_mod = (base_mod * base_mod) % mod
    return {'result': result, 'steps': steps, 'binary': binary}
