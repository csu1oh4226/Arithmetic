# 기본 사칙연산 메서드 최소 단위 구현 시나리오

## 개요
TDD (Test-Driven Development)의 Green 단계에 따라, 각 메서드를 최소 단위로 하나씩 구현하는 시나리오입니다.

## 전제 조건
- Python 3.10.11 환경
- pytest 테스트 프레임워크
- 기존 테스트 케이스가 모두 작성되어 있음 (Red 단계 완료)

---

## 구현 시나리오

### Phase 1: 덧셈 메서드 (`add`) 구현

#### Step 1.1: 최소 구현
- **목표**: `test_addition_positive_numbers` 테스트 통과
- **구현 내용**:
  ```python
  def add(self, a: int, b: int) -> int:
      return a + b
  ```
- **검증**: 
  - `pytest tests/test_arithmetic_operations.py::TestArithmeticOperations::test_addition_positive_numbers -v`
  - 예상 결과: ✅ PASSED

#### Step 1.2: 추가 테스트 통과 확인
- **목표**: `test_addition_with_zero`, `test_addition_negative_numbers` 테스트 통과
- **구현 내용**: Step 1.1의 구현으로 자동 통과 (추가 구현 불필요)
- **검증**:
  - `pytest tests/test_arithmetic_operations.py::TestArithmeticOperations::test_addition_with_zero -v`
  - `pytest tests/test_arithmetic_operations.py::TestArithmeticOperations::test_addition_negative_numbers -v`
  - 예상 결과: ✅ 모두 PASSED

**Phase 1 완료 기준**: 덧셈 관련 테스트 3개 모두 통과

---

### Phase 2: 뺄셈 메서드 (`subtract`) 구현

#### Step 2.1: 최소 구현
- **목표**: `test_subtraction` 테스트 통과
- **구현 내용**:
  ```python
  def subtract(self, a: int, b: int) -> int:
      return a - b
  ```
- **검증**:
  - `pytest tests/test_arithmetic_operations.py::TestArithmeticOperations::test_subtraction -v`
  - 예상 결과: ✅ PASSED

**Phase 2 완료 기준**: 뺄셈 테스트 1개 통과

---

### Phase 3: 곱셈 메서드 (`multiply`) 구현

#### Step 3.1: 최소 구현
- **목표**: `test_multiplication_negative_numbers` 테스트 통과
- **구현 내용**:
  ```python
  def multiply(self, a: int, b: int) -> int:
      return a * b
  ```
- **검증**:
  - `pytest tests/test_arithmetic_operations.py::TestArithmeticOperations::test_multiplication_negative_numbers -v`
  - 예상 결과: ✅ PASSED

#### Step 3.2: 추가 테스트 통과 확인
- **목표**: `test_multiplication_with_zero` 테스트 통과
- **구현 내용**: Step 3.1의 구현으로 자동 통과 (추가 구현 불필요)
- **검증**:
  - `pytest tests/test_arithmetic_operations.py::TestArithmeticOperations::test_multiplication_with_zero -v`
  - 예상 결과: ✅ PASSED

**Phase 3 완료 기준**: 곱셈 관련 테스트 2개 모두 통과

---

### Phase 4: 정수 나눗셈 메서드 (`divide`) 구현

#### Step 4.1: 기본 나눗셈 구현
- **목표**: `test_division_integer`, `test_division_negative_number` 테스트 통과
- **구현 내용**:
  ```python
  def divide(self, a: int, b: int) -> int:
      return a // b
  ```
- **검증**:
  - `pytest tests/test_arithmetic_operations.py::TestArithmeticOperations::test_division_integer -v`
  - `pytest tests/test_arithmetic_operations.py::TestArithmeticOperations::test_division_negative_number -v`
  - 예상 결과: ✅ 모두 PASSED

#### Step 4.2: 예외 처리 추가
- **목표**: `test_division_by_zero` 테스트 통과
- **구현 내용**:
  ```python
  def divide(self, a: int, b: int) -> int:
      if b == 0:
          raise ArithmeticError("Division by zero")
      return a // b
  ```
- **검증**:
  - `pytest tests/test_arithmetic_operations.py::TestArithmeticOperations::test_division_by_zero -v`
  - 예상 결과: ✅ PASSED (예외가 정상적으로 발생)

**Phase 4 완료 기준**: 나눗셈 관련 테스트 3개 모두 통과 (예외 처리 포함)

---

### Phase 5: 소수점 나눗셈 메서드 (`divide_quotient`) 구현

#### Step 5.1: 기본 소수점 나눗셈 구현
- **목표**: `test_division_quotient` 테스트 통과
- **구현 내용**:
  ```python
  def divide_quotient(self, a: int, b: int) -> float:
      return a / b
  ```
- **검증**:
  - `pytest tests/test_arithmetic_operations.py::TestArithmeticOperations::test_division_quotient -v`
  - 예상 결과: ✅ PASSED

#### Step 5.2: 예외 처리 추가
- **목표**: `divide_quotient` 메서드의 0으로 나누기 예외 처리
- **구현 내용**:
  ```python
  def divide_quotient(self, a: int, b: int) -> float:
      if b == 0:
          raise ArithmeticError("Division by zero")
      return a / b
  ```
- **검증**:
  - 수동 테스트: `calculator.divide_quotient(5, 0)` 호출 시 예외 발생 확인
  - 예상 결과: ✅ ArithmeticError 발생

**Phase 5 완료 기준**: 소수점 나눗셈 테스트 1개 통과 및 예외 처리 구현

---

## 최종 검증

### 전체 테스트 실행
```bash
pytest tests/test_arithmetic_operations.py -v
```

### 예상 결과
```
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

============================= 10 passed in 0.04s =============================
```

---

## 구현 순서 요약

1. ✅ **Phase 1**: `add()` 메서드 구현 (덧셈)
2. ✅ **Phase 2**: `subtract()` 메서드 구현 (뺄셈)
3. ✅ **Phase 3**: `multiply()` 메서드 구현 (곱셈)
4. ✅ **Phase 4**: `divide()` 메서드 구현 (정수 나눗셈 + 예외 처리)
5. ✅ **Phase 5**: `divide_quotient()` 메서드 구현 (소수점 나눗셈 + 예외 처리)

---

## 주의사항

1. **최소 구현 원칙**: 각 Phase에서 테스트를 통과하는 최소한의 코드만 작성
2. **단계별 검증**: 각 Phase 완료 후 해당 테스트가 통과하는지 확인
3. **예외 처리**: 나눗셈 메서드는 반드시 0으로 나누기 예외 처리 포함
4. **타입 힌트**: Python 타입 힌트를 명시하여 코드 가독성 향상

---

## 완료 기준

- [x] Phase 1: 덧셈 메서드 구현 완료
- [x] Phase 2: 뺄셈 메서드 구현 완료
- [x] Phase 3: 곱셈 메서드 구현 완료
- [x] Phase 4: 정수 나눗셈 메서드 구현 완료 (예외 처리 포함)
- [x] Phase 5: 소수점 나눗셈 메서드 구현 완료 (예외 처리 포함)
- [x] 전체 테스트 10개 모두 통과
- [x] 컴파일/런타임 오류 없음

---

**시나리오 작성일**: 2025-12-16  
**버전**: v1.0

