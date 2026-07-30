"""
Example 1: GCD - The Foundation of Shor's Algorithm
Level: Beginner
"""

from shors_classical import gcd
from shors_classical.gcd import gcd_with_steps


def main():
    print("=" * 60)
    print("Example 1: Euclidean GCD Algorithm")
    print("=" * 60)

    pairs = [(48, 18), (17, 5), (100, 35), (7, 13), (0, 5)]

    for a, b in pairs:
        result = gcd(a, b)
        print(f"\ngcd({a}, {b}) = {result}")

    print("\n\nStep-by-step trace of gcd(48, 18):")
    print("-" * 40)
    steps = gcd_with_steps(48, 18)
    for step in steps:
        print(f"  {step['equation']}")


if __name__ == "__main__":
    main()
