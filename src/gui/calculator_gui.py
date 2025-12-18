"""
PyQt6 기반 계산기 GUI 애플리케이션
Windows 계산기와 유사한 인터페이스를 제공합니다.
"""

import sys
from pathlib import Path

# 프로젝트 루트를 Python 경로에 추가
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout,
    QPushButton, QLineEdit, QLabel
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

from src.arithmetic.arithmetic_operations import ArithmeticOperations
from src.arithmetic.exceptions import DivisionByZeroError
from src.gui.operation_strategies import OperationStrategyFactory

# 상수 정의
WINDOW_WIDTH = 320
WINDOW_HEIGHT = 500
BUTTON_HEIGHT = 60
BUTTON_FONT_SIZE = 14
DISPLAY_FONT_SIZE = 24
MAX_DISPLAY_LENGTH = 15
SCIENTIFIC_NOTATION_DECIMALS = 10
PERCENTAGE_DIVISOR = 100
SQUARE_ROOT_POWER = 0.5


class CalculatorGUI(QMainWindow):
    """
    계산기 GUI 메인 윈도우 클래스
    """
    
    def __init__(self):
        super().__init__()
        self.calculator = ArithmeticOperations()
        self.current_value = "0"
        self.previous_value = None
        self.operation = None
        self.memory_value = 0.0
        self.should_reset_display = False
        
        self.init_ui()
    
    def init_ui(self):
        """UI 초기화"""
        self.setWindowTitle("계산기")
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)
        
        # 중앙 위젯
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 메인 레이아웃
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        
        # 디스플레이 생성
        self._create_display(main_layout)
        
        # 버튼 레이아웃 생성
        button_layout = self._create_button_layout()
        main_layout.addLayout(button_layout)
    
    def _create_display(self, parent_layout):
        """
        디스플레이 위젯을 생성하고 레이아웃에 추가합니다.
        
        Args:
            parent_layout: 부모 레이아웃
        """
        self.display = QLineEdit()
        self.display.setText("0")
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setFont(QFont("Arial", DISPLAY_FONT_SIZE))
        self.display.setStyleSheet("""
            QLineEdit {
                border: 2px solid #ccc;
                border-radius: 5px;
                padding: 10px;
                background-color: white;
            }
        """)
        parent_layout.addWidget(self.display)
    
    def _create_button_layout(self) -> QGridLayout:
        """
        버튼 레이아웃을 생성하고 반환합니다.
        
        Returns:
            버튼이 배치된 GridLayout
        """
        button_layout = QGridLayout()
        button_layout.setSpacing(5)
        
        # 메모리 버튼 생성
        self._create_memory_buttons(button_layout)
        
        # 일반 버튼 생성
        self._create_operation_buttons(button_layout)
        
        return button_layout
    
    def _create_memory_buttons(self, button_layout: QGridLayout):
        """
        메모리 버튼을 생성하고 레이아웃에 추가합니다.
        
        Args:
            button_layout: 버튼 레이아웃
        """
        memory_buttons = ['MC', 'MR', 'M+', 'M-', 'MS', 'M▼']
        memory_row = 0
        for i, btn_text in enumerate(memory_buttons):
            btn = self.create_button(btn_text, self.handle_memory_operation)
            btn.setStyleSheet(self._get_button_style('memory'))
            button_layout.addWidget(btn, memory_row, i)
    
    def _create_operation_buttons(self, button_layout: QGridLayout):
        """
        연산 버튼을 생성하고 레이아웃에 추가합니다.
        
        Args:
            button_layout: 버튼 레이아웃
        """
        buttons = [
            # 첫 번째 행: 고급 기능
            ['%', 'CE', 'C', '⌫'],
            # 두 번째 행: 고급 연산
            ['1/x', 'x²', '²√x', '÷'],
            # 세 번째 행
            ['7', '8', '9', '×'],
            # 네 번째 행
            ['4', '5', '6', '-'],
            # 다섯 번째 행
            ['1', '2', '3', '+'],
            # 여섯 번째 행
            ['+/-', '0', '.', '='],
        ]
        
        row_offset = 1
        for row_idx, row in enumerate(buttons):
            for col_idx, btn_text in enumerate(row):
                btn = self._create_single_button(btn_text)
                button_layout.addWidget(btn, row_idx + row_offset, col_idx)
    
    def _create_single_button(self, btn_text: str) -> QPushButton:
        """
        단일 버튼을 생성하고 적절한 핸들러와 스타일을 설정합니다.
        
        Args:
            btn_text: 버튼 텍스트
            
        Returns:
            생성된 버튼
        """
        if btn_text == '=':
            btn = self.create_button(btn_text, self.calculate_result)
            btn.setStyleSheet(self._get_button_style('equals'))
        elif btn_text in ['+', '-', '×', '÷', '%', '1/x', 'x²', '²√x']:
            btn = self.create_button(btn_text, self.handle_operation)
            btn.setStyleSheet(self._get_button_style('operator'))
        elif btn_text in ['CE', 'C', '⌫']:
            btn = self.create_button(btn_text, self.handle_clear)
            btn.setStyleSheet(self._get_button_style('clear'))
        elif btn_text == '+/-':
            btn = self.create_button(btn_text, self.handle_plus_minus)
        else:
            btn = self.create_button(btn_text, self.handle_number_input)
        
        return btn
    
    def create_button(self, text, handler):
        """버튼 생성 헬퍼 메서드"""
        button = QPushButton(text)
        button.setFixedHeight(BUTTON_HEIGHT)
        button.setFont(QFont("Arial", BUTTON_FONT_SIZE))
        button.clicked.connect(handler)
        button.setStyleSheet(self._get_button_style('default'))
        return button
    
    def _get_button_style(self, button_type: str) -> str:
        """
        버튼 타입에 따른 스타일시트를 반환합니다.
        
        Args:
            button_type: 버튼 타입 ('memory', 'operator', 'equals', 'clear', 'default')
            
        Returns:
            스타일시트 문자열
        """
        styles = {
            'memory': """
                QPushButton {
                    background-color: #f0f0f0;
                    color: #666;
                    font-size: 12px;
                }
                QPushButton:hover {
                    background-color: #e0e0e0;
                }
            """,
            'operator': """
                QPushButton {
                    background-color: #e0e0e0;
                }
                QPushButton:hover {
                    background-color: #d0d0d0;
                }
            """,
            'equals': """
                QPushButton {
                    background-color: #0078d4;
                    color: white;
                    font-weight: bold;
                }
                QPushButton:hover {
                    background-color: #106ebe;
                }
            """,
            'clear': """
                QPushButton {
                    background-color: #f0f0f0;
                }
                QPushButton:hover {
                    background-color: #e0e0e0;
                }
            """,
            'default': """
                QPushButton {
                    background-color: white;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                }
                QPushButton:hover {
                    background-color: #f0f0f0;
                }
                QPushButton:pressed {
                    background-color: #e0e0e0;
                }
            """
        }
        return styles.get(button_type, styles['default'])
    
    def update_display(self, value):
        """디스플레이 업데이트"""
        # 값이 정수인 경우 소수점 제거
        if isinstance(value, float) and value.is_integer():
            value = int(value)
        
        display_text = str(value)
        # 너무 긴 숫자는 과학적 표기법 사용
        if len(display_text) > MAX_DISPLAY_LENGTH:
            display_text = f"{value:.{SCIENTIFIC_NOTATION_DECIMALS}e}"
        
        self.display.setText(display_text)
        self.current_value = display_text
    
    def handle_number_input(self):
        """숫자 입력 처리"""
        button = self.sender()
        digit = button.text()
        
        if self.should_reset_display:
            self.current_value = "0"
            self.should_reset_display = False
        
        if self.current_value == "0":
            if digit == '.':
                self.current_value = "0."
            else:
                self.current_value = digit
        else:
            if digit == '.' and '.' in self.current_value:
                return  # 이미 소수점이 있으면 무시
            self.current_value += digit
        
        self.update_display(self.current_value)
    
    def handle_operation(self):
        """연산자 버튼 처리"""
        button = self.sender()
        operation_text = button.text()
        
        # 기존 연산이 있으면 먼저 계산
        if self.operation and self.previous_value is not None:
            self.calculate_result()
        
        # 현재 값을 이전 값으로 저장
        try:
            self.previous_value = float(self.current_value)
        except ValueError:
            self.previous_value = 0.0
        
        # 연산자 매핑
        operation_map = {
            '+': 'add',
            '-': 'subtract',
            '×': 'multiply',
            '÷': 'divide_quotient',
            '%': 'percentage',
            '1/x': 'reciprocal',
            'x²': 'square',
            '²√x': 'square_root',
        }
        
        self.operation = operation_map.get(operation_text)
        self.should_reset_display = True
        
        # 단항 연산은 즉시 계산
        if operation_text in ['%', '1/x', 'x²', '²√x']:
            self.calculate_unary_operation(operation_text)
    
    def calculate_unary_operation(self, operation):
        """단항 연산 계산"""
        try:
            value = float(self.current_value)
            
            # 연산자 매핑
            operation_map = {
                '%': 'percentage',
                '1/x': 'reciprocal',
                'x²': 'square',
                '²√x': 'square_root',
            }
            
            operation_name = operation_map.get(operation)
            if operation_name is None:
                return
            
            # Strategy Pattern을 사용하여 연산 수행
            strategy = OperationStrategyFactory.get_strategy(operation_name)
            result = strategy.execute(self.calculator, value)
            
            self.update_display(result)
            self.should_reset_display = True
            
        except DivisionByZeroError:
            self.show_error("0으로 나눌 수 없습니다")
        except ValueError as e:
            self.show_error(str(e))
        except Exception as e:
            self.show_error(f"오류: {str(e)}")
    
    def calculate_result(self):
        """계산 결과 처리"""
        if self.operation is None or self.previous_value is None:
            return
        
        try:
            current = float(self.current_value)
            
            # Strategy Pattern을 사용하여 연산 수행
            strategy = OperationStrategyFactory.get_strategy(self.operation)
            result = strategy.execute(self.calculator, self.previous_value, current)
            
            self.update_display(result)
            self.previous_value = None
            self.operation = None
            self.should_reset_display = True
            
        except DivisionByZeroError:
            self.show_error("0으로 나눌 수 없습니다")
            self.reset_calculator()
        except ValueError as e:
            self.show_error(str(e))
            self.reset_calculator()
        except Exception as e:
            self.show_error(f"오류: {str(e)}")
            self.reset_calculator()
    
    def handle_plus_minus(self):
        """+/- 버튼 처리 (부호 변경)"""
        try:
            value = float(self.current_value)
            value = -value
            self.update_display(value)
        except Exception:
            pass
    
    def handle_clear(self):
        """Clear 버튼 처리"""
        button = self.sender()
        button_text = button.text()
        
        if button_text == 'C':
            # 전체 초기화
            self.reset_calculator()
        elif button_text == 'CE':
            # 현재 입력만 초기화
            self.current_value = "0"
            self.update_display("0")
        elif button_text == '⌫':
            # 백스페이스
            if len(self.current_value) > 1:
                self.current_value = self.current_value[:-1]
            else:
                self.current_value = "0"
            self.update_display(self.current_value)
    
    def reset_calculator(self):
        """계산기 초기화"""
        self.current_value = "0"
        self.previous_value = None
        self.operation = None
        self.should_reset_display = False
        self.update_display("0")
    
    def handle_memory_operation(self):
        """메모리 연산 처리"""
        button = self.sender()
        operation = button.text()
        
        try:
            current = float(self.current_value)
            
            if operation == 'MC':
                # Memory Clear
                self.memory_value = 0.0
            elif operation == 'MR':
                # Memory Recall
                self.update_display(self.memory_value)
                self.should_reset_display = True
            elif operation == 'M+':
                # Memory Add
                self.memory_value += current
            elif operation == 'M-':
                # Memory Subtract
                self.memory_value -= current
            elif operation == 'MS':
                # Memory Store
                self.memory_value = current
            
            # 메모리에 값이 있으면 버튼 활성화 표시
            self.update_memory_buttons()
            
        except Exception as e:
            self.show_error(str(e))
    
    def update_memory_buttons(self):
        """메모리 버튼 상태 업데이트"""
        # 메모리에 값이 있으면 버튼 활성화 표시 (구현 생략)
        pass
    
    def show_error(self, message):
        """에러 메시지 표시"""
        self.display.setText(f"오류: {message}")
        self.current_value = "0"
        self.should_reset_display = True


def main():
    """메인 함수: GUI 애플리케이션 실행"""
    app = QApplication(sys.argv)
    
    # 애플리케이션 스타일 설정
    app.setStyle('Fusion')
    
    calculator = CalculatorGUI()
    calculator.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

