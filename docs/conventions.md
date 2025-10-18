# 코드 컨벤션 (Code Conventions)

이 문서는 저장소의 코드 스타일과 컨벤션을 설명합니다.

## 언어 및 주석

### 한글 주석
모든 코드 파일에는 **한글 주석**이 포함되어 있습니다. 이는 한국어 학습자를 위한 교재이므로, 주석은 개념을 설명하는 중요한 역할을 합니다.

```python
# calculator.py
result = 0

def add(num):
    global result
    result += num  # 결괏값(result)에 입력값(num) 더하기
    return result  # 결괏값 리턴
```

### 변수명 및 함수명
- 변수명과 함수명은 주로 **영문**을 사용합니다
- 일부 예제에서는 학습 목적으로 한글 변수명을 사용할 수 있습니다

## 파일 구조

### 파일명 규칙
- 소문자 사용
- 언더스코어(`_`) 사용 (snake_case)
- 예: `string_format.py`, `vartest_global.py`, `try_except.py`

### 파일 헤더
일부 파일은 주석으로 파일 경로를 포함합니다:

```python
# c:/doit/memo.py
```

이는 책에서 사용된 원래 경로를 나타냅니다.

## 코드 스타일

### 데모용 코드
대부분의 파일은 **데모/학습용 스크립트**로, 다음과 같은 특징이 있습니다:

1. **인라인 `print()` 문**: 결과를 즉시 보여주기 위해 사용
   ```python
   print(add(3))
   print(add(4))
   ```

2. **단순한 구조**: 복잡한 추상화보다는 개념 이해에 초점
   ```python
   # 간단하고 직관적인 예제
   if 4 in [1, 2, 3, 4]:
       print("4가 있습니다.")
   ```

3. **주석을 통한 설명**: 코드의 동작을 한글로 상세히 설명
   ```python
   result += num  # 결괏값(result)에 입력값(num) 더하기
   ```

### 의도적 오류 예제
일부 파일은 **학습 목적으로 의도적인 오류**를 포함합니다:

- `indent_error.py`, `indent_error2.py`: 들여쓰기 오류
- `vartest_error.py`: 변수 스코프 오류
- `error_make.py`: 사용자 정의 예외

이러한 파일들은:
- 파일명에 `error`를 포함하여 구분
- 오류 메시지 이해를 돕기 위한 교육 자료
- **실행 시 오류가 발생하는 것이 정상**

## 모듈 및 패키지

### 임포트 스타일

**상대 임포트** (패키지 내부):
```python
# game/graphic/render.py
from ..sound.echo import echo_test
```

**절대 임포트** (표준 라이브러리):
```python
import sys
import os
from operator import itemgetter
```

### 패키지 구조
`05-3/game/` 패키지는 표준 Python 패키지 구조를 따릅니다:

```
game/
├── __init__.py         # 패키지 초기화 파일
├── graphic/
│   ├── __init__.py
│   └── render.py
└── sound/
    ├── __init__.py
    └── echo.py
```

모든 패키지 디렉토리에는 `__init__.py` 파일이 필요합니다.

## 파일 I/O 패턴

### 파일 열기/닫기

**전통적 방식**:
```python
f = open('memo.txt', 'a')
f.write(memo)
f.close()
```

**`with` 문 사용** (권장):
```python
with open('memo.txt', 'a') as f:
    f.write(memo)
```

### 파일 모드
- `'r'`: 읽기 (기본값)
- `'w'`: 쓰기 (덮어쓰기)
- `'a'`: 추가 (append)

## 함수 및 클래스

### 함수 정의
```python
def get_total_page(m, n):
    """함수 설명 (선택적)"""
    if m % n == 0:
        return m // n
    else:
        return m // n + 1
```

### 클래스 정의
```python
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result
```

## 변수 스코프 처리

### 전역 변수 (초기 예제)
```python
result = 0  # 전역 변수

def add(num):
    global result  # global 키워드 사용
    result += num
```

### 인스턴스 변수 (개선된 방식)
```python
class Calculator:
    def __init__(self):
        self.result = 0  # 인스턴스 변수

    def add(self, num):
        self.result += num  # self 사용
```

### 반환값 사용 (함수형 방식)
```python
def add(result, num):
    return result + num  # 새 값을 반환

result = add(result, 3)
```

## 커맨드라인 인터페이스

### `sys.argv` 사용
```python
import sys

option = sys.argv[1]  # 첫 번째 인자

if option == '-a':
    memo = sys.argv[2]  # 두 번째 인자
    # ...
elif option == '-v':
    # ...
```

## 코드 작성 시 주의사항

### 새 코드 추가 시

1. **챕터 구조 유지**: 적절한 챕터 디렉토리에 파일 배치
2. **한글 주석 추가**: 기존 스타일과 일관성 유지
3. **단순성 유지**: 복잡한 패턴보다는 이해하기 쉬운 코드
4. **예제 중심**: 실제 프로덕션 코드가 아닌 학습용 예제임을 염두

### 연습문제 풀이 추가 시

연습문제 풀이는 `풀이/` 디렉토리에 추가:
- 적절한 챕터 폴더 선택 (`03장`, `04장`, `05장`, `코딩면허시험`)
- 파일명은 `q숫자.py` 형식 (예: `q1.py`, `q12.py`)

## 타입 힌트 (Type Hints)

고급 예제(`07-4/typing_sample.py`)에서는 타입 힌트를 사용합니다:

```python
def greet(name: str) -> str:
    return f"안녕하세요, {name}님!"
```

단, 기초 예제에서는 타입 힌트를 사용하지 않아 학습 부담을 줄입니다.

## 인코딩

- 기본 인코딩: **UTF-8**
- 특수 케이스: `07-1/euc_kr.py`는 EUC-KR 인코딩 학습용

파일 상단에 인코딩 선언이 필요한 경우:
```python
# -*- coding: utf-8 -*-
```

## 스타일 가이드 요약

| 항목 | 스타일 |
|------|--------|
| 파일명 | snake_case |
| 변수/함수명 | snake_case |
| 클래스명 | PascalCase |
| 주석 | 한글 |
| 들여쓰기 | 4 spaces |
| 문자열 따옴표 | 작은따옴표(`'`) 또는 큰따옴표(`"`) 혼용 |
| 파일 인코딩 | UTF-8 (기본) |

---

## 작업 가이드 (Working Guide)

### 새 예제 코드 추가

새로운 학습 예제를 추가할 때 따라야 할 가이드라인:

1. **적절한 챕터 디렉토리 선택**
   - 주제에 맞는 챕터 번호 확인 (01~08장)
   - 해당 챕터 내 적절한 섹션 선택 (예: `04-1`, `05-3`)
   - 섹션이 없다면 새로 생성 가능

2. **파일명 규칙**
   - snake_case 사용
   - 명확하고 설명적인 이름
   - 예: `string_format.py`, `try_except.py`, `vartest_global.py`

3. **코드 작성**
   - 한글 주석 포함 (개념 설명)
   - 단순하고 이해하기 쉬운 구조
   - 실행 가능한 예제 (보통 `print()` 포함)
   - 필요시 파일 헤더에 경로 주석 추가

4. **예제 코드 템플릿**
   ```python
   # 파일 설명 또는 경로 (선택적)
   # 예: c:/doit/example.py

   # 개념 설명이나 목적을 한글로 작성

   def example_function():
       """함수 설명 (선택적)"""
       result = 1 + 2  # 연산 설명
       return result  # 결과 반환

   # 실행 및 결과 출력
   print(example_function())
   ```

### 연습문제 풀이 추가

연습문제 해답을 추가할 때:

1. **디렉토리 선택**
   - `풀이/03장/`, `풀이/04장/`, `풀이/05장/` 중 선택
   - 또는 `풀이/코딩면허시험/` (종합 테스트)

2. **파일명 규칙**
   - `q숫자.py` 형식 사용
   - 예: `q1.py`, `q12.py`, `q15.py`

3. **풀이 코드 작성**
   - 문제를 주석으로 명시 (선택적)
   - 풀이 과정을 한글 주석으로 설명
   - 실행 가능한 완성된 코드

### 문서 업데이트

코드를 추가하거나 변경할 때 문서도 함께 업데이트:

1. **`docs/chapters.md` 업데이트**
   - 새로운 챕터나 섹션 추가 시
   - 주요 예제 파일이 추가될 때
   - 챕터 설명 보완이 필요할 때

2. **`docs/running-code.md` 업데이트**
   - 새로운 실행 방법이 필요한 경우
   - 외부 라이브러리가 추가된 경우
   - 특별한 실행 방법이 필요한 도구가 추가된 경우

3. **`docs/conventions.md` 업데이트**
   - 새로운 코딩 패턴이 도입된 경우
   - 컨벤션이 변경된 경우

4. **`docs/overview.md` 업데이트**
   - 저장소 구조가 크게 변경된 경우
   - 주요 특징이 추가된 경우

### 의도적 오류 예제 추가

학습용 오류 예제를 만들 때:

1. **파일명에 `error` 포함**
   - 예: `indent_error.py`, `vartest_error.py`

2. **주석으로 명확히 표시**
   ```python
   # 이 파일은 의도적으로 오류를 포함하고 있습니다.
   # 목적: 들여쓰기 오류 이해하기
   ```

3. **어떤 오류인지 설명**
   - 어떤 오류가 발생하는지
   - 왜 이 오류가 발생하는지
   - 어떻게 수정할 수 있는지

### 커맨드라인 도구 추가

CLI 도구를 만들 때:

1. **`sys.argv` 사용**
   ```python
   import sys

   option = sys.argv[1]

   if option == '-a':
       # 옵션 처리
   ```

2. **사용법 주석 추가**
   ```python
   # 사용법:
   # python tool.py -a "인자"
   # python tool.py -v
   ```

3. **`docs/running-code.md`에 사용 예시 추가**

### Git 작업

1. **Staged 파일 확인**
   ```bash
   git status
   ```

2. **새 파일 추가**
   ```bash
   git add 파일경로
   ```

3. **커밋 시 의미있는 메시지 작성**
   ```bash
   git commit -m "05-6장: itertools 예제 추가"
   ```

## 참고사항 (Notes)

### 특수 파일 및 디렉토리

- **`.idea/`**: PyCharm IDE 설정 파일 (git 무시됨)
- **`.venv/`**: Python 가상 환경 (git 무시됨)
- **`풀이/`**: 연습문제 해답 모음

### 의도적 오류 파일 목록

다음 파일들은 **실행 시 오류가 발생하는 것이 정상**입니다:

- `03-1/indent_error.py`: 들여쓰기 오류
- `03-1/indent_error2.py`: 들여쓰기 오류 (다른 케이스)
- `04-1/vartest_error.py`: 변수 스코프 오류

### 외부 라이브러리 필요 파일

- `05-7/sympy_test.py`: SymPy 라이브러리 필요
  ```bash
  pip install sympy
  ```

### 인코딩 주의

- 대부분의 파일: UTF-8
- `07-1/euc_kr.py`: EUC-KR 인코딩 (학습 목적)

### 파일 경로 주의

일부 파일은 Windows 경로를 포함할 수 있습니다:
- 예: `# c:/doit/memo.py`
- 이는 책에서 사용된 원래 경로
- 실제 환경에 맞게 조정 필요할 수 있음
