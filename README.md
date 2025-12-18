# 사칙연산 시스템 (Arithmetic Operations)

## 프로젝트 개요

이 프로젝트는 사칙연산(덧셈, 뺄셈, 곱셈, 나눗셈)의 정확도를 검증하는 애플리케이션입니다. 다양한 경계 조건과 예외 상황을 처리하여 견고한 산술 연산 기능을 제공합니다.

## 테스트 케이스

### 테스트 범위
- **테스트 ID**: TC-CMM-001 (Common Module) / TC-AO-001 (Arithmetic Operations)
- **테스트 목적**: 사칙연산 정확도 테스트
- **테스트 기능**: +, -, *, / 기능 점검
- **작성일**: 2020-09-01
- **버전**: v1.0

### 테스트 케이스 상세

| 테스트 케이스 | 입력값 | 예상 결과 | 중요도 | 상태 |
|--------------|--------|----------|--------|------|
| 덧셈 (양수) | 1 + 10 | 11 | 중요 | 성공 |
| 덧셈 (0 포함) | 0 + 1 | 1 | 중요 | 성공 |
| 나눗셈 (0으로 나누기) | 0 / 0 | ArithmeticException 예외 발생 | 중요 | 성공 |
| 덧셈 (음수) | -1 + (-10) | -11 | 보통 | 성공 |
| 뺄셈 | 5 - 2 | 3 | 중요 | 성공 |
| 곱셈 (음수) | -5 * -3 | 15 | 보통 | 성공 |
| 나눗셈 (정수) | 5 / 2 | 2 | 중요 | 성공 |
| 나눗셈 (몫, 소수점) | 5 ÷ 2 (quotient) | 2.5 | 보통 | 성공 |
| 곱셈 (0 포함) | 0 * 10 | 0 | 낮음 | 성공 |
| 나눗셈 (음수) | -10 / 2 | -5 | 중요 | 성공 |

### 추가 테스트 사례

#### 예외 처리 확인
- **0 / 0** → `ArithmeticException` 예외 발생 확인

#### 다양한 조합
- 양수, 음수, 0을 포함한 다양한 테스트 케이스를 추가하여 연산의 정확도와 범위를 검증

#### 몫 계산 테스트 (quotient)
- 정수 나눗셈 대신 소수점을 포함한 결과를 테스트

이 테스트 케이스는 기능의 정확성과 예외 처리를 포함하여 클래스의 모든 기능을 검증합니다.

## Red-Green-Refactor 방식

이 프로젝트는 **TDD (Test-Driven Development)** 방식인 **Red-Green-Refactor** 사이클을 따릅니다.

### 사이클 설명

1. **🔴 Red (빨강)**: 실패하는 테스트를 먼저 작성 -> 진행 중
   - 테스트를 작성하고 실행하여 실패하는 것을 확인
   - 실패하는 테스트가 있어야 올바른 방향으로 개발하고 있음을 보장
   - 현재 브랜치: `red`

2. **🟢 Green (초록)**: 테스트를 통과하는 최소한의 코드 작성
   - 테스트를 통과시키기 위해 필요한 최소한의 코드만 작성
   - 복잡한 최적화나 리팩토링은 아직 하지 않음
   - 브랜치: `green`

3. **🔵 Refactor (리팩토링)**: 코드 개선
   - 테스트가 통과하는 상태를 유지하면서 코드 품질 개선
   - 중복 제거, 가독성 향상, 성능 최적화 등
   - 브랜치: `refactor`

### 진행 단계

#### Step 1: Red - 테스트 작성 (현재 단계)
```bash
# red 브랜치에서 작업
git checkout red

# 테스트 파일 작성 (ArithmeticOperationsTest.java)
# 모든 테스트 케이스를 작성하고 실행하여 실패 확인
./gradlew test
# 또는
mvn test
```

**작성할 테스트 메서드:**
- `testAdditionPositiveNumbers()` - 1 + 10 = 11
- `testAdditionWithZero()` - 0 + 1 = 1
- `testDivisionByZero()` - 0 / 0 → ArithmeticException
- `testAdditionNegativeNumbers()` - -1 + (-10) = -11
- `testSubtraction()` - 5 - 2 = 3
- `testMultiplicationNegativeNumbers()` - -5 * -3 = 15
- `testDivisionInteger()` - 5 / 2 = 2
- `testDivisionQuotient()` - 5 ÷ 2 = 2.5
- `testMultiplicationWithZero()` - 0 * 10 = 0
- `testDivisionNegativeNumber()` - -10 / 2 = -5

#### Step 2: Green - 최소 구현
```bash
# green 브랜치 생성 및 전환
git checkout -b green

# ArithmeticOperations.java 파일에 최소한의 구현 작성
# 모든 테스트가 통과할 때까지 반복
./gradlew test
# 또는
mvn test
```

**구현 우선순위 목록:**

##### 🔴 높은 우선순위 (필수 구현)
1. **기본 사칙연산 메서드 구현**
   - `add(int a, int b)` - 덧셈 (양수, 음수, 0 포함)
   - `subtract(int a, int b)` - 뺄셈
   - `multiply(int a, int b)` - 곱셈 (양수, 음수, 0 포함)
   - `divide(int a, int b)` - 정수 나눗셈 (소수점 버림)
   - `divideQuotient(int a, int b)` - 소수점 나눗셈

2. **예외 처리 구현**
   - `divide()` 메서드의 0으로 나누기 예외 처리
     - `b == 0`일 때 `ArithmeticException` 발생
     - 예외 메시지: "Division by zero"
   - `divideQuotient()` 메서드의 0으로 나누기 예외 처리
     - `b == 0`일 때 `ArithmeticException` 발생
     - 예외 메시지: "Division by zero"

##### 🟡 중간 우선순위 (권장 구현)
3. **경계값 처리 검증**
   - 음수 연산 정확도 확인
   - 0 포함 연산 정확도 확인
   - 정수 나눗셈과 소수점 나눗셈 구분 확인

##### 🟢 낮은 우선순위 (선택적 구현)
4. **추가 테스트 케이스 고려**
   - 매우 큰 수(Big Integer) 처리 테스트
   - 소수점 나눗셈 정밀도 테스트

**구현 체크리스트:**
- [x] 모든 기본 사칙연산 메서드 구현 완료
- [x] `divide()` 메서드 예외 처리 구현 완료
- [x] `divideQuotient()` 메서드 예외 처리 구현 완료
- [x] `divideQuotient()`의 0으로 나누기 테스트 추가 완료
- [x] 경계값 처리 검증 테스트 추가 완료 (음수, 0 포함, 나눗셈 구분)
- [x] 매우 큰 수(Big Integer) 처리 테스트 추가 완료
- [x] 소수점 나눗셈 정밀도 테스트 추가 완료
- [x] 모든 테스트 케이스 통과 확인 (24/24)
- [x] 컴파일 오류 없음 확인
- [x] 런타임 오류 없음 확인

#### Step 3: Refactor - 코드 개선
```bash
# refactor 브랜치 생성 및 전환
git checkout -b refactor

# 테스트가 통과하는 상태를 유지하면서 코드 개선
# 리팩토링 후 테스트 재실행하여 회귀 테스트
./gradlew test
# 또는
mvn test
```

---

## Refactoring TODO

### 📋 리팩토링 체크리스트 (Code Smells & SOLID 원칙 위반)

**분석 일자**: 2025-12-16  
**분석 범위**: 전체 프로젝트 (Core, CLI, GUI)  
**총 항목**: 18개 (High: 7, Med: 7, Low: 4)

---

#### 🔴 High 우선순위 (7개)

##### 1. 코드 스멜: 긴 함수
- [x] **긴 함수: `init_ui()` 메서드**
  - 위치: `src/gui/calculator_gui.py:40-149` (110줄)
  - 문제: UI 초기화, 버튼 생성, 스타일 설정 등 여러 책임 포함
  - 리팩토링 기법: Extract Method, Extract Class
  - 작업: `_create_display()`, `_create_memory_buttons()`, `_create_operation_buttons()`, `_create_number_buttons()` 메서드로 분리 또는 `ButtonFactory` 클래스 생성
  - 완료일: 2025-12-16

##### 2. 코드 스멜: 중복 코드
- [x] **중복 코드: 버튼 스타일시트**
  - 위치: `src/gui/calculator_gui.py:94-147`
  - 문제: 메모리 버튼, 연산자 버튼, Clear 버튼 등에서 유사한 스타일시트 중복
  - 리팩토링 기법: Extract Method
  - 작업: `_get_button_style(button_type: str) -> str` 메서드 생성 및 버튼 타입별 스타일 상수 정의
  - 완료일: 2025-12-16

- [x] **중복 코드: 연산자 처리 if-elif 체인 (GUI)**
  - 위치: `src/gui/calculator_gui.py:calculate_result()` (269-298)
  - 문제: 연산자별 if-elif 체인으로 연산 처리 로직 중복
  - 리팩토링 기법: Strategy Pattern
  - 작업: 각 연산을 Strategy 클래스로 분리하고 Factory Pattern으로 인스턴스 생성
  - 완료일: 2025-12-16

- [x] **중복 코드: 단항 연산 처리 if-elif 체인 (GUI)**
  - 위치: `src/gui/calculator_gui.py:calculate_unary_operation()` (241-267)
  - 문제: 단항 연산별 if-elif 체인으로 연산 처리 로직 중복
  - 리팩토링 기법: Strategy Pattern
  - 작업: 단항 연산 Strategy 클래스 생성 및 Factory Pattern 적용
  - 완료일: 2025-12-16

- [x] **중복 코드: 연산자 처리 if-elif 체인 (CLI)**
  - 위치: `calculator_console.py:calculate()` (51-75)
  - 문제: 연산자별 if-elif 체인으로 연산 처리 로직 중복
  - 리팩토링 기법: Strategy Pattern
  - 작업: OperationStrategy 인터페이스 및 구현 클래스 생성, Factory Pattern 적용
  - 완료일: 2025-12-16

##### 3. SOLID 위반: SRP (Single Responsibility Principle)
- [ ] **SRP 위반: CalculatorGUI 클래스의 다중 책임**
  - 위치: `src/gui/calculator_gui.py` 전체 클래스
  - 문제: UI 초기화, 계산 로직, 메모리 관리, 이벤트 처리 등 여러 책임
  - 리팩토링 기법: Extract Class
  - 작업: `CalculatorController` (계산 로직), `MemoryManager` (메모리 기능), `DisplayManager` (디스플레이 업데이트) 클래스로 분리

##### 4. SOLID 위반: OCP (Open/Closed Principle)
- [x] **OCP 위반: 연산자 처리 확장성 부족**
  - 위치: `src/gui/calculator_gui.py` 전체 클래스
  - 문제: 새 연산자 추가 시 `calculate_result()`, `calculate_unary_operation()` 수정 필요
  - 리팩토링 기법: Strategy Pattern, Factory Pattern
  - 작업: Strategy Pattern + Factory Pattern 적용 및 연산자 등록 시스템 구현
  - 완료일: 2025-12-16

---

#### 🟡 Med 우선순위 (7개)

##### 5. 코드 스멜: 매직 넘버
- [x] **매직 넘버: 윈도우 크기**
  - 위치: `src/gui/calculator_gui.py:init_ui()` (42-43)
  - 문제: 윈도우 크기 `320, 500` 하드코딩
  - 리팩토링 기법: Extract Constant
  - 작업: `WINDOW_WIDTH = 320`, `WINDOW_HEIGHT = 500` 상수 정의
  - 완료일: 2025-12-16

- [x] **매직 넘버: 버튼 및 폰트 크기**
  - 위치: `src/gui/calculator_gui.py:create_button()` (154), `init_ui()` (58)
  - 문제: 버튼 높이 `60`, 폰트 크기 `14`, `24` 하드코딩
  - 리팩토링 기법: Extract Constant
  - 작업: `BUTTON_HEIGHT = 60`, `BUTTON_FONT_SIZE = 14`, `DISPLAY_FONT_SIZE = 24` 상수 정의
  - 완료일: 2025-12-16

- [x] **매직 넘버: 디스플레이 관련**
  - 위치: `src/gui/calculator_gui.py:update_display()` (180)
  - 문제: 최대 디스플레이 길이 `15`, 과학적 표기법 소수점 `10` 하드코딩
  - 리팩토링 기법: Extract Constant
  - 작업: `MAX_DISPLAY_LENGTH = 15`, `SCIENTIFIC_NOTATION_DECIMALS = 10` 상수 정의
  - 완료일: 2025-12-16

- [x] **매직 넘버: 연산 관련**
  - 위치: `src/gui/calculator_gui.py:calculate_unary_operation()` (247, 259)
  - 문제: 백분율 `100`, 제곱근 `0.5` 하드코딩
  - 리팩토링 기법: Extract Constant
  - 작업: `PERCENTAGE_DIVISOR = 100`, `SQUARE_ROOT_POWER = 0.5` 상수 정의
  - 완료일: 2025-12-16

- [ ] **매직 넘버: 구분선 길이 (CLI)**
  - 위치: `calculator_console.py:_print_separator()` (93), `display_result()` (116)
  - 문제: 구분선 길이 `40` 하드코딩
  - 리팩토링 기법: Extract Constant
  - 작업: `SEPARATOR_LENGTH = 40` 상수 정의

##### 6. 코드 스멜: 예외 처리
- [ ] **예외 처리: 일반 Exception 사용**
  - 위치: `src/gui/calculator_gui.py:calculate_result()`, `calculate_unary_operation()` (266, 297)
  - 문제: 일반 `Exception` 사용으로 구체적인 예외 처리 불가
  - 리팩토링 기법: Replace Exception with Specific Exception
  - 작업: 구체적인 예외 타입으로 변경 (예: `ValueError`, `ArithmeticError` 등)

##### 7. SOLID 위반: DIP (Dependency Inversion Principle)
- [ ] **DIP 위반: 구체 클래스 직접 의존**
  - 위치: `src/gui/calculator_gui.py:__init__()` (31)
  - 문제: `ArithmeticOperations` 구체 클래스에 직접 의존
  - 리팩토링 기법: Dependency Injection
  - 작업: 인터페이스 정의 및 생성자에서 `calculator` 인스턴스를 주입받도록 수정

---

#### 🟢 Low 우선순위 (4개)

##### 8. 코드 스멜: 중복 코드 (추가)
- [ ] **중복 코드: 스타일시트 문자열**
  - 위치: `src/gui/calculator_gui.py:init_ui()` (59-66, 94-103, 112-121, 124-131, 134-141)
  - 문제: 스타일시트 문자열이 여러 곳에서 중복
  - 리팩토링 기법: Extract Constant
  - 작업: `BUTTON_STYLES` 딕셔너리로 상수화

##### 9. 코드 스멜: 하드코딩
- [ ] **하드코딩: 연산자 리스트**
  - 위치: `calculator_console.py:get_operator_input()` (41)
  - 문제: 연산자 리스트 하드코딩
  - 리팩토링 기법: Configuration, Strategy Pattern
  - 작업: 설정 파일 또는 Strategy Pattern과 연계하여 확장성 향상

##### 10. 미완성 코드
- [ ] **미완성 코드: 빈 메서드**
  - 위치: `src/gui/calculator_gui.py:update_memory_buttons()` (368-371)
  - 문제: 빈 메서드 (pass만 있음)
  - 리팩토링 기법: Implement or Remove
  - 작업: 메모리 버튼 상태 업데이트 로직 구현 또는 메서드 제거

##### 11. 의존성: 프로젝트 구조
- [ ] **의존성: sys.path 조작**
  - 위치: `src/gui/calculator_gui.py:init_ui()` (10-11)
  - 문제: `sys.path` 조작으로 프로젝트 루트 추가
  - 리팩토링 기법: Proper Package Structure
  - 작업: 적절한 패키지 구조로 변경하여 `sys.path` 조작 제거

---

### 🎯 리팩토링 진행 현황

| 우선순위 | 총 항목 | 완료 | 진행중 | 미시작 | 완료율 |
|---------|---------|------|--------|--------|--------|
| **High** | 7 | 5 | 0 | 2 | 71% |
| **Med** | 7 | 4 | 0 | 3 | 57% |
| **Low** | 4 | 0 | 0 | 4 | 0% |
| **합계** | **18** | **9** | **0** | **9** | **50%** |

---

### ✅ 완료 기준 (Definition of Done)

#### 필수 완료 기준

1. **코드 변경**
   - [ ] 리팩토링 기법이 올바르게 적용되었으며, 코드의 가독성과 유지보수성이 향상되었는가?
   - [ ] 기능 동작은 변경되지 않았는가? (기존 기능 100% 유지)

2. **테스트 통과**
   - [ ] 모든 기존 테스트 케이스가 100% 통과하는가?
   - [ ] 코드 커버리지가 유지되거나 향상되었는가?
   - [ ] 새로운 테스트 케이스가 추가되었는가? (필요한 경우)

3. **코드 품질**
   - [ ] Linter (flake8, pylint 등)를 통과하며, 새로운 경고나 오류가 발생하지 않는가?
   - [ ] 타입 힌트가 일관되게 유지되는가?
   - [ ] 관련 문서화(docstrings, 주석)가 업데이트되었는가?

4. **검증**
   - [ ] 코드 리뷰를 통해 변경 사항이 승인되었는가? (필요한 경우)
   - [ ] 수동 테스트 또는 회귀 테스트를 통해 예상치 못한 부작용이 없는지 확인되었는가?
   - [ ] GUI/CLI 애플리케이션이 정상적으로 동작하는가?

#### 우선순위별 완료 기준

##### High 우선순위
- [ ] 모든 High 우선순위 항목이 위의 필수 완료 기준을 충족하며, 코드의 주요 중복이 제거되고 SOLID 원칙 위반이 해결되었는가?
- [ ] 시스템의 핵심 기능에 대한 안정성과 확장성이 확보되었는가?

##### Med 우선순위
- [ ] 모든 Med 우선순위 항목이 위의 필수 완료 기준을 충족하며, 코드의 가독성과 명확성이 크게 향상되었는가?
- [ ] 주요 의존성 문제가 해결되고 예외 처리가 개선되었는가?

##### Low 우선순위
- [ ] 모든 Low 우선순위 항목이 위의 필수 완료 기준을 충족하며, 전반적인 코드 품질과 일관성이 개선되었는가?

#### 최종 완료 기준
- [ ] 모든 리팩토링 항목이 완료되었는가?
- [ ] 모든 테스트가 100% 통과하는가?
- [ ] 코드 커버리지가 최소 90% 이상 유지되는가?
- [ ] `README.md` 및 관련 문서가 최신 상태로 업데이트되었는가?
- [ ] 리팩토링 리포트가 작성되었는가? (선택적)

---

### 📝 참고 문서

- 상세 분석 내용: `Code_Smell_SOLID_Analysis_v2.md` 참조
- 리팩토링 기법 가이드: 각 항목별 리팩토링 기법 상세 설명 포함

---

### 📊 리팩토링 진행 현황

| 우선순위 | 총 항목 | 완료 | 진행중 | 미시작 | 완료율 |
|---------|---------|------|--------|--------|--------|
| **High** | 9 | 0 | 0 | 9 | 0% |
| **Med** | 6 | 0 | 0 | 6 | 0% |
| **Low** | 2 | 0 | 0 | 2 | 0% |
| **합계** | **17** | **0** | **0** | **17** | **0%** |

---

### 📝 참고 문서

- 상세 분석 내용: `Code_Smell_SOLID_Analysis.md` 참조
- 리팩토링 기법 가이드: 각 항목별 리팩토링 기법 상세 설명 포함

---

## 프로젝트 구조

```
ARITHMETIC/
├── README.md
├── requirements.txt
├── pytest.ini
├── src/
│   ├── arithmetic/
│   │   ├── __init__.py
│   │   ├── arithmetic_operations.py    # 사칙연산 Core 로직
│   │   └── exceptions.py                # 커스텀 예외 클래스
│   ├── cli/
│   │   ├── __init__.py
│   │   └── demo.py                      # CLI 데모 프로그램
│   └── gui/
│       ├── __init__.py
│       └── calculator_gui.py            # PyQt6 GUI 애플리케이션
├── tests/
│   ├── __init__.py
│   └── test_arithmetic_operations.py    # 단위 테스트
├── calculator_console.py                 # 콘솔 프로그램
├── main.py                               # 메인 데모 프로그램
└── .gitignore
```

## 환경 설정

### 요구사항
- **Python**: 3.10 이상
- **운영 체제**: Windows 10 이상 (Linux, macOS도 지원)
- **GUI 프레임워크**: PyQt6 (GUI 사용 시)
- **테스트 프레임워크**: pytest

### 설치 방법

1. **Python 버전 확인**
```bash
python --version
```

2. **프로젝트 클론 (이미 있는 경우)**
```bash
git clone https://github.com/csu1oh4226/Arithmetic.git
cd ARITHMETIC
```

3. **의존성 설치**
```bash
pip install -r requirements.txt
```

4. **의존성 확인**
```bash
pip list | grep -E "pytest|PyQt6"
```

## 실행 방법

### 🖥️ GUI 애플리케이션 실행 (PyQt6)

Windows 계산기와 유사한 GUI 인터페이스를 제공합니다.

#### 1. PyQt6 설치
```bash
pip install -r requirements.txt
```

#### 2. GUI 실행
```bash
# 방법 1: 모듈로 실행 (권장)
python -m src.gui.calculator_gui

# 방법 2: 직접 실행
python src/gui/calculator_gui.py
```

#### 3. GUI 기능
- **기본 연산**: 덧셈(+), 뺄셈(-), 곱셈(×), 나눗셈(÷)
- **고급 연산**: 백분율(%), 역수(1/x), 제곱(x²), 제곱근(²√x)
- **메모리 기능**: MC, MR, M+, M-, MS
- **Clear 기능**: C (전체 초기화), CE (현재 입력 초기화), ⌫ (백스페이스)
- **부호 변경**: +/- 버튼

자세한 사용법은 `GUI_SETUP_GUIDE.md`를 참조하세요.

---

### 💻 CLI 애플리케이션 실행

#### 콘솔 프로그램 실행
```bash
python calculator_console.py
```

#### 데모 프로그램 실행
```bash
python main.py
```

---

## 테스트 실행

### 전체 테스트 실행 (pytest)
```bash
pytest tests/test_arithmetic_operations.py -v
```

### 커버리지 확인
```bash
pytest tests/test_arithmetic_operations.py --cov=src/arithmetic --cov-report=html
```

### 특정 테스트 실행
```bash
pytest tests/test_arithmetic_operations.py::TestArithmeticOperations::test_addition_positive -v
```

## 개발 가이드

### 클래스 시그니처 예시
```java
package com.arithmetic;

public class ArithmeticOperations {
    
    /**
     * 두 정수의 덧셈을 수행합니다.
     * 
     * @param a 첫 번째 정수
     * @param b 두 번째 정수
     * @return a + b의 결과
     */
    public int add(int a, int b) {
        // TODO: 구현 필요
        return 0;
    }
    
    /**
     * 두 정수의 뺄셈을 수행합니다.
     * 
     * @param a 첫 번째 정수
     * @param b 두 번째 정수
     * @return a - b의 결과
     */
    public int subtract(int a, int b) {
        // TODO: 구현 필요
        return 0;
    }
    
    /**
     * 두 정수의 곱셈을 수행합니다.
     * 
     * @param a 첫 번째 정수
     * @param b 두 번째 정수
     * @return a * b의 결과
     */
    public int multiply(int a, int b) {
        // TODO: 구현 필요
        return 0;
    }
    
    /**
     * 두 정수의 나눗셈을 수행합니다 (정수 나눗셈).
     * 
     * @param a 첫 번째 정수
     * @param b 두 번째 정수
     * @return a / b의 결과 (정수)
     * @throws ArithmeticException b가 0인 경우
     */
    public int divide(int a, int b) {
        // TODO: 구현 필요
        return 0;
    }
    
    /**
     * 두 정수의 나눗셈을 수행합니다 (소수점 포함).
     * 
     * @param a 첫 번째 정수
     * @param b 두 번째 정수
     * @return a / b의 결과 (소수점)
     * @throws ArithmeticException b가 0인 경우
     */
    public double divideQuotient(int a, int b) {
        // TODO: 구현 필요
        return 0.0;
    }
}
```

### 테스트 작성 예시
```java
package com.arithmetic;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class ArithmeticOperationsTest {
    
    private ArithmeticOperations calculator = new ArithmeticOperations();
    
    @Test
    void testAdditionPositiveNumbers() {
        assertEquals(11, calculator.add(1, 10));
    }
    
    @Test
    void testAdditionWithZero() {
        assertEquals(1, calculator.add(0, 1));
    }
    
    @Test
    void testDivisionByZero() {
        assertThrows(ArithmeticException.class, () -> {
            calculator.divide(0, 0);
        });
    }
    
    @Test
    void testAdditionNegativeNumbers() {
        assertEquals(-11, calculator.add(-1, -10));
    }
    
    @Test
    void testSubtraction() {
        assertEquals(3, calculator.subtract(5, 2));
    }
    
    @Test
    void testMultiplicationNegativeNumbers() {
        assertEquals(15, calculator.multiply(-5, -3));
    }
    
    @Test
    void testDivisionInteger() {
        assertEquals(2, calculator.divide(5, 2));
    }
    
    @Test
    void testDivisionQuotient() {
        assertEquals(2.5, calculator.divideQuotient(5, 2));
    }
    
    @Test
    void testMultiplicationWithZero() {
        assertEquals(0, calculator.multiply(0, 10));
    }
    
    @Test
    void testDivisionNegativeNumber() {
        assertEquals(-5, calculator.divide(-10, 2));
    }
}
```

## 성공/실패 기준

### 성공 기준
- ✅ 모든 테스트 케이스가 예상한 결과를 생성
- ✅ 코드가 오류 없이 컴파일/실행됨
- ✅ 모든 종속성이 올바르게 설치되고 구성됨
- ✅ 예외 처리가 올바르게 동작 (0으로 나누기 등)

### 실패 기준
- ❌ 테스트 케이스가 예상한 결과를 생성하지 않음
- ❌ 컴파일 오류 또는 런타임 오류 발생
- ❌ 예외 처리가 올바르게 동작하지 않음

## 전제 조건

- 프로그램은 오류 없이 성공적으로 컴파일되어야 합니다.
- 모든 종속성을 올바르게 설치하고 구성해야 합니다.

## 특별 절차

1. **테스트 결과 기록**: 모든 테스트 실행 결과를 기록하고 문서화
2. **테스트 사례 업데이트**: 테스트 결과에 따라 테스트 케이스 문서 업데이트
3. **실패 보고**: 모든 실패 사례를 개발팀에 즉시 전달하여 해결

## 브랜치 전략

이 프로젝트는 Red-Green-Refactor 방식에 따라 브랜치를 분리합니다:

- **main**: 메인 브랜치 (최종 완성된 코드)
- **red**: 테스트 작성 단계 (현재 브랜치)
- **green**: 최소 구현 단계
- **refactor**: 코드 개선 단계

각 단계를 완료한 후 main 브랜치로 병합합니다.

## 참고사항

- 정수 나눗셈(`/`)과 몫 계산(`÷`)은 다른 결과를 반환합니다.
  - 정수 나눗셈: `5 / 2 = 2` (정수 결과)
  - 몫 계산: `5 ÷ 2 = 2.5` (소수점 결과)
- 0으로 나누기는 `DivisionByZeroError` 예외를 발생시킵니다.
- 음수 연산도 올바르게 처리되어야 합니다.

---

## 예외 처리 정책

### 📋 정책 결정

#### 1. 0으로 나누기 처리

**결정**: 예외를 던지는 방식 (`DivisionByZeroError` 발생)

**이유**:
- **명확성**: 0으로 나누기는 수학적으로 정의되지 않은 연산이므로 예외가 적절함
- **안전성**: 잘못된 결과(0 반환)를 조용히 반환하는 것보다 예외로 명시적으로 처리하는 것이 안전함
- **디버깅 용이성**: 예외를 통해 문제를 즉시 발견하고 처리할 수 있음
- **일관성**: Python의 표준 라이브러리와 동일한 방식 (`ZeroDivisionError`와 유사)

**구현**:
```python
# 0으로 나누기 시 DivisionByZeroError 발생
calculator.divide(10, 0)  # DivisionByZeroError: Division by zero
```

**대안 고려사항**:
- ❌ 0 반환: 잘못된 결과를 반환하여 버그를 숨길 수 있음
- ❌ None 반환: 타입 안정성 저하 및 추가 None 체크 필요
- ✅ 예외 발생: 명확하고 안전한 처리 방식

---

#### 2. 입력 타입 검증

**결정**: CLI에서는 재시도 방식, Core 로직에서는 타입 힌트로 검증

**이유**:
- **사용자 경험**: CLI에서는 잘못된 입력 시 재시도를 통해 사용자 친화적 경험 제공
- **타입 안정성**: Python의 타입 힌트를 통해 정적 타입 검사 가능
- **유연성**: Core 로직은 순수 함수로 유지하여 다양한 인터페이스에서 사용 가능

**구현**:
```python
# CLI: 재시도 방식 (사용자 친화적)
def get_integer_input(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ 올바른 정수를 입력해주세요.")

# Core: 타입 힌트로 검증 (런타임 검증은 호출자 책임)
def add(self, first_number: int, second_number: int) -> int:
    return first_number + second_number
```

**향후 개선 가능성**:
- API 인터페이스에서는 `InvalidInputError` 예외를 던지는 방식으로 변경 가능
- 설정 파일을 통해 검증 정책을 선택할 수 있도록 확장 가능

---

#### 3. 커스텀 예외 클래스

**도입한 예외 클래스**:

1. **`DivisionByZeroError`**
   - 상속: `ArithmeticError`
   - 용도: 0으로 나누기 시 발생
   - 위치: `src/arithmetic/exceptions.py`

2. **`InvalidInputError`**
   - 상속: `ValueError`
   - 용도: 잘못된 입력값 처리 (향후 확장용)
   - 위치: `src/arithmetic/exceptions.py`

**이유**:
- **명확성**: 일반적인 `ArithmeticError`보다 구체적인 예외로 의도 전달
- **필터링 용이성**: 특정 예외만 처리 가능 (`except DivisionByZeroError`)
- **확장성**: 향후 추가 예외 처리 정책 적용 용이

---

### 📝 예외 처리 가이드

#### Core 로직 (`ArithmeticOperations`)

```python
# 0으로 나누기 시 DivisionByZeroError 발생
try:
    result = calculator.divide(10, 0)
except DivisionByZeroError as e:
    print(f"나눗셈 오류: {e}")
```

#### CLI 인터페이스 (`calculator_console.py`)

```python
# DivisionByZeroError를 사용자 친화적 메시지로 변환
try:
    result = calculate(calculator, a, op, b)
except DivisionByZeroError as e:
    _handle_calculation_error(e, "0으로 나누기 오류")
```

---

### 🔄 정책 변경 이력

| 버전 | 날짜 | 변경 내용 |
|------|------|----------|
| v1.0 | 2025-12-16 | 예외 처리 정책 수립 및 문서화 |
| - | - | `DivisionByZeroError` 커스텀 예외 도입 |
| - | - | 입력 검증 정책 통일 |

---

## 라이선스

이 프로젝트는 교육 목적으로 작성되었습니다.
