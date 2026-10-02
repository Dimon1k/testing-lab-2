def test_file_creation(tmp_path):
	# Створення тимчасового файлу
	test_file = tmp_path / "sample.txt"
	test_file.write_text("Hello Pytest!", encoding="utf-8")
	assert test_file.read_text(encoding="utf-8") == "Hello Pytest!"


def test_stdout_output(capsys):
	print("Вітання студентам!")
	captured = capsys.readouterr()
	assert captured.out == "Вітання студентам!\n"
