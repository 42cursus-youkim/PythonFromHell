from sys import argv

import pytest


def main():
    # 입력 인자: argv[2:]
    # 실행할 테스트 파일: argv[1]
    # 커맨드 라인 실행 방식: /usr/bin/python3 run.py filename.py [args...]
    pytest.main(args=[argv[1]])


if __name__ == "__main__":
    main()
