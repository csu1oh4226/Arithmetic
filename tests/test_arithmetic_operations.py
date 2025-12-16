"""
Arithmetic Operations Test Module
사칙연산 기능에 대한 테스트 케이스입니다.
"""

import pytest
from src.arithmetic.arithmetic_operations import ArithmeticOperations


class TestArithmeticOperations:
    """
    ArithmeticOperations 클래스에 대한 테스트 케이스
    """
    
    def setup_method(self):
        """각 테스트 메서드 실행 전에 호출되는 설정 메서드"""
        self.calculator = ArithmeticOperations()
    
    def test_addition_positive_numbers(self):
        """덧셈 테스트: 양수"""
        # 입력: 1 + 10
        # 예상 결과: 11
        assert self.calculator.add(1, 10) == 11
    
    def test_addition_with_zero(self):
        """덧셈 테스트: 0 포함"""
        # 입력: 0 + 1
        # 예상 결과: 1
        assert self.calculator.add(0, 1) == 1
    
    def test_division_by_zero(self):
        """나눗셈 테스트: 0으로 나누기 (예외 발생)"""
        # 입력: 0 / 0
        # 예상 결과: ArithmeticError 예외 발생
        with pytest.raises(ArithmeticError):
            self.calculator.divide(0, 0)
    
    def test_addition_negative_numbers(self):
        """덧셈 테스트: 음수"""
        # 입력: -1 + (-10)
        # 예상 결과: -11
        assert self.calculator.add(-1, -10) == -11
    
    def test_subtraction(self):
        """뺄셈 테스트"""
        # 입력: 5 - 2
        # 예상 결과: 3
        assert self.calculator.subtract(5, 2) == 3
    
    def test_multiplication_negative_numbers(self):
        """곱셈 테스트: 음수"""
        # 입력: -5 * -3
        # 예상 결과: 15
        assert self.calculator.multiply(-5, -3) == 15
    
    def test_division_integer(self):
        """나눗셈 테스트: 정수 나눗셈"""
        # 입력: 5 / 2
        # 예상 결과: 2 (정수 나눗셈)
        assert self.calculator.divide(5, 2) == 2
    
    def test_division_quotient(self):
        """나눗셈 테스트: 몫 계산 (소수점)"""
        # 입력: 5 ÷ 2
        # 예상 결과: 2.5
        assert self.calculator.divide_quotient(5, 2) == 2.5
    
    def test_multiplication_with_zero(self):
        """곱셈 테스트: 0 포함"""
        # 입력: 0 * 10
        # 예상 결과: 0
        assert self.calculator.multiply(0, 10) == 0
    
    def test_division_negative_number(self):
        """나눗셈 테스트: 음수"""
        # 입력: -10 / 2
        # 예상 결과: -5
        assert self.calculator.divide(-10, 2) == -5

