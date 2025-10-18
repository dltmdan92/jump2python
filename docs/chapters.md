# 챕터 구조 (Chapter Structure)

이 문서는 "Doit 점프 투 파이썬" 책의 챕터별 내용과 주요 예제 파일을 설명합니다.

## 챕터별 주제 (Topics by Chapter)

### 01장 - Python 기초
Python 프로그래밍 입문

**주요 파일:**
- `01-1/simple1.py`: 기본 조건문 예제
- `01-2/simple.py`: 기본 연산
- `01-6/editor.py`, `hello.py`: 편집기와 실행 예제

---

### 02장 - 문자열 (Strings)
문자열 조작 및 포매팅

**주요 파일:**
- `02-2/string.py`: 기본 문자열 연산
- `02-2/string_format.py`: 문자열 포매팅 (`format()`, f-string)
- `02-2/string_slice.py`: 문자열 슬라이싱
- `02-2/multistring.py`: 멀티라인 문자열

---

### 03장 - 제어문 (Control Flow)
조건문과 반복문, 들여쓰기

**주요 파일:**
- `03-1/indent_error.py`, `indent_error2.py`: 들여쓰기 오류 예제 (학습용)
- `03-2/coffee.py`: 조건문 예제
- `03-3/marks1.py`, `marks2.py`, `marks3.py`: 반복문과 조건문 조합

---

### 04장 - 함수와 파일 I/O (Functions and File I/O)

#### 04-1: 함수와 변수 스코프
**주요 파일:**
- `vartest.py`: 지역 변수와 전역 변수
- `vartest_global.py`: `global` 키워드 사용
- `vartest_return.py`: 반환값을 통한 변수 전달
- `vartest_error.py`: 변수 스코프 오류 예제 (학습용)
- `default1.py`, `default2.py`: 기본 매개변수

#### 04-3: 파일 입출력
**주요 파일:**
- `newfile.py`, `newfile2.py`: 파일 생성 및 쓰기
- `write_data.py`: 데이터 쓰기
- `add_data.py`: 데이터 추가 (append)
- `read.py`: 파일 읽기
- `readline_test.py`, `readline_all.py`: `readline()` 사용
- `readlines.py`: `readlines()` 사용
- `read_for.py`: 반복문으로 파일 읽기
- `file_with.py`: `with` 문 사용

#### 04-4: 시스템 인자
**주요 파일:**
- `sys1.py`, `sys2.py`: `sys.argv`를 통한 커맨드라인 인자 처리

---

### 05장 - 클래스, 모듈, 패키지 (Classes, Modules, Packages)

#### 05-1: 클래스
**주요 파일:**
- `calculator.py`: 기본 클래스 예제 (전역 변수 사용)
- `calculator2.py`: 인스턴스 변수를 사용한 클래스
- `calculator3.py`: 개선된 계산기 클래스

#### 05-2: 모듈
**주요 파일:**
- `mod1.py`, `mod2.py`: 모듈 생성과 임포트

#### 05-3: 패키지
**디렉토리 구조:**
```
game/
├── __init__.py
├── graphic/
│   ├── __init__.py
│   └── render.py
└── sound/
    ├── __init__.py
    └── echo.py
```
- 패키지 구조 예제
- 상대 임포트 사용 (`from ..sound.echo import echo_test`)

#### 05-4: 예외 처리 (Exception Handling)
**주요 파일:**
- `try_except.py`: 기본 예외 처리
- `many_error.py`: 여러 예외 처리
- `try_else.py`: `else` 절 사용
- `try_finally.py`: `finally` 절 사용
- `error_pass.py`: 예외 무시 (`pass`)
- `error_raise.py`: 예외 발생시키기 (`raise`)
- `error_make.py`: 사용자 정의 예외

#### 05-5: 함수형 프로그래밍
**주요 파일:**
- `filter1.py`: `filter()` 함수
- `positive.py`: 양수 필터링 예제
- `two_times.py`: `lambda` 함수

#### 05-6: 표준 라이브러리
**주요 파일:**
- `itemgetter1.py`, `itemgetter2.py`: `operator.itemgetter`
- `attrgetter1.py`: `operator.attrgetter`
- `itertools_zip.py`: `itertools`와 `zip`
- `reduce_test.py`: `functools.reduce`
- `random_pop.py`: `random` 모듈
- `thread_test.py`: `threading` 모듈
- `sleep1.py`: `time.sleep()`
- `urllib_test.py`: URL 처리
- `webbrowser_test.py`: 웹 브라우저 제어
- `zipfile_test.py`: ZIP 파일 처리
- `traceback_test.py`: 트레이스백 정보

#### 05-7: 외부 라이브러리
**주요 파일:**
- `sympy_test.py`: SymPy (기호 수학 라이브러리)

---

### 06장 - 연습 문제 (Practice Problems)

**주요 파일:**
- `06-1/gugu.py`: 구구단 출력
- `06-2/add_multiple.py`: 배수 더하기
- `06-3/paging.py`: 페이징 로직 (`get_total_page()` 함수)
- `06-4/memo.py`: 커맨드라인 메모 애플리케이션
  - `-a`: 메모 추가
  - `-v`: 메모 보기
- `06-5/tabto4.py`: 탭을 4칸 공백으로 변환
- `06-6/oswalk.py`, `sub_dir_search.py`: 디렉토리 탐색 (`os.walk()`)

---

### 07장 - 고급 Python (Advanced Python)

#### 07-1: 인코딩
**주요 파일:**
- `euc_kr.py`: EUC-KR 인코딩

#### 07-2: 클로저와 데코레이터
**주요 파일:**
- `closure.py`: 클로저 (closure)
- `wrapper.py`: 래퍼 함수
- `decorator.py`: 데코레이터 기초
- `decorator2.py`: 데코레이터 활용

#### 07-3: 제너레이터와 이터레이터
**주요 파일:**
- `iterator.py`: 이터레이터 프로토콜
- `reviterator.py`: 역방향 이터레이터
- `generator.py`: 제너레이터 기초
- `generator2.py`: 제너레이터 활용

#### 07-4: 타입 힌트
**주요 파일:**
- `typing_sample.py`: 타입 어노테이션 예제

---

### 08장 - 정규 표현식 (Regular Expressions)
**주요 파일:**
- `08-2/multiline.py`: 멀티라인 정규 표현식

---

## 풀이 (Solutions)

`풀이/` 디렉토리에는 장별 연습문제 해답이 포함되어 있습니다:

- `풀이/03장/`: 3장 연습문제 풀이
- `풀이/04장/`: 4장 연습문제 풀이
- `풀이/05장/`: 5장 연습문제 풀이
- `풀이/코딩면허시험/`: 코딩 면허 시험 문제 풀이

---

## 주요 개념 빠른 참조 (Quick Reference)

특정 Python 개념을 학습하거나 예제를 찾을 때 사용하세요.

| 개념 | 챕터 | 주요 파일 | 설명 |
|------|------|-----------|------|
| **변수 스코프** | 04-1 | `vartest_global.py`, `vartest_return.py` | 전역 변수, 지역 변수, `global` 키워드 |
| **파일 읽기** | 04-3 | `read.py`, `readline_test.py`, `readlines.py` | `read()`, `readline()`, `readlines()` |
| **파일 쓰기** | 04-3 | `write_data.py`, `add_data.py`, `file_with.py` | 파일 생성, 추가, `with` 문 |
| **클래스 기초** | 05-1 | `calculator.py` ~ `calculator3.py` | 클래스 정의, 인스턴스 변수 |
| **모듈** | 05-2 | `mod1.py`, `mod2.py` | 모듈 생성과 임포트 |
| **패키지** | 05-3 | `game/` | 패키지 구조, 상대 임포트 |
| **예외 처리** | 05-4 | `try_except.py`, `error_raise.py` | `try`/`except`/`finally`, 사용자 정의 예외 |
| **람다 함수** | 05-5 | `filter1.py`, `two_times.py` | `lambda`, `filter()` |
| **데코레이터** | 07-2 | `decorator.py`, `decorator2.py` | 함수 데코레이터, 클로저 |
| **제너레이터** | 07-3 | `generator.py`, `generator2.py` | `yield`, 제너레이터 표현식 |
| **이터레이터** | 07-3 | `iterator.py`, `reviterator.py` | `__iter__()`, `__next__()` |
| **타입 힌트** | 07-4 | `typing_sample.py` | 타입 어노테이션 |
| **정규식** | 08-2 | `multiline.py` | 정규 표현식 패턴 |

### 실용 도구 예제

| 도구 | 파일 | 용도 |
|------|------|------|
| **메모 앱** | `06-4/memo.py` | CLI 메모 저장/조회 (`-a`, `-v`) |
| **페이지 계산** | `06-3/paging.py` | 페이지네이션 로직 |
| **탭 변환** | `06-5/tabto4.py` | 탭을 4칸 공백으로 변환 |
| **디렉토리 탐색** | `06-6/sub_dir_search.py` | `os.walk()` 사용 예제 |

### 표준 라이브러리 예제

| 모듈 | 파일 | 기능 |
|------|------|------|
| **operator** | `05-6/itemgetter1.py`, `attrgetter1.py` | `itemgetter`, `attrgetter` |
| **functools** | `05-6/reduce_test.py` | `reduce()` |
| **itertools** | `05-6/itertools_zip.py` | `zip()`, itertools |
| **threading** | `05-6/thread_test.py` | 멀티스레딩 |
| **time** | `05-6/sleep1.py` | `sleep()` |
| **urllib** | `05-6/urllib_test.py` | URL 처리 |
| **zipfile** | `05-6/zipfile_test.py` | ZIP 파일 압축/해제 |
