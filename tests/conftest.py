import pytest

from src.bank_account import BankAccount


@pytest.fixture(scope="session")
def global_config():
	return {"env": "testing", "base_url": "https://api.test.com"}


@pytest.fixture(scope="function")
def account_fixture():
	# SETUP
	account = BankAccount(owner="Іван", initial_balance=1000.0)

	yield account

	# TEARDOWN
	account.balance = 0.0
	account.owner = ""
