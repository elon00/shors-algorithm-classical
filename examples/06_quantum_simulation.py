"""
Example 6: Advanced - Simulated Quantum Period Finding
Level: Advanced
"""

import time
from shors_classical import shors_algorithm_classical


def main():
    print("=" * 60)
    print("Example 6: Simulated Quantum Period Finding")
    print("=" * 60)
    print()
    print("This uses continued fractions to simulate what")
    print("a quantum computer would do, instead of brute-force.")
    print("This is how Shor's algorithm ACTUALLY works.")
    print()

    numbers = [15, 21, 35]

    for N in numbers:
        print(f"\nFactoring N = {N} with simulated quantum period finding...")
        t0 = time.time()
        result = shors_algorithm_classical(N, use_quantum_simulation=True, verbose=True)
        elapsed = time.time() - t0
        if result:
            print(f"  Time: {elapsed:.4f}s")
            print(f"  N = {N} = {result} × {N // result}")
        else:
            print(f"  Failed (expected for some random seeds)")

    print()
    print("Key insight: The quantum simulation uses continued fractions")
    print("to extract the period from approximate measurements.")
    print("A real quantum computer would provide these measurements")
    print("exponentially faster than classical methods.")


if __name__ == "__main__":
    main()
