# def main():
#     print("Hello World!" * 10)
def main():
    ...

def test_main(capsys):
    """
    stdout에 출력된 내용을 확인하고 싶을때
    입력 인자로 capsys
    낚아챈 출력값은 capsys.readouterr().out에 보관됨
    capsys.readouterr()은 실행할 때마다 초기화됨, 예)
    a = lambda: print("AAA")
    b = lambda: print("BBB")

    def test_ab(capsys):
        a()
        assert capsys.readouterr().out == "AAA\n"
        b()
        assert capsys.readouterr().out == "BBB\n"
    """
    main()
    assert capsys.readouterr().out == "Hello World!" * 10 + "\n"
