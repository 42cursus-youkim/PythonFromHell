# Python Piscine

## Py01

_요약: 첫날에는 가볍게 파이썬의 기초 문법을 배워 봅시다._

> **_오류나 개선 사항은 [이슈 트래커](https://github.com/youkim005/PythonFromHell/issues)에 등록해 주세요_**

# 목차

# 챕터 1

## 개요

- 프로그램만 잘 작동한다면 아무 문제도 없답니다...
- ...테스터기를 통과했다면 말이죠!
- [`PyNorme`](../README.md#PyNorme)을 따랐는지 꼭 확인해 주세요! 그 여부는 [`PyNorminette`](../README.md#PyNorminette)가 가장 잘 알고 있습니다.

# 챕터 2

## 시작하기 전에

![xkcd 353](https://imgs.xkcd.com/comics/python.png)

> ℹ️ `import antigravity`

# 챕터 3

## 연습 00: 안녕 세상!!!

| ⚙️ Py00     | 연습 00    |
| :---------- | :--------- |
| 제출할 폴더 | `ex00`     |
| 제출할 파일 | `hello.py` |
| 금지 함수   | `None`     |

- 콘솔에 `Hello World!`을 표시해보세요! 다른 문장이어도 상관 없습니다. 창의력을 발휘해 보아요!
- 프로그램은 다음과 같이 작성합니다:

```python
def main():
  ... # 여기에 몬가 하기

if __name__ == "__main__":
    main()
```

출력 예시:

```bash
# 예시 1
> python3 hello.py
Hello World!%

# 예시 2
> python3 hello.py
안녕 세상!%

# 예시 3
> python3 hello.py
What is the meaning of life, the universe and everything? 42%
```

> **줄바꿈**이 있어서는 안 됩니다.

## ex00

허용 함수 : print

print는 파이썬의 문자열 출력 함수입니다

그리고 기본적으로 print로 출력을 하면 줄바꿈이 따라옵니다.

이번 과제에서는 줄바꿈을 출력하지 않고, "Hello, World!"를 출력해야 합니다.

help() 함수를 이용하여, print에 대해서 알아본다면, 충분히 답을 찾으실 수 있습니다.
