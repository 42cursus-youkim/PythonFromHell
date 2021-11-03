from sys import argv


def main():
    요일, 날씨, 한거 = argv[1:]
    print(f"요일: {요일}, 날씨: {날씨}")
    print(f"오늘은 {한거}. 참 재미있었다.")
