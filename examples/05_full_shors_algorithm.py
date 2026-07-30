"""
Example 5: Full Shor's Algorithm - End to End
Level: Advanced
"""

from shors_classical import factor, shors_algorithm_classical
from shors_classical.gcd import gcd


def main():
    print("=" * 60)
    print("Example 5: Full Shor's Algorithm - End to End")
    print("=" * 60)
    print()
    print("This example runs the COMPLETE Shor's algorithm on")
    print("several numbers, showing every step.")
    print()

    numbers = [15, 21, 35, 77, 143]

    for N in numbers:
        result = shors_algorithm_classical(N, use_quantum_simulation=False, verbose=True)
        if result:
            print(f"\n  N = {N} = {result} × {N // result}")
        else:
            print(f"\n  Failed to factor {N}")
        print()

    print()
    print("Using the 'factor' convenience function:")
    print("-" * 40)

    for N in [15, 21, 35]:
        factors = factor(N, verbose=False)
        print(f"  factor({N}) = {factors}")


if __name__ == "__main__":
    main()
