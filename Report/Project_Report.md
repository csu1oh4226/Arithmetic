# 사칙연산 시스템 프로젝트 리포트

## 프로젝트 정보

- **프로젝트명**: 사칙연산 시스템 (Arithmetic Operations)
- **테스트 ID**: TC-CMM-001 (Common Module) / TC-AO-001 (Arithmetic Operations)
- **작성일**: 2025-12-16
- **버전**: v1.0
- **개발 방법론**: TDD (Test-Driven Development) - Red-Green-Refactor
- **프로그래밍 언어**: Python 3.10
- **테스트 프레임워크**: pytest 9.0.2
- **Git 저장소**: https://github.com/csu1oh4226/Arithmetic.git
- **현재 브랜치**: red

---

## 목차

1. [프로젝트 개요](#프로젝트-개요)
2. [작업 단계별 진행 내용](#작업-단계별-진행-내용)
3. [구현된 기능](#구현된-기능)
4. [테스트 케이스 및 결과](#테스트-케이스-및-결과)
5. [테스트 커버리지](#테스트-커버리지)
6. [프로젝트 구조](#프로젝트-구조)
7. [Git 커밋 이력](#git-커밋-이력)
8. [결론 및 향후 계획](#결론-및-향후-계획)

---

## 프로젝트 개요

이 프로젝트는 사칙연산(덧셈, 뺄셈, 곱셈, 나눗셈)의 정확도를 검증하는 애플리케이션입니다. 다양한 경계 조건과 예외 상황을 처리하여 견고한 산술 연산 기능을 제공합니다.

### 주요 목표

- TDD 방식(Red-Green-Refactor)을 통한 견고한 코드 작성
- 다양한 경계 조건 및 예외 상황 처리
- 높은 테스트 커버리지 달성
- 명확한 코드 구조 및 문서화

---

## 작업 단계별 진행 내용

### 1단계: 프로젝트 구조 생성

#### 생성된 디렉토리 구조
```
ARITHMETIC/
├── src/
│   └── arithmetic/
│       ├── __init__.py
│       └── arithmetic_operations.py
├── tests/
│   ├── __init__.py
│   └── test_arithmetic_operations.py
├── pytest.ini
├── requirements.txt
└── README.md
```

#### 생성된 설정 파일
- **pytest.ini**: pytest 테스트 실행 설정
- **requirements.txt**: 프로젝트 의존성 (pytest, pytest-cov)

---

### 2단계: Red 단계 - 실패하는 테스트 작성

#### 테스트 파일 작성
- `tests/test_arithmetic_operations.py` 파일 생성
- 10개의 테스트 케이스 작성
- 모든 테스트가 실패하는 상태 확인 (Red 단계 목표 달성)

#### 테스트 실행 결과 (Red 단계)
```
============================= test session starts =============================
collected 10 items

tests/test_arithmetic_operations.py::TestArithmeticOperations::test_addition_positive_numbers FAILED
tests/test_arithmetic_operations.py::TestArithmeticOperations::test_addition_with_zero FAILED
tests/test_arithmetic_operations.py::TestArithmeticOperations::test_division_by_zero FAILED
tests/test_arithmetic_operations.py::TestArithmeticOperations::test_addition_negative_numbers FAILED
tests/test_arithmetic_operations.py::TestArithmeticOperations::test_subtraction FAILED
tests/test_arithmetic_operations.py::TestArithmeticOperations::test_multiplication_negative_numbers FAILED
tests/test_arithmetic_operations.py::TestArithmeticOperations::test_division_integer FAILED
tests/test_arithmetic_operations.py::TestArithmeticOperations::test_division_quotient FAILED
tests/test_arithmetic_operations.py::TestArithmeticOperations::test_multiplication_with_zero FAILED
tests/test_arithmetic_operations.py::TestArithmeticOperations::test_division_negative_number FAILED

============================= 10 failed in 0.16s ==============================
```

**결과**: ✅ Red 단계 완료 - 모든 테스트가 예상대로 실패

---

### 3단계: Green 단계 - 테스트를 통과하는 최소 구현

#### 구현된 메서드

1. **`add(a, b)`** - 덧셈
   ```python
   def add(self, a: int, b: int) -> int:
       return a + b
   ```

2. **`subtract(a, b)`** - 뺄셈
   ```python
   def subtract(self, a: int, b: int) -> int:
       return a - b
   ```

3. **`multiply(a, b)`** - 곱셈
   ```python
   def multiply(self, a: int, b: int) -> int:
       return a * b
   ```

4. **`divide(a, b)`** - 정수 나눗셈
   ```python
   def divide(self, a: int, b: int) -> int:
       if b == 0:
           raise ArithmeticError("Division by zero")
       return a // b
   ```

5. **`divide_quotient(a, b)`** - 소수점 나눗셈
   ```python
   def divide_quotient(self, a: int, b: int) -> float:
       if b == 0:
           raise ArithmeticError("Division by zero")
       return a / b
   ```

#### 테스트 실행 결과 (Green 단계)
```
============================= test session starts =============================
collected 10 items

tests/test_arithmetic_operations.py::TestArithmeticOperations::test_addition_positive_numbers PASSED
tests/test_arithmetic_operations.py::TestArithmeticOperations::test_addition_with_zero PASSED
tests/test_arithmetic_operations.py::TestArithmeticOperations::test_division_by_zero PASSED
tests/test_arithmetic_operations.py::TestArithmeticOperations::test_addition_negative_numbers PASSED
tests/test_arithmetic_operations.py::TestArithmeticOperations::test_subtraction PASSED
tests/test_arithmetic_operations.py::TestArithmeticOperations::test_multiplication_negative_numbers PASSED
tests/test_arithmetic_operations.py::TestArithmeticOperations::test_division_integer PASSED
tests/test_arithmetic_operations.py::TestArithmeticOperations::test_division_quotient PASSED
tests/test_arithmetic_operations.py::TestArithmeticOperations::test_multiplication_with_zero PASSED
tests/test_arithmetic_operations.py::TestArithmeticOperations::test_division_negative_number PASSED

============================= 10 passed in 0.03s ==============================
```

**결과**: ✅ Green 단계 완료 - 모든 테스트 통과

---

## 구현된 기능

### ArithmeticOperations 클래스

사칙연산을 수행하는 클래스로, 다음 5개의 메서드를 제공합니다:

| 메서드 | 설명 | 반환 타입 | 예외 처리 |
|--------|------|----------|----------|
| `add(a, b)` | 두 정수의 덧셈 | `int` | 없음 |
| `subtract(a, b)` | 두 정수의 뺄셈 | `int` | 없음 |
| `multiply(a, b)` | 두 정수의 곱셈 | `int` | 없음 |
| `divide(a, b)` | 두 정수의 정수 나눗셈 | `int` | `ArithmeticError` (b=0) |
| `divide_quotient(a, b)` | 두 정수의 소수점 나눗셈 | `float` | `ArithmeticError` (b=0) |

### 주요 특징

- **타입 힌팅**: 모든 메서드에 타입 힌팅 적용
- **문서화**: 모든 메서드에 docstring 작성
- **예외 처리**: 0으로 나누기 시 `ArithmeticError` 발생
- **정수/소수점 나눗셈 구분**: `divide()`와 `divide_quotient()` 메서드로 구분

---

## 테스트 케이스 및 결과

### 테스트 케이스 상세

| # | 테스트 케이스 | 입력값 | 예상 결과 | 중요도 | 상태 |
|---|--------------|--------|----------|--------|------|
| 1 | 덧셈 (양수) | 1 + 10 | 11 | 중요 | ✅ PASSED |
| 2 | 덧셈 (0 포함) | 0 + 1 | 1 | 중요 | ✅ PASSED |
| 3 | 나눗셈 (0으로 나누기) | 0 / 0 | ArithmeticError 예외 발생 | 중요 | ✅ PASSED |
| 4 | 덧셈 (음수) | -1 + (-10) | -11 | 보통 | ✅ PASSED |
| 5 | 뺄셈 | 5 - 2 | 3 | 중요 | ✅ PASSED |
| 6 | 곱셈 (음수) | -5 * -3 | 15 | 보통 | ✅ PASSED |
| 7 | 나눗셈 (정수) | 5 / 2 | 2 | 중요 | ✅ PASSED |
| 8 | 나눗셈 (몫, 소수점) | 5 ÷ 2 | 2.5 | 보통 | ✅ PASSED |
| 9 | 곱셈 (0 포함) | 0 * 10 | 0 | 낮음 | ✅ PASSED |
| 10 | 나눗셈 (음수) | -10 / 2 | -5 | 중요 | ✅ PASSED |

### 테스트 결과 요약

- **총 테스트 케이스**: 10개
- **통과한 테스트**: 10개 (100%)
- **실패한 테스트**: 0개
- **테스트 실행 시간**: 0.03초

### 테스트 코드 예시

```python
def test_addition_positive_numbers(self):
    """덧셈 테스트: 양수"""
    # 입력: 1 + 10
    # 예상 결과: 11
    assert self.calculator.add(1, 10) == 11

def test_division_by_zero(self):
    """나눗셈 테스트: 0으로 나누기 (예외 발생)"""
    # 입력: 0 / 0
    # 예상 결과: ArithmeticError 예외 발생
    with pytest.raises(ArithmeticError):
        self.calculator.divide(0, 0)
```

---

## 테스트 커버리지

### 커버리지 결과

```
Name                                      Stmts   Miss  Cover   Missing
-----------------------------------------------------------------------
src\arithmetic\arithmetic_operations.py      15      1    93%   84
-----------------------------------------------------------------------
TOTAL                                        15      1    93%
```

### 커버리지 분석

- **전체 커버리지**: 93%
- **커버된 라인**: 14줄
- **커버되지 않은 라인**: 1줄 (84번 라인)

### 커버되지 않은 코드

**84번 라인**: `divide_quotient()` 메서드의 0으로 나누기 예외 처리
```python
if b == 0:
    raise ArithmeticError("Division by zero")  # 84번 라인 (커버되지 않음)
```

**이유**: 현재 테스트에서 `divide(0, 0)`만 테스트하고 있으며, `divide_quotient(0, 0)`는 테스트하지 않아 해당 예외 경로가 커버되지 않았습니다.

### 커버리지 개선 제안

100% 커버리지를 달성하기 위해 다음 테스트를 추가할 수 있습니다:

```python
def test_division_quotient_by_zero(self):
    """나눗셈 테스트: divide_quotient 0으로 나누기"""
    with pytest.raises(ArithmeticError):
        self.calculator.divide_quotient(0, 0)
```

---

## 프로젝트 구조

### 최종 디렉토리 구조

```
ARITHMETIC/
├── README.md                          # 프로젝트 문서
├── requirements.txt                   # Python 의존성
├── pytest.ini                         # pytest 설정
├── .gitignore                         # Git 무시 파일
├── src/                               # 소스 코드
│   └── arithmetic/
│       ├── __init__.py
│       └── arithmetic_operations.py   # 메인 클래스
├── tests/                             # 테스트 코드
│   ├── __init__.py
│   └── test_arithmetic_operations.py  # 테스트 케이스
├── htmlcov/                           # 커버리지 HTML 리포트
└── Report/                            # 프로젝트 리포트
    └── Project_Report.md              # 이 문서
```

### 주요 파일 설명

| 파일 | 설명 |
|------|------|
| `src/arithmetic/arithmetic_operations.py` | 사칙연산 기능을 제공하는 메인 클래스 |
| `tests/test_arithmetic_operations.py` | 모든 테스트 케이스를 포함하는 테스트 파일 |
| `pytest.ini` | pytest 실행 설정 (테스트 경로, 옵션 등) |
| `requirements.txt` | 프로젝트 의존성 (pytest, pytest-cov) |

---

## Git 커밋 이력

### 커밋 내역

```
9a0baaa (HEAD -> red, origin/red) Complete Green step: Implement all arithmetic operations
022c334 Implement add() function - Green step for addition operations
3b9141e Update README: Change to Arithmetic Operations test cases with Red-Green-Refactor guide
f264f83 (origin/main, main) Initial commit: Add README and project setup files
```

### 커밋 상세

#### 1. Initial commit (f264f83)
- README.md 추가
- .gitignore 추가
- requirements.txt 추가

#### 2. Update README (3b9141e)
- README를 사칙연산 테스트 케이스에 맞게 업데이트
- Red-Green-Refactor 가이드 추가
- Java에서 Python으로 변경

#### 3. Implement add() function (022c334)
- `add()` 메서드 구현
- 덧셈 관련 3개 테스트 통과 확인

#### 4. Complete Green step (9a0baaa)
- 모든 산술 연산 메서드 구현
  - `subtract()`, `multiply()`, `divide()`, `divide_quotient()`
- 프로젝트 구조 완성
  - `src/arithmetic/` 디렉토리
  - `tests/` 디렉토리
  - `pytest.ini` 설정 파일
- 모든 10개 테스트 케이스 통과

### 브랜치 정보

- **main**: 메인 브랜치 (초기 설정)
- **red**: 현재 작업 브랜치 (Red-Green 단계 완료)

---

## 결론 및 향후 계획

### 완료된 작업

✅ **Red 단계**: 실패하는 테스트 작성 완료  
✅ **Green 단계**: 모든 테스트를 통과하는 코드 구현 완료  
✅ **프로젝트 구조**: 표준 Python 프로젝트 구조 생성  
✅ **테스트 커버리지**: 93% 달성  
✅ **문서화**: README 및 코드 문서화 완료  

### 현재 상태

- **테스트 통과율**: 100% (10/10)
- **코드 커버리지**: 93%
- **구현된 기능**: 5개 메서드 (사칙연산 전체)
- **예외 처리**: 0으로 나누기 예외 처리 구현

### 향후 계획

#### Refactor 단계 (다음 단계)

1. **코드 개선**
   - 중복 코드 제거 (0으로 나누기 검사 로직)
   - 코드 가독성 향상
   - 성능 최적화 (필요시)

2. **테스트 커버리지 향상**
   - `divide_quotient()`의 0으로 나누기 테스트 추가
   - 100% 커버리지 달성

3. **추가 기능 검토**
   - 입력 검증 강화
   - 로깅 기능 추가
   - 에러 메시지 개선

4. **문서화 개선**
   - API 문서 자동 생성 (Sphinx 등)
   - 사용 예제 추가

### 권장 사항

1. **Refactor 브랜치 생성**: 코드 개선 작업을 위한 별도 브랜치 생성
2. **CI/CD 파이프라인**: 자동 테스트 실행 및 커버리지 체크
3. **코드 리뷰**: 팀 내 코드 리뷰 진행
4. **성능 테스트**: 대용량 데이터에 대한 성능 테스트 추가

---

## 부록

### A. 테스트 실행 명령어

```bash
# 전체 테스트 실행
python -m pytest tests/test_arithmetic_operations.py -v

# 커버리지 포함 테스트 실행
python -m pytest tests/test_arithmetic_operations.py --cov=src.arithmetic.arithmetic_operations --cov-report=term-missing

# HTML 커버리지 리포트 생성
python -m pytest tests/test_arithmetic_operations.py --cov=src.arithmetic.arithmetic_operations --cov-report=html
```

### B. 프로젝트 의존성

```
pytest>=7.0.0
pytest-cov>=4.0.0
```

### C. 환경 요구사항

- Python 3.10 이상
- pytest 9.0.2
- Windows 10 (개발 환경)

---

**작성일**: 2025-12-16  
**작성자**: 개발팀  
**문서 버전**: v1.0

