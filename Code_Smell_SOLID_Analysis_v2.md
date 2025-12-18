# 코드 스멜 및 SOLID 원칙 위반 분석 (v2.0)

**분석 일자**: 2025-12-16  
**분석 범위**: 전체 프로젝트 (Core, CLI, GUI)

---

## 📊 분석 결과 요약

| 카테고리 | 총 항목 | High | Med | Low |
|---------|---------|------|-----|-----|
| **코드 스멜** | 12 | 4 | 5 | 3 |
| **SOLID 위반** | 6 | 3 | 2 | 1 |
| **합계** | **18** | **7** | **7** | **4** |

---

## 🔴 High 우선순위 (7개)

| # | 파일 | 위치 | 문제 유형 | 문제 설명 | 리팩토링 기법 | 우선순위 |
|---|------|------|----------|----------|-------------|---------|
| 1 | `calculator_gui.py` | `init_ui()` (40-149) | **긴 함수** | `init_ui()` 메서드가 110줄로 너무 김 (UI 초기화, 버튼 생성, 스타일 설정 모두 포함) | Extract Method, Extract Class | High |
| 2 | `calculator_gui.py` | `init_ui()` (94-147) | **중복 코드** | 버튼 스타일시트가 여러 곳에서 중복 (메모리 버튼, 연산자 버튼, Clear 버튼 등) | Extract Method (`_get_button_style`) | High |
| 3 | `calculator_gui.py` | `calculate_result()` (269-298) | **중복 코드** | 연산자별 if-elif 체인으로 연산 처리 로직 중복 | Strategy Pattern | High |
| 4 | `calculator_gui.py` | `calculate_unary_operation()` (241-267) | **중복 코드** | 단항 연산별 if-elif 체인으로 연산 처리 로직 중복 | Strategy Pattern | High |
| 5 | `calculator_console.py` | `calculate()` (51-75) | **중복 코드** | 연산자별 if-elif 체인으로 연산 처리 로직 중복 | Strategy Pattern | High |
| 6 | `calculator_gui.py` | 전체 클래스 | **SRP 위반** | `CalculatorGUI`가 UI 초기화, 계산 로직, 메모리 관리, 이벤트 처리 등 여러 책임 | Extract Class (CalculatorController, MemoryManager) | High |
| 7 | `calculator_gui.py` | 전체 클래스 | **OCP 위반** | 새 연산자 추가 시 `calculate_result()`, `calculate_unary_operation()` 수정 필요 | Strategy Pattern, Factory Pattern | High |

---

## 🟡 Med 우선순위 (7개)

| # | 파일 | 위치 | 문제 유형 | 문제 설명 | 리팩토링 기법 | 우선순위 |
|---|------|------|----------|----------|-------------|---------|
| 8 | `calculator_gui.py` | `init_ui()` (42-43) | **매직 넘버** | 윈도우 크기 `320, 500` 하드코딩 | Extract Constant (`WINDOW_WIDTH`, `WINDOW_HEIGHT`) | Med |
| 9 | `calculator_gui.py` | `create_button()` (154) | **매직 넘버** | 버튼 높이 `60`, 폰트 크기 `14`, `24` 하드코딩 | Extract Constant | Med |
| 10 | `calculator_gui.py` | `update_display()` (180) | **매직 넘버** | 최대 디스플레이 길이 `15`, 과학적 표기법 소수점 `10` 하드코딩 | Extract Constant | Med |
| 11 | `calculator_gui.py` | `calculate_unary_operation()` (247, 259) | **매직 넘버** | 백분율 `100`, 제곱근 `0.5` 하드코딩 | Extract Constant | Med |
| 12 | `calculator_console.py` | `_print_separator()` (93), `display_result()` (116) | **매직 넘버** | 구분선 길이 `40` 하드코딩 | Extract Constant (`SEPARATOR_LENGTH`) | Med |
| 13 | `calculator_gui.py` | `calculate_result()`, `calculate_unary_operation()` (266, 297) | **예외 처리** | 일반 `Exception` 사용으로 구체적인 예외 처리 불가 | Replace Exception with Specific Exception | Med |
| 14 | `calculator_gui.py` | `__init__()` (31) | **의존성** | `ArithmeticOperations` 구체 클래스에 직접 의존 | Dependency Injection | Med |

---

## 🟢 Low 우선순위 (4개)

| # | 파일 | 위치 | 문제 유형 | 문제 설명 | 리팩토링 기법 | 우선순위 |
|---|------|------|----------|----------|-------------|---------|
| 15 | `calculator_gui.py` | `init_ui()` (59-66, 94-103, 112-121, 124-131, 134-141) | **중복 코드** | 스타일시트 문자열이 여러 곳에서 중복 | Extract Constant (`BUTTON_STYLES`) | Low |
| 16 | `calculator_console.py` | `get_operator_input()` (41) | **매직 넘버/하드코딩** | 연산자 리스트 하드코딩 | Configuration, Strategy Pattern | Low |
| 17 | `calculator_gui.py` | `update_memory_buttons()` (368-371) | **미완성 코드** | 빈 메서드 (pass만 있음) | Implement or Remove | Low |
| 18 | `calculator_gui.py` | `init_ui()` (10-11) | **의존성** | `sys.path` 조작으로 프로젝트 루트 추가 | Proper Package Structure | Low |

---

## 📋 상세 분석

### 🔴 High 우선순위 상세

#### 1. 긴 함수: `init_ui()` (calculator_gui.py:40-149)

**문제**:
- 110줄의 긴 메서드
- UI 초기화, 버튼 생성, 스타일 설정 등 여러 책임

**리팩토링 기법**:
- Extract Method: `_create_display()`, `_create_memory_buttons()`, `_create_operation_buttons()`, `_create_number_buttons()`
- Extract Class: `ButtonFactory` 클래스로 버튼 생성 로직 분리

**예상 효과**:
- 가독성 향상
- 테스트 용이성 증가
- 유지보수성 향상

---

#### 2. 중복 코드: 버튼 스타일시트 (calculator_gui.py:94-147)

**문제**:
- 메모리 버튼, 연산자 버튼, Clear 버튼 등에서 유사한 스타일시트 중복

**리팩토링 기법**:
- Extract Method: `_get_button_style(button_type: str) -> str`
- Extract Constant: 버튼 타입별 스타일을 상수로 정의

**예상 효과**:
- 스타일 변경 시 한 곳만 수정
- 일관성 있는 UI

---

#### 3-5. 중복 코드: 연산자 처리 if-elif 체인

**문제**:
- `calculator_gui.py`: `calculate_result()` (277-284), `calculate_unary_operation()` (246-259)
- `calculator_console.py`: `calculate()` (64-73)
- 연산자별 if-elif 체인으로 확장성 부족

**리팩토링 기법**:
- Strategy Pattern: 각 연산을 Strategy 클래스로 분리
- Factory Pattern: 연산자 기호로 Strategy 인스턴스 생성

**예상 효과**:
- 새 연산자 추가 시 기존 코드 수정 불필요
- OCP 준수

---

#### 6. SRP 위반: CalculatorGUI 클래스

**문제**:
- UI 초기화, 계산 로직, 메모리 관리, 이벤트 처리 등 여러 책임

**리팩토링 기법**:
- Extract Class:
  - `CalculatorController`: 계산 로직 관리
  - `MemoryManager`: 메모리 기능 관리
  - `DisplayManager`: 디스플레이 업데이트 관리

**예상 효과**:
- 단일 책임 원칙 준수
- 테스트 용이성 증가

---

#### 7. OCP 위반: 연산자 처리 확장성 부족

**문제**:
- 새 연산자 추가 시 `calculate_result()`, `calculate_unary_operation()` 수정 필요

**리팩토링 기법**:
- Strategy Pattern + Factory Pattern
- 연산자 등록 시스템

**예상 효과**:
- 확장성 향상
- OCP 준수

---

### 🟡 Med 우선순위 상세

#### 8-11. 매직 넘버

**문제**:
- 하드코딩된 숫자 값들 (윈도우 크기, 버튼 크기, 폰트 크기 등)

**리팩토링 기법**:
- Extract Constant: 상수로 정의

**예상 효과**:
- 가독성 향상
- 유지보수성 향상

---

#### 13. 예외 처리

**문제**:
- 일반 `Exception` 사용으로 구체적인 예외 처리 불가

**리팩토링 기법**:
- Replace Exception with Specific Exception
- 커스텀 예외 클래스 사용

**예상 효과**:
- 더 정확한 예외 처리
- 디버깅 용이성 증가

---

#### 14. 의존성

**문제**:
- `ArithmeticOperations` 구체 클래스에 직접 의존

**리팩토링 기법**:
- Dependency Injection
- Abstract Interface 정의

**예상 효과**:
- DIP 준수
- 테스트 용이성 증가

---

### 🟢 Low 우선순위 상세

#### 15-18. 기타 개선 사항

- 스타일시트 상수화
- 연산자 리스트 설정화
- 미완성 코드 구현/제거
- 프로젝트 구조 개선

---

## 🎯 리팩토링 우선순위 추천

### Phase 1: High 우선순위 (즉시)
1. 연산자 처리 Strategy Pattern 적용 (항목 3, 4, 5)
2. `init_ui()` 메서드 분리 (항목 1)
3. 버튼 스타일시트 중복 제거 (항목 2)

### Phase 2: Med 우선순위 (단기)
4. 매직 넘버 상수화 (항목 8-12)
5. 예외 처리 개선 (항목 13)
6. 의존성 주입 적용 (항목 14)

### Phase 3: Low 우선순위 (중기)
7. 기타 개선 사항 (항목 15-18)

---

## 📝 참고사항

- **코드 스멜**: 코드의 품질을 저하시키는 패턴
- **SOLID 원칙**: 객체지향 설계 원칙
  - **S**ingle Responsibility Principle (단일 책임 원칙)
  - **O**pen/Closed Principle (개방/폐쇄 원칙)
  - **L**iskov Substitution Principle (리스코프 치환 원칙)
  - **I**nterface Segregation Principle (인터페이스 분리 원칙)
  - **D**ependency Inversion Principle (의존성 역전 원칙)

---

**작성일**: 2025-12-16  
**버전**: v2.0 (GUI 코드 포함)

