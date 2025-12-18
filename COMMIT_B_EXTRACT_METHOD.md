# B. Extract Method 커밋 - PR 설명

## 📝 변경 목록

### 1. `if __name__ == "__main__"` 블록 분리

#### 변경 전
- 97줄의 긴 블록이 모든 로직을 포함
- 테스트 실행, 예외 처리, 예제 실행이 모두 한 곳에 있음

#### 변경 후
다음 함수들로 분리:

1. **`_print_separator(length, character)`**
   - 책임: 구분선 출력
   - 위치: `src/arithmetic/arithmetic_operations.py`
   - 이유: 구분선 출력 로직이 여러 곳에서 중복 사용됨

2. **`_print_header()`**
   - 책임: 프로그램 헤더 출력
   - 위치: `src/arithmetic/arithmetic_operations.py`
   - 이유: 헤더 출력 로직을 독립적으로 관리

3. **`_run_basic_arithmetic_tests(calculator)`**
   - 책임: 기본 사칙연산 테스트 실행 및 결과 출력
   - 위치: `src/arithmetic/arithmetic_operations.py`
   - 이유: 테스트 실행 로직을 독립적으로 관리

4. **`_run_exception_handling_tests(calculator)`**
   - 책임: 예외 처리 테스트 실행 및 결과 출력
   - 위치: `src/arithmetic/arithmetic_operations.py`
   - 이유: 예외 처리 테스트 로직을 독립적으로 관리

5. **`_execute_calculation_by_operation(calculator, first_number, second_number, operation_name)`**
   - 책임: 연산 이름에 따라 계산 수행
   - 위치: `src/arithmetic/arithmetic_operations.py`
   - 이유: if-elif 체인을 별도 함수로 분리하여 가독성 향상

6. **`_run_calculation_examples(calculator)`**
   - 책임: 계산 예제 실행 및 결과 출력
   - 위치: `src/arithmetic/arithmetic_operations.py`
   - 이유: 예제 실행 로직을 독립적으로 관리

7. **`_run_demo()`**
   - 책임: 전체 데모 프로그램 실행 흐름 관리
   - 위치: `src/arithmetic/arithmetic_operations.py`
   - 이유: 메인 실행 로직을 명확하게 분리

**변경 위치:**
- `src/arithmetic/arithmetic_operations.py`: `if __name__ == "__main__"` 블록

**변경 이유:**
- 긴 함수를 작은 단위로 분리하여 가독성 향상
- 각 함수의 책임을 명확히 하여 유지보수성 개선
- 테스트 가능한 단위로 분리

---

### 2. `main()` 함수 분리

#### 변경 전
- 입력 처리, 계산, 출력, 예외 처리가 모두 한 함수에 있음
- 예외 처리 블록이 중복됨

#### 변경 후
다음 함수들로 분리:

1. **`_print_separator(length, character)`**
   - 책임: 구분선 출력
   - 위치: `calculator_console.py`
   - 이유: 구분선 출력 로직 재사용

2. **`_get_user_inputs()`**
   - 책임: 사용자로부터 입력 받기
   - 위치: `calculator_console.py`
   - 반환값: `(first_number, operation_symbol, second_number)` 튜플
   - 이유: 입력 처리 로직을 독립적으로 관리

3. **`_perform_calculation(calculator, first_number, operation_symbol, second_number)`**
   - 책임: 계산 수행
   - 위치: `calculator_console.py`
   - 이유: 계산 로직을 독립적으로 관리

4. **`_display_calculation_result(first_number, operation_symbol, second_number, calculation_result)`**
   - 책임: 계산 결과 출력
   - 위치: `calculator_console.py`
   - 이유: 출력 로직을 독립적으로 관리

5. **`_handle_calculation_error(error, error_type)`**
   - 책임: 계산 오류 처리 및 사용자에게 표시
   - 위치: `calculator_console.py`
   - 이유: 중복된 예외 처리 로직을 통합

**변경 위치:**
- `calculator_console.py`: `main()` 함수

**변경 이유:**
- Single Responsibility Principle 준수
- 각 함수의 책임을 명확히 하여 테스트 및 유지보수 용이
- 중복 코드 제거

---

## ✅ 검증 결과

- ✅ 모든 테스트 통과 (24/24)
- ✅ 기능 동작 변경 없음
- ✅ Linter 오류 없음
- ✅ 각 함수의 책임이 명확함

---

## 📊 변경 통계

| 항목 | 변경 전 | 변경 후 |
|------|---------|---------|
| `if __name__ == "__main__"` 블록 | 97줄 (단일 블록) | 7개 함수로 분리 |
| `main()` 함수 | 32줄 (다중 책임) | 5개 함수로 분리 |
| 최대 함수 길이 | 97줄 | 약 20줄 이하 |
| 함수 개수 증가 | - | +12개 함수 |

---

## 🎯 변경 목적

이번 리팩토링은 **긴 함수를 작은 메서드로 분리**하여 코드 가독성과 유지보수성을 향상시키는 것을 목적으로 합니다:

1. **가독성 향상**: 각 함수가 하나의 명확한 책임을 가짐
2. **재사용성 향상**: 작은 함수 단위로 재사용 가능
3. **테스트 용이성**: 각 함수를 독립적으로 테스트 가능
4. **유지보수성 향상**: 변경 시 영향 범위가 명확함
5. **Single Responsibility Principle 준수**: 각 함수가 하나의 책임만 담당

**동작 변경 없음**: 모든 기능은 기존과 동일하게 동작하며, 구조만 개선되었습니다.

---

## 📋 함수별 책임 요약

### `arithmetic_operations.py`

| 함수 | 책임 | 접근성 |
|------|------|--------|
| `_print_separator()` | 구분선 출력 | private |
| `_print_header()` | 헤더 출력 | private |
| `_run_basic_arithmetic_tests()` | 기본 테스트 실행 | private |
| `_run_exception_handling_tests()` | 예외 테스트 실행 | private |
| `_execute_calculation_by_operation()` | 연산별 계산 수행 | private |
| `_run_calculation_examples()` | 예제 실행 | private |
| `_run_demo()` | 데모 프로그램 실행 | private |

### `calculator_console.py`

| 함수 | 책임 | 접근성 |
|------|------|--------|
| `_print_separator()` | 구분선 출력 | private |
| `_get_user_inputs()` | 사용자 입력 받기 | private |
| `_perform_calculation()` | 계산 수행 | private |
| `_display_calculation_result()` | 결과 출력 | private |
| `_handle_calculation_error()` | 오류 처리 | private |
| `main()` | 프로그램 실행 흐름 관리 | public |

