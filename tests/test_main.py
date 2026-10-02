import sys

import pytest


def test_initial_balance(account_fixture):
	assert account_fixture.balance == 1000.0
	assert account_fixture.owner == "Іван"


@pytest.mark.parametrize("deposit_amount, expected_balance", [
	(100.0, 1100.0),
	(500.5, 1500.5),
	(0.1, 1000.1)
])
def test_deposit_parametrized(account_fixture, deposit_amount, expected_balance):
	account_fixture.deposit(deposit_amount)
	assert account_fixture.balance == pytest.approx(expected_balance)


def test_withdraw_success(account_fixture):
	account_fixture.withdraw(400.0)
	assert account_fixture.balance == 600.0


def test_withdraw_insufficient_funds(account_fixture):
	with pytest.raises(ValueError, match="Insufficient funds"):
		account_fixture.withdraw(2000.0)


def test_deposit_negative_amount(account_fixture):
	with pytest.raises(ValueError, match="Deposit amount must be positive"):
		account_fixture.deposit(-50.0)


def test_add_interest(account_fixture):
	account_fixture.add_interest(5.5)
	assert account_fixture.balance == pytest.approx(1055.0)


@pytest.mark.skipif(sys.platform == "win32", reason="Disabled for Windows OS")
def test_conditional_feature(account_fixture):
	assert account_fixture.owner == "Іван"
