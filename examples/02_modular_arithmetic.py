"""
Example 2: Modular Arithmetic - The Computational Backbone
Level: Beginner
"""

from shors_classical import modular_exponentiate, modular_inverse
from shors_classical.modular_arithmetic import modular_exponentiate_with_steps


def main():
    print("=" * 60)
    print("Example 2: Modular Arithmetic")
    print("=" * 60)

    print("\n--- Modular Exponentiation (a^x mod N) ---")
    print("This is how we compute huge powers efficiently.")
    print("Without this, Shor's algorithm would be impossible.")
    print()

    examples = [
        (2, 10, 1000, 24),
        (3, 5, 7, 5),
        (7, 4, 15, 1),
        (2, 4, 15, 1),
        (5, 100, 13, None),
    ]

    for base, exp, mod, expected in examples:
        result = modular_exponentiate(base, exp, mod)
        check = f"✓ (expected {expected})" if expected and result == expected else ""
        print(f"  {base}^{exp} mod {mod} = {result}  {check}")

    print("\n--- Step-by-step: 3^5 mod 7 ---")
    trace = modular_exponentiate_with_steps(3, 5, 7)
    print(f"Binary of 5 = {trace['binary']}")
    for s in trace['steps']:
        print(f"  Step {s['step']}: bit={s['bit']}, {s['action']}, result={s.get('result_after', s['result'])}")
    print(f"Result: {trace['result']}")

    print("\n--- Modular Inverse ---")
    inv_pairs = [(3, 7), (2, 5), (5, 12)]
    for a, m in inv_pairs:
        inv = modular_inverse(a, m)
        print(f"  {a}⁻¹ mod {m} = {inv}  (check: {a}×{inv} mod {m} = {(a*inv) % m})")


if __name__ == "__main__":
    main()
