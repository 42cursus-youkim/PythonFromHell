# Python Piscine

## Py03

_요약: 클래스를 쉽게 배워봅시다._

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
  - [연습 00: say_myname](#연습-00-say_myname)
  - [연습 01: getter,setter](#연습-01-gettersetter)
  - [연습 02: myname](#연습-02-myname)
  - [연습 03: 온도계](#연습-03-온도계)
  - [](#)
  - [연습 04: 밸런스 조절](#연습-04-밸런스-조절)
  - [연습 05: 상속](#연습-05-상속)

# 챕터 1

## 개요

- 프로그램만 잘 작동한다면 아무 문제도 없답니다...
- ...테스터기를 통과했다면 말이죠!
- [`PyNorme`](../README.md#PyNorme)을 따랐는지 꼭 확인해 주세요! 그 여부는 [`PyNorminette`](../README.md#PyNorminette)가 가장 잘 알고 있습니다.

# 챕터 2

## 시작하기 전에

TODO

# 챕터 3


## 연습 00: say_myname

| :gear: Py03 | 연습 00         |
| :---------- | :-------------- |
| 제출할 폴더 | `ex00`          |
| 제출할 파일 | `say_myname.py` |

이제부터 우리는 클래스를 통해 몬스터를 만들 것 입니다.

1. `__init__` 을 이용해서 몬스터의 이름을 문자열로 입력받고, 그 몬스터의 이름을 출력하는 `say_myname` 함수를 만드세요.

- 클래스의 프로토타입은 다음과 같습니다.

  ```python
  class monster:
      def __init__(self, name : str) -> None:

      def say_myname(~~):

  ```

> :desktop_computer: 출력 예시

```python
from say_myname import monster

a = monster("Kim")
a.say_myname()
#출력 결과
kim
#
```
> :bulb: `__init__`

## 연습 01: getter,setter

| :gear: Py03 | 연습 01     |
| :---------- | :---------- |
| 제출할 폴더 | `ex01`      |
| 제출할 파일 | `getset.py` |

이제부터 우리는 클래스를 통해 몬스터를 만들 것 입니다.
1. 몬스터 클래스를 생성할 때, `__init__`을 이용하여  `Slime`이라는 이름을 가진 몬스터를 default로 생성해야 합니다.
2. 몬스터의 이름을 return 해주는 get_name과 몬스터의 이름을 지정해주는 set_name 함수를 만드세요.

- 클래스의 프로토타입은 다음과 같습니다.

  ```python
  class monster:
      def __init__(self) -> None:

      def get_name(~~):

      def set_name(~~):
  ```

> :desktop_computer: 출력 예시

```python
from getset import monster


worm = monster()
print(worm.name)
#출력 결과
Slime
#
print(worm.get_name())
#출력 결과
Slime
#
worm.set_name("Crying Worm")
print(worm.name)
#출력 결과
Crying Worm
#
print(worm.get_name())
#출력 결과
Crying Worm
#
```
> :bulb: `__init__`

## 연습 05: myname

| :gear: Py03 | 연습 02                          |
| :---------- | :------------------------------- |
| 제출할 폴더 | `ex02`                           |
| 제출할 파일 | `myname.py`                      |

위에 4번 문제와 동일한 조건의 클래스를 만들 것 입니다.
다만, 위에서 구현한 set_name과 get_name은 property를 이용하면, 다음 구현할 함수를 변수처럼 사용할 수 있습니다.
1. 우리는   `@property` `~.setter` 를 통해서 `myname`이라는 함수를 만들어서, 값을 반환하거나, 값을 입력하거나 두가지 기능이 작동하도록 함수를 구현할 것입니다. 

- 클래스의 프로토타입은 다음과 같습니다.

  ```python
  class monster:
      def __init__(self) -> None:
      
      ~~
      def myname(~~):

      ~~
      def myname(~~):
  ```

> :desktop_computer: 출력 예시

```python
from myname import monster


worm = monster()
print(worm.name)
#출력 결과
Slime
#
print(worm.myname)
#출력 결과
Slime
#
worm.myname = "Crying Worm"
print(worm.name)
#출력 결과
Crying Worm
#
print(worm.myname)
#출력 결과
Crying Worm
#
```
> :bulb: `__init__``@property` `~.setter`

## 연습 03: 온도계

| :gear: Py03 | 연습 03          |
| :---------- | :--------------- |
| 제출할 폴더 | `ex06`           |
| 제출할 파일 | `celsius.py` |

우리는 온도계 클래스를 만들어야 합니다.

1. 이 온도계 클래스는 선언할 때 값을 입력받지 않으면, 기본 값으로 4도가 설정됩니다.
  (int형으로 값을 받습니다.)
2. to_fahrenheit라는 함수를 호출하면, 설정된 온도의 화씨로 변경하여 출력합니다.
3. 위에서 전 문제에서 사용한 방법 그대로, property를 이용하여, 온도계 클래스를 완성해주세요.
4. 값이 설정될 때마다 "set value"를 출력해야하고, 출력할때마다 "get value"를 출력해야 합니다.
5. 섭씨 온도는 영하 273도보다 낮을 경우, raise ValueError()를 사용하여 에러메세지를 출력해야 합니다

- 클래스의 프로토타입은 다음과 같습니다.

  ```python
  class Celsius:
      def __init__(~~):
      
      def to_fahrenheit(~~):

      ~~
      def temperature(~~):
      
      ~~
      def temperature(~~):

  ```


> :desktop_computer: 출력 예시

```python
from celsius import Celsius


c = Celsius()
#출력 결과
set value
#
print(c.temperature)
#출력 결과
get value
4
#
print(c.to_fahrenheit())
#출력 결과
get value
39.2
#
c.temperature = 300
#출력 결과
set value
#
c.temperature = -700
#출력 결과
Traceback (most recent call last):
    raise ValueError("Temperature can't be lower than absolute zero!")
ValueError: Temperature error
#
```
> :bulb: `__init__``@property` `~.setter`

## 연습 04: 밸런스 조절

| :gear: Py03 | 연습 04    |
| :---------- | :----------- |
| 제출할 폴더 | `ex07`       |
| 제출할 파일 | `balance.py` |

우리는 새로운 몬스터 클래스를 만들 것 입니다.

1. 이 몬스터 클래스는 인스턴스를 생성할 때, 그 몬스터의 name, hp, level, exp를 입력받아야 합니다.
  (모든 인자는 10 이상의 자연수만 입력됩니다.)
2. 그리고 `change_level`이라는 함수를 구현하여, level을 인자로 입력받아서, 기존의 level을 해당 level로 변경합니다. 이 때, 우리는 1보다 작은 정수를 넣지는 않을 것 입니다.
3. 변경하려는 level이 기존 level가 차이가 있다면, 그 차이의 10배만큼 hp와 exp의 값을 변경해야 합니다. 
4. hp와 exp는 10보다 작아질 수 없습니다.

- 클래스의 프로토타입은 다음과 같습니다.

  ```python
  class monster:
      def __init__(~~):

      def change_level(~~):

  ```

> :desktop_computer: 출력 예시

```python
a = monster("1", 100, 20, 100)
print(a.name, a.hp, a.level, a.exp)
#출력 결과
1 100 20 100
#
a.change_level(15)
print(a.name, a.hp, a.level, a.exp)
#출력 결과
1 50 15 50
#
```
> :bulb: `__init__``@property` `~.setter`

## 연습 05: 상속

| :gear: Py03 | 연습 05        |
| :---------- | :------------- |
| 제출할 폴더 | `ex08`         |
| 제출할 파일 | `new_slime.py` |

이전 문제에서 사용된 몬스터 클래스가 있습니다.
우리는 상속이라는 개념을 통해서, 새로운 슬라임 클래스를 정의할 것입니다.
이전 문제에서 사용했던 balance.py도 같은 디렉토리 내에 있어야 합니다.
1. 이 새로운 슬라임은 생성할 때, 그 슬라임의 name, hp, level, exp를 입력받아야 합니다. 모두 기본 공격력은 50이고, 선언할 때 따로 공격력을 입력받지 않습니다.
((모든 인자는 자연수만 입력됩니다.))
2. 기존 몬스터 클래스의 기능에 추가로, 새로운 능력을 추가하는 함수들을 만들 것 입니다.
- atk
몬스터 클래스 내의 myname 함수와 같이 공격력을 입력도 받고, 출력도 할 수 있는 함수를 만들어야 합니다.
해당 공격력은 0보다 작아질 수 없습니다. 0보다 작을 경우, raise ValueError()를 사용하여 에러메세지를 출력해야 합니다.
- change_level
몬스터 클래스 내의 change_level 함수를 오버라이딩 하여, 기존 기능에다가 공격력도 변경하는 함수를 만들어야 합니다.
공격력은 레벨 차이만큼의 5배로 값을 변경해야 합니다.

- 클래스의 프로토타입은 다음과 같습니다.

  ```python
  from balance import monster


  class slime(~~):
      def __init__(~~):
      
      ~~
      def atk(~~):
      
      ~~
      def atk(~~):
      
      def change_level(~~):

  ```

> :desktop_computer: 출력 예시

```python
from new_slime import slime


a = slime("1", 100, 20, 100)
print(a.name, a.hp, a.level, a.exp, a.atk)
#출력 결과
1 100 20 100 50
#
a.atk = 30
print(a.name, a.hp, a.level, a.exp, a.atk)
#출력 결과
1 100 20 100 30
#
a.change_level(15)
print(a.name, a.hp, a.level, a.exp, a.atk)
#출력 결과
1 50 15 50 5
#
a.change_level(10)
print(a.name, a.hp, a.level, a.exp, a.atk)
#출력 결과
Traceback (most recent call last):
    raise ValueError("atk error")
ValueError: atk error
#
```

> :bulb: `__init__``@property` `~.setter` `상속` `overriding`