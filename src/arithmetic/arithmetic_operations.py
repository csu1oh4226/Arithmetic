"""
사칙연산 시스템
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


if __name__ == "__main__":
    """
    파일을 직접 실행할 때 실행되는 코드입니다.
    """
    print("=" * 60)
    print("사칙연산 시스템 (Arithmetic Operations System)")
    print("=" * 60)
    print()
    
    # ArithmeticOperations 인스턴스 생성
    calculator = ArithmeticOperations()
    
    # 테스트 케이스 실행
    print("📊 사칙연산 테스트 결과:")
    print("-" * 60)
    
    # 덧셈 테스트
    result1 = calculator.add(1, 10)
    print(f"덧셈 (양수)      | 1 + 10 = {result1}")
    
    result2 = calculator.add(0, 1)
    print(f"덧셈 (0 포함)     | 0 + 1 = {result2}")
    
    result3 = calculator.add(-1, -10)
    print(f"덧셈 (음수)      | -1 + (-10) = {result3}")
    
    # 뺄셈 테스트
    result4 = calculator.subtract(5, 2)
    print(f"뺄셈             | 5 - 2 = {result4}")
    
    # 곱셈 테스트
    result5 = calculator.multiply(-5, -3)
    print(f"곱셈 (음수)      | -5 * -3 = {result5}")
    
    result6 = calculator.multiply(0, 10)
    print(f"곱셈 (0 포함)     | 0 * 10 = {result6}")
    
    # 나눗셈 테스트
    result7 = calculator.divide(5, 2)
    print(f"나눗셈 (정수)    | 5 // 2 = {result7}")
    
    result8 = calculator.divide(-10, 2)
    print(f"나눗셈 (음수)    | -10 // 2 = {result8}")
    
    result9 = calculator.divide_quotient(5, 2)
    print(f"나눗셈 (소수점)  | 5 / 2 = {result9}")
    
    print("-" * 60)
    print()
    
    # 예외 처리 테스트
    print("⚠️  예외 처리 테스트:")
    print("-" * 60)
    
    try:
        calculator.divide(0, 0)
    except ArithmeticError as e:
        print(f"0으로 나누기    | 0 / 0 → {type(e).__name__}: {e}")
    
    try:
        calculator.divide_quotient(5, 0)
    except ArithmeticError as e:
        print(f"divide_quotient(5, 0) | → {type(e).__name__}: {e}")
    
    print("-" * 60)
    print()
    
    # 사용자 입력 예제
    print("💡 추가 예제:")
    print("-" * 60)
    
    examples = [
        (10, 5, "덧셈", "+"),
        (10, 5, "뺄셈", "-"),
        (10, 5, "곱셈", "*"),
        (10, 5, "나눗셈", "//"),
        (10, 5, "소수점 나눗셈", "/"),
    ]
    
    for a, b, operation, symbol in examples:
        if operation == "덧셈":
            result = calculator.add(a, b)
        elif operation == "뺄셈":
            result = calculator.subtract(a, b)
        elif operation == "곱셈":
            result = calculator.multiply(a, b)
        elif operation == "나눗셈":
            result = calculator.divide(a, b)
        elif operation == "소수점 나눗셈":
            result = calculator.divide_quotient(a, b)
        
        print(f"{operation:12} | {a} {symbol} {b} = {result}")
    
    print("-" * 60)
    print()
    print("✅ 프로그램 실행 완료!")
    print("=" * 60)

