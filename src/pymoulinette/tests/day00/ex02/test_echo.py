from sys import argv


def main():
    for arg in argv[1:]:
        print(arg)


argv = ["test", "hi", "hello", "안녕"]


def test_main(capsys):
    main()
    assert capsys.readouterr().out == "\n".join(argv[1:]) + "\n"
