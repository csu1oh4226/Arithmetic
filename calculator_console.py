5
"""
간단한 사칙연산 콘솔 프로그램
사용자로부터 두 정수와 연산자를 입력받아 계산 결과를 출력합니다.
"""

from src.arithmetic.arithmetic_operations import ArithmeticOperations

def get_integer_input(prompt: str) -> int:
    """
    사용자로부터 정수를 입력받습니다.
    
    Args:
        prompt: 입력 프롬프트 메시지
        
    Returns:
        입력받은 정수값
    """
    while True:
        try:
            value = input(prompt)
            return int(value)
        except ValueError:
            print("❌ 올바른 정수를 입력해주세요.")


def get_operator_input() -> str:
    """
    사용자로부터 연산자를 입력받습니다.
    
    Returns:
        입력받은 연산자 (+, -, *, /, //)
    """
    valid_operators = ['+', '-', '*', '/', '//']
    while True:
        operator = input("연산자>>")
        if operator in valid_operators:
            return operator
        else:
            print(f"❌ 올바른 연산자를 입력해주세요. ({', '.join(valid_operators)})")


def calculate(calculator: ArithmeticOperations, a: int, operator: str, b: int):
    """
    연산자를 기반으로 계산을 수행합니다.
    
    Args:
        calculator: ArithmeticOperations 인스턴스
        a: 첫 번째 정수
        operator: 연산자
        b: 두 번째 정수
        
    Returns:
        계산 결과값
    """
    if operator == '+':
        return calculator.add(a, b)
    elif operator == '-':
        return calculator.subtract(a, b)
    elif operator == '*':
        return calculator.multiply(a, b)
    elif operator == '/':
        return calculator.divide_quotient(a, b)
    elif operator == '//':
        return calculator.divide(a, b)
    else:
        raise ValueError(f"지원하지 않는 연산자: {operator}")


def format_expression(a: int, operator: str, b: int) -> str:
    """
    계산식을 문자열로 포맷팅합니다.
    
    Args:
        a: 첫 번째 정수
        operator: 연산자
        b: 두 번째 정수
        
    Returns:
        포맷팅된 계산식 문자열
    """
    return f"{a}{operator}{b}"


def display_result(a: int, operator: str, b: int, result):
    """
    계산 결과를 화면에 출력합니다.
    
    Args:
        a: 첫 번째 정수
        operator: 연산자
        b: 두 번째 정수
        result: 계산 결과
    """
    expression = format_expression(a, operator, b)
    
    print("=" * 40)
    print(f"{expression}을 계산합니다.")
    print("=" * 40)
    print(f"{expression}={result}입니다.")


def main():
    """
    메인 함수: 간단한 사칙연산 콘솔 프로그램
    """
    calculator = ArithmeticOperations()
    
    try:
        # 입력 화면
        print("입력화면")
        a = get_integer_input("첫번째 정수값 >>")
        operator = get_operator_input()
        b = get_integer_input("두번째 정수값>>")
        
        print()
        
        # 계산 수행
        result = calculate(calculator, a, operator, b)
        
        # 결과 뷰 화면
        print("결과 뷰 화면")
        display_result(a, operator, b, result)
        
    except ArithmeticError as e:
        print()
        print("=" * 40)
        print(f"❌ 오류 발생: {e}")
        print("=" * 40)
    except Exception as e:
        print()
        print("=" * 40)
        print(f"❌ 예상치 못한 오류 발생: {e}")
        print("=" * 40)


if __name__ == "__main__":
    main()

