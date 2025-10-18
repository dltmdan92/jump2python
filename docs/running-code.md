# 코드 실행 가이드 (Running Code Guide)

이 문서는 저장소의 Python 코드를 실행하는 방법을 설명합니다.

## 가상 환경 (Virtual Environment)

이 저장소는 `.venv/` 디렉토리에 Python 가상 환경을 사용합니다.

### 가상 환경 활성화

**macOS / Linux:**
```bash
source .venv/bin/activate
```

**Windows:**
```bash
.venv\Scripts\activate
```

### 가상 환경 비활성화

```bash
deactivate
```

## 개별 스크립트 실행

이 저장소는 학습용 예제 스크립트들의 모음입니다. 각 파일은 독립적으로 실행 가능합니다.

### 기본 실행

```bash
# 가상 환경 활성화 후
python 02-2/string_format.py
python 05-1/calculator.py
python 07-3/generator.py
```

### 커맨드라인 인자가 필요한 스크립트

일부 스크립트는 `sys.argv`를 통해 커맨드라인 인자를 받습니다.

**메모 애플리케이션 (`06-4/memo.py`):**
```bash
# 메모 추가
python 06-4/memo.py -a "오늘 할 일: Python 공부"

# 메모 보기
python 06-4/memo.py -v
```

**시스템 인자 예제 (`04-4/sys1.py`, `sys2.py`):**
```bash
python 04-4/sys1.py arg1 arg2 arg3
```

**탭 변환 유틸리티 (`06-5/tabto4.py`):**
```bash
python 06-5/tabto4.py input_file.py
```

### 패키지 실행

`05-3/game/` 패키지의 모듈을 실행하려면:

```bash
# game 패키지가 있는 디렉토리에서 실행
cd 05-3
python -c "from game.graphic.render import render_test; render_test()"
```

또는 Python 인터프리터에서:
```python
>>> from game.graphic.render import render_test
>>> render_test()
```

## 파일 I/O가 있는 스크립트

일부 스크립트는 파일을 생성하거나 읽습니다.

**파일 쓰기 예제:**
```bash
cd 04-3
python newfile.py          # newfile.txt 생성
python write_data.py       # 데이터 쓰기
python add_data.py         # 데이터 추가
```

**파일 읽기 예제:**
```bash
cd 04-3
python read.py             # 파일 전체 읽기
python readline_test.py    # 한 줄씩 읽기
python readlines.py        # 모든 줄을 리스트로 읽기
```

## 의도적 오류 예제

일부 파일은 학습 목적으로 의도적으로 오류를 포함하고 있습니다:

- `03-1/indent_error.py`: 들여쓰기 오류
- `03-1/indent_error2.py`: 들여쓰기 오류 (다른 케이스)
- `04-1/vartest_error.py`: 변수 스코프 오류

이러한 파일들은 오류 메시지를 확인하고 학습하기 위한 것입니다.

## 외부 라이브러리가 필요한 스크립트

일부 스크립트는 외부 라이브러리를 필요로 합니다:

**SymPy 예제 (`05-7/sympy_test.py`):**
```bash
# SymPy가 설치되어 있지 않다면
pip install sympy

# 실행
python 05-7/sympy_test.py
```

## 인터랙티브 테스트

모듈을 인터랙티브하게 테스트하려면 Python 인터프리터를 사용하세요:

```bash
# Python 인터프리터 시작
python

# 또는 iPython (더 나은 인터랙티브 경험)
ipython
```

```python
>>> # 모듈 임포트
>>> from calculator import Calculator
>>>
>>> # 함수 테스트
>>> from paging import get_total_page
>>> get_total_page(25, 10)
3
```

## 디렉토리 구조 확인

특정 챕터의 모든 예제를 확인하려면:

```bash
# 해당 챕터 디렉토리로 이동
cd 04-1

# 모든 Python 파일 나열
ls *.py

# 모든 Python 파일 순차 실행 (신중하게!)
for file in *.py; do
    echo "Running $file..."
    python "$file"
done
```

## 주의사항

1. **작업 디렉토리**: 일부 스크립트는 현재 작업 디렉토리에 파일을 생성합니다 (예: `memo.txt`). 적절한 디렉토리에서 실행하세요.

2. **상대 임포트**: 패키지 내 상대 임포트를 사용하는 스크립트는 패키지 외부에서 실행해야 합니다.

3. **인코딩**: `07-1/euc_kr.py` 같은 일부 파일은 특정 인코딩을 사용합니다.

4. **파일 경로**: `06-4/memo.py` 같은 스크립트는 절대 경로(`c:/doit/memo.txt`)를 포함할 수 있습니다. 필요시 경로를 수정하세요.
