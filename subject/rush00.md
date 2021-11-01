# Python Piscine

## Py{번호}

_요약: {내용}_

> :information_source: 오류나 개선 사항은 [이슈 트래커](https://github.com/youkim005/PythonFromHell/issues)에 등록해 주세요

# 목차



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

| :gear: Rush00 | Rush 00 |
| :-------------- | :---------- |
| 제출할 폴더     | `rush00`  |
| 제출할 파일     | `convert_roman_numerals.py`        |

입력인자로 받은 숫자를 로마 숫자로 바꿔서 출력하세요.
- 숫자는 1~10, 50, 100, 500, 1000만 사용한다.
- 11, 12, 13, ...에 해당하는 숫자는 사용하지 않는다.
- 출력되는 로마숫자는 유니코드입니다.
> :desktop_computer: 출력 예시

```
$> python3 convert_roman_numerals.py 1
Ⅰ
$> python3 convert_roman_numerals.py 123
Ⅽ
Ⅹ
Ⅹ
Ⅲ
$>
```

> :key: dictionary와 slicing을 잘 이용해보세요!