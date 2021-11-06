# Python Piscine

## Py{번호}

_요약: {내용}_

> :information_source: 오류나 개선 사항은 [이슈 트래커](https://github.com/youkim005/PythonFromHell/issues)에 등록해 주세요

# 목차

- [Python Piscine](#python-piscine)
  - [Py{번호}](#py번호)
- [목차](#목차)
- [챕터 1](#챕터-1)
  - [개요](#개요)
- [챕터 2](#챕터-2)
  - [시작하기 전에](#시작하기-전에)
- [챕터 3](#챕터-3)
  - [Rush 00: Convert_Roman_Numerals](#rush-00-convert_roman_numerals)

# 챕터 1

## 개요

- 프로그램만 잘 작동한다면 아무 문제도 없답니다...
- ...테스터기를 통과했다면 말이죠!
- [`PyNorme`](../README.md#PyNorme)을 따랐는지 꼭 확인해 주세요! 그 여부는 [`PyNorminette`](../README.md#PyNorminette)가 가장 잘 알고 있습니다.

# 챕터 2

## 시작하기 전에

> :information_source: {}

# 챕터 3

## Rush 00: Convert_Roman_Numerals

| :gear: Rush00 | Rush 00                     |
| :------------ | :-------------------------- |
| 제출할 폴더   | `rush00`                    |
| 제출할 파일   | `convert_roman_numerals.py` |

입력인자로 받은 숫자를 로마 숫자로 바꿔서 출력하세요.
- 한개의 인자를 입력받아야 합니다.
- 입력 숫자의 범위는 **1이상 1000이하** 입니다.
- 로마 숫자의 계산법은 가산계산법, 감산계산법이 있습니다.
- 하지만 우리는 편의를 위해서 가산계산법만 사용하겠습니다.

> :desktop_computer: 출력 예시

```
$> python3 convert_roman_numerals.py 1
Ⅰ
$> python3 convert_roman_numerals.py 123
ⅭⅩⅩⅠⅠⅠ
$>
```

> :key: 로마 숫자는 유니코드에 있습니다.
