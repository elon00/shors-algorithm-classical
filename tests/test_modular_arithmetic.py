from shors_classical.modular_arithmetic import (
    modular_exponentiate,
    modular_inverse,
    modular_exponentiate_with_steps,
)


class TestModularArithmetic:
    def test_modular_exponentiate(self):
        assert modular_exponentiate(2, 10, 1000) == 24
        assert modular_exponentiate(3, 5, 7) == 5
        assert modular_exponentiate(7, 0, 11) == 1
        assert modular_exponentiate(0, 5, 7) == 0
        assert modular_exponentiate(2, 4, 15) == 1  # period 4 for 2 mod 15
        assert modular_exponentiate(7, 4, 15) == 1  # period 4 for 7 mod 15

    def test_modular_exponentiate_large(self):
        assert modular_exponentiate(5, 100, 13) == modular_exponentiate(5, 100 % 12, 13)

    def test_modular_inverse(self):
        assert modular_inverse(3, 7) == 5
        assert modular_inverse(2, 5) == 3
        assert (3 * modular_inverse(3, 7)) % 7 == 1

    def test_modular_inverse_does_not_exist(self):
        import pytest
        with pytest.raises(ValueError):
            modular_inverse(2, 4)

    def test_modular_exponentiate_with_steps(self):
        r = modular_exponentiate_with_steps(3, 5, 7)
        assert r["result"] == 5
        assert len(r["steps"]) > 0
