# Python Piscine

## Py02

_요약: 뭐라고 적어야할까~요?_

> :information_source: 오류나 개선 사항은 [이슈 트래커](https://github.com/youkim005/PythonFromHell/issues)에 등록해 주세요

# 목차

- [Python Piscine](#python-piscine)
  - [Py02](#py02)
- [목차](#목차)
- [챕터 1](#챕터-1)
  - [개요](#개요)
- [챕터 2](#챕터-2)
  - [시작하기 전에](#시작하기-전에)
- [챕터 3](#챕터-3)
  - [연습 00: ft_join](#연습-00-ft_join)
  - [연습 01: 가변인자](#연습-01-가변인자)
  - [연습 02: print_line](#연습-02-print_line)
  - [연습 00: lambda](#연습-00-lambda)
  - [연습 01: map](#연습-01-map)
  - [연습 02: filter](#연습-02-filter)

# 챕터 1

## 개요

- 프로그램만 잘 작동한다면 아무 문제도 없답니다...
- ...테스터기를 통과했다면 말이죠!
- [`PyNorme`](../README.md#PyNorme)을 따랐는지 꼭 확인해 주세요! 그 여부는 [`PyNorminette`](../README.md#PyNorminette)가 가장 잘 알고 있습니다.

# 챕터 2

## 시작하기 전에

그림

# 챕터 3

## 연습 00: ft_join
| :gear: Py01 | 연습 00           |
| :---------- | :---------------- |
| 제출할 폴더 | `ex00`            |
| 제출할 파일 | `.py`             |
| 허용 함수   | `enumerate` `len` |

내장함수 중 하나인 str.join()과 비슷하게 작동하는 df_join 함수를 만들어야 합니다.
- 함수의 프로토타입은 다음과 같습니다.

  ```python
  def ft_join(word: str, *args: str) -> str:
  ```


> :desktop_computer: 출력 예시

```bash
answer = ft_join("42", "a", "b", "c", "d")
print(answer)

a42b42c42d
```

## 연습 01: 가변인자
| :gear: Py01 | 연습 01             |
| :---------- | :------------------ |
| 제출할 폴더 | `ex01`              |
| 제출할 파일 | `ft_longargs.py`    |
| 허용 함수   | `str` `len` `items` |

파이썬의 가변인자는 크게 2가지 종류가 있습니다. (*args, **kwargs)

해당 가변인자를 이용해서 다음과 같은 함수를 구현해야 합니다.

args와 kwargs 중 더 많은 인자를 가진 쪽을 선택합니다.

그 후, 더 많은 인자들을 각각 문자열로 변환하였을 때, 가장 길이가 큰 문자열을 반환해야 합니다.

args와 kwargs가 서로 가진 인자의 수가 같을 때, "42" 문자열을 반환해야 합니다.

가장 길이가 큰 문자열이 여러 개일 경우, 처음의 문자열만 반환합니다.

- 함수의 프로토타입은 다음과 같습니다.

  ```python
  from typing import Any
  
  
  def ft_longargs(*args: Any, **kwargs: Any) -> str:
  ```

> :desktop_computer: 출력 예시

```bash
answer1 = ft_longargs(42, a="24", b=4422, c="424242424242")
print(answer1)

424242424242

answer2 = ft_longargs(42, [1234, 5678, 3214], a="12")
print(answer2)

[1234, 5678, 3214]

answer2 = ft_longargs(42, [1234, 5678, 3214], a="12")
print(answer2)

42
```



## 연습 02: print_line

| :gear: Py01 | 연습 02         |
| :---------- | :-------------- |
| 제출할 폴더 | `ex02`          |
| 제출할 파일 | `print_line.py` |
| 허용 함수   | `print`         |

파이썬에는 @(decorator)라는 개념이 있습니다.

데코레이터를 사용하여 문장을 출력하는 함수 앞, 뒤로 라인을 자동으로 출력해야 합니다.

- 함수의 프로토타입은 다음과 같습니다.

  ```python
  def print_line(func: Callable[[], None]) -> Callable[[], None]:
  ```

> :desktop_computer: 출력 예시

```python
@print_line
def ft_print():
    print("hello")

ft_print


=====
hello
=====


```

## 연습 03: lambda

| :gear: Py02 | 연습 03     |
| :---------- | :---------- |
| 제출할 폴더 | `ex03`      |
| 제출할 파일 | `square.py` |
| 허용 함수   | `lambda`    |

def를 통해 함수를 정의해서 사용할 수 있지만,
파이썬에서는 lambda 함수(익명함수)를 이용해 더 간단하게 함수를 사용할 수도 있습니다.
lambda함수를 변수로 지정하여 사용하지 않으면, 메모리도 계속해서 차지하지 않습니다!!.
먼저 단순하게 lambda를 이용하여 간단한 함수를 만들어봅시다.

answer이라는 변수에 입력받은 값을 제곱해서 반환하는 lambda 함수를 넣어주세요. 
다음과 같이 평가할 예정입니다.

> :desktop_computer: 출력 예시

```bash
answer =  lambda ~~~ 
print(answer(5))

25
```

## 연습 04: map

| :gear: Py04 | 연습 04              |
| :---------- | :-------------------- |
| 제출할 폴더 | `ex04`                |
| 제출할 파일 | `map.py`              |
| 허용 함수   | `map` `lambda` `list` |

map이라는 함수가 있습니다. map함수는 함수와 iterable 인자를 받아서,
각 함수를 iterable 인자에 적용한 값을 이러레이터로 반환해줍니다.

위에 만들었던 lambda 함수를 이용하여, 리스트에 있는 값들을 제곱해서 다시 리스트로 반환하는 함수를 만드세요

- 함수의 프로토타입은 다음과 같습니다.

  ```python 
  def square(int_list):
      return list(map(lambda x : x ** 2, int_list))
  ```

> :desktop_computer: 출력 예시

```bash
answer = square([1,2,3,4])
print(answer)


```



## 연습 05: filter

| :gear: Py02 | 연습 05                 |
| :---------- | :---------------------- |
| 제출할 폴더 | `ex05`                  |
| 제출할 파일 | `check_level.py`        |
| 허용 함수   | `labmda` `filter` `map` |

map이라는 함수가 있습니다.  filter 함수는 함수와 iterable 인자를 받아서,
각 함수를 iterable 인자에 적용한 값이 참인 요소만 이러레이터로 반환해줍니다.

다음 list 안에 몬스터에 대한 정보가 담긴 dictionary가 저장되어있습니다.
list_monster = [
    {'name' : 'monster1`, 'hp' : 100, 'level' : 20},
    ~~~,
    ~~~,
    ~~~,
]

해당 리스트 안에서 filter를 이용하여, level이 20 이상인 몬스터의 이름을 출력하는 함수를 만드세요.

- 함수의 프로토타입은 다음과 같습니다.

  ```python
  def check_level(list_monster):
      for monster in filter(lambda x : x['level'] >= 20, list_monster))
        print(monster['name'])
  ```

> :desktop_computer: 출력 예시

```python
list_monster = [
    {'name' : 'monster1', 'hp' : 100, 'level' : 20},
    {'name' : 'monster2', 'hp' : 200, 'level' : 30},
    {'name' : 'monster3', 'hp' : 300, 'level' : 10},
    {'name' : 'monster4', 'hp' : 400, 'level' : 210},
]

check_level(list_monster)

monster1
monster2
monster4

```

