# Python Piscine

## Py00

_요약: 첫날에는 가볍게 파이썬의 기초 문법을 배워 봅시다._

> :information_source: 오류나 개선 사항은 [이슈 트래커](https://github.com/youkim005/PythonFromHell/issues)에 등록해 주세요

# 목차

- [Python Piscine](#python-piscine)
  - [Py00](#py00)
- [목차](#목차)
- [챕터 1](#챕터-1)
  - [개요](#개요)
- [챕터 2](#챕터-2)
  - [시작하기 전에](#시작하기-전에)
- [챕터 3](#챕터-3)
  - [연습 00: 안녕 세상!!!](#연습-00-안녕-세상)
  - [연습 01: 안녕 모듈???](#연습-01-안녕-모듈)
  - [연습 02: 메아리](#연습-02-메아리)
  - [연습 03: 안녕 변수???](#연습-03-안녕-변수)
  - [연습 04: 안녕 객체???](#연습-04-안녕-객체)
  - [연습 05: 오늘의 날씨: 맑음](#연습-05-오늘의-날씨-맑음)

# 챕터 1

## 개요

- 프로그램만 잘 작동한다면 아무 문제도 없답니다...
- ...테스터기를 통과했다면 말이죠!
- [`PyNorme`](../README.md#PyNorme)을 따랐는지 꼭 확인해 주세요! 그 여부는 [`PyNorminette`](../README.md#PyNorminette)가 가장 잘 알고 있습니다.

# 챕터 2

## 시작하기 전에

![xkcd 353](https://imgs.xkcd.com/comics/python.png)

> :information_source: `import antigravity`

# 챕터 3

## 연습 00: 안녕 세상!!!

| :gear: Py00 | 연습 00    |
| :---------- | :--------- |
| 제출할 폴더 | `ex00`     |
| 제출할 파일 | `hello.py` |

콘솔에 `Hello World!`을 표시해보세요! 그런데 10번, 연속해서 출력해야 합니다.

**프로그램**은 다음과 같이 선언합니다:

```python
def main():
    ... # 여기에 코드 적기...

if __name__ == "__main__":
    main()
```
앞으로 모든 프로그램은 위와 같은 방식으로 작성해야 합니다.

> :desktop_computer: 출력 예시

```bash
$> python3 hello.py
Hello World!Hello World!Hello World!Hello World!Hello World!Hello World!Hello World!Hello World!Hello World!Hello World!
$>
```

## 연습 01: 안녕 모듈???

| :gear: Py00 | 연습 01    |
| :---------- | :--------- |
| 제출할 폴더 | `ex01`     |
| 제출할 파일 | `world.py` |

파이썬의 각 파일은 모듈이랍니다.
그런데 어떻게 하면 이렇게 출력할 수 있을까요??
모듈의 전역 변수를 담고 있는 사전을 출력하는 프로그램을 만들어 보세요.

> :desktop_computer: 출력 예시

```bash
$>python3 world.py
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>}
$>
```

> :bulb: `globals()`

## 연습 02: 메아리

| :gear: Py00 | 연습 02  |
| :---------- | :-------- |
| 제출할 폴더 | `ex01`    |
| 제출할 파일 | `echo.py` |

커맨드 라인에서 입력을 받고 그대로 다시 출력하는 프로그램을 만들어보세요.


> :desktop_computer: 출력 예시

```bash
$> python3 echo.py some random word
some
random
word
$>

$> python3 what.py
$>
```

> :bulb: `sys.argv`

## 연습 03: 안녕 변수???

| :gear: Py00 | 연습 03      |
| :---------- | :----------- |
| 제출할 폴더 | `ex03`       |
| 제출할 파일 | `my_vars.py` |

파이썬에서 모든 변수는 객체를 '가리키는' **명찰**입니다. 변수에 대해 알아 볼까요?
함수 프로토타입은 다음과 같이 작성합니다:

```python
def answer(spam: int):
    ... # 여기에 코드 적기...
```

앞으로 **프로그램**이 아닌 모든 제출은 다음과 같은 `answer()` 함수로 제출해야 합니다.


`spam`은 아래 과제에서 사용할 정수형 `변수`입니다.

1. 변수(가 가리키는 객체)의 값을 출력하세요.
2. 변수(가 가리키는 객체)의 주소를 16진수로 출력하세요.
3. 변수(가 가리키는 객체)의 속성을 출력하세요.
4. 변수(가 가리키는 객체)에 11을 더한 값을 출력하세요.

> :desktop_computer: 출력 예시

```python
>>> from my_vars import answer
>>> spam = 42
>>> answer(spam)
42
0x10ead4610
<class 'int'>
53
>>>
```

> 메모리 주소는 실행 시마다 변경될 수 있습니다. 걱정하지 마세요!

> :bulb: `type`, `id()`, `hex()`

## 연습 04: 안녕 객체???

| :gear: Py00 | 연습 04     |
| :---------- | :---------- |
| 제출할 폴더 | `ex04`      |
| 제출할 파일 | `myobjs.py` |

뭘 했길래 이런 출력이 나왔을까요??
입력 인자로 주어진 객체가 가진 변수와 기능(Method)들의 목록을 출력하는 함수를 만들어보세요:

함수 프로토타입은 다음과 같이 작성합니다:

```python
from typing import Any

def answer(obj: Any):
    ... # 여기에 코드 적기...
```
가령 아래 목록에 대해 모두 작동하여야 합니다:
- `정수` 객체 `42`
- `소수` 객체 `3.14`
- `문자열` 객체 `Spam`

> :desktop_computer: 출력 예시

```python
>>> from my_objs import answer
>>> answer(42)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>>
```

> :bulb: `dirs()`

> :information_source: `a = 42; a + 11`, `a = 42; a.__add__(11)`

## 연습 05: 오늘의 날씨: 맑음

| :gear: Py00 | 연습 05                |
| :---------- | :--------------------- |
| 제출할 폴더 | `ex04`                 |
| 제출할 파일 | `diary.py`             |
| 금지 함수   | `+`, `%`, `str.format` |

요일, 날씨, 한 일을 인자로 받아서 다음과 같이 출력해주는 일기 프로그램을 만들어봅시다!

> 출력 예시

```bash
$>python3 diary.py 월요일 맑음 "학교에 갔다"
요일: 월요일, 날씨: 맑음
오늘은 학교에 갔다. 참 재미있었다.
$>
```

> :bulb: a, b, c = [1, 2, 3]
