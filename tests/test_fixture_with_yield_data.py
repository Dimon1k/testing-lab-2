import pytest


@pytest.fixture(scope='function')
def sample_account_data():
	# SETUP
	account = {
		'owner': 'Іван',
		'balance': 1000.0
	}
	user = {
		'id': 1,
		'name': 'Іван'
	}
	data = {
		'account': account,
		'user': user
	}

	yield data

	# TEARDOWN
	account.clear()
	user.clear()
	data.clear()


@pytest.mark.parametrize('deposit, expected', [
	(100.0, 1100.0),
	(500.0, 1500.0)
])
def test_deposit(sample_account_data, deposit, expected):
	account = sample_account_data['account']
	user = sample_account_data['user']
	account['balance'] += deposit
	assert account['balance'] == expected
	assert user['name'] == 'Іван'
