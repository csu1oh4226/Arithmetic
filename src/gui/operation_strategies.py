"""
연산 전략 패턴 구현
각 연산을 Strategy 클래스로 분리하여 확장성을 높입니다.
"""

from abc import ABC, abstractmethod
from src.arithmetic.arithmetic_operations import ArithmeticOperations
from src.arithmetic.exceptions import DivisionByZeroError


class OperationStrategy(ABC):
    """연산 전략 인터페이스"""
    
    @abstractmethod
    def execute(self, calculator: ArithmeticOperations, first: float, second: float = None) -> float:
        """
        연산을 수행합니다.
        
        Args:
            calculator: ArithmeticOperations 인스턴스
            first: 첫 번째 피연산자
            second: 두 번째 피연산자 (이항 연산의 경우)
            
        Returns:
            연산 결과
        """
        pass


class BinaryOperationStrategy(OperationStrategy):
    """이항 연산 전략 기본 클래스"""
    
    @abstractmethod
    def execute(self, calculator: ArithmeticOperations, first: float, second: float) -> float:
        pass


class UnaryOperationStrategy(OperationStrategy):
    """단항 연산 전략 기본 클래스"""
    
    @abstractmethod
    def execute(self, calculator: ArithmeticOperations, first: float, second: float = None) -> float:
        pass


class AddStrategy(BinaryOperationStrategy):
    """덧셈 전략"""
    
    def execute(self, calculator: ArithmeticOperations, first: float, second: float) -> float:
        return float(calculator.add(int(first), int(second)))


class SubtractStrategy(BinaryOperationStrategy):
    """뺄셈 전략"""
    
    def execute(self, calculator: ArithmeticOperations, first: float, second: float) -> float:
        return float(calculator.subtract(int(first), int(second)))


class MultiplyStrategy(BinaryOperationStrategy):
    """곱셈 전략"""
    
    def execute(self, calculator: ArithmeticOperations, first: float, second: float) -> float:
        return float(calculator.multiply(int(first), int(second)))


class DivideStrategy(BinaryOperationStrategy):
    """나눗셈 전략 (소수점 포함)"""
    
    def execute(self, calculator: ArithmeticOperations, first: float, second: float) -> float:
        return calculator.divide_quotient(first, second)


class DivideIntegerStrategy(BinaryOperationStrategy):
    """정수 나눗셈 전략"""
    
    def execute(self, calculator: ArithmeticOperations, first: float, second: float) -> float:
        return float(calculator.divide(int(first), int(second)))


class PercentageStrategy(UnaryOperationStrategy):
    """백분율 전략"""
    
    PERCENTAGE_DIVISOR = 100
    
    def execute(self, calculator: ArithmeticOperations, first: float, second: float = None) -> float:
        return first / self.PERCENTAGE_DIVISOR


class ReciprocalStrategy(UnaryOperationStrategy):
    """역수 전략"""
    
    def execute(self, calculator: ArithmeticOperations, first: float, second: float = None) -> float:
        if first == 0:
            raise DivisionByZeroError("0으로 나눌 수 없습니다")
        return 1 / first


class SquareStrategy(UnaryOperationStrategy):
    """제곱 전략"""
    
    def execute(self, calculator: ArithmeticOperations, first: float, second: float = None) -> float:
        return first ** 2


class SquareRootStrategy(UnaryOperationStrategy):
    """제곱근 전략"""
    
    SQUARE_ROOT_POWER = 0.5
    
    def execute(self, calculator: ArithmeticOperations, first: float, second: float = None) -> float:
        if first < 0:
            raise ValueError("음수의 제곱근을 계산할 수 없습니다")
        return first ** self.SQUARE_ROOT_POWER


class OperationStrategyFactory:
    """연산 전략 팩토리"""
    
    _strategies = {
        'add': AddStrategy(),
        'subtract': SubtractStrategy(),
        'multiply': MultiplyStrategy(),
        'divide_quotient': DivideStrategy(),
        'divide': DivideIntegerStrategy(),
        'percentage': PercentageStrategy(),
        'reciprocal': ReciprocalStrategy(),
        'square': SquareStrategy(),
        'square_root': SquareRootStrategy(),
    }
    
    @classmethod
    def get_strategy(cls, operation_name: str) -> OperationStrategy:
        """
        연산 이름에 해당하는 전략을 반환합니다.
        
        Args:
            operation_name: 연산 이름
            
        Returns:
            OperationStrategy 인스턴스
            
        Raises:
            ValueError: 지원하지 않는 연산인 경우
        """
        strategy = cls._strategies.get(operation_name)
        if strategy is None:
            raise ValueError(f"지원하지 않는 연산: {operation_name}")
        return strategy
    
    @classmethod
    def register_strategy(cls, operation_name: str, strategy: OperationStrategy):
        """
        새로운 연산 전략을 등록합니다.
        
        Args:
            operation_name: 연산 이름
            strategy: OperationStrategy 인스턴스
        """
        cls._strategies[operation_name] = strategy

