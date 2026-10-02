import pytest


@pytest.fixture(params=["Chrome", "Firefox", "Edge"])
def browser_type(request):
	# request.param містить поточне значення параметра
	return request.param


def test_web_page_title(browser_type):
	print(f"Тестування у браузері: {browser_type}")
	assert browser_type in ["Chrome", "Firefox", "Edge"]
