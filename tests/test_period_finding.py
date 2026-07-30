from shors_classical import modular_exponentiate
from shors_classical.period_finding import (
    find_period_brute_force,
    find_period_quantum_simulation,
    find_period_quantum_deterministic,
)


class TestPeriodFinding:
    def test_brute_force_small(self):
        assert find_period_brute_force(2, 15) == 4
        assert find_period_brute_force(7, 15) == 4
        assert find_period_brute_force(2, 21) == 6
        assert find_period_brute_force(5, 21) == 6

    def test_brute_force_gcd_not_one(self):
        r = find_period_brute_force(3, 15)
        assert r == 1 or r is None

    def test_quantum_deterministic(self):
        assert find_period_quantum_deterministic(2, 15) == 4
        assert find_period_quantum_deterministic(7, 15) == 4

    def test_quantum_simulation_runs(self):
        r = find_period_quantum_simulation(2, 15, shots=50)
        assert r is not None
        assert modular_exponentiate(2, r, 15) == 1

    def test_quantum_simulation_multiple(self):
        for a, N, expected in [(2, 15, 4), (7, 15, 4)]:
            r = find_period_quantum_simulation(a, N, shots=50)
            assert r == expected
