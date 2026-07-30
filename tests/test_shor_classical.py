from shors_classical.shor_classical import shors_algorithm_classical, factor


class TestShorsClassical:
    def test_factor_15(self):
        result = shors_algorithm_classical(15, verbose=False)
        assert result in (3, 5)

    def test_factor_21(self):
        result = shors_algorithm_classical(21, verbose=False)
        assert result in (3, 7)

    def test_factor_35(self):
        result = shors_algorithm_classical(35, verbose=False)
        assert result in (5, 7)

    def test_factor_even_number(self):
        result = shors_algorithm_classical(12, verbose=False)
        assert result == 2

    def test_factor_function(self):
        factors = factor(15, verbose=False)
        assert sorted(factors) == [3, 5]

    def test_factor_21_function(self):
        factors = factor(21, verbose=False)
        assert sorted(factors) == [3, 7]

    def test_quantum_simulation_factor(self):
        result = shors_algorithm_classical(15, use_quantum_simulation=True, verbose=False)
        assert result in (3, 5)
