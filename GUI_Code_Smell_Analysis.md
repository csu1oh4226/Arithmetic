# GUI 계산기 코드 스멜 분석

**분석 일자**: 2025-12-16  
**분석 범위**: `src/gui/calculator_gui.py`, `src/gui/operation_strategies.py`  
**총 항목**: 20개

---

## 📊 분석 결과 요약

| 카테고리 | 총 항목 | High | Med | Low |
|---------|---------|------|-----|-----|
| **코드 스멜** | 14 | 5 | 6 | 3 |
| **SOLID 위반** | 6 | 2 | 3 | 1 |
| **합계** | **20** | **7** | **9** | **4** |

---

## 🔴 High 우선순위 (7개)

| # | 파일 | 위치 | 문제 유형 | 문제 설명 | 리팩토링 기법 | 우선순위 |
|---|------|------|----------|----------|-------------|---------|
| 1 | `calculator_gui.py` | `handle_operation()` (400-409), `calculate_unary_operation()` (428-433) | **중복 코드** | 연산자 매핑 딕셔너리가 두 곳에서 중복 정의 | Extract Constant (`OPERATION_MAP`) | High |
| 2 | `calculator_gui.py` | `_update_expression_display()` (538), `_update_expression_display_with_result()` (546), `calculate_unary_operation()` (440) | **중복 코드** | 값 포맷팅 로직 (정수 체크 및 변환)이 여러 곳에서 중복 | Extract Method (`_format_value_for_display`) | High |
| 3 | `calculator_gui.py` | `init_ui()` (106-108) | **중복 코드** | `setContentsMargins`가 두 번 호출됨 (중복 설정) | Remove Duplicate | High |
| 4 | `calculator_gui.py` | `_get_button_style()` (283-347) | **긴 함수** | 스타일시트 문자열이 매우 길고 복잡함 (65줄) | Extract Constant (`BUTTON_STYLES`), Extract Method | High |
| 5 | `calculator_gui.py` | `CalculatorGUI` 클래스 전체 | **SRP 위반** | UI 초기화, 계산 로직, 메모리 관리, 이벤트 처리, 디스플레이 관리 등 여러 책임 | Extract Class (CalculatorController, MemoryManager, DisplayManager) | High |
| 6 | `calculator_gui.py` | `resizeEvent()` (70, 74, 78) | **매직 넘버** | 폰트 크기 계산 비율 (0.025, 0.06, 0.04) 하드코딩 | Extract Constant (`FONT_SIZE_RATIOS`) | High |
| 7 | `calculator_gui.py` | `init_ui()` (87-88) | **매직 넘버** | 최소 크기 (180, 250) 하드코딩 | Extract Constant (`MIN_WINDOW_WIDTH`, `MIN_WINDOW_HEIGHT`) | High |

---

## 🟡 Med 우선순위 (9개)

| # | 파일 | 위치 | 문제 유형 | 문제 설명 | 리팩토링 기법 | 우선순위 |
|---|------|------|----------|----------|-------------|---------|
| 8 | `calculator_gui.py` | `_create_display()` (130-136), `_get_button_style()` (294-345) | **매직 넘버** | 스타일시트에 하드코딩된 색상 값들 (#d0d0d0, #c0c0c0, #b5b5b5, #0078d4 등) | Extract Constant (`COLOR_PALETTE`) | Med |
| 9 | `calculator_gui.py` | `resizeEvent()` (70, 74, 78) | **매직 넘버** | 폰트 크기 최소/최대 값 (10, 20, 14, 48, 10, 28) 하드코딩 | Extract Constant (`FONT_SIZE_LIMITS`) | Med |
| 10 | `calculator_gui.py` | `_create_display()` (137, 156) | **매직 넘버** | 최소 높이 (25, 40) 하드코딩 | Extract Constant | Med |
| 11 | `calculator_gui.py` | `create_button()` (268-269) | **매직 넘버** | 버튼 최소 크기 (20, 25) 하드코딩 | Extract Constant | Med |
| 12 | `calculator_gui.py` | `handle_plus_minus()` (501) | **예외 처리** | 일반 `Exception`을 조용히 무시 (`pass`) | Replace Exception with Specific Exception | Med |
| 13 | `calculator_gui.py` | `calculate_result()`, `calculate_unary_operation()` (491, 458) | **예외 처리** | 일반 `Exception` 사용으로 구체적인 예외 처리 불가 | Replace Exception with Specific Exception | Med |
| 14 | `calculator_gui.py` | `__init__()` (10-11) | **의존성** | `sys.path` 조작으로 프로젝트 루트 추가 | Proper Package Structure | Med |
| 15 | `calculator_gui.py` | `__init__()` (44) | **의존성** | `ArithmeticOperations` 구체 클래스에 직접 의존 | Dependency Injection | Med |
| 16 | `calculator_gui.py` | `_create_single_button()` (245-257) | **중복 코드** | 버튼 타입별 if-elif 체인으로 핸들러/스타일 설정 중복 | Strategy Pattern 또는 Factory Pattern | Med |

---

## 🟢 Low 우선순위 (4개)

| # | 파일 | 위치 | 문제 유형 | 문제 설명 | 리팩토링 기법 | 우선순위 |
|---|------|------|----------|----------|-------------|---------|
| 17 | `calculator_gui.py` | `update_memory_buttons()` (582-585) | **미완성 코드** | 빈 메서드 (pass만 있음) | Implement or Remove | Low |
| 18 | `calculator_gui.py` | `calculate_unary_operation()` (451-452) | **주석 처리된 코드** | 주석 처리된 코드가 남아있음 | Remove Dead Code | Low |
| 19 | `calculator_gui.py` | `_create_memory_buttons()` (192-204) | **사용되지 않는 코드** | 메모리 버튼 생성 메서드가 주석 처리되어 사용되지 않음 | Remove or Implement | Low |
| 20 | `calculator_gui.py` | `handle_operation()`, `calculate_unary_operation()` (419, 435) | **의미없는 이름** | 변수명 `operation`, `operation_name`이 혼용됨 | Rename Variable (일관성 유지) | Low |

---

## 📋 상세 분석

### 🔴 High 우선순위 상세

#### 1. 중복 코드: 연산자 매핑 딕셔너리

**문제**:
- `handle_operation()` (400-409)와 `calculate_unary_operation()` (428-433)에서 연산자 매핑 딕셔너리가 중복 정의됨

**리팩토링 기법**:
- Extract Constant: 클래스 레벨 상수로 정의
- 예: `OPERATION_MAP = {'+': 'add', ...}`

**예상 효과**:
- 중복 제거
- 유지보수성 향상
- 일관성 확보

---

#### 2. 중복 코드: 값 포맷팅 로직

**문제**:
- `_update_expression_display()`, `_update_expression_display_with_result()`, `calculate_unary_operation()`에서 값 포맷팅 로직이 중복
- `str(int(value)) if value == int(value) else str(value)` 패턴 반복

**리팩토링 기법**:
- Extract Method: `_format_value_for_display(value: float) -> str`

**예상 효과**:
- 중복 제거
- 일관된 포맷팅
- 테스트 용이성 증가

---

#### 3. 중복 코드: setContentsMargins 중복 호출

**문제**:
- `init_ui()` (106-108)에서 `setContentsMargins`가 두 번 호출됨
- 첫 번째 호출이 무의미함

**리팩토링 기법**:
- Remove Duplicate: 첫 번째 호출 제거

**예상 효과**:
- 불필요한 코드 제거
- 가독성 향상

---

#### 4. 긴 함수: _get_button_style()

**문제**:
- 스타일시트 문자열이 매우 길고 복잡함 (65줄)
- 유지보수 어려움

**리팩토링 기법**:
- Extract Constant: `BUTTON_STYLES` 딕셔너리로 상수화
- 별도 파일로 분리 가능 (`styles.py`)

**예상 효과**:
- 가독성 향상
- 스타일 관리 용이
- 재사용성 증가

---

#### 5. SRP 위반: CalculatorGUI 클래스

**문제**:
- UI 초기화, 계산 로직, 메모리 관리, 이벤트 처리, 디스플레이 관리 등 여러 책임

**리팩토링 기법**:
- Extract Class:
  - `CalculatorController`: 계산 로직 관리
  - `MemoryManager`: 메모리 기능 관리
  - `DisplayManager`: 디스플레이 업데이트 관리

**예상 효과**:
- 단일 책임 원칙 준수
- 테스트 용이성 증가
- 코드 재사용성 향상

---

#### 6-7. 매직 넘버

**문제**:
- 폰트 크기 계산 비율, 최소 크기 등 하드코딩

**리팩토링 기법**:
- Extract Constant

**예상 효과**:
- 가독성 향상
- 유지보수성 향상

---

### 🟡 Med 우선순위 상세

#### 8-11. 매직 넘버 (색상, 크기 등)

**문제**:
- 스타일시트에 하드코딩된 색상 값들
- 최소/최대 폰트 크기, 최소 높이 등 하드코딩

**리팩토링 기법**:
- Extract Constant: 색상 팔레트, 크기 상수 정의

**예상 효과**:
- 일관성 있는 UI
- 테마 변경 용이

---

#### 12-13. 예외 처리

**문제**:
- 일반 `Exception` 사용
- 예외를 조용히 무시하는 경우

**리팩토링 기법**:
- Replace Exception with Specific Exception
- 적절한 예외 처리

**예상 효과**:
- 더 정확한 예외 처리
- 디버깅 용이성 증가

---

#### 14-15. 의존성

**문제**:
- `sys.path` 조작
- 구체 클래스 직접 의존

**리팩토링 기법**:
- Proper Package Structure
- Dependency Injection

**예상 효과**:
- DIP 준수
- 테스트 용이성 증가

---

#### 16. 중복 코드: 버튼 타입별 if-elif 체인

**문제**:
- `_create_single_button()`에서 버튼 타입별 if-elif 체인

**리팩토링 기법**:
- Strategy Pattern 또는 Factory Pattern

**예상 효과**:
- 확장성 향상
- 중복 제거

---

### 🟢 Low 우선순위 상세

#### 17-19. 미완성/사용되지 않는 코드

**문제**:
- 빈 메서드
- 주석 처리된 코드
- 사용되지 않는 메서드

**리팩토링 기법**:
- Implement or Remove
- Remove Dead Code

**예상 효과**:
- 코드 정리
- 혼란 방지

---

#### 20. 의미없는 이름

**문제**:
- 변수명 일관성 부족

**리팩토링 기법**:
- Rename Variable

**예상 효과**:
- 가독성 향상

---

## 🎯 리팩토링 우선순위 추천

### Phase 1: High 우선순위 (즉시)
1. 중복 코드 제거 (연산자 매핑, 값 포맷팅)
2. 중복 설정 제거
3. 매직 넘버 상수화

### Phase 2: Med 우선순위 (단기)
4. 스타일시트 상수화
5. 예외 처리 개선
6. 의존성 주입 적용

### Phase 3: Low 우선순위 (중기)
7. 미완성 코드 정리
8. 변수명 일관성 개선

---

## 📝 참고사항

- **코드 스멜**: 코드의 품질을 저하시키는 패턴
- **SOLID 원칙**: 객체지향 설계 원칙
- **리팩토링 기법**: 각 항목별 상세 설명은 기존 `Code_Smell_SOLID_Analysis_v2.md` 참조

---

**작성일**: 2025-12-16  
**버전**: v1.0 (GUI 코드 전용)

