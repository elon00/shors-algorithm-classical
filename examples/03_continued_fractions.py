"""
Example 3: Continued Fractions - The Classical Bridge
Level: Intermediate
"""

from shors_classical import continued_fraction_expansion, continued_fraction_expansion_rational
from shors_classical import convergent_from_cf, find_period_from_continued_fraction


def main():
    print("=" * 60)
    print("Example 3: Continued Fractions")
    print("=" * 60)
    print()
    print("In Shor's algorithm, the quantum computer measures a value")
    print("'m' such that m/Q ≈ j/r. We use continued fractions to")
    print("extract the period r from this approximation.")
    print()

    print("1. Basic continued fraction expansions:")
    print("-" * 40)
    numbers = [
        (3.14159, "π (approx)"),
        (0.625, "5/8"),
        (1.4142, "√2 (approx)"),
        (0.3333, "1/3 (approx)"),
    ]
    for val, name in numbers:
        terms = continued_fraction_expansion(val, 6)
        frac = " + 1/(" + " + 1/(".join(str(t) for t in terms[1:3]) + "..."
        print(f"  {name} = {terms[0]} {frac}")

    print()
    print("2. Rational expansion (integer arithmetic, no precision loss):")
    print("-" * 40)
    rationals = [(5, 8), (355, 113), (1, 3)]
    for num, den in rationals:
        terms = continued_fraction_expansion_rational(num, den)
        print(f"  {num}/{den} = {terms}")

    print()
    print("3. Convergents are the best rational approximations:")
    print("-" * 40)
    terms = continued_fraction_expansion_rational(5, 8)
    for i in range(len(terms)):
        p, q = convergent_from_cf(terms, i)
        print(f"  Convergent {i}: {p}/{q} = {p/q:.6f}")

    print()
    print("4. Period extraction - THE KEY STEP in Shor's algorithm:")
    print("-" * 40)
    print()
    print("  Problem: Factor N = 15")
    print("  We pick a = 7 (coprime to 15)")
    print("  We know the quantum computer gives us a measurement m")
    print("  such that m/Q ≈ j/r where r is the period we need.")
    print()

    Q = 256
    N = 15
    r_actual = 4

    for j in range(1, r_actual):
        m = round(j * Q / r_actual)
        candidates = find_period_from_continued_fraction(m, Q, N)
        print(f"  If j = {j}, measurement m ≈ {m}")
        print(f"    m/Q = {m}/{Q} = {m/Q:.6f}")
        print(f"    Candidate periods from convergents: {candidates}")
        print()

    print("The correct period r = 4 appears as a convergent denominator.")
    print("Once we have r, we can compute factors!")


if __name__ == "__main__":
    main()
