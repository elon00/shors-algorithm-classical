import random

from .gcd import gcd
from .modular_arithmetic import modular_exponentiate
from .continued_fractions import find_period_from_continued_fraction


def find_period_brute_force(a: int, N: int, max_r: int | None = None) -> int | None:
    """Brute-force period finding - Beginner Level.

    Find the order (period) r of a modulo N, i.e., the smallest
    positive r such that a^r ≡ 1 (mod N).

    This is the naive, classical approach. It works by repeatedly
    multiplying until we find the period. This is O(r) and is
    exponentially slow for large N, which is WHY we need the
    quantum algorithm.

    Args:
        a: The base element.
        N: The modulus.
        max_r: Maximum period to search (defaults to N).

    Returns:
        The period r, or None if not found.

    Examples:
        >>> find_period_brute_force(2, 15)
        4    # because 2^1=2, 2^2=4, 2^3=8, 2^4=16≡1 mod 15
        >>> find_period_brute_force(7, 15)
        4    # because 7^1=7, 7^2=4, 7^3=13, 7^4=1 mod 15
    """
    if max_r is None:
        max_r = N
    current = a % N
    for r in range(1, max_r + 1):
        if current == 1:
            return r
        current = (current * a) % N
    return None


def find_period_quantum_simulation(
    a: int, N: int, Q: int | None = None, shots: int = 10
) -> int | None:
    """Simulate quantum period finding - Advanced Level.

    This simulates WHAT the quantum computer would do:
    1. "Measure" a random value that is approximately (j * Q) / r
       for some integer j.
    2. Use the classical continued fractions algorithm to extract r.

    The result is probabilistic, just like the real quantum algorithm.

    Args:
        a: The base element.
        N: The modulus.
        Q: The quantum register size (must satisfy N^2 ≤ Q < 2N^2).
           Defaults to the smallest power of 2 ≥ N^2.
        shots: Number of simulated measurements to try.

    Returns:
        The period r if found, None otherwise.

    Examples:
        >>> r = find_period_quantum_simulation(2, 15)
        >>> r is not None
        True
    """
    if Q is None:
        Q = 1
        while Q < N * N:
            Q <<= 1

    for _ in range(shots):
        j = random.randint(1, Q - 1)
        measurement = (j * Q) // N
        measurement = measurement % Q

        candidates = find_period_from_continued_fraction(measurement, Q, N)

        for r_candidate in candidates:
            if modular_exponentiate(a, r_candidate, N) == 1:
                return r_candidate

            r_double = r_candidate * 2
            if r_double <= N and modular_exponentiate(a, r_double, N) == 1:
                return r_double

    return None


def find_period_quantum_deterministic(a: int, N: int, Q: int | None = None) -> int | None:
    """Deterministic simulation of quantum period finding - Intermediate Level.

    Instead of random sampling, this tries ALL possible measurement
    outcomes that a quantum computer could produce. This demonstrates
    the correctness guarantee of the algorithm.

    Args:
        a: Base element.
        N: Modulus.
        Q: Register size (default: smallest power of 2 >= N^2).

    Returns:
        The period r, or None.
    """
    if Q is None:
        Q = 1
        while Q < N * N:
            Q <<= 1

    r = find_period_brute_force(a, N)
    if r is None:
        return None

    for j in range(1, r):
        measurement = round(j * Q / r)
        candidates = find_period_from_continued_fraction(measurement, Q, N)
        for c in candidates:
            if c == r:
                return r

    return None
