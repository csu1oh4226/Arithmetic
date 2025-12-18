# D. 예외/검증 커밋 - PR 설명

## 📝 변경 목록

### 1. 커스텀 예외 클래스 도입

#### 새로 생성된 파일
- `src/arithmetic/exceptions.py`: 커스텀 예외 클래스 정의

#### 도입한 예외 클래스

1. **`DivisionByZeroError`**
   ```python
   class DivisionByZeroError(ArithmeticError):
       """0으로 나누기 시 발생하는 예외"""
   ```
   - 상속: `ArithmeticError`
   - 용도: 0으로 나누기 전용 예외
   - 이유: 일반 `ArithmeticError`보다 구체적이고 명확한 예외 처리

2. **`InvalidInputError`**
   ```python
   class InvalidInputError(ValueError):
       """잘못된 입력값에 대한 예외"""
   ```
   - 상속: `ValueError`
   - 용도: 잘못된 입력값 처리 (향후 확장용)
   - 이유: 입력 검증 정책 통일을 위한 기반 마련

**변경 위치:**
- 새 파일: `src/arithmetic/exceptions.py`

**변경 이유:**
- 명확성: 일반 예외보다 구체적인 예외로 의도 전달
- 필터링 용이성: 특정 예외만 처리 가능
- 확장성: 향후 추가 예외 처리 정책 적용 용이

---

### 2. 0으로 나누기 예외 처리 통일

#### 변경 전
```python
def _validate_divisor(self, divisor: int) -> None:
    if divisor == 0:
        raise ArithmeticError("Division by zero")
```

#### 변경 후
```python
from src.arithmetic.exceptions import DivisionByZeroError

def _validate_divisor(self, divisor: int) -> None:
    if divisor == 0:
        raise DivisionByZeroError("Division by zero")
```

**변경 위치:**
- `src/arithmetic/arithmetic_operations.py`: `_validate_divisor()` 메서드
- `tests/test_arithmetic_operations.py`: 테스트 케이스 업데이트
- `calculator_console.py`: 예외 처리 업데이트

**변경 이유:**
- 커스텀 예외로 더 명확한 예외 처리
- 예외 타입으로 구분하여 처리 가능

---

### 3. 입력 타입 검증 정책 통일

#### 현재 정책

**CLI 인터페이스**: 재시도 방식
```python
def get_integer_input(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ 올바른 정수를 입력해주세요.")
```

**Core 로직**: 타입 힌트로 검증
```python
def add(self, first_number: int, second_number: int) -> int:
    return first_number + second_number
```

**변경 위치:**
- `calculator_console.py`: 입력 함수에 Docstring 추가 및 향후 확장 가능성 표시

**변경 이유:**
- CLI에서는 사용자 친화적인 재시도 방식 유지
- Core 로직은 순수 함수로 유지하여 다양한 인터페이스에서 사용 가능
- 향후 API 인터페이스에서는 예외를 던지는 방식으로 확장 가능

---

### 4. 예외 처리 정책 문서화

#### README.md에 추가된 섹션

**"예외 처리 정책"** 섹션 추가:
- 0으로 나누기 처리 정책 및 결정 이유
- 입력 타입 검증 정책 및 결정 이유
- 커스텀 예외 클래스 설명
- 예외 처리 가이드
- 정책 변경 이력

**변경 위치:**
- `README.md`: "참고사항" 섹션 다음에 "예외 처리 정책" 섹션 추가

**변경 이유:**
- 예외 처리 정책을 명확히 문서화하여 일관성 유지
- 결정 이유를 기록하여 향후 변경 시 참고 가능
- 개발자 가이드 제공

---

## ✅ 검증 결과

- ✅ 모든 테스트 통과 (24/24)
- ✅ 기능 동작 변경 없음 (예외 타입만 변경)
- ✅ Linter 오류 없음
- ✅ 예외 처리 정책 문서화 완료

---

## 📊 변경 통계

| 항목 | 변경 전 | 변경 후 |
|------|---------|---------|
| 예외 클래스 | `ArithmeticError` (기본) | `DivisionByZeroError` (커스텀) |
| 예외 파일 | 없음 | `src/arithmetic/exceptions.py` |
| 예외 클래스 수 | 0개 | 2개 |
| README 예외 정책 섹션 | 없음 | 추가됨 |

---

## 🎯 변경 목적

이번 리팩토링은 **예외 처리 정책을 통일하고 문서화**하는 것을 목적으로 합니다:

1. **명확성**: 커스텀 예외로 의도 전달
2. **일관성**: 모든 나눗셈 연산에서 동일한 예외 사용
3. **문서화**: 예외 처리 정책과 결정 이유를 명확히 기록
4. **확장성**: 향후 추가 예외 처리 정책 적용 용이

**동작 변경**: 예외 타입만 변경되었으며, 기능은 동일하게 동작합니다.

---

## 📋 예외 처리 정책 요약

### 0으로 나누기

**정책**: 예외를 던지는 방식 (`DivisionByZeroError` 발생)

**결정 이유**:
- 0으로 나누기는 수학적으로 정의되지 않은 연산
- 잘못된 결과를 반환하는 것보다 예외로 명시적 처리
- Python 표준 라이브러리와 일관성 유지

### 입력 타입 검증

**정책**: 
- CLI: 재시도 방식 (사용자 친화적)
- Core: 타입 힌트로 검증 (순수 함수 유지)

**결정 이유**:
- 사용자 경험과 타입 안정성의 균형
- 다양한 인터페이스에서 재사용 가능

---

## 🔍 상세 변경 내용

### 예외 클래스 계층 구조

```
ArithmeticError (Python 기본)
└── DivisionByZeroError (커스텀)

ValueError (Python 기본)
└── InvalidInputError (커스텀, 향후 확장용)
```

### 예외 사용 예시

```python
# Core 로직
try:
    result = calculator.divide(10, 0)
except DivisionByZeroError as e:
    print(f"나눗셈 오류: {e}")

# CLI 인터페이스
try:
    result = calculate(calculator, a, op, b)
except DivisionByZeroError as e:
    _handle_calculation_error(e, "0으로 나누기 오류")
```

---

## 📝 README 문서화 내용

README.md에 다음 내용이 추가되었습니다:

1. **예외 처리 정책** 섹션
   - 0으로 나누기 처리 정책 및 결정 이유
   - 입력 타입 검증 정책 및 결정 이유
   - 커스텀 예외 클래스 설명

2. **예외 처리 가이드**
   - Core 로직에서의 예외 처리 방법
   - CLI 인터페이스에서의 예외 처리 방법

3. **정책 변경 이력**
   - 버전별 변경 내용 추적

