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
from PyQt6 import QtWidgets
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
        self.operation_symbol = None  # 연산자 기호 저장 (표시용)
        self.memory_value = 0.0
        self.should_reset_display = False
        self.buttons = []  # 버튼 리스트 저장 (폰트 크기 조정용)
        
        self.init_ui()
    
    def resizeEvent(self, event):
        """
        창 크기 변경 시 버튼과 디스플레이의 폰트 크기를 동적으로 조정합니다.
        Windows 계산기처럼 부드럽게 크기 조정됩니다.
        
        Args:
            event: 리사이즈 이벤트
        """
        super().resizeEvent(event)
        
        # 창 크기에 따라 폰트 크기 계산
        width = self.width()
        height = self.height()
        
        # 계산 과정 표시 폰트 크기 조정
        expression_font_size = max(10, min(20, int(height * 0.025)))
        self.expression_display.setFont(QFont("Arial", expression_font_size))
        
        # 디스플레이 폰트 크기 조정 (창 높이의 6% 정도, 더 큰 범위)
        display_font_size = max(14, min(48, int(height * 0.06)))
        self.display.setFont(QFont("Arial", display_font_size))
        
        # 버튼 폰트 크기 조정 (창 높이의 4% 정도, 더 큰 범위)
        button_font_size = max(10, min(28, int(height * 0.04)))
        for button in self.buttons:
            if button:
                button.setFont(QFont("Arial", button_font_size))
    
    def init_ui(self):
        """UI 초기화"""
        self.setWindowTitle("계산기")
        # 최소 크기 설정 (Windows 계산기처럼 작게도 가능)
        min_width = 180
        min_height = 250
        self.setMinimumSize(min_width, min_height)
        # 초기 크기를 최소 크기로 설정 (최대 축소 상태로 시작)
        self.resize(min_width, min_height)
        
        # 윈도우 배경색 설정
        self.setStyleSheet("""
            QMainWindow {
                background-color: #d0d0d0;
            }
        """)
        
        # 중앙 위젯
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 메인 레이아웃
        main_layout = QVBoxLayout()
        main_layout.setSpacing(2)  # spacing을 더 작게
        main_layout.setContentsMargins(2, 2, 2, 2)  # margins도 더 작게
        main_layout.setContentsMargins(0, 0, 0, 0)  # 공백 제거를 위해 margins를 0으로
        central_widget.setLayout(main_layout)
        
        # 디스플레이 생성 (stretch factor: 1.5 - Windows 계산기 비율)
        self._create_display(main_layout)
        
        # 버튼 레이아웃 생성 (stretch factor: 4 - Windows 계산기 비율)
        button_layout = self._create_button_layout()
        main_layout.addLayout(button_layout, 4)
    
    def _create_display(self, parent_layout):
        """
        디스플레이 위젯을 생성하고 레이아웃에 추가합니다.
        계산 과정을 표시하는 라인도 함께 생성합니다.
        
        Args:
            parent_layout: 부모 레이아웃
        """
        # 계산 과정 표시 라인 (작은 폰트)
        self.expression_display = QLabel("")
        self.expression_display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.expression_display.setFont(QFont("Arial", 12))
        self.expression_display.setStyleSheet("""
            QLabel {
                color: #555;
                padding: 5px 10px;
                background-color: #e0e0e0;
            }
        """)
        self.expression_display.setMinimumHeight(25)
        parent_layout.addWidget(self.expression_display)
        
        # 메인 디스플레이 (결과 표시)
        self.display = QLineEdit()
        self.display.setText("0")
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setFont(QFont("Arial", DISPLAY_FONT_SIZE))
        self.display.setStyleSheet("""
            QLineEdit {
                border: 2px solid #999;
                border-radius: 5px;
                padding: 10px;
                background-color: #e0e0e0;
                color: #222;
            }
        """)
        # 디스플레이도 최소 높이만 설정하여 확대/축소 가능 (Windows 계산기처럼)
        self.display.setMinimumHeight(40)
        # 디스플레이도 확장되도록 설정
        self.display.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Expanding
        )
        # stretch factor 설정으로 창 크기에 비례하여 확대/축소
        parent_layout.addWidget(self.display, 1)
    
    def _create_button_layout(self) -> QGridLayout:
        """
        버튼 레이아웃을 생성하고 반환합니다.
        Windows 계산기처럼 버튼들이 균등하게 공간을 차지하고 공백이 생기지 않습니다.
        
        Returns:
            버튼이 배치된 GridLayout
        """
        button_layout = QGridLayout()
        button_layout.setSpacing(1)  # spacing을 최소화하여 공백 제거
        button_layout.setContentsMargins(0, 0, 0, 0)  # margins 제거
        # 모든 열에 균등한 stretch 설정 (Windows 계산기처럼)
        for i in range(6):
            button_layout.setColumnStretch(i, 1)
        
        # 메모리 버튼 생성
        self._create_memory_buttons(button_layout)
        
        # 일반 버튼 생성
        self._create_operation_buttons(button_layout)
        
        # 모든 행에 균등한 stretch 설정 (Windows 계산기처럼 높이도 균등)
        for i in range(7):  # 메모리 1행 + 일반 버튼 6행
            button_layout.setRowStretch(i, 1)
        
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
        """
        버튼 생성 헬퍼 메서드
        Windows 계산기처럼 크기가 자동으로 조정되고 공백이 생기지 않습니다.
        """
        button = QPushButton(text)
        # 고정 크기 제거 - 레이아웃에 맞게 완전히 채우도록 (Windows 계산기처럼)
        button.setMinimumHeight(20)  # 최소 높이만 설정
        button.setMinimumWidth(25)   # 최소 너비만 설정
        # 버튼이 항상 확장되도록 설정
        button.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Expanding
        )
        # 폰트 크기도 동적으로 조정되도록 (resizeEvent에서 처리)
        button.setFont(QFont("Arial", BUTTON_FONT_SIZE))
        button.clicked.connect(handler)
        button.setStyleSheet(self._get_button_style('default'))
        # 버튼 리스트에 추가 (resizeEvent에서 폰트 크기 조정용)
        self.buttons.append(button)
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
                    background-color: #c0c0c0;
                    color: #222;
                    font-size: 12px;
                }
                QPushButton:hover {
                    background-color: #b0b0b0;
                }
            """,
            'operator': """
                QPushButton {
                    background-color: #b5b5b5;
                    color: #111;
                }
                QPushButton:hover {
                    background-color: #a5a5a5;
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
                    background-color: #c0c0c0;
                    color: #222;
                }
                QPushButton:hover {
                    background-color: #b0b0b0;
                }
            """,
            'default': """
                QPushButton {
                    background-color: #d5d5d5;
                    border: 1px solid #999;
                    border-radius: 5px;
                    color: #222;
                }
                QPushButton:hover {
                    background-color: #c5c5c5;
                }
                QPushButton:pressed {
                    background-color: #b5b5b5;
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
        self.operation_symbol = operation_text  # 연산자 기호 저장
        self.should_reset_display = True
        
        # 계산 과정 표시 업데이트
        self._update_expression_display()
        
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
            
            # 계산 과정 표시
            value_display = str(int(value)) if value == int(value) else str(value)
            expression = f"{operation}({value_display}) ="
            self.expression_display.setText(expression)
            
            # Strategy Pattern을 사용하여 연산 수행
            strategy = OperationStrategyFactory.get_strategy(operation_name)
            result = strategy.execute(self.calculator, value)
            
            self.update_display(result)
            self.should_reset_display = True
            
            # 계산 완료 후 표현식 초기화 (약간의 지연 후)
            # self.expression_display.setText("")  # 즉시 초기화하지 않고 결과와 함께 표시
            
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
            
            # 계산 과정 표시 업데이트 (계산 전)
            self._update_expression_display_with_result(current)
            
            # Strategy Pattern을 사용하여 연산 수행
            strategy = OperationStrategyFactory.get_strategy(self.operation)
            result = strategy.execute(self.calculator, self.previous_value, current)
            
            self.update_display(result)
            self.previous_value = None
            self.operation = None
            self.operation_symbol = None
            self.should_reset_display = True
            
            # 계산 완료 후 표현식 초기화
            self.expression_display.setText("")
            
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
        self.operation_symbol = None
        self.should_reset_display = False
        self.update_display("0")
        self.expression_display.setText("")
    
    def _update_expression_display(self):
        """계산 과정 표시 업데이트 (연산자 입력 시)"""
        if self.previous_value is not None and self.operation_symbol:
            # 값이 정수인 경우 소수점 제거
            prev_display = str(int(self.previous_value)) if self.previous_value == int(self.previous_value) else str(self.previous_value)
            expression = f"{prev_display} {self.operation_symbol}"
            self.expression_display.setText(expression)
    
    def _update_expression_display_with_result(self, second_value):
        """계산 과정 표시 업데이트 (결과 계산 전)"""
        if self.previous_value is not None and self.operation_symbol:
            # 값이 정수인 경우 소수점 제거
            prev_display = str(int(self.previous_value)) if self.previous_value == int(self.previous_value) else str(self.previous_value)
            second_display = str(int(second_value)) if second_value == int(second_value) else str(second_value)
            expression = f"{prev_display} {self.operation_symbol} {second_display} ="
            self.expression_display.setText(expression)
    
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

