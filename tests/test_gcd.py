from shors_classical.gcd import gcd, extended_gcd, gcd_with_steps, lcm


class TestGCD:
    def test_basic_gcd(self):
        assert gcd(48, 18) == 6
        assert gcd(17, 5) == 1
        assert gcd(100, 35) == 5
        assert gcd(0, 5) == 5
        assert gcd(5, 0) == 5

    def test_negative_gcd(self):
        assert gcd(-48, 18) == 6
        assert gcd(48, -18) == 6

    def test_extended_gcd(self):
        g, x, y = extended_gcd(48, 18)
        assert g == 6
        assert 48 * x + 18 * y == g

        g, x, y = extended_gcd(17, 5)
        assert g == 1
        assert 17 * x + 5 * y == g

    def test_gcd_with_steps(self):
        steps = gcd_with_steps(48, 18)
        assert len(steps) == 4
        assert steps[-1]["equation"] == "gcd = 6"

    def test_lcm(self):
        assert lcm(4, 6) == 12
        assert lcm(7, 5) == 35
        assert lcm(0, 5) == 0
