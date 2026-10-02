from src.bank_account import BankAccount


def main() -> None:
	print("=== BankAccount Demonstration ===")

	# Create account
	account = BankAccount(owner="Іван", initial_balance=1000.0)
	print(f"Account created for: {account.owner}, Balance: {account.balance} UAH")

	# Deposit
	account.deposit(500.0)
	print(f"After depositing 500 UAH: {account.balance} UAH")

	# Withdraw
	account.withdraw(200.0)
	print(f"After withdrawing 200 UAH: {account.balance} UAH")

	# Add interest
	account.add_interest(5.0)
	print(f"After 5% interest addition: {account.balance} UAH")

	# Demonstrate exception handling
	try:
		account.withdraw(5000.0)
	except ValueError as e:
		print(f"Expected Error Handled: {e}")


if __name__ == "__main__":
	main()
