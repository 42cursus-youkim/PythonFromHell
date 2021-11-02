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

| :gear: Rush01 | Rush 01         |
| :------------ | :-------------- |
| 제출할 폴더   | `rush01`        |
| 제출할 파일   | `decryption.py` |

복면산 퍼즐을 만들어봅시다.
- 복면산 퍼즐은 문자와 숫자를 1:1 대응해서 계산이 맞게하는 퍼즐입니다.
    - 'SEND + MORE = MONEY'를 예로 들겠습니다.
    - 아래와 같은 1:1 대응된 문자와 숫자가 있습니다.
        - {'D': 1, 'R': 2, 'S': 7, 'O': 8, 'Y': 6, 'N': 3, 'M': 0, 'E': 5}
    - SEND = 7531, MORE = 825(0825), MONEY = 8356(08356)이 매칭됩니다.
    - 즉, SEND + MORE = MONEY ⇒ 7531 + 825 = 8356으로 복면산 퍼즐을 풀 수 있습니다.
    - 한 가지 답만 존재하는 것은 아닙니다.
- 아래 여러가지 예들이 있습니다.
    - PLAY + THE = GAME
    - BEAT + THE = DRUM
    - ONE + TWO + FOUR = SEVEN
    - ALL + COWS + EAT = GRASS
    - SEVEN + SEVEN + SIX = TWENTY
    - APPLE + GRAPE + PLUM = BANANA
    - YELLOW + BROWN = PUPPLE
    - ONE + THREE + FOUR = EIGHT
    - HEART + MYTH = RHYME
- 테스트 코드는 아래와 같습니다.
    ``` python
    lst = ['SEND','MORE']
    answer = 'MONEY'

    print(cryptarithm(lst, answer))
    ```
> :desktop_computer: 출력 예시

```
$> python3 test.py
{'D': 1, 'R': 2, 'S': 7, 'O': 8, 'Y': 6, 'N': 3, 'M': 0, 'E': 5}
$>
```

> :key: python에서는 순열을 만들어주는 모듈이 있어요!