from typing import Callable

def print_line(func: Callable[[], None]):
	def wrapper():
		print("=====")
		func()
		print("=====")
	return wrapper()


@print_line
def answer():
	print("Hello, Python!!")