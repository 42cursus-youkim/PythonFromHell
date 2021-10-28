# 지옥에서 온 파이썬

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[read in english!](./README.en.md)

## 개요

**_지옥에서 온 파이썬_** 은 파이썬을 기초부터 배우기 위한 피신 프로그램입니다.

- `파이썬 3.8.2+` 를 이용하여 진행됩니다.
- [_PyNorminette_](#pynorminette) 를 준수하여야 합니다.
- PyMoulinette 가 서브젝트를 평가하게 됩니다.

## PyNorminette

*PyNorminette*는 [*PyNorme*]의 준수 여부를 확인하는 프로그램입니다.
아래 명령어로 설치할 수 있습니다 (테스트 버전):

`pip install -i https://test.pypi.org/simple/ pynorminette`

## PyNorme

### 개요

- *PyNorme*은 ['파이써닉'](https://blex.me/@baealex/pythonic이란-무엇인가)
  한 코드를 작성하기 위해 준수하여야 하는 규칙의 목록입니다.
- 모든 프로그램은 [pep8](https://www.python.org/dev/peps/pep-0008/)
  을 따라야 합니다. pep8 준수 여부는 `pip install pep8; pep8 program.py`로 확인 가능합니다.
- 변수, 함수 및 모든 이름은 pep8의 [naming convention](https://www.python.org/dev/peps/pep-0008/#id35)
  을 기본으로 따릅니다.

### 서식

- 테스터기는 여러분이 작성한 `main()` 함수를 실행하고 그 결과로 판단합니다. 예시:

```python
if __name__ == "__main__":
  main()
```

- 전역에 코드를 작성하면 안 되요! 필요한 것들은 함수나 클래스 안에 넣도록 합시다.

직접 실행

- 모든 파일은 [Black](https://github.com/psf/black)
  포매터를 이용해 포매팅되어야 합니다. 아래는 거기에 추가로 준수해야 하는 규칙입니다.
- 들여쓰기로 공백 4칸을 사용하여야 합니다. 탭 문자의 사용은 금지됩니다.
  대부분의 편집기에서는 `tab`을 공백 4칸으로 바꾸는 기능을 지원합니다.
- 각 `함수 블록`은 함수 정의를 제외하고 최대 열 80글자, 행 25줄이어야 합니다.
- `선언문`은 함수의 맨 앞에 있어야 합니다.

### 함수 및 클래스

- `중첩 함수`의 사용은 금지됩니다.
- 최대 4개의 인자를 받을 수 있습니다.
- `*args`, `**kwargs`의 사용은 명백한 이유가 없다면 금지됩니다.

### 타이핑

- 함수와 변수에 타이핑을 하는 것은 매우 권장됩니다 - 더 자주 하도록 합시다!
- 변수의 타입은 암시적/명시적으로 추론이 가능해야 합니다.
  - 두 가지 이상의 타입을 사용한다면 명시적으로 표현해 주어야 합니다.
    (예시: `spam: Union[str, int] = 42`)
  - [mypy](https://github.com/python/mypy) 또는 [pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) 의 `python.analysis.typeCheckingMode: strict` 모드를 통해 확인할 수 있습니다.

### 스코프

- 전역 변수, `global`, `nonlocal` 의 사용은 금지됩니다.
- `import *` 구문의 사용은 금지됩니다.

### 파이써닉 코딩

- 변수 언패킹 시 사용하지 않는 변수는 `_`로 표현합니다.
- `range(len(x))`의 사용은 금지됩니다.
