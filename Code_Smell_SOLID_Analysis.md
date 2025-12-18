# 코드 스멜 및 SOLID 위반 분석 리포트

**분석 일시**: 2025-12-16  
**프로젝트**: 사칙연산 시스템 (Arithmetic Operations)  
**분석 대상 파일**:
- `src/arithmetic/arithmetic_operations.py`
- `calculator_console.py`
- `tests/test_arithmetic_operations.py`

---

## 📊 코드 스멜 분석 표

| # | 코드 스멜 유형 | 발견 위치 | 문제 설명 | 리팩토링 기법 | 우선순위 |
|---|--------------|----------|----------|--------------|---------|
| 1 | **중복 코드** | `arithmetic_operations.py:65-66, 83-84` | `divide()`와 `divide_quotient()`에서 0으로 나누기 검사 로직 중복 | Extract Method, Template Method Pattern | **High** |
| 2 | **긴 함수** | `arithmetic_operations.py:88-184` | `if __name__ == "__main__"` 블록이 97줄로 너무 김 (테스트/출력/예제 모두 포함) | Extract Method, Move Method | **High** |
| 3 | **중복 코드** | `calculator_console.py:56-67` | `calculate()` 함수의 if-elif 체인으로 연산자 처리 중복 | Strategy Pattern, Command Pattern | **High** |
| 4 | **매직 넘버** | `calculator_console.py:97, 127, 132` | `"=" * 40`, `"=" * 60` 등 하드코딩된 구분선 길이 | Extract Constant, Named Constants | **Med** |
| 5 | **의미없는 이름** | `arithmetic_operations.py:12, 25, 38, 51, 69` | 매개변수 이름 `a`, `b`가 너무 일반적임 | Rename Variable (first_number, second_number) | **Med** |
| 6 | **예외 처리** | `arithmetic_operations.py:65-66, 83-84` | 기본 `ArithmeticError` 사용, 커스텀 예외 클래스 없음 | Replace Exception with Custom Exception | **Med** |
| 7 | **긴 함수** | `calculator_console.py:103-134` | `main()` 함수가 입력/계산/출력/예외처리 모두 담당 | Extract Method, Single Responsibility | **Med** |
| 8 | **의존성** | `calculator_console.py:7, 107` | `ArithmeticOperations` 구체 클래스에 직접 의존 | Dependency Injection, Interface Segregation | **Med** |
| 9 | **중복 코드** | `calculator_console.py:125-133` | 예외 처리 블록에서 출력 형식 중복 | Extract Method | **Low** |
| 10 | **매직 넘버** | `arithmetic_operations.py:92, 102, 135, 152` | `"=" * 60`, `"-" * 60` 등 하드코딩된 구분선 | Extract Constant | **Low** |
| 11 | **의미없는 이름** | `calculator_console.py:43, 70, 85` | 함수 매개변수 `a`, `b`, `operator`가 일반적 | Rename Variable | **Low** |
| 12 | **중복 코드** | `arithmetic_operations.py:168-177` | if-elif 체인으로 연산자별 메서드 호출 중복 | Strategy Pattern | **Low** |

---

## 🔍 SOLID 원칙 위반 분석 표

| # | SOLID 원칙 | 위반 위치 | 위반 내용 | 리팩토링 기법 | 우선순위 |
|---|-----------|----------|----------|--------------|---------|
| 1 | **SRP (Single Responsibility)** | `arithmetic_operations.py:88-184` | `if __name__ == "__main__"` 블록이 테스트 실행, 결과 출력, 예제 실행 등 여러 책임 | Extract Class, Separate Concerns | **High** |
| 2 | **SRP** | `calculator_console.py:103-134` | `main()` 함수가 입력 처리, 계산, 출력, 예외 처리 모두 담당 | Extract Method, Single Responsibility | **High** |
| 3 | **OCP (Open/Closed)** | `calculator_console.py:56-67` | `calculate()` 함수의 if-elif 체인으로 새 연산자 추가 시 수정 필요 | Strategy Pattern, Factory Pattern | **High** |
| 4 | **OCP** | `arithmetic_operations.py:168-177` | 연산자별 if-elif 체인으로 확장 시 수정 필요 | Strategy Pattern | **Med** |
| 5 | **DIP (Dependency Inversion)** | `calculator_console.py:7, 107` | 구체 클래스 `ArithmeticOperations`에 직접 의존 | Dependency Injection, Abstract Interface | **Med** |
| 6 | **SRP** | `arithmetic_operations.py:51-67, 69-85` | `divide()`와 `divide_quotient()`가 유사한 책임을 가짐 | Extract Common Method | **Med** |
| 7 | **OCP** | `calculator_console.py:34` | 하드코딩된 연산자 리스트로 확장 시 수정 필요 | Configuration, Strategy Pattern | **Low** |

---

## 📋 상세 분석 및 리팩토링 제안

### 🔴 High 우선순위

#### 1. 중복 코드: 0으로 나누기 검사 로직
**위치**: `arithmetic_operations.py:65-66, 83-84`

```python
# 현재 코드 (중복)
def divide(self, a: int, b: int) -> int:
    if b == 0:
        raise ArithmeticError("Division by zero")
    return a // b

def divide_quotient(self, a: int, b: int) -> float:
    if b == 0:
        raise ArithmeticError("Division by zero")
    return a / b
```

**리팩토링 기법**: Extract Method
```python
def _validate_divisor(self, b: int) -> None:
    """나눗셈 전 제수 검증"""
    if b == 0:
        raise ArithmeticError("Division by zero")

def divide(self, a: int, b: int) -> int:
    self._validate_divisor(b)
    return a // b

def divide_quotient(self, a: int, b: int) -> float:
    self._validate_divisor(b)
    return a / b
```

#### 2. 긴 함수: `if __name__ == "__main__"` 블록
**위치**: `arithmetic_operations.py:88-184` (97줄)

**리팩토링 기법**: Extract Method, Move Method
- 테스트 실행 로직을 별도 함수로 분리
- 출력 형식화를 별도 함수로 분리
- 예제 실행을 별도 함수로 분리

#### 3. 중복 코드: 연산자 처리 if-elif 체인
**위치**: `calculator_console.py:56-67`

**리팩토링 기법**: Strategy Pattern
```python
class OperationStrategy:
    def execute(self, a: int, b: int):
        raise NotImplementedError

class AddStrategy(OperationStrategy):
    def execute(self, a: int, b: int):
        return calculator.add(a, b)

# Strategy Factory 사용
OPERATION_STRATEGIES = {
    '+': AddStrategy(),
    '-': SubtractStrategy(),
    # ...
}
```

#### 4. SRP 위반: `main()` 함수의 다중 책임
**위치**: `calculator_console.py:103-134`

**리팩토링 기법**: Extract Method
- 입력 처리: `get_user_inputs()`
- 계산 수행: `perform_calculation()`
- 결과 출력: `display_calculation_result()`
- 예외 처리: 별도 핸들러

#### 5. OCP 위반: 연산자 처리 확장성 부족
**위치**: `calculator_console.py:56-67`

**리팩토링 기법**: Strategy Pattern + Factory Pattern
- 새로운 연산자 추가 시 기존 코드 수정 없이 확장 가능

---

### 🟡 Med 우선순위

#### 6. 매직 넘버: 하드코딩된 구분선 길이
**위치**: `calculator_console.py:97, 127, 132`

**리팩토링 기법**: Extract Constant
```python
SEPARATOR_LENGTH = 40
LONG_SEPARATOR_LENGTH = 60

print("=" * SEPARATOR_LENGTH)
```

#### 7. 의미없는 이름: 매개변수 `a`, `b`
**위치**: `arithmetic_operations.py` 전체

**리팩토링 기법**: Rename Variable
```python
def add(self, first_number: int, second_number: int) -> int:
    return first_number + second_number
```

#### 8. 예외 처리: 커스텀 예외 클래스 부재
**위치**: `arithmetic_operations.py:65-66, 83-84`

**리팩토링 기법**: Replace Exception with Custom Exception
```python
class DivisionByZeroError(ArithmeticError):
    """0으로 나누기 시 발생하는 예외"""
    def __init__(self):
        super().__init__("Division by zero")
```

#### 9. DIP 위반: 구체 클래스 직접 의존
**위치**: `calculator_console.py:7, 107`

**리팩토링 기법**: Dependency Injection
```python
def main(calculator: ArithmeticOperations = None):
    if calculator is None:
        calculator = ArithmeticOperations()
    # ...
```

---

### 🟢 Low 우선순위

#### 10. 중복 코드: 예외 처리 출력 형식
**위치**: `calculator_console.py:125-133`

**리팩토링 기법**: Extract Method
```python
def display_error(error: Exception, error_type: str = "오류"):
    print()
    print("=" * 40)
    print(f"❌ {error_type} 발생: {error}")
    print("=" * 40)
```

#### 11. 매직 넘버: 구분선 하드코딩
**위치**: `arithmetic_operations.py:92, 102, 135, 152`

**리팩토링 기법**: Extract Constant
```python
DISPLAY_SEPARATOR_LENGTH = 60
```

#### 12. 의미없는 이름: 함수 매개변수
**위치**: `calculator_console.py:43, 70, 85`

**리팩토링 기법**: Rename Variable
```python
def calculate(calculator: ArithmeticOperations, 
              first_number: int, 
              operator: str, 
              second_number: int):
    # ...
```

---

## 📈 우선순위별 요약

### High 우선순위 (5개)
1. 중복 코드: 0으로 나누기 검사 로직
2. 긴 함수: `if __name__ == "__main__"` 블록
3. 중복 코드: 연산자 처리 if-elif 체인
4. SRP 위반: `main()` 함수의 다중 책임
5. OCP 위반: 연산자 처리 확장성 부족

### Med 우선순위 (4개)
6. 매직 넘버: 하드코딩된 구분선 길이
7. 의미없는 이름: 매개변수 `a`, `b`
8. 예외 처리: 커스텀 예외 클래스 부재
9. DIP 위반: 구체 클래스 직접 의존

### Low 우선순위 (3개)
10. 중복 코드: 예외 처리 출력 형식
11. 매직 넘버: 구분선 하드코딩
12. 의미없는 이름: 함수 매개변수

---

## 🎯 리팩토링 권장 순서

1. **1단계**: High 우선순위 항목 리팩토링
   - 중복 코드 제거 (0으로 나누기 검사)
   - 긴 함수 분리 (`if __name__ == "__main__"` 블록)
   - Strategy Pattern 적용 (연산자 처리)

2. **2단계**: Med 우선순위 항목 리팩토링
   - 매직 넘버 상수화
   - 변수명 개선
   - 커스텀 예외 클래스 도입

3. **3단계**: Low 우선순위 항목 리팩토링
   - 나머지 중복 코드 제거
   - 코드 가독성 개선

---

**분석 완료일**: 2025-12-16  
**분석자**: 개발팀  
**문서 버전**: v1.0

