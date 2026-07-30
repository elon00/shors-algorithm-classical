"""
Example 4: Period Finding - The Heart of Shor's Algorithm
Level: Intermediate / Advanced
"""

from shors_classical import modular_exponentiate
from shors_classical.period_finding import (
    find_period_brute_force,
    find_period_quantum_simulation,
    find_period_quantum_deterministic,
)
from shors_classical.gcd import gcd


def compute_sequence(a, N, length=20):
    """Compute a^x mod N for x = 0, 1, 2, ..."""
    return [modular_exponentiate(a, x, N) for x in range(length)]


def main():
    print("=" * 60)
    print("Example 4: Period Finding (Order Finding)")
    print("=" * 60)
    print()
    print("The period r of a modulo N is the smallest r > 0 such")
    print("that a^r ≡ 1 (mod N). Finding this period is the hard")
    print("part that the quantum algorithm accelerates.")
    print()

    examples = [
        (2, 15, 4),
        (7, 15, 4),
        (2, 21, 6),
        (5, 21, 6),
        (3, 7, 6),
    ]

    print("1. Brute-force period finding (showing the sequence):")
    print("-" * 60)
    for a, N, expected_r in examples:
        seq = compute_sequence(a, N, expected_r * 2 + 2)
        r = find_period_brute_force(a, N)
        check = "✓" if r == expected_r else "✗"
        seq_str = ", ".join(str(x) for x in seq[: r * 2 + 1])
        print(f"  a={a}, N={N}: period r = {r} {check}")
        print(f"    Sequence: {seq_str}")
        print()

    print("2. Quantum simulation (using continued fractions):")
    print("-" * 60)
    for a, N, expected_r in examples[:2]:
        r_sim = find_period_quantum_simulation(a, N, shots=20)
        r_det = find_period_quantum_deterministic(a, N)
        print(f"  a={a}, N={N}:")
        print(f"    Simulated (probabilistic): r = {r_sim}")
        print(f"    Deterministic simulation: r = {r_det}")
        print()

    print("3. Why period finding is hard (classically):")
    print("-" * 60)
    print("  Brute force checks every r from 1 to N.")
    print("  For N ~ 10^6, we check up to 10^6 values.")
    print("  For RSA-2048 (N ~ 10^617), this is impossible.")
    print("  The quantum algorithm finds r in O(log N) steps!")
    print()
    print("  The quantum speedup: O(exp) → O(poly)")
    print("  Classical period finding:  O(N) or O(exp)")
    print("  Quantum period finding:    O((log N)²)")


if __name__ == "__main__":
    main()
