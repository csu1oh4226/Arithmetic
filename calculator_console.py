"""
간단한 사칙연산 콘솔 프로그램
사용자로부터 두 정수와 연산자를 입력받아 계산 결과를 출력합니다.
"""

from src.arithmetic.arithmetic_operations import ArithmeticOperations
from src.arithmetic.exceptions import DivisionByZeroError, InvalidInputError
from src.gui.operation_strategies import OperationStrategyFactory

def get_integer_input(prompt: str) -> int:
    """
    사용자로부터 정수를 입력받습니다.
    
    Args:
        prompt: 입력 프롬프트 메시지
        
    Returns:
        입력받은 정수값
        
    Raises:
        InvalidInputError: 입력값이 정수가 아닌 경우 (현재는 재시도하지만, 향후 예외로 변경 가능)
    """
    while True:
        try:
            value = input(prompt)
            return int(value)
        except ValueError:
            print("❌ 올바른 정수를 입력해주세요.")
            # 향후 정책 변경 시: raise InvalidInputError("입력값이 정수가 아닙니다.")


def get_operator_input() -> str:
    """
    사용자로부터 연산자를 입력받습니다.
    
    Returns:
        입력받은 연산자 (+, -, *, /, //)
        
    Raises:
        InvalidInputError: 입력값이 유효한 연산자가 아닌 경우 (현재는 재시도하지만, 향후 예외로 변경 가능)
    """
    valid_operators = ['+', '-', '*', '/', '//']
    while True:
        operator = input("연산자>>")
        if operator in valid_operators:
            return operator
        else:
            print(f"❌ 올바른 연산자를 입력해주세요. ({', '.join(valid_operators)})")
            # 향후 정책 변경 시: raise InvalidInputError(f"지원하지 않는 연산자: {operator}")


def calculate(calculator: ArithmeticOperations, first_number: int, operation_symbol: str, second_number: int):
    """
    연산자를 기반으로 계산을 수행합니다.
    
    Args:
        calculator: ArithmeticOperations 인스턴스
        first_number: 첫 번째 정수
        operation_symbol: 연산 기호
        second_number: 두 번째 정수
        
    Returns:
        계산 결과값
    """
    # 연산자 매핑
    operation_map = {
        '+': 'add',
        '-': 'subtract',
        '*': 'multiply',
        '/': 'divide_quotient',
        '//': 'divide',  # 정수 나눗셈
    }
    
    operation_name = operation_map.get(operation_symbol)
    if operation_name is None:
        raise ValueError(f"지원하지 않는 연산자: {operation_symbol}")
    
    # Strategy Pattern을 사용하여 연산 수행
    strategy = OperationStrategyFactory.get_strategy(operation_name)
    result = strategy.execute(calculator, float(first_number), float(second_number))
    
    return result


def format_expression(first_number: int, operation_symbol: str, second_number: int) -> str:
    """
    계산식을 문자열로 포맷팅합니다.
    
    Args:
        first_number: 첫 번째 정수
        operation_symbol: 연산 기호
        second_number: 두 번째 정수
        
    Returns:
        포맷팅된 계산식 문자열
    """
    return f"{first_number}{operation_symbol}{second_number}"


def _print_separator(length: int = 40, character: str = "=") -> None:
    """
    구분선을 출력합니다.
    
    Args:
        length: 구분선 길이
        character: 구분선 문자
    """
    print(character * length)


def display_result(first_number: int, operation_symbol: str, second_number: int, result):
    """
    계산 결과를 화면에 출력합니다.
    
    Args:
        first_number: 첫 번째 정수
        operation_symbol: 연산 기호
        second_number: 두 번째 정수
        result: 계산 결과
    """
    expression = format_expression(first_number, operation_symbol, second_number)
    
    _print_separator(40, "=")
    print(f"{expression}을 계산합니다.")
    _print_separator(40, "=")
    print(f"{expression}={result}입니다.")


def _get_user_inputs() -> tuple[int, str, int]:
    """
    사용자로부터 입력을 받습니다.
    
    Returns:
        (첫 번째 정수, 연산 기호, 두 번째 정수) 튜플
    """
    print("입력화면")
    first_number = get_integer_input("첫번째 정수값 >>")
    operation_symbol = get_operator_input()
    second_number = get_integer_input("두번째 정수값>>")
    return first_number, operation_symbol, second_number


def _perform_calculation(
    calculator: ArithmeticOperations,
    first_number: int,
    operation_symbol: str,
    second_number: int
) -> float:
    """
    계산을 수행합니다.
    
    Args:
        calculator: ArithmeticOperations 인스턴스
        first_number: 첫 번째 정수
        operation_symbol: 연산 기호
        second_number: 두 번째 정수
        
    Returns:
        계산 결과값
    """
    return calculate(calculator, first_number, operation_symbol, second_number)


def _display_calculation_result(
    first_number: int,
    operation_symbol: str,
    second_number: int,
    calculation_result: float
) -> None:
    """
    계산 결과를 화면에 출력합니다.
    
    Args:
        first_number: 첫 번째 정수
        operation_symbol: 연산 기호
        second_number: 두 번째 정수
        calculation_result: 계산 결과
    """
    print("결과 뷰 화면")
    display_result(first_number, operation_symbol, second_number, calculation_result)


def _handle_calculation_error(error: Exception, error_type: str = "오류") -> None:
    """
    계산 오류를 처리하고 사용자에게 표시합니다.
    
    Args:
        error: 발생한 예외
        error_type: 오류 유형 설명
    """
    print()
    _print_separator(40, "=")
    print(f"❌ {error_type} 발생: {error}")
    _print_separator(40, "=")


def main():
    """
    메인 함수: 간단한 사칙연산 콘솔 프로그램
    """
    calculator = ArithmeticOperations()
    
    try:
        first_number, operation_symbol, second_number = _get_user_inputs()
        print()
        
        calculation_result = _perform_calculation(
            calculator, first_number, operation_symbol, second_number
        )
        
        _display_calculation_result(
            first_number, operation_symbol, second_number, calculation_result
        )
        
    except DivisionByZeroError as e:
        _handle_calculation_error(e, "0으로 나누기 오류")
    except ArithmeticError as e:
        _handle_calculation_error(e, "산술 오류")
    except InvalidInputError as e:
        _handle_calculation_error(e, "입력 오류")
    except Exception as e:
        _handle_calculation_error(e, "예상치 못한 오류")


if __name__ == "__main__":
    main()

