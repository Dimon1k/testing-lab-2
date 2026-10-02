from contextlib import nullcontext as does_not_raise

import pytest

from src.calculator import Calculator, Number


def test_divide_by_zero_exception():
	calculator = Calculator()
	with pytest.raises(ZeroDivisionError) as exc_info:
		calculator.divide(10, 0)

	assert "Cannot divide by zero" in str(exc_info.value)


def test_floating_point():
	# Звичайний assert (0.1 + 0.2 == 0.3) викликав би AssertionError
	assert (0.1 + 0.2) == pytest.approx(0.3)


class TestCalculator:
	@pytest.mark.parametrize(
		"x, y, expected_result, expectation",
		[
			(1, 2, 0.5, does_not_raise()),
			(5, -1, -5.0, does_not_raise()),
			(10, 2, 5.0, does_not_raise()),
			(5, "-1", None, pytest.raises(TypeError)),
			("5", 2, None, pytest.raises(TypeError)),
			(5, 0, None, pytest.raises(ZeroDivisionError)),
		],
	)
	def test_divide(self, x: Number, y: Number, expected_result: Number, expectation) -> None:
		calculator = Calculator()

		with expectation:
			result = calculator.divide(x, y)
			assert result == expected_result
