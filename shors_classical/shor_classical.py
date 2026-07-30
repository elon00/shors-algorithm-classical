import random

from .gcd import gcd
from .modular_arithmetic import modular_exponentiate
from .continued_fractions import find_period_from_continued_fraction
from .period_finding import find_period_brute_force, find_period_quantum_simulation


def shors_algorithm_classical(
    N: int,
    use_quantum_simulation: bool = False,
    max_attempts: int = 100,
    verbose: bool = True,
) -> int | None:
    """Shor's algorithm - Full Classical Implementation - All Levels.

    This implements the complete Shor's factoring algorithm, using
    classical subroutines for every step. When use_quantum_simulation
    is True, it simulates the quantum period-finding step using
    continued fractions (the actual method a quantum computer would
    use). When False, it uses brute-force period finding (which is
    exponentially slow but easier to understand).

    Args:
        N: The composite number to factor.
        use_quantum_simulation: If True, simulate the quantum
            period-finding (probabilistic but realistic). If False,
            use brute-force (deterministic, for small N).
        max_attempts: Maximum number of random a values to try.
        verbose: If True, print step-by-step progress.

    Returns:
        A non-trivial factor of N, or None if factoring failed.

    Examples:
        >>> factor = shors_algorithm_classical(15, verbose=False)
        >>> factor in [3, 5]
        True
        >>> factor = shors_algorithm_classical(21, verbose=False)
        >>> factor in [3, 7]
        True
    """
    if verbose:
        print(f"\n{'='*60}")
        print(f"Shor's Algorithm: Factoring N = {N}")
        print(f"{'='*60}")

    if N % 2 == 0:
        factor = 2
        if verbose:
            print(f"\nStep 0: N is even -> factor = {factor}")
        return factor

    if N < 2:
        if verbose:
            print(f"\nN < 2, cannot factor")
        return None

    for attempt in range(1, max_attempts + 1):
        if verbose:
            print(f"\n--- Attempt {attempt} ---")

        a = random.randint(2, N - 2)

        if verbose:
            print(f"  Step 1: Choose random a = {a}")

        g = gcd(a, N)
        if g != 1:
            if verbose:
                print(f"  Step 2: gcd({a}, {N}) = {g} != 1 -> lucky guess!")
                print(f"  -> Factor found: {g}")
            return g

        if verbose:
            print(f"  Step 2: gcd({a}, {N}) = 1, continue...")

        if verbose:
            print(f"  Step 3: Find period r of {a} mod {N}...")

        if use_quantum_simulation:
            r = find_period_quantum_simulation(a, N)
            if r is None:
                if verbose:
                    print(f"  Step 3: Period finding failed, retry with new a")
                continue
        else:
            r = find_period_brute_force(a, N)
            if r is None:
                if verbose:
                    print(f"  Step 3: No period found (a might not be coprime)")
                continue

        if verbose:
            print(f"  -> Period r = {r} (since {a}^{r} mod {N} = 1)")

        if r % 2 != 0:
            if verbose:
                print(f"  Step 4: r is odd, retry with new a")
            continue

        if verbose:
            print(f"  Step 4: r = {r} is even, continue...")

        half = r // 2
        lhs = (modular_exponentiate(a, half, N) - 1) % N
        rhs = (modular_exponentiate(a, half, N) + 1) % N

        if verbose:
            print(f"  Step 5: a^(r/2) ≡ {modular_exponentiate(a, half, N)} (mod {N})")
            print(f"  Step 6: Compute gcd(a^(r/2) - 1, N) and gcd(a^(r/2) + 1, N)")

        factor1 = gcd(lhs, N)
        factor2 = gcd(rhs, N)

        if verbose:
            print(f"  -> gcd({a}^{half} - 1, {N}) = gcd({lhs}, {N}) = {factor1}")
            print(f"  -> gcd({a}^{half} + 1, {N}) = gcd({rhs}, {N}) = {factor2}")

        if factor1 not in (1, N) or factor2 not in (1, N):
            result = factor1 if factor1 not in (1, N) else factor2
            if verbose:
                print(f"\n  {'='*40}")
                print(f"  SUCCESS: N = {N} = {result} * {N // result}")
                print(f"  {'='*40}")
            return result

        if verbose:
            print(f"  -> Both factors are trivial, retry with new a")

    if verbose:
        print(f"\nFailed to factor {N} after {max_attempts} attempts.")
    return None


def factor(
    N: int,
    method: str = "auto",
    verbose: bool = False,
) -> list[int]:
    """High-level factoring function - Entry Point.

    Public API for factoring a number using Shor's classical
    subroutines. Returns the prime factors.

    Args:
        N: Number to factor.
        method: 'brute' for brute-force period finding,
                'quantum_sim' for simulated quantum,
                'auto' to choose based on N size.
        verbose: Print step-by-step output.

    Returns:
        List of prime factors of N.

    Examples:
        >>> sorted(factor(15))
        [3, 5]
        >>> sorted(factor(21))
        [3, 7]
    """
    use_sim = (method == "quantum_sim") or (method == "auto" and N > 50)
    result = shors_algorithm_classical(N, use_quantum_simulation=use_sim, verbose=verbose)
    if result is None:
        raise ValueError(f"Failed to factor {N}")
    return [result, N // result]
