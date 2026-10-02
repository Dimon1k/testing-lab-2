def is_even(number: int) -> bool:
	return number % 2 == 0


def test_even_number():
	assert is_even(4) == True


def test_odd_number():
	assert is_even(5) == False, "Число 5 має бути непарним!"
