def answer_main():
    print(globals())


def test_globals(capsys):
    print(globals())
    answer = capsys.readouterr().out
    main()
    submit = capsys.readouterr().out
    assert answer == submit
