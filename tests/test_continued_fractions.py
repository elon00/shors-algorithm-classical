from shors_classical.continued_fractions import (
    continued_fraction_expansion,
    continued_fraction_expansion_rational,
    convergent_from_cf,
    find_period_from_continued_fraction,
)


class TestContinuedFractions:
    def test_expansion_rational(self):
        terms = continued_fraction_expansion_rational(5, 8)
        assert terms == [0, 1, 1, 1, 2]

    def test_expansion_rational_355_113(self):
        terms = continued_fraction_expansion_rational(355, 113)
        assert terms == [3, 7, 16]

    def test_expansion_float(self):
        terms = continued_fraction_expansion(0.625, 10)
        reconstructed = 0.0
        for t in reversed(terms):
            if reconstructed == 0.0:
                reconstructed = t
            else:
                reconstructed = t + 1.0 / reconstructed
        assert abs(reconstructed - 0.625) < 1e-10

    def test_convergent(self):
        terms = continued_fraction_expansion_rational(5, 8)
        p, q = convergent_from_cf(terms)
        assert p == 5 and q == 8

    def test_convergent_partial(self):
        terms = continued_fraction_expansion_rational(5, 8)
        p0, q0 = convergent_from_cf(terms, 0)
        p1, q1 = convergent_from_cf(terms, 1)
        assert (p0, q0) == (0, 1)
        assert (p1, q1) == (1, 1)

    def test_period_extraction(self):
        Q = 256
        N = 15
        r = 4
        candidates = find_period_from_continued_fraction(64, Q, N)
        assert 4 in candidates or 2 in candidates

    def test_period_extraction_multiple_j(self):
        Q = 256
        N = 15
        r = 4
        for j in range(1, r):
            m = round(j * Q / r)
            candidates = find_period_from_continued_fraction(m, Q, N)
            if j in (1, 3):
                assert r in candidates, f"j={j}: expected {r} in {candidates}"
            elif j == 2:
                assert 2 in candidates, f"j={j}: expected 2 in {candidates}"
