def test_some_text():
	with open("myinfo.txt") as f:
		content = f.read()
	assert "Tiger" in content


def test_some_text_again():
	with open("myinfo")
