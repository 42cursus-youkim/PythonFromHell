from sys import argv


def main():
    요일, 날씨, 한거 = argv[1:]
    print(f"요일: {요일}, 날씨: {날씨}")
    print(f"오늘은 {한거}. 참 재미있었다.")


argv = ["test", "월", "맑음", "자전거를 탔다"]


def test_main(capsys):
    main()
    assert (
        capsys.readouterr().out
        == str(f"요일: {argv[1]}, 날씨: {argv[2]}")
        + "\n"
        + str(f"오늘은 {argv[3]}. 참 재미있었다.")
        + "\n"
    )
