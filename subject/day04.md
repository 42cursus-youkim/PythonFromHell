# Python Piscine

## Py04

_요약: {내용}_

> :information_source: 오류나 개선 사항은 [이슈 트래커](https://github.com/youkim005/PythonFromHell/issues)에 등록해 주세요

# 목차

- [Python Piscine](#python-piscine)
  - [Py04](#py04)
- [목차](#목차)
- [챕터 1](#챕터-1)
  - [개요](#개요)
- [챕터 2](#챕터-2)
  - [시작하기 전에](#시작하기-전에)
- [챕터 3](#챕터-3)
  - [연습 00: 무엇이든 해내는 힘!](#연습-00-무엇이든-해내는-힘)
  - [연습 01: 가장 큰 수](#연습-01-가장-큰-수)
  - [연습 02: 암호해독](#연습-02-암호해독)
  - [연습 03: 대문자, 소문자 바꾸기](#연습-03-대문자-소문자-바꾸기)
  - [연습 04: Iterator](#연습-04-iterator)
  - [연습 05: Generator](#연습-05-generator)
  - [연습 06: Get_next_line](#연습-06-get_next_line)

# 챕터 1

## 개요

- 프로그램만 잘 작동한다면 아무 문제도 없답니다...
- ...테스터기를 통과했다면 말이죠!
- [`PyNorme`](../README.md#PyNorme)을 따랐는지 꼭 확인해 주세요! 그 여부는 [`PyNorminette`](../README.md#PyNorminette)가 가장 잘 알고 있습니다.

# 챕터 2

## 시작하기 전에

> :information_source: {}

# 챕터 3

## 연습 00: 무엇이든 해내는 힘!

| :gear: Py04 | 연습 00             |
| :---------- | :------------------ |
| 제출할 폴더 | `ex01`              |
| 제출할 파일 | `all_around_key.py` |

무엇이든 해내는 힘!
- 함수를 import 하지 않아도 쓸 수 있는 방법이있다?
- 실행시 1개의 인자를 받아야합니다.
- 인자는 쌍따옴표로 묶여있어야 합니다.

> :desktop_computer: 출력 예시

```
$> python3 all_around_key "round(3.14+9*7)"
66
$> python3 all_around_key "abs(-456)"
456
$>
```

> :key: eval은 흑마법과 같은 함수죠....

## 연습 01: 가장 큰 수

| :gear: Py04 | 연습 01          |
| :---------- | :--------------- |
| 제출할 폴더 | `ex01`           |
| 제출할 파일 | `largest_num.py` |

주어진 숫자(string) 리스트를 더해서 가장 큰 수 만들어 출력하세요.
- 함수를 만드는 겁니다.
- 실행시 1개의 입력인자를 입력받게 해주세요.
- 주어진 입력인자를 더해서 가장 큰 수를 만들어라.
- 숫자의 범위는 1~1000까지이다.
- 테스트 코드는 아래와 같습니다.
  ```python
  num_lst = ['3', '300', '303', '9']
  print(largest_num(num_lst))
  ```

> :desktop_computer: 출력 예시

```
$> python3 test.py
93303300
$>
```

>:key: 숫자와 문자의 정렬순서는 다르답니다.

## 연습 02: 암호해독

| :gear: Py04 | 연습 02         |
| :---------- | :-------------- |
| 제출할 폴더 | `ex02`          |
| 제출할 파일 | `decryption.py` |

당신은 전쟁중인 나라에 장군입니다.
어느날 스파이가 밀서를 보내왔습니다.
밀서를 해독을 해주세요.
- 2개의 입력인자를 입력받게 해주세요.
- 입력인자를 번갈아 출력하면 암호해독이 됩니다.
- 테스트 코드는 아래와 같습니다.
  ```python
  str1 = "오 시북쪽로기대 전켜!"
  str2 = "후3 동으 병를출시라"
  lst = [str1, str2]
  print(decryption(lst))
  ```

> :desktop_computer: 출력 예시

```
$> python3 test.py
오후 3시 북동쪽으로 기병대를 출전시켜라!
$>
```

> :key: zip과 *를 이용하면 손쉽게 할 수 있어요!

## 연습 03: 대문자, 소문자 바꾸기

| :gear: Py04 | 연습 03         |
| :---------- | :-------------- |
| 제출할 폴더 | `ex03`          |
| 제출할 파일 | `is_in_word.py` |

입력받은 문자열에서 주어진 알파벳이 있는 단어는 소문자로 없는 문자는 대문자로 리스트에 저장하세요.
- 함수를 만드는 겁니다.
- 2개의 입력인자를 입력받게 해주세요.
- 테스트 코드는 아래와 같습니다.
  ```python
  string = "Hello welcome to Python World!"
  word = "l"
  print(is_in_word(string, word))
  ```

> :desktop_computer: 출력 예시

```
$> python3 test.py
["HELLO", "WELCOME", "to", "python" "WORLD!"]
$>
```

>:key: 문자를 바꾸는 것은 간단한 일이죠.

## 연습 04: Iterator

| :gear: Py04 | 연습 04       |
| :---------- | :------------ |
| 제출할 폴더 | `ex04`        |
| 제출할 파일 | `iterator.py` |
| 허용 함수   | `next`        |

입력받은 두개의 숫자 사이의 숫자들을 차례대로 출력할 수 있는 Class를 만들어 반환하세요.
- 함수를 만드는 겁니다.
- 범위는 첫번째 인자 이상 두번째 인자 이하의 수 입니다. 
- 테스트 함수는 아래와 같습니다.
```bash
fruits = ("apple", "banana", "cherry")
iter = iterator(fruits)
print(next(myit))
print(next(myit))
print(next(myit))
```

> :desktop_computer: 출력 예시

```
$> python3 test.py apple banana cherry
apple
banana
cherry
$>
```

> :key: Iterator는 강력합니다.

## 연습 05: Generator
| :gear: Py04 | 연습 05        |
| :---------- | :------------- |
| 제출할 폴더 | `ex05`         |
| 제출할 파일 | `generator.py` |

피보나치 수열을 만드는데 무한히 출력할 수 있게 해주세요.
- 함수를 만드는 겁니다.
- 테스트 코드는 아래와 같습니다.
  ```bash
  answer = generator()
  n = 5
  for i in range(n):
    print(next(answer))
  ```

> :desktop_computer: 출력 예시

```
$> python3 test.py
1
1
2
3
5
$>
```

:key: Generator는 다음 문제에도 사용됩니다.

## 연습 06: Get_next_line
| :gear: Py04 | 연습 06            |
| :---------- | :----------------- |
| 제출할 폴더 | `ex06`             |
| 제출할 파일 | `get_next_line.py` |

함수를 실행할 때마다 다음 줄을 출력될 수 있게 해주세요.
- 두 개의 함수를 만드는 겁니다.
- 함수 get_next_line은 두개의 인자를 받습니다.
  - 하나는 file descriptor, 다른 하나는 bytesize입니다.
  - bytesize는 주어지지 않는다면 임의의 숫자로 지정해주어야 합니다.
- 함수open_file은 file descriptor를 반환해야 합니다.
- 테스트 코드는 아래와 같습니다.
  ```bash
  import os
  base_path = os.getcwd()
  target_path = "{파일이름}"
  
  f = open_file(base_path + target_path)
  
  for line in get_next_line(f):
    print(line)
  ```

> :desktop_computer: 출력 예시
```
$> python3 test.py
this
is
test
file
you
can
do
it!
$>
```

> :key:  파일을 open하고 read해서 yield 해봅시다.