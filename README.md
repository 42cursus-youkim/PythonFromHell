# 지옥에서 온 파이썬

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# 만든 사람!

[@jj150618](https://github.com/jj150618)
[@bingu-k](https://github.com/bingu-k)
[@youkim](https://github.com/youkim005)

# 과제

[day00](./subject/day00.md)
[day01](./subject/day01.md)
[day02](./subject/day02.md)
[day03](./subject/day03.md)
[day04](./subject/day04.md)

[rush00](./subject/rush00.md)
[rush01](./subject/rush01.md)

## 개요

**_지옥에서 온 파이썬_** 은 파이썬을 기초부터 배우기 위한 피신 프로그램입니다.

- `파이썬 3.8.2+` 를 이용하여 진행됩니다.
- [_PyNorminette_](#pynorminette) 를 준수하여야 합니다.
- PyMoulinette 가 서브젝트를 평가하게 됩니다.

## PyNorminette

*PyNorminette*는 [_PyNorme_](#PyNorme)의 준수 여부를 확인하는 프로그램입니다.
아래 명령어로 설치할 수 있습니다 (테스트 버전):

```bash
pip install -i https://test.pypi.org/simple/ pynorminette
```

`PyNorminette`에서는 다음 세 가지 테스터기를 사용합니다: `black`, `mypy`, `flake8`.

`PyNorminette`가 검사하지 않는 그 외에 `PyNorme`의 다른 부분은 **권고 사항**이며,
**평가에 반영되지 않습니다.** 하지만 지키면 좋겠죠? :smirk:

## PyNorme

### 개요

- *PyNorme*은 ['파이써닉'](https://blex.me/@baealex/pythonic이란-무엇인가)
  한 코드를 작성하기 위해 준수하여야 하는 규칙의 목록입니다.
- 모든 프로그램은 [pep8](https://www.python.org/dev/peps/pep-0008/)
  을 따라야 합니다.
- 변수, 함수 및 모든 이름은 pep8의 [naming convention](https://www.python.org/dev/peps/pep-0008/#id35)
  을 기본으로 따릅니다.

### 서식

- 테스터기는 여러분이 작성한 `main()` 함수를 실행하고 그 결과로 판단합니다. 예시:

```python
if __name__ == "__main__":
  main()
```

- 전역에 코드를 작성하면 안 되요! 필요한 것들은 함수나 클래스 안에 넣어 주세요.

- 모든 파일은 [Black](https://github.com/psf/black)
  포매터를 이용해 포매팅되어야 합니다. 이는 통일된 코딩 스타일 통해 서식 작성의 피로를 줄이고 개발에 집중할 수 있게 하기 위해서입니다. 대부분의 에디터에서는 `black`을 통해 저장 시마다 자동으로 포매팅 할 수 있습니다.
- 들여쓰기로 공백 4칸을 사용하여야 합니다. 탭 문자의 사용은 금지됩니다.
  대부분의 편집기에서는 `tab`을 공백 4칸으로 바꾸는 기능을 지원합니다.
- 각 `함수 블록`은 함수 정의를 제외하고 최대 열 80글자, 행 25줄이어야 합니다.
- `선언문`은 함수의 맨 앞에 있어야 합니다.
- 세미콜론은 `;` **절대!** 사용해서는 안돼요!

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
- 변수의 타입이 중간에 변경되어서는 안 됩니다. 예)

  ```python
  # 옳은 경우
  숫자나문자: Union[str, int] = 42
  숫자나문자 = "egg" # 변수 '숫자나문자'는 정수나 문자열일 수 있습니다.

  # 잘못된 경우
  숫자 = 13
  숫자 = "hello world" # 정수형 변수 '숫자'에 문자열이 대입되었습니다
  ```

### 스코프

- 전역 변수, `global`, `nonlocal` 의 사용은 금지됩니다.
- `import *` 구문의 사용은 금지됩니다.

### 파이써닉 코딩

- 변수 언패킹 시 사용하지 않는 변수는 `_`로 표현합니다.
- `range(len(x))`의 사용은 금지됩니다.
