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

