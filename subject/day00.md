# Python Piscine

## Py00

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

| :gear: Py00 | 연습 00    |
| :---------- | :--------- |
| 제출할 폴더 | `ex00`     |
| 제출할 파일 | `hello.py` |

콘솔에 `Hello World!`을 표시해보세요! 다른 문장이어도 상관 없습니다. 창의력을 발휘해 보아요!

> 출력 예시

```bash
# 예시 1
$> python3 hello.py
Hello World!$>

# 예시 2
$> python3 hello.py
안녕 세상!$>

# 예시 3
$> python3 hello.py
What is the meaning of life, the universe and everything? 42$>
```

> **줄바꿈**이 있어서는 안 됩니다.

프로그램은 다음과 같이 작성합니다:

```python
def main():
  ... # 여기에 몬가 하기

if __name__ == "__main__":
    main()
```

## 연습 01: 뭐라고???

| :gear: Py00 | 연습 01   |
| :---------- | :-------- |
| 제출할 폴더 | `ex01`    |
| 제출할 파일 | `what.py` |

입력을 받고 다음과 같이 출력하는 프로그램을 만드세요.

> 출력 예시

```bash
$> python3 what.py
get input: some random word
SOME RANDOM WORD!!!
$>

$> python3 what.py
get input:
$>
```

## 연습 02: 안녕 세상???

| :gear: Py00 | 연습 02    |
| :---------- | :--------- |
| 제출할 폴더 | `ex02`     |
| 제출할 파일 | `world.py` |

어떻게 하면 이렇게 출력할 수 있을까요??
모듈의 전역 변수를 담고 있는 사전을 출력해 보세요.

> 출력 예시

```bash
$>python3 world.py
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>}
$>
```

## 연습 03: 안녕 객체???

| :gear: Py00 | 연습 03                                 |
| :---------- | :-------------------------------------- |
| 제출할 폴더 | `ex03`                                  |
| 제출할 파일 | `intobj.py`, `strobj.py`, `floatobj.py` |

뭘 했길래 이런 출력이 나왔을까요??
다음 객체들이 가지고 있는 변수와 기능(Method)들의 목록을 출력해보세요:

- `정수` 객체 `42`
- `소수` 객체 `3.14`
- `문자열` 객체 `Spam`

> 출력 예시

```bash
$>python3 intobj.py
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
```

# TODO

## 연습 05: 별 :star: 모양으로 꾸며볼게요

| :gear: Py00 | 연습 05                |
| :---------- | :--------------------- |
| 제출할 폴더 | `ex04`                 |
| 제출할 파일 | `tag.py`               |
| 금지 함수   | `+`, `%`, `str.format` |

> 출력 예시

```bash
$>python3 world.py
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>}
$>
```
