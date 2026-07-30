from .gcd import gcd


def continued_fraction_expansion(x: float, max_terms: int = 100) -> list[int]:
    """Compute continued fraction expansion of a real number - Beginner Level.

    Represent x as: a0 + 1/(a1 + 1/(a2 + 1/(a3 + ...)))
    Returns [a0, a1, a2, ...]

    In Shor's algorithm, the quantum part returns a measured value
    that is approximately (some integer j) / r * Q, where r is the
    period. By computing the continued fraction expansion of
    (measurement / Q), we can extract the period r as the denominator
    of one of the convergents.

    Args:
        x: The real number to expand.
        max_terms: Maximum number of terms in the expansion.

    Returns:
        List of integer coefficients [a0, a1, a2, ...].

    Examples:
        >>> continued_fraction_expansion(3.14159, 5)
        [3, 7, 15, 1, 25]
        >>> continued_fraction_expansion(0.625)
        [0, 1, 1, 1, 2]
    """
    terms = []
    for _ in range(max_terms):
        a = int(x)
        terms.append(a)
        frac = x - a
        if abs(frac) < 1e-12:
            break
        x = 1.0 / frac
    return terms


def continued_fraction_expansion_rational(num: int, den: int, max_terms: int = 100) -> list[int]:
    """Continued fraction expansion of a rational number using integer arithmetic.

    Uses the Euclidean algorithm to avoid floating-point errors.
    This is the version used in Shor's algorithm since we work with
    rational approximations of the measured value.

    Args:
        num: Numerator.
        den: Denominator.
        max_terms: Maximum number of terms.

    Returns:
        List of integer coefficients [a0, a1, a2, ...].

    Examples:
        >>> continued_fraction_expansion_rational(5, 8)
        [0, 1, 1, 1, 2]
        >>> continued_fraction_expansion_rational(355, 113)
        [3, 7, 15, 1]
    """
    terms = []
    for _ in range(max_terms):
        a = num // den
        terms.append(a)
        remainder = num % den
        if remainder == 0:
            break
        num, den = den, remainder
    return terms


def convergent_from_cf(terms: list[int], n: int | None = None) -> tuple[int, int]:
    """Compute the n-th convergent of a continued fraction - Intermediate Level.

    Returns (p_n, q_n) where p_n/q_n is the n-th convergent.

    The convergents are the best rational approximations to the
    original number. In Shor's algorithm, we examine successive
    convergents until we find a denominator q_n that is a candidate
    for the period r.

    Args:
        terms: List of continued fraction coefficients [a0, a1, ...].
        n: Index of convergent to compute (0-indexed). If None, use all terms.

    Returns:
        (numerator, denominator) of the n-th convergent.

    Examples:
        >>> convergent_from_cf([1, 2], 0)  # 1/1
        (1, 1)
        >>> convergent_from_cf([1, 2], 1)  # 1 + 1/2 = 3/2
        (3, 2)
        >>> convergent_from_cf([0, 1, 1, 1, 2])
        (5, 8)  # equivalent to 5/8 = 0.625
    """
    if n is None:
        n = len(terms) - 1
    terms = terms[: n + 1]

    if len(terms) == 1:
        return (terms[0], 1)

    p_prev2, p_prev1 = 1, terms[0]
    q_prev2, q_prev1 = 0, 1

    for a in terms[1:]:
        p = a * p_prev1 + p_prev2
        q = a * q_prev1 + q_prev2
        p_prev2, p_prev1 = p_prev1, p
        q_prev2, q_prev1 = q_prev1, q

    return (p_prev1, q_prev1)


def find_period_from_continued_fraction(
    measurement: int, Q: int, N: int, max_period: int | None = None
) -> list[int]:
    """Find candidate periods via continued fractions - Advanced Level.

    This is THE critical classical step in Shor's algorithm.
    After the quantum subroutine measures a value 'measurement',
    the classical computer must extract the period 'r'.

    The quantum circuit prepares a state whose measurement outcome
    is likely to be close to (j * Q) / r for some integer j.
    By expanding measurement/Q as a continued fraction and examining
    convergents, we find candidate denominators that might be r.

    Args:
        measurement: The value measured from the quantum register.
        Q: The size of the quantum register (Q = 2^n where n is
           the number of qubits, must satisfy N^2 <= Q < 2N^2).
        N: The number to factor.
        max_period: Maximum period to consider (defaults to N).

    Returns:
        List of candidate periods (denominators of convergents).

    Examples:
        # If the measured value suggests period 4:
        >>> candidates = find_period_from_continued_fraction(64, 256, 15)
        >>> 4 in candidates
        True
    """
    if max_period is None:
        max_period = N

    candidates = []
    terms = continued_fraction_expansion_rational(measurement, Q)

    for i in range(len(terms)):
        _, denom = convergent_from_cf(terms, i)
        if denom > 1 and denom <= max_period and denom not in candidates:
            candidates.append(denom)

    return candidates


def _demo_continued_fraction():
    """Demonstrate how continued fractions extract the period."""
    print("=" * 60)
    print("Continued Fractions: The Classical Bridge in Shor's Algorithm")
    print("=" * 60)
    print()
    print("The quantum part returns a measurement 'm' such that")
    print("  m/Q ≈ j/r  (for some integer j)")
    print()
    print("We expand m/Q as a continued fraction and try each")
    print("convergent's denominator as a candidate period r.")
    print()

    N = 15
    Q = 256
    r = 4

    print(f"Example: N={N}, Q={Q}, actual r={r}")
    print()

    for j in range(1, r):
        m = round(j * Q / r)
        candidates = find_period_from_continued_fraction(m, Q, N)
        print(f"  j={j}: measurement ≈ {m}, candidates r = {candidates}")
