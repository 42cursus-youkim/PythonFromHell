def main():
    print(globals())

def test_main(capsys):
    main()
    assert capsys.readouterr().out == str(globals())+"\n"