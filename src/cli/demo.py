"""
사칙연산 시스템 데모 프로그램
ArithmeticOperations 클래스를 사용한 데모 프로그램입니다.
"""

import sys
from pathlib import Path

# 프로젝트 루트를 Python 경로에 추가
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from src.arithmetic.arithmetic_operations import ArithmeticOperations
from src.arithmetic.exceptions import DivisionByZeroError


def _print_separator(length: int = 60, character: str = "-") -> None:
    """
    구분선을 출력합니다.
    
    Args:
        length: 구분선 길이
        character: 구분선 문자
    """
    print(character * length)


def _print_header() -> None:
    """
    프로그램 헤더를 출력합니다.
    """
    _print_separator(60, "=")
    print("사칙연산 시스템 (Arithmetic Operations System)")
    _print_separator(60, "=")
    print()


def _run_basic_arithmetic_tests(calculator: ArithmeticOperations) -> None:
    """
    기본 사칙연산 테스트를 실행하고 결과를 출력합니다.
    
    Args:
        calculator: ArithmeticOperations 인스턴스
    """
    print("📊 사칙연산 테스트 결과:")
    _print_separator(60, "-")
    
    # 덧셈 테스트
    addition_result_positive = calculator.add(1, 10)
    print(f"덧셈 (양수)      | 1 + 10 = {addition_result_positive}")
    
    addition_result_with_zero = calculator.add(0, 1)
    print(f"덧셈 (0 포함)     | 0 + 1 = {addition_result_with_zero}")
    
    addition_result_negative = calculator.add(-1, -10)
    print(f"덧셈 (음수)      | -1 + (-10) = {addition_result_negative}")
    
    # 뺄셈 테스트
    subtraction_result = calculator.subtract(5, 2)
    print(f"뺄셈             | 5 - 2 = {subtraction_result}")
    
    # 곱셈 테스트
    multiplication_result_negative = calculator.multiply(-5, -3)
    print(f"곱셈 (음수)      | -5 * -3 = {multiplication_result_negative}")
    
    multiplication_result_with_zero = calculator.multiply(0, 10)
    print(f"곱셈 (0 포함)     | 0 * 10 = {multiplication_result_with_zero}")
    
    # 나눗셈 테스트
    division_result_integer = calculator.divide(5, 2)
    print(f"나눗셈 (정수)    | 5 // 2 = {division_result_integer}")
    
    division_result_negative = calculator.divide(-10, 2)
    print(f"나눗셈 (음수)    | -10 // 2 = {division_result_negative}")
    
    division_result_quotient = calculator.divide_quotient(5, 2)
    print(f"나눗셈 (소수점)  | 5 / 2 = {division_result_quotient}")
    
    _print_separator(60, "-")
    print()


def _run_exception_handling_tests(calculator: ArithmeticOperations) -> None:
    """
    예외 처리 테스트를 실행하고 결과를 출력합니다.
    
    Args:
        calculator: ArithmeticOperations 인스턴스
    """
    print("⚠️  예외 처리 테스트:")
    _print_separator(60, "-")
    
    try:
        calculator.divide(0, 0)
    except DivisionByZeroError as e:
        print(f"0으로 나누기    | 0 / 0 → {type(e).__name__}: {e}")
    
    try:
        calculator.divide_quotient(5, 0)
    except DivisionByZeroError as e:
        print(f"divide_quotient(5, 0) | → {type(e).__name__}: {e}")
    
    _print_separator(60, "-")
    print()


def _execute_calculation_by_operation(
    calculator: ArithmeticOperations,
    first_number: int,
    second_number: int,
    operation_name: str
) -> float:
    """
    연산 이름에 따라 계산을 수행합니다.
    
    Args:
        calculator: ArithmeticOperations 인스턴스
        first_number: 첫 번째 정수
        second_number: 두 번째 정수
        operation_name: 연산 이름
        
    Returns:
        계산 결과값
    """
    if operation_name == "덧셈":
        return calculator.add(first_number, second_number)
    elif operation_name == "뺄셈":
        return calculator.subtract(first_number, second_number)
    elif operation_name == "곱셈":
        return calculator.multiply(first_number, second_number)
    elif operation_name == "나눗셈":
        return calculator.divide(first_number, second_number)
    elif operation_name == "소수점 나눗셈":
        return calculator.divide_quotient(first_number, second_number)
    else:
        raise ValueError(f"지원하지 않는 연산: {operation_name}")


def _run_calculation_examples(calculator: ArithmeticOperations) -> None:
    """
    계산 예제를 실행하고 결과를 출력합니다.
    
    Args:
        calculator: ArithmeticOperations 인스턴스
    """
    print("💡 추가 예제:")
    _print_separator(60, "-")
    
    calculation_examples = [
        (10, 5, "덧셈", "+"),
        (10, 5, "뺄셈", "-"),
        (10, 5, "곱셈", "*"),
        (10, 5, "나눗셈", "//"),
        (10, 5, "소수점 나눗셈", "/"),
    ]
    
    for first_number, second_number, operation_name, operation_symbol in calculation_examples:
        calculation_result = _execute_calculation_by_operation(
            calculator, first_number, second_number, operation_name
        )
        print(f"{operation_name:12} | {first_number} {operation_symbol} {second_number} = {calculation_result}")
    
    _print_separator(60, "-")
    print()


def run_demo() -> None:
    """
    데모 프로그램을 실행합니다.
    """
    _print_header()
    
    calculator = ArithmeticOperations()
    
    _run_basic_arithmetic_tests(calculator)
    _run_exception_handling_tests(calculator)
    _run_calculation_examples(calculator)
    
    print("✅ 프로그램 실행 완료!")
    _print_separator(60, "=")


if __name__ == "__main__":
    """
    파일을 직접 실행할 때 실행되는 코드입니다.
    """
    run_demo()

