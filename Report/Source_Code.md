# 소스 코드 리포트

## 소스 코드 구조

### 메인 클래스: ArithmeticOperations

**파일 경로**: `src/arithmetic/arithmetic_operations.py`

---

## 전체 소스 코드

```python
"""
Arithmetic Operations Module
사칙연산 기능을 제공하는 클래스입니다.
"""


class ArithmeticOperations:
    """
    사칙연산을 수행하는 클래스입니다.
    """
    
    def add(self, a: int, b: int) -> int:
        """
        두 정수의 덧셈을 수행합니다.
        
        Args:
            a: 첫 번째 정수
            b: 두 번째 정수
            
        Returns:
            a + b의 결과
        """
        return a + b
    
    def subtract(self, a: int, b: int) -> int:
        """
        두 정수의 뺄셈을 수행합니다.
        
        Args:
            a: 첫 번째 정수
            b: 두 번째 정수
            
        Returns:
            a - b의 결과
        """
        return a - b
    
    def multiply(self, a: int, b: int) -> int:
        """
        두 정수의 곱셈을 수행합니다.
        
        Args:
            a: 첫 번째 정수
            b: 두 번째 정수
            
        Returns:
            a * b의 결과
        """
        return a * b
    
    def divide(self, a: int, b: int) -> int:
        """
        두 정수의 나눗셈을 수행합니다 (정수 나눗셈).
        
        Args:
            a: 첫 번째 정수
            b: 두 번째 정수
            
        Returns:
            a / b의 결과 (정수)
            
        Raises:
            ArithmeticError: b가 0인 경우
        """
        if b == 0:
            raise ArithmeticError("Division by zero")
        return a // b
    
    def divide_quotient(self, a: int, b: int) -> float:
        """
        두 정수의 나눗셈을 수행합니다 (소수점 포함).
        
        Args:
            a: 첫 번째 정수
            b: 두 번째 정수
            
        Returns:
            a / b의 결과 (소수점)
            
        Raises:
            ArithmeticError: b가 0인 경우
        """
        if b == 0:
            raise ArithmeticError("Division by zero")
        return a / b
```

---

## 메서드별 상세 설명

### 1. add(a, b)

**기능**: 두 정수의 덧셈을 수행합니다.

**시그니처**:
```python
def add(self, a: int, b: int) -> int
```

**매개변수**:
- `a` (int): 첫 번째 정수
- `b` (int): 두 번째 정수

**반환값**:
- `int`: a + b의 결과

**예외**: 없음

**사용 예시**:
```python
calculator = ArithmeticOperations()
result = calculator.add(1, 10)  # 결과: 11
result = calculator.add(-1, -10)  # 결과: -11
```

---

### 2. subtract(a, b)

**기능**: 두 정수의 뺄셈을 수행합니다.

**시그니처**:
```python
def subtract(self, a: int, b: int) -> int
```

**매개변수**:
- `a` (int): 첫 번째 정수
- `b` (int): 두 번째 정수

**반환값**:
- `int`: a - b의 결과

**예외**: 없음

**사용 예시**:
```python
calculator = ArithmeticOperations()
result = calculator.subtract(5, 2)  # 결과: 3
result = calculator.subtract(0, 5)  # 결과: -5
```

---

### 3. multiply(a, b)

**기능**: 두 정수의 곱셈을 수행합니다.

**시그니처**:
```python
def multiply(self, a: int, b: int) -> int
```

**매개변수**:
- `a` (int): 첫 번째 정수
- `b` (int): 두 번째 정수

**반환값**:
- `int`: a * b의 결과

**예외**: 없음

**사용 예시**:
```python
calculator = ArithmeticOperations()
result = calculator.multiply(-5, -3)  # 결과: 15
result = calculator.multiply(0, 10)  # 결과: 0
```

---

### 4. divide(a, b)

**기능**: 두 정수의 정수 나눗셈을 수행합니다.

**시그니처**:
```python
def divide(self, a: int, b: int) -> int
```

**매개변수**:
- `a` (int): 첫 번째 정수
- `b` (int): 두 번째 정수

**반환값**:
- `int`: a // b의 결과 (정수 나눗셈)

**예외**:
- `ArithmeticError`: b가 0인 경우

**사용 예시**:
```python
calculator = ArithmeticOperations()
result = calculator.divide(5, 2)  # 결과: 2 (정수 나눗셈)
result = calculator.divide(-10, 2)  # 결과: -5
result = calculator.divide(0, 0)  # ArithmeticError 발생
```

---

### 5. divide_quotient(a, b)

**기능**: 두 정수의 소수점 나눗셈을 수행합니다.

**시그니처**:
```python
def divide_quotient(self, a: int, b: int) -> float
```

**매개변수**:
- `a` (int): 첫 번째 정수
- `b` (int): 두 번째 정수

**반환값**:
- `float`: a / b의 결과 (소수점 포함)

**예외**:
- `ArithmeticError`: b가 0인 경우

**사용 예시**:
```python
calculator = ArithmeticOperations()
result = calculator.divide_quotient(5, 2)  # 결과: 2.5
result = calculator.divide_quotient(10, 3)  # 결과: 3.333...
result = calculator.divide_quotient(0, 0)  # ArithmeticError 발생
```

---

## 코드 품질 분석

### 장점

1. **타입 힌팅**: 모든 메서드에 타입 힌팅이 적용되어 코드 가독성 향상
2. **문서화**: 모든 메서드에 docstring이 작성되어 있음
3. **예외 처리**: 0으로 나누기 시 적절한 예외 발생
4. **명확한 네이밍**: 메서드 이름이 기능을 명확히 표현
5. **단일 책임**: 각 메서드가 하나의 기능만 수행

### 개선 가능한 부분

1. **중복 코드**: `divide()`와 `divide_quotient()`에서 0으로 나누기 검사 로직이 중복됨
   - **개선 방안**: 공통 검증 메서드 추출
   
2. **입력 검증**: 음수나 매우 큰 수에 대한 검증이 없음
   - **개선 방안**: 입력값 범위 검증 추가 (필요시)

3. **에러 메시지**: 에러 메시지를 더 구체적으로 개선 가능
   - **개선 방안**: 어떤 값으로 나누려고 했는지 포함

---

## 리팩토링 제안

### 제안 1: 중복 코드 제거

**현재 코드**:
```python
def divide(self, a: int, b: int) -> int:
    if b == 0:
        raise ArithmeticError("Division by zero")
    return a // b

def divide_quotient(self, a: int, b: int) -> float:
    if b == 0:
        raise ArithmeticError("Division by zero")
    return a / b
```

**리팩토링 후**:
```python
def _validate_divisor(self, b: int) -> None:
    """나눗셈의 제수(divisor)가 0이 아닌지 검증합니다."""
    if b == 0:
        raise ArithmeticError("Division by zero")

def divide(self, a: int, b: int) -> int:
    """두 정수의 나눗셈을 수행합니다 (정수 나눗셈)."""
    self._validate_divisor(b)
    return a // b

def divide_quotient(self, a: int, b: int) -> float:
    """두 정수의 나눗셈을 수행합니다 (소수점 포함)."""
    self._validate_divisor(b)
    return a / b
```

### 제안 2: 에러 메시지 개선

```python
def _validate_divisor(self, b: int) -> None:
    """나눗셈의 제수(divisor)가 0이 아닌지 검증합니다."""
    if b == 0:
        raise ArithmeticError(f"Cannot divide by zero. Divisor: {b}")
```

---

## 테스트 코드

### 테스트 파일 경로

`tests/test_arithmetic_operations.py`

### 테스트 클래스 구조

```python
class TestArithmeticOperations:
    def setup_method(self):
        """각 테스트 메서드 실행 전에 호출되는 설정 메서드"""
        self.calculator = ArithmeticOperations()
    
    # 10개의 테스트 메서드...
```

---

## 코드 통계

- **총 라인 수**: 87줄
- **코드 라인 수**: 15줄 (주석 및 빈 줄 제외)
- **메서드 수**: 5개
- **클래스 수**: 1개
- **예외 처리**: 2개 (divide, divide_quotient)

---

**작성일**: 2025-12-16  
**문서 버전**: v1.0

