"""
Example 7: Visualizing the Modular Exponentiation Sequence
Level: All Levels
"""

from shors_classical import modular_exponentiate


def compute_sequence(a, N, length):
    return [modular_exponentiate(a, x, N) for x in range(length)]


def find_period_from_sequence(seq):
    if len(seq) < 2:
        return None
    first = seq[1]
    for i in range(2, len(seq)):
        if seq[i] == first:
            return i - 1
    return None


def main():
    print("=" * 60)
    print("Example 7: Visualizing Modular Periodicity")
    print("=" * 60)
    print()

    N = 15
    bases = [2, 7, 11, 13, 4, 8]

    print(f"All sequences modulo N = {N}")
    print(f"{'a':>3} | {'Sequence (a^x mod N)':<40} | {'Period':>6}")
    print("-" * 60)

    for a in bases:
        seq = compute_sequence(a, N, 16)
        r = find_period_from_sequence(seq)
        seq_str = ", ".join(str(x) for x in seq[:8])
        if r and modular_exponentiate(a, r, N) == 1:
            print(f"  {a:>1} | {seq_str:<38} | r = {r:>2} ")
        else:
            print(f"  {a:>1} | {seq_str:<38} | no period")

    print()
    print("Note: For Shor's algorithm to work, we need:")
    print("  1. gcd(a, N) = 1  (a coprime to N)")
    print("  2. r is even")
    print("  3. a^(r/2) ≢ -1 (mod N)")
    print()
    print("When these conditions hold:")
    print("  gcd(a^(r/2) - 1, N) and gcd(a^(r/2) + 1, N)")
    print("  reveal the factors of N!")


if __name__ == "__main__":
    main()
