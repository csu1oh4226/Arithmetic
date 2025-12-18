"""
사칙연산 시스템 예외 클래스
사칙연산 관련 커스텀 예외를 정의합니다.
"""


class DivisionByZeroError(ArithmeticError):
    """
    0으로 나누기 시 발생하는 예외입니다.
    
    이 예외는 나눗셈 연산에서 제수(divisor)가 0인 경우 발생합니다.
    """
    
    def __init__(self, message: str = "Division by zero"):
        """
        DivisionByZeroError를 초기화합니다.
        
        Args:
            message: 예외 메시지 (기본값: "Division by zero")
        """
        super().__init__(message)
        self.message = message


class InvalidInputError(ValueError):
    """
    잘못된 입력값에 대한 예외입니다.
    
    이 예외는 입력값이 예상된 형식이나 범위를 벗어난 경우 발생합니다.
    """
    
    def __init__(self, message: str):
        """
        InvalidInputError를 초기화합니다.
        
        Args:
            message: 예외 메시지
        """
        super().__init__(message)
        self.message = message

