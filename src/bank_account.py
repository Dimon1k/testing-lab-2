from typing import Union

Number = Union[int, float]


class BankAccount:
	"""Class representing a bank account for Variant 1."""

	def __init__(self, owner: str, initial_balance: Number = 0.0):
		if initial_balance < 0:
			raise ValueError("Initial balance cannot be negative")
		self.owner = owner
		self.balance = initial_balance

	def deposit(self, amount: Number) -> None:
		if amount <= 0:
			raise ValueError("Deposit amount must be positive")
		self.balance += amount

	def withdraw(self, amount: Number) -> None:
		if amount <= 0:
			raise ValueError("Withdrawal amount must be positive")
		if amount > self.balance:
			raise ValueError("Insufficient funds")
		self.balance -= amount

	def add_interest(self, rate_percent: Number) -> None:
		if rate_percent < 0:
			raise ValueError("Interest rate cannot be negative")
		self.balance += self.balance * (rate_percent / 100)
