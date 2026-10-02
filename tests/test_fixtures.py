import pytest


class DatabaseConnection:
	def __init__(self):
		self.status = "connected"

	def close(self):
		self.status = "closed"


@pytest.fixture
def db_session():
	# --- SETUP (підготовка) ---
	print("\n[SETUP] Відкриття з'єднання з базою даних...")
	db = DatabaseConnection()

	yield db  # Передача ресурсу в тест

	# --- TEARDOWN (очищення) ---
	print("\n[TEARDOWN] Закриття з'єднання з базою даних...")
	db.close()


def test_db_query(db_session):
	print("Виконання запиту до БД...")
	assert db_session.status == "connected"
