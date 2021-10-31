# Python Piscine

## Py03

_요약: {내용}_

> :information_source: 오류나 개선 사항은 [이슈 트래커](https://github.com/youkim005/PythonFromHell/issues)에 등록해 주세요

# 목차
- [Python Piscine](#python-piscine)
  - [Py03](#py03)
- [목차](#목차)
- [챕터 1](#챕터-1)
  - [개요](#개요)
- [챕터 2](#챕터-2)
  - [시작하기 전에](#시작하기-전에)
- [챕터 3](#챕터-3)
  - [연습 00: 가장 큰 수](#연습-00-가장-큰-수)
  - [연습 01: 전치행렬](#연습-01-전치행렬)
  - [연습 02: 행렬의 곱](#연습-02-행렬의-곱)
  - [연습 03: 대문자, 소문자 바꾸기](#연습-03-대문자-소문자-바꾸기)
  - [연습 04: Iterator](#연습-04-iterator)
  - [연습 05: Generator](#연습-05-generator)

# 챕터 1

## 개요

- 프로그램만 잘 작동한다면 아무 문제도 없답니다...
- ...테스터기를 통과했다면 말이죠!
- [`PyNorme`](../README.md#PyNorme)을 따랐는지 꼭 확인해 주세요! 그 여부는 [`PyNorminette`](../README.md#PyNorminette)가 가장 잘 알고 있습니다.

# 챕터 2

## 시작하기 전에

> :information_source: {}

# 챕터 3

## 연습 00: 가장 큰 수

| :gear: Py03 | 연습 00                                          |
| :---------- | :----------------------------------------------- |
| 제출할 폴더 | `ex00`                                           |
| 제출할 파일 | `largest_num.py`                                 |
| 허용 함수   | `sort` `sorted` `reverse` `reversed` `int` `len` |

주어진 숫자(string) 리스트를 더해서 가장 큰 수 만들어 출력하세요.
- 함수를 만드는 겁니다.
- 실행시 1개의 입력인자를 입력받게 해주세요.
- 주어진 입력인자를 더해서 가장 큰 수를 만들어라.
- 숫자의 범위는 1~1000까지이다.
- 테스트하는 코드는 아래와 같습니다.
  ```python
  num_lst = [3, 300, 303, 9]
  print(largest_num(num_lst))
  ```  

> :desktop_computer: 출력 예시

```
$> python3 test.py
93303300
$>
```

## 연습 01: 전치행렬

| :gear: Py03 | 연습 01          |
| :---------- | :--------------- |
| 제출할 폴더 | `ex01`           |
| 제출할 파일 | `transpose.py`   |
| 허용 함수   | `sys.argv` `zip` |

입력받은 이중 리스트(행렬)의 전치행렬를 만드세요.
- 실행시 1개의 입력인자를 입력받게 해주세요.

> :desktop_computer: 출력 예시

```
$> python3 transpose.py "[[1,2],[3,4]]"
[[1, 3], [2, 4]]
$>
```

> :information_source: 행렬의 특성을 검색해봅시다~!

## 연습 02: 행렬의 곱

| :gear: Py03 | 연습 02                |
| :---------- | :--------------------- |
| 제출할 폴더 | `ex02`                 |
| 제출할 파일 | `pow_arr.py`           |
| 허용 함수   | `sys.argv` `zip` `sum` |

입력받은 이중 리스트(행렬)의 제곱을 구하세요.
- 실행시 1개의 입력인자를 입력받게 해주세요.

> :desktop_computer: 출력 예시

```
$> python3 pow_arr.py "[[1,2],[3,4]]"
[[7, 10], [15, 22]]
$> 
```

> :information_source: 행렬의 곱을 검색해봅시다~!

## 연습 03: 대문자, 소문자 바꾸기

| :gear: Py03 | 연습 03                                                 |
| :---------- | :------------------------------------------------------ |
| 제출할 폴더 | `ex03`                                                  |
| 제출할 파일 | `is_in_word.py`                                         |
| 허용 함수   | `sys.argv` `int` `split` `map` `lambda` `upper` `lower` |

입력받은 문자열에서 주어진 알파벳이 있는 단어는 소문자로 없는 문자는 대문자로 리스트에 저장하세요.
- 함수를 만드는 겁니다.
- 2개의 입력인자를 입력받게 해주세요.
- 테스트하는 코드는 아래와 같습니다.
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

## 연습 04: Iterator

| :gear: Py03 | 연습 4        |
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
<class 'StopIteration'>
$>
```

> :information_source: iteration을 사용해봅시다!!!
## 연습 05: Generator
| :gear: Py03 | 연습 5                |
| :---------- | :-------------------- |
| 제출할 폴더 | `ex05`                |
| 제출할 파일 | `generator.py`        |
| 허용 함수   | `int` `yield` `range` |

피보나치 수열을 만드는데 무한히 출력할 수 있게 해주세요.
- 함수를 만드는 겁니다.
- 테스트하는 코드는 아래와 같습니다.
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