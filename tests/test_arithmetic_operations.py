"""
사칙연산 시스템 테스트 모듈
사칙연산 기능에 대한 테스트 케이스입니다.
"""

import pytest
from src.arithmetic.arithmetic_operations import ArithmeticOperations
from src.arithmetic.exceptions import DivisionByZeroError


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
        # 예상 결과: DivisionByZeroError 예외 발생
        with pytest.raises(DivisionByZeroError):
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

    # ========== 추가 구현 기능 테스트 ==========
    
    def test_division_quotient_by_zero(self):
        """나눗셈 테스트: divide_quotient()의 0으로 나누기 (예외 발생)"""
        # 입력: 5 / 0
        # 예상 결과: DivisionByZeroError 예외 발생
        with pytest.raises(DivisionByZeroError) as exc_info:
            self.calculator.divide_quotient(5, 0)
        assert str(exc_info.value) == "Division by zero"
    
    # ========== 경계값 처리 검증 테스트 ==========
    
    def test_subtraction_with_zero(self):
        """뺄셈 테스트: 0 포함 (경계값)"""
        # 입력: 5 - 0
        # 예상 결과: 5
        assert self.calculator.subtract(5, 0) == 5
        # 입력: 0 - 5
        # 예상 결과: -5
        assert self.calculator.subtract(0, 5) == -5
    
    def test_subtraction_negative_numbers(self):
        """뺄셈 테스트: 음수 연산 (경계값)"""
        # 입력: -5 - (-3)
        # 예상 결과: -2
        assert self.calculator.subtract(-5, -3) == -2
        # 입력: 5 - (-3)
        # 예상 결과: 8
        assert self.calculator.subtract(5, -3) == 8
    
    def test_division_integer_vs_quotient(self):
        """나눗셈 테스트: 정수 나눗셈과 소수점 나눗셈 구분 확인"""
        # 정수 나눗셈: 소수점 버림
        assert self.calculator.divide(7, 3) == 2
        # 소수점 나눗셈: 소수점 포함
        assert self.calculator.divide_quotient(7, 3) == pytest.approx(7 / 3)
        # 정수 나눗셈과 소수점 나눗셈이 다른지 확인
        assert self.calculator.divide(7, 3) != self.calculator.divide_quotient(7, 3)
    
    def test_negative_operations_comprehensive(self):
        """음수 연산 정확도 종합 테스트"""
        # 음수 + 음수
        assert self.calculator.add(-10, -5) == -15
        # 음수 - 음수
        assert self.calculator.subtract(-10, -5) == -5
        # 음수 * 양수
        assert self.calculator.multiply(-10, 5) == -50
        # 양수 * 음수
        assert self.calculator.multiply(10, -5) == -50
        # 음수 / 양수
        assert self.calculator.divide(-10, 5) == -2
        # 양수 / 음수
        assert self.calculator.divide(10, -5) == -2
    
    # ========== 매우 큰 수(Big Integer) 처리 테스트 ==========
    
    def test_big_integer_addition(self):
        """덧셈 테스트: 매우 큰 수"""
        # Python int는 자동으로 Big Integer를 처리
        big_num1 = 999999999999999999999999999999
        big_num2 = 111111111111111111111111111111
        expected = big_num1 + big_num2
        assert self.calculator.add(big_num1, big_num2) == expected
    
    def test_big_integer_subtraction(self):
        """뺄셈 테스트: 매우 큰 수"""
        big_num1 = 999999999999999999999999999999
        big_num2 = 111111111111111111111111111111
        expected = big_num1 - big_num2
        assert self.calculator.subtract(big_num1, big_num2) == expected
    
    def test_big_integer_multiplication(self):
        """곱셈 테스트: 매우 큰 수"""
        big_num1 = 12345678901234567890
        big_num2 = 98765432109876543210
        expected = big_num1 * big_num2
        assert self.calculator.multiply(big_num1, big_num2) == expected
    
    def test_big_integer_division(self):
        """나눗셈 테스트: 매우 큰 수"""
        big_num1 = 999999999999999999999999999999
        big_num2 = 333333333333333333333333333333
        expected = big_num1 // big_num2
        assert self.calculator.divide(big_num1, big_num2) == expected
    
    def test_big_integer_division_quotient(self):
        """소수점 나눗셈 테스트: 매우 큰 수"""
        big_num1 = 999999999999999999999999999999
        big_num2 = 333333333333333333333333333333
        expected = big_num1 / big_num2
        assert self.calculator.divide_quotient(big_num1, big_num2) == pytest.approx(expected)
    
    # ========== 소수점 나눗셈 정밀도 테스트 ==========
    
    def test_division_quotient_precision(self):
        """소수점 나눗셈 정밀도 테스트"""
        # 1/3 = 0.333...
        result = self.calculator.divide_quotient(1, 3)
        assert result == pytest.approx(0.3333333333333333, rel=1e-15)
        
        # 22/7 (파이 근사값)
        result = self.calculator.divide_quotient(22, 7)
        assert result == pytest.approx(3.142857142857143, rel=1e-15)
    
    def test_division_quotient_precision_repeating_decimal(self):
        """소수점 나눗셈 정밀도 테스트: 순환소수"""
        # 1/7 = 0.142857142857...
        result = self.calculator.divide_quotient(1, 7)
        expected = 1 / 7
        assert result == pytest.approx(expected, rel=1e-15)
    
    def test_division_quotient_precision_small_numbers(self):
        """소수점 나눗셈 정밀도 테스트: 작은 수"""
        # 1/1000 = 0.001
        result = self.calculator.divide_quotient(1, 1000)
        assert result == 0.001
        
        # 1/1000000 = 0.000001
        result = self.calculator.divide_quotient(1, 1000000)
        assert result == 0.000001
    
    def test_division_quotient_precision_large_result(self):
        """소수점 나눗셈 정밀도 테스트: 큰 결과값"""
        # 1000000 / 3
        result = self.calculator.divide_quotient(1000000, 3)
        expected = 1000000 / 3
        assert result == pytest.approx(expected, rel=1e-10)

