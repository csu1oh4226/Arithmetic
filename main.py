"""
사칙연산 시스템 데모 프로그램
ArithmeticOperations 클래스를 사용한 예제 프로그램입니다.
"""

from src.arithmetic.arithmetic_operations import ArithmeticOperations


def main():
    """메인 함수: 사칙연산 시스템 데모"""
    print("=" * 60)
    print("사칙연산 시스템 (Arithmetic Operations System)")
    print("=" * 60)
    print()
    
    # ArithmeticOperations 인스턴스 생성
    calculator = ArithmeticOperations()
    
    # 테스트 케이스 실행
    print("📊 테스트 케이스 실행 결과:")
    print("-" * 60)
    
    # TC-001: 덧셈 (양수)
    result1 = calculator.add(1, 10)
    print(f"TC-001: 덧셈 (양수)      | 1 + 10 = {result1}")
    
    # TC-002: 덧셈 (0 포함)
    result2 = calculator.add(0, 1)
    print(f"TC-002: 덧셈 (0 포함)     | 0 + 1 = {result2}")
    
    # TC-004: 덧셈 (음수)
    result3 = calculator.add(-1, -10)
    print(f"TC-004: 덧셈 (음수)      | -1 + (-10) = {result3}")
    
    # TC-005: 뺄셈
    result4 = calculator.subtract(5, 2)
    print(f"TC-005: 뺄셈             | 5 - 2 = {result4}")
    
    # TC-006: 곱셈 (음수)
    result5 = calculator.multiply(-5, -3)
    print(f"TC-006: 곱셈 (음수)      | -5 * -3 = {result5}")
    
    # TC-009: 곱셈 (0 포함)
    result6 = calculator.multiply(0, 10)
    print(f"TC-009: 곱셈 (0 포함)     | 0 * 10 = {result6}")
    
    # TC-007: 나눗셈 (정수)
    result7 = calculator.divide(5, 2)
    print(f"TC-007: 나눗셈 (정수)    | 5 // 2 = {result7}")
    
    # TC-010: 나눗셈 (음수)
    result8 = calculator.divide(-10, 2)
    print(f"TC-010: 나눗셈 (음수)    | -10 // 2 = {result8}")
    
    # TC-008: 나눗셈 (소수점)
    result9 = calculator.divide_quotient(5, 2)
    print(f"TC-008: 나눗셈 (소수점)  | 5 / 2 = {result9}")
    
    print("-" * 60)
    print()
    
    # 예외 처리 테스트
    print("⚠️  예외 처리 테스트:")
    print("-" * 60)
    
    try:
        calculator.divide(0, 0)
    except ArithmeticError as e:
        print(f"TC-003: 0으로 나누기    | 0 / 0 → {type(e).__name__}: {e}")
    
    try:
        calculator.divide_quotient(5, 0)
    except ArithmeticError as e:
        print(f"divide_quotient(5, 0)  | → {type(e).__name__}: {e}")
    
    print("-" * 60)
    print()
    
    # 사용자 입력 예제
    print("💡 사용자 입력 예제:")
    print("-" * 60)
    
    examples = [
        (10, 5, "덧셈"),
        (10, 5, "뺄셈"),
        (10, 5, "곱셈"),
        (10, 5, "나눗셈"),
        (10, 5, "소수점 나눗셈"),
    ]
    
    for a, b, operation in examples:
        if operation == "덧셈":
            result = calculator.add(a, b)
            symbol = "+"
        elif operation == "뺄셈":
            result = calculator.subtract(a, b)
            symbol = "-"
        elif operation == "곱셈":
            result = calculator.multiply(a, b)
            symbol = "*"
        elif operation == "나눗셈":
            result = calculator.divide(a, b)
            symbol = "//"
        elif operation == "소수점 나눗셈":
            result = calculator.divide_quotient(a, b)
            symbol = "/"
        
        print(f"{operation:12} | {a} {symbol} {b} = {result}")
    
    print("-" * 60)
    print()
    print("✅ 프로그램 실행 완료!")
    print("=" * 60)


if __name__ == "__main__":
    main()

