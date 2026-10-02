from typing import Union

Number = Union[int, float]


class Calculator:
	def divide(self, x: Number, y: Number) -> float:
		if (not isinstance(x, (int, float))
				or not isinstance(y, (int, float))):
			raise TypeError("Both arguments should be numeric")

		if y == 0:
			raise ZeroDivisionError("Cannot divide by zero")

		return x / y

	def add(self, x: Number, y: Number) -> Number:
		if (not isinstance(x, (int, float))
				or not isinstance(y, (int, float))):
			raise TypeError("Both arguments should be numeric")

		return x + y
