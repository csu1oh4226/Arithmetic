"""
사칙연산 시스템
사칙연산 기능을 제공하는 클래스입니다.
"""

from src.arithmetic.exceptions import DivisionByZeroError


class ArithmeticOperations:
    """
    사칙연산을 수행하는 클래스입니다.
    """
    
    def add(self, first_number: int, second_number: int) -> int:
        """
        두 정수의 덧셈을 수행합니다.
        
        Args:
            first_number: 첫 번째 정수
            second_number: 두 번째 정수
            
        Returns:
            first_number + second_number의 결과
        """
        return first_number + second_number
    
    def subtract(self, first_number: int, second_number: int) -> int:
        """
        두 정수의 뺄셈을 수행합니다.
        
        Args:
            first_number: 첫 번째 정수
            second_number: 두 번째 정수
            
        Returns:
            first_number - second_number의 결과
        """
        return first_number - second_number
    
    def multiply(self, first_number: int, second_number: int) -> int:
        """
        두 정수의 곱셈을 수행합니다.
        
        Args:
            first_number: 첫 번째 정수
            second_number: 두 번째 정수
            
        Returns:
            first_number * second_number의 결과
        """
        return first_number * second_number
    
    def _validate_divisor(self, divisor: int) -> None:
        """
        나눗셈 전 제수를 검증합니다.
        
        Args:
            divisor: 제수 (나누는 수)
            
        Raises:
            DivisionByZeroError: divisor가 0인 경우
        """
        if divisor == 0:
            raise DivisionByZeroError("Division by zero")
    
    def divide(self, first_number: int, second_number: int) -> int:
        """
        두 정수의 나눗셈을 수행합니다 (정수 나눗셈).
        
        Args:
            first_number: 첫 번째 정수
            second_number: 두 번째 정수 (제수)
            
        Returns:
            first_number / second_number의 결과 (정수)
            
        Raises:
            DivisionByZeroError: second_number가 0인 경우
        """
        self._validate_divisor(second_number)
        return first_number // second_number
    
    def divide_quotient(self, first_number: int, second_number: int) -> float:
        """
        두 정수의 나눗셈을 수행합니다 (소수점 포함).
        
        Args:
            first_number: 첫 번째 정수
            second_number: 두 번째 정수 (제수)
            
        Returns:
            first_number / second_number의 결과 (소수점)
            
        Raises:
            DivisionByZeroError: second_number가 0인 경우
        """
        self._validate_divisor(second_number)
        return first_number / second_number

