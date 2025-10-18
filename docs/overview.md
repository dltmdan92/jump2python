# 저장소 개요 (Repository Overview)

## 프로젝트 정보

**Doit 점프 투 파이썬** (Jump to Python) 책의 예제 코드 저장소입니다.

- **언어**: Python
- **목적**: Python 학습용 예제 및 연습문제
- **구조**: 챕터별 디렉토리 구성 (`01-*` ~ `08-*`)
- **특징**: 한글 주석, 단계별 학습 예제

## 저장소 구조

```
jump2python/
├── 01-* ~ 08-*        # 챕터별 예제 코드
│   ├── 01-1/          # 1장 섹션 1
│   ├── 01-2/          # 1장 섹션 2
│   ├── 02-2/          # 2장 섹션 2 (문자열)
│   ├── 04-1/          # 4장 섹션 1 (함수)
│   ├── 04-3/          # 4장 섹션 3 (파일 I/O)
│   ├── 05-3/          # 5장 섹션 3 (패키지)
│   │   └── game/      # 패키지 예제
│   └── ...
├── 풀이/               # 연습문제 해답
│   ├── 03장/          # 3장 연습문제
│   ├── 04장/          # 4장 연습문제
│   ├── 05장/          # 5장 연습문제
│   └── 코딩면허시험/   # 종합 테스트
├── docs/              # 문서화
│   ├── overview.md    # 이 파일 (저장소 개요)
│   ├── chapters.md    # 챕터별 상세 구조
│   ├── running-code.md # 실행 가이드
│   └── conventions.md # 코드 컨벤션
├── .venv/             # Python 가상 환경
├── .idea/             # PyCharm 설정 (무시)
├── CLAUDE.md          # Claude Code 가이드
└── README.md          # 저장소 소개
```

## 빠른 시작 (Quick Start)

### 1. 가상 환경 활성화

**macOS / Linux:**
```bash
source .venv/bin/activate
```

**Windows:**
```bash
.venv\Scripts\activate
```

### 2. 예제 실행

```bash
# 문자열 포매팅 예제
python 02-2/string_format.py

# 계산기 클래스 예제
python 05-1/calculator.py

# 제너레이터 예제
python 07-3/generator.py
```

### 3. 커맨드라인 도구 사용

```bash
# 메모 추가
python 06-4/memo.py -a "오늘 할 일: Python 공부"

# 메모 보기
python 06-4/memo.py -v

# 탭을 공백으로 변환
python 06-5/tabto4.py input_file.py
```

### 4. 패키지 탐색

```bash
cd 05-3
python -c "from game.graphic.render import render_test; render_test()"
```

## 주요 특징

### 학습 중심 구조
- **단계별 진행**: 기초부터 고급까지 체계적 학습
- **실습 중심**: 모든 개념마다 실행 가능한 예제 제공
- **한글 설명**: 모든 코드에 한글 주석 포함

### 챕터 구성
- **01-02장**: Python 기초 (문법, 문자열, 리스트)
- **03장**: 제어문 (조건문, 반복문)
- **04장**: 함수와 파일 처리
- **05장**: 객체지향 프로그래밍 (클래스, 모듈, 패키지)
- **06장**: 실전 연습 문제
- **07장**: 고급 기능 (데코레이터, 제너레이터, 타입 힌트)
- **08장**: 정규 표현식

### 특수 파일들

#### 의도적 오류 예제
학습 목적으로 오류를 포함하는 파일들:
- `03-1/indent_error.py`, `indent_error2.py`: 들여쓰기 오류
- `04-1/vartest_error.py`: 변수 스코프 오류

이 파일들은 **실행 시 오류가 발생하는 것이 정상**입니다.

#### 커맨드라인 도구
실용적인 CLI 도구 예제:
- `06-4/memo.py`: 간단한 메모 앱 (`-a`: 추가, `-v`: 보기)
- `06-5/tabto4.py`: 탭을 4칸 공백으로 변환
- `06-6/sub_dir_search.py`: 디렉토리 탐색

#### 외부 라이브러리
추가 설치가 필요한 예제:
- `05-7/sympy_test.py`: SymPy (기호 수학)
  ```bash
  pip install sympy
  ```

## 학습 경로

### 초급 (Beginner)
1. 01-02장: Python 기본 문법
2. 03장: 제어문
3. 04장: 함수

### 중급 (Intermediate)
4. 04-3: 파일 I/O
5. 05-1, 05-2: 클래스와 모듈
6. 05-4: 예외 처리

### 고급 (Advanced)
7. 05-3: 패키지 구조
8. 07-2: 클로저와 데코레이터
9. 07-3: 제너레이터와 이터레이터
10. 07-4: 타입 힌트

## Git 작업 시 주의사항

### Git 무시 파일
- `.idea/` - PyCharm IDE 설정 파일 (gitignore에 포함)
- `.venv/` - Python 가상 환경 (gitignore에 포함)
- `.DS_Store` - macOS 시스템 파일 (gitignore에 포함)

### 작업 가이드
- **새 예제 추가**: 적절한 챕터 디렉토리에 배치 (예: `04-1/`, `05-3/`)
- **풀이 추가**: `풀이/` 디렉토리의 해당 챕터에 배치
- **문서 업데이트**: 코드 추가 시 관련 문서(`docs/`)도 함께 업데이트

자세한 작업 가이드는 [conventions.md](conventions.md)를 참조하세요.
