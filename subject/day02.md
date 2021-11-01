# Python Piscine

## Py02

_요약: 클래스를 쉽게 배워봅시다._

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
  - [연습 00: 안녕 클래스!!!](#연습-00-안녕-클래스)
  - [연습 01: 안녕 객체!!!](#연습-01-안녕-객체)
  - [연습 02: 안녕 클래스와 객체!!!](#연습-02-안녕-클래스와-객체)

# 챕터 1

## 개요

- 프로그램만 잘 작동한다면 아무 문제도 없답니다...
- ...테스터기를 통과했다면 말이죠!
- [`PyNorme`](../README.md#PyNorme)을 따랐는지 꼭 확인해 주세요! 그 여부는 [`PyNorminette`](../README.md#PyNorminette)가 가장 잘 알고 있습니다.

# 챕터 2

## 시작하기 전에

TODO

# 챕터 3

## 연습 00: 안녕 클래스!!!

| :gear: Py02 | 연습 00    |
| :---------- | :--------- |
| 제출할 폴더 | `ex00`     |
| 제출할 파일 | `hicls.py` |

4학년 2반 학생들에 대한 정보를 정리하기 위해 클래스를 만들어 보려고 합니다.

1. `Class42`라는 이름의 클래스를 만드세요.
2. 클래스 `teacher`라는 이름의 변수를 만들고 값을 `parrot`으로 설정하세요.
3. 클래스 **외부에** 함수 `show_teacher_outcls(cls) -> None`를 만드세요. 이 함수는 입력 인자로 받은 클래스가 가진 변수 `teacher`의 값을 `teacher: {teacher}` 형식으로 출력합니다.
4. 중간에 앵무새 선생님이 전근 가셨고 펭귄 선생님이 새로 왔습니다. 클래스 **외부에** 함수 `change_teacher_outcls(cls, teacher) -> None`을 만드세요. 이 함수는 입력 인자로 받은 클래스의 선생님을 `teacher`의 값으로 바꿉니다. 이 함수를 이용해 `teacher`의 값을 `penguin`로 바꾸세요.

> :desktop_computer: 출력 예시

```bash
$> python3 hicls.py
teacher: parrot
teacher: penguin
$>
```

## 연습 01: 안녕 객체!!!

| :gear: Py02 | 연습 01    |
| :---------- | :--------- |
| 제출할 폴더 | `ex01`     |
| 제출할 파일 | `hiobj.py` |
| 금지 함수   | `__init__` |

4학년 2반을 만들었으니 이제 반의 학생 네 명에 대한 정보를 정리해 봅시다.

| 이름     | 좋아하는 것 |
| :------- | :---------- |
| bear     | fish        |
| fox      | grape       |
| monkey   | patching    |
| aligator | bath        |

- [연습 00](#연습-00-안녕-클래스)에서 만든 `Class42`에다 네 객체 `bear`, `fox`, `monkey`, `aligaor`을 만들어 아래 내용을 정리해보세요.

> :bulb: bear = Class42()

- 각 값은 변수 `name`과 `likes`에 저장되어야 합니다.
- 값을 출력할 때 클래스 내부의 변수 (예: `teacher`, `name`, `likes`)를 사용해야 합니다.
- 클래스 **외부에** 함수 `run_student(obj) -> None`를 만드세요. 이 함수는 입력 인자로 받은 객체가 가진 변수 `name`의 값을 조회하여 `{obj.name} is running!` 의 형식으로 출력합니다.

최종적으로 다음과 같이 출력해 보세요:

> :desktop_computer: 출력 예시

```bash
$> python3 hiobj.py
[student bear]
likes: fish
bear is running!
teacher: parrot

[student fox]
likes: grape
fox is running!
teacher: parrot

[student monkey]
likes: patching
monkey is running!
teacher: parrot

[student aligator]
likes: bath
aligator is running!
teacher: parrot
$>
```

> :warning: `Class42.name`이나 `Class42.likes`의 값이 조회가 가능하면 안됩니다.

## 연습 02: 안녕 클래스와 객체!!!

TODO

| :gear: Py02 | 연습 00       |
| :---------- | :------------ |
| 제출할 폴더 | `ex02`        |
| 제출할 파일 | `hiclsobj.py` |

[연습 00](#연습-00-안녕-클래스)과 [연습01](#연습-01-안녕-객체)에서 만든 `Class42`를 개선시켜봅시다.

1. [연습 00](#연습-00-안녕-클래스)의 `show_teacher_outcls(cls)`, `change_teacher_outcls(cls, teacher)`을 클래스 내부로 옮겨 봅시다.

   - 두 함수와 똑같은 역할을 하는 함수 `show_teacher(cls)`, `change_teacher(cls, teacher)`를 만들어 봅시다.
   - 어떻게 하면 `Class42.show_teacher(Class42)`가 아닌 `Class42.show_teacher()` 형식으로 사용할 수 있을까요?

   > :bulb: `@classmethod`

2.

> :desktop_computer: 출력 예시

```bash
$> python3 hiobj.py

teacher: parrot

[student bear]
likes: fish
bear is running!
teacher: parrot

[student fox]
likes: grape
fox is running!
teacher: parrot

[student monkey]
likes: patching
monkey is running!
teacher: parrot

[student aligator]
likes: bath
aligator is running!
teacher: parrot

teacher: penguin

[student bear]
likes: fish
bear is running!
teacher: penguin

[student fox]
likes: grape
fox is running!
teacher: penguin

[student monkey]
likes: patching
monkey is running!
teacher: penguin

[student aligator]
likes: bath
aligator is running!
teacher: penguin
$>
```
