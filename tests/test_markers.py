import pytest

FEATURE_ENABLED = False


@pytest.mark.smoke
def test_quick():
	assert True


@pytest.mark.skip(reason="Функціонал сповіщень ще не реалізовано розробниками")
def test_notifications():
	assert False


@pytest.mark.skipif(not FEATURE_ENABLED, reason="Фіча вимкнена у налаштуваннях середовища")
def test_conditional_feature():
	assert True
