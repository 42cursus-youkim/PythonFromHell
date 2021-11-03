# Python Piscine

## Py01

_요약: 뭐라고 적어야할까~요?_

> :information_source: 오류나 개선 사항은 [이슈 트래커](https://github.com/youkim005/PythonFromHell/issues)에 등록해 주세요

# 목차

- [Python Piscine](#python-piscine)
  - [Py01](#py01)
- [목차](#목차)
- [챕터 1](#챕터-1)
  - [개요](#개요)
- [챕터 2](#챕터-2)
  - [시작하기 전에](#시작하기-전에)
- [챕터 3](#챕터-3)
  - [연습 00: n층 피라미드](#연습-00-n층-피라미드)
  - [연습 01: 알파벳](#연습-01-알파벳)
  - [연습 02: fizz buzz](#연습-02-fizz-buzz)
  - [연습 03: Number of fizz buzz](#연습-03-number-of-fizz-buzz)
  - [연습 04: 각종 연산 함수](#연습-04-각종-연산-함수)
  - [연습 05: 리스트 계산하기](#연습-05-리스트-계산하기)
  - [연습 06: 최대공약수와 최소공배수](#연습-06-최대공약수와-최소공배수)
  - [연습 07: 학생 인적사항](#연습-07-학생-인적사항)
  - [연습 08: 1년 후](#연습-08-1년-후)
  - [연습 09: 국가와 수도](#연습-09-국가와-수도)
  - [연습 10: 국가와 수도 ex](#연습-10-국가와-수도-ex)


# 챕터 1

## 개요

- 프로그램만 잘 작동한다면 아무 문제도 없답니다...
- ...테스터기를 통과했다면 말이죠!
- [`PyNorme`](../README.md#PyNorme)을 따랐는지 꼭 확인해 주세요! 그 여부는 [`PyNorminette`](../README.md#PyNorminette)가 가장 잘 알고 있습니다.

# 챕터 2

## 시작하기 전에

그림

# 챕터 3

## 연습 00: n층 피라미드
| :gear: Py01 | 연습 00      |
| :---------- | :----------- |
| 제출할 폴더 | `ex00`       |
| 제출할 파일 | `pyramid.py` |


주어진 높이만큼 *모양 피라미드를 만드세요.
- 실행시 1개의 숫자를 입력받을 수 있게 해주세요.

> :desktop_computer: 출력 예시

```bash
$> python3 pyramid.py 5
    *
   ***
  *****
 *******
*********
$> 
```

> :key:  range는 유용합니다.

## 연습 01: 알파벳
| :gear: Py01 | 연습 01      |
| :---------- | :----------- |
| 제출할 폴더 | `ex01`       |
| 제출할 파일 | `alphabet.py` |

알파벳을 a부터 z까지 출력하세요.

> :desktop_computer: 출력 예시

```bash
$> python3 alphabet.py
a
b
c

...

x
y
z
$>
```

> :key:  Ascii Code 혹은 string을 확인해보세요.

## 연습 02: fizz buzz
| :gear: Py01 | 연습 02        |
| :---------- | :------------- |
| 제출할 폴더 | `ex02`         |
| 제출할 파일 | `fizz_buzz.py` |

아래 설명에 따라 결과를 출력하세요.
- 실행시 1개의 숫자를 입력받게 해주세요.
- 3의 배수는 "Fizz"를 5의 배수는 "Buzz"를 출력하세요.
- 단, 3의 배수면서 5의 배수인 수는 "Fizz"와 "Buzz"를 출력해야해요.
- 1부터 시작해서 n까지 출력하세요.
> :desktop_computer: 출력 예시

```bash
$> python3 fizz_buzz.py 15
1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14
fizz
buzz
$>
```

> :key: 몫과 나머지는 경우를 나눌때 중요하죠.

## 연습 03: Number of fizz buzz
| :gear: Py01 | 연습 03                  |
| :---------- | :----------------------- |
| 제출할 폴더 | `ex03`                   |
| 제출할 파일 | `number_of_fizz_buzz.py` |

아래 설명에 따라 결과를 출력하세요.
- 실행시 1개의 숫자를 입력받게 해주세요.
- Fizz와 Buzz가 n번 출력될 때까지 출력하세요.
- 단, Fizz와 Buzz가 모두 n번 출력되야 하며 만약 Fizz가 n번 출력되었으나 Buzz가 n번 이하로 출력되었을때 Buzz에 해당하는 숫자가 아니라면 숫자로 출력되어야 해요.
> :desktop_computer: 출력 예시

```bash
$> python3 number_of_fizz_buzz.py 7
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
Fizz
Buzz
16
17
Fizz
19
Buzz
Fizz
22
23
24
Buzz
26
27
28
29
30
Buzz
31
32
33
34
Buzz
$>
```

## 연습 04: 각종 연산 함수
| :gear: Py01 | 연습 04          |
| :---------- | :--------------- |
| 제출할 폴더 | `ex04`           |
| 제출할 파일 | `calculation.py` |

두 숫자의 덧셈, 뺄셈, 곱셈, 나눗셈 결과를 출력하세요.
- 실행시 2개의 인자를 입력받게 해주세요.
- 첫번째와 두번째 인자은 숫자입니다.

> :desktop_computer: 출력 예시

```bash
$> python3 calculation.py 5 18
sum : 23
sub : -13
mul : 90
div : 0.2777777777777778
$> 
```

> :key: Python의 Bulitin Function은 아주 다양합니다.

## 연습 05: 리스트 계산하기
| :gear: Py01 | 연습 05       |
| :---------- | :------------ |
| 제출할 폴더 | `ex05`        |
| 제출할 파일 | `cal_list.py` |

리스트의 모든 숫자를 연산자로 계산하여 결과를 출력하세요.
- 함수를 만드는 겁니다.
- 실행시 2개의 인자를 입력받게 해주세요.
- 첫번째 인자는 연산자, 두번째 인자는 숫자로 이뤄진 리스트입니다.
- 테스트하는 코드는 아래와 같습니다.
  ```bash
  oper = '+'
  num_list = [1,2,3,4,5,6,7]
  print(cal_list(oper, num_list))
  ```

> :desktop_computer: 출력 예시

```
$> python3 test.py
1+2+3+4+5+6+7=28
$> 
```

## 연습 06: 최대공약수와 최소공배수
| :gear: Py01 | 연습 06      |
| :---------- | :----------- |
| 제출할 폴더 | `ex06`       |
| 제출할 파일 | `gcd_lcm.py` |

두개의 숫자의 최대 공약수, 최소 공배수를 출력하세요.
- 실행시 2개의 인자를 입력받게 해주세요.
    
> :desktop_computer: 출력 예시

```bash
$> python3 gcf_and_lcm.py 38 152
gcf : 38
lcm : 152
$> 
```

> :key: 몫과 나머지를 이용하면 보다 쉽습니다.

## 연습 07: 학생 인적사항
| :gear: Py01 | 연습 07         |
| :---------- | :-------------- |
| 제출할 폴더 | `ex07`          |
| 제출할 파일 | `infomation.py` |

학생의 인적사항을 tuple의 형태로 만드세요.
- 함수를 만드는 겁니다.
- 주어진 인자는 학생의 인적사항이 원소로 들어가있는 리스트입니다.
- 주어진 인자를 tuple의 형태로 만드세요.
- 이름의 오름차순으로 정렬되어야 해요.
- 인적사항이 잘못되있으면 삭제합니다.
- 테스트하는 코드는 아래와 같습니다.
  ```bash
  info = [['jake',184,81,4],['norman',182,86,2],['amy',157,59,1]]
  print(infomation(info))
  ```

> :desktop_computer: 출력 예시

```bash
$> python3 test.py
(('amy', 157, 59, 1), ('jake', 184, 81, 4), ('norman', 182, 86, 2))
$> 
```
> :key: tuple이란 무엇일까요?
> sort는 아주 유용한 Bulitin Function입니다.

## 연습 08: 1년 후
| :gear: Py01 | 연습 08              |
| :---------- | :------------------- |
| 제출할 폴더 | `ex08`               |
| 제출할 파일 | `next_infomation.py` |

연습 07에서 일년이 지났어요.
- 함수를 만드는 겁니다.
- 2개의 인자를 입력받게 해주세요.
- 졸업한 사람의 데이터는 삭제, 신입생의 데이터는 추가합니다.
- 5학년 이상은 졸업입니다.
- 인적사항이 잘못되었으면 삭제합니다.
- 테스트하는 코드는 아래와 같습니다.
  ```bash
  info = (('amy', 157, 59, 1), ('jake', 184, 81, 4), ('norman', 182, 86, 2))
  info_news = [['rachel',178,63,1]]
  print(next_infomation(info, info_news))
  ```
> :desktop_computer: 출력 예시

```
$> python3 test.py
(('amy', 157, 59, 2), ('norman', 182, 86, 3), ('rachel', 178, 63, 1))
$> 
```

## 연습 09: 국가와 수도
| :gear: Py01 | 연습 09                  |
| :---------- | :----------------------- |
| 제출할 폴더 | `ex09`                   |
| 제출할 파일 | `country_and_capital.py` |

국가와 국가의 수도가 알맞게 dict 형태로 만드세요.
- 함수를 만드는 겁니다.
- 2개의 인자를 입력받게 해주세요.
- 첫번째 인자는 국가의 이름이고 두번째 인자는 수도입니다.
- 중복된 데이터는 삭제하세요.
- 국가를 오름차순으로 저장하세요.
- 테스트하는 코드는 아래와 같습니다.
  ```bash
  country = ['korea','Singapore','Kenya','Iceland','France','Kenya']
  capital = ['Seoul','Singapore','Nairobi','Reykjavik','Paris','Nairobi']
  print(country_and_capital(country, capital))
  ```

> :desktop_computer: 출력 예시

```
$> python3 test.py
{'France': 'Paris', 'Iceland': 'Reykjavik', 'Kenya': 'Nairobi', 'Korea': 'Seoul', 'Singapore': 'Singapore'}
$> 
```

> :key: dictionary는 직접 만들순 있지만 어렵습니다.

## 연습 10: 국가와 수도 ex
| :gear: Py01 | 연습 10                                |
| :---------- | :------------------------------------- |
| 제출할 폴더 | `ex10`                                 |
| 제출할 파일 | `number_of_country_and_capital.py`     |
| 허용 함수   | `dict` `set` `list` `sort` `enumerate` |

인덱스가 key, 국가와 국가의 수도가 알맞게된 리스트를 value로한 dict 형태로 만드세요.
- 함수를 만드는 겁니다.
- 2개의 인자를 입력받게 해주세요.
- 첫번째 인자는 국가의 이름이고 두번째 인자는 수도입니다.
- 중복된 데이터는 삭제하세요.
- 국가를 오름차순으로 저장하세요.
- 테스트하는 코드는 아래와 같습니다.
- ```bash
  country = ['korea','Singapore','Kenya','Iceland','France','Kenya']
  capital = ['Seoul','Singapore','Nairobi','Reykjavik','Paris','Nairobi']
  print(number_of_country_and_capital(country, capital))
  ```
    
> :desktop_computer: 출력 예시

```
$> python3 test.py
0: France's capital is Paris
1: Iceland's capital is Reykjavik
2: Kenya's capital is Nairobi
3: Korea's capital is Seoul
4: Singapore's capital is Singapore
$> 
```

>:key: 혹시 index를 증가시켰나요..? enumerate는 신기한 함수입니다.