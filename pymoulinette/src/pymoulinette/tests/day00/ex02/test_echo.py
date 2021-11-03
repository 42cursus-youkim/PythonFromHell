from sys import argv

from unittest.mock import patch
import pytest


def main():
    for arg in argv[1:]:
        print(arg)


def test_main(capsys):
    with patch('sys.argv', ['echo.py', 'foo', 'bar']):
        for arg in argv[1:]:
            print(arg)
        answer = capsys.readouterr().out
        main()
        submit = capsys.readouterr().out
        assert submit == "1\n2\n3\n"  # answer


if __name__ == "__main__":
    pytest.main()
