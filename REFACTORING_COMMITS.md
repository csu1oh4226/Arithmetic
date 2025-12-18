# 리팩토링 커밋 계획

## A. Rename 커밋

### 변경 목록

#### 1. 매개변수 이름 변경
- `a` → `first_number` (첫 번째 숫자)
- `b` → `second_number` (두 번째 숫자)
- `operator` → `operation_symbol` (연산 기호)

**변경 위치:**
- `src/arithmetic/arithmetic_operations.py`: 모든 메서드의 매개변수
- `calculator_console.py`: `calculate()`, `format_expression()`, `display_result()` 함수

**변경 이유:**
- `a`, `b`는 너무 일반적이고 의미가 불명확함
- `first_number`, `second_number`는 의도를 명확히 표현
- `operator`는 연산자 객체를 의미할 수 있어 `operation_symbol`이 더 정확

#### 2. 변수 이름 변경
- `result1`, `result2`, `result3` → `addition_result`, `subtraction_result` 등 의미있는 이름
- `examples` → `calculation_examples` (더 명확한 의미)
- `operation` → `operation_name` (연산 이름)
- `symbol` → `operation_symbol` (연산 기호)

**변경 위치:**
- `src/arithmetic/arithmetic_operations.py`: `if __name__ == "__main__"` 블록 내부

**변경 이유:**
- 숫자로 된 변수명은 의미를 파악하기 어려움
- 의미있는 이름으로 변경하여 코드 가독성 향상

#### 3. 함수/메서드 이름 변경
- 변경 없음 (현재 이름이 이미 명확함)

---

## B. Extract Method 커밋

### 변경 목록

#### 1. `if __name__ == "__main__"` 블록 분리
- `run_basic_arithmetic_tests()` - 기본 사칙연산 테스트 실행
- `run_exception_handling_tests()` - 예외 처리 테스트 실행
- `run_calculation_examples()` - 계산 예제 실행
- `print_separator()` - 구분선 출력 헬퍼 함수

#### 2. `main()` 함수 분리
- `get_user_inputs()` - 사용자 입력 받기
- `perform_calculation()` - 계산 수행
- `display_calculation_result()` - 결과 출력
- `handle_calculation_error()` - 예외 처리

---

## C. 중복 제거 커밋

### 변경 목록

#### 1. 0으로 나누기 검사 로직 통합
- `_validate_divisor()` - 제수 검증 메서드 추출
- `divide()`와 `divide_quotient()`에서 공통 사용

#### 2. 예외 처리 출력 형식 통합
- `display_error()` - 에러 출력 헬퍼 함수
- 중복된 예외 처리 출력 코드 제거

---

## D. 예외/검증 커밋

### 변경 목록

#### 1. 커스텀 예외 클래스 도입
- `DivisionByZeroError` - 0으로 나누기 전용 예외

#### 2. 입력 검증 정책 통일
- 타입 검증 추가
- 예외 처리 정책 문서화

---

## E. 구조 정리 커밋

### 변경 목록

#### 1. Core 로직 분리
- `src/arithmetic/core.py` - 순수 계산 로직
- `src/arithmetic/exceptions.py` - 예외 클래스

#### 2. UI/CLI 분리
- `src/cli/calculator_cli.py` - CLI 인터페이스
- `src/arithmetic/arithmetic_operations.py` - Core 로직만 유지

