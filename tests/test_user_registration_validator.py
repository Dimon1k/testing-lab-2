import pytest

from src.user_registration_validator import (
	UserRegistrationValidator,
	EmailValidationError,
	PasswordValidationError,
	AgeValidationError
)

# =================================
# Email Validation Tests
# =================================

validator = UserRegistrationValidator()


def test_validate_email_success():
	assert validator.validate_email("user@example.com") is True
	assert validator.validate_email("name.lastname+tag@sub.domain.co.uk") is True


@pytest.mark.parametrize("email", ["", "   "])
def test_validate_email_empty_raises(email):
	with pytest.raises(EmailValidationError, match="Email cannot be empty"):
		validator.validate_email(email)


@pytest.mark.parametrize("email", [
	"no-at-symbol.com",
	"user@.com",
	"user@site",
	"user@@site.com",
	"@domain.com",
])
def test_validate_email_invalid_format(email):
	with pytest.raises(EmailValidationError, match="Invalid email format"):
		validator.validate_email(email)


def test_validate_email_type_error():
	with pytest.raises(TypeError, match="Email must be a string"):
		validator.validate_email(None)


# =================================
# Password Validation Tests
# =================================


def test_validate_password_success():
	assert validator.validate_password("Abcd1234") is True
	assert validator.validate_password("ValidPassword1") is True


@pytest.mark.parametrize("password, expected_message", [
	("short1A", "Password must contain at least 8 characters"),
	("alllowercase1", "Password must contain an uppercase letter"),
	("ALLUPPERCASE1", "Password must contain a lowercase letter"),
	("NoDigitsHere", "Password must contain a digit")
])
def test_validate_password_invalid(password, expected_message):
	with pytest.raises(PasswordValidationError, match=expected_message):
		validator.validate_password(password)


def test_validate_password_type_error():
	with pytest.raises(TypeError, match="Password must be a string"):
		validator.validate_password(12345678)


# =================================
# Age Validation Tests
# =================================

def test_validate_age_success():
	assert validator.validate_age(18) is True
	assert validator.validate_age(30) is True


@pytest.mark.parametrize("age, expected_message", [
	(-1, "Age cannot be negative"),
	(17, "User must be at least 18 years old"),
])
def test_validate_age_invalid(age, expected_message):
	with pytest.raises(AgeValidationError, match=expected_message):
		validator.validate_age(age)


def test_validate_age_type_error():
	with pytest.raises(TypeError, match="Age must be an integer"):
		validator.validate_age("20")


# =================================
# User Validation Tests
# =================================

def test_validate_user_success():
	assert validator.validate_user("user@example.com", "GoodPass1", 25) is True


def test_validate_user_raises_password_error_when_email_ok():
	with pytest.raises(PasswordValidationError):
		validator.validate_user("user@example.com", "weak", 25)


def test_validate_user_raises_age_error_when_email_and_password_ok():
	with pytest.raises(AgeValidationError):
		validator.validate_user("user@example.com", "GoodPass1", 16)
