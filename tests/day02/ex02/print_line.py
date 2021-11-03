from typing import Callable

def print_line(func: Callable[[], None]):
	def wrapper():
		print("=====")
		func()
		print("=====")
	return wrapper



@print_line
def answer():
	print("Hello, Python!!")

import pytest


def test_say_myname(capsys):
	answer()
	out = capsys.readouterr().out
	assert out == "=====\nHello, Python!!\n=====\n"

if __name__ == "__main__":
    pytest.main()