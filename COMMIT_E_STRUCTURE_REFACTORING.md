# E. 구조 정리 커밋 - PR 설명

## 📝 변경 목록

### 1. Core 로직과 I/O 분리

#### 변경 전
- `src/arithmetic/arithmetic_operations.py`: 계산 로직 + I/O 코드 (`if __name__ == "__main__"` 블록)
- I/O 코드가 Core 로직 파일에 포함되어 있음

#### 변경 후
- `src/arithmetic/arithmetic_operations.py`: 순수 계산 로직만 포함 (I/O 제거)
- `src/cli/demo.py`: I/O 관련 코드 분리 (데모 프로그램)
- `main.py`: CLI 데모 프로그램 호출

**변경 위치:**
- `src/arithmetic/arithmetic_operations.py`: `if __name__ == "__main__"` 블록 및 모든 I/O 함수 제거
- 새 파일: `src/cli/demo.py`: I/O 관련 코드 이동
- `main.py`: CLI 데모 프로그램 호출로 변경

**변경 이유:**
- **관심사 분리**: Core 로직과 I/O를 명확히 분리
- **재사용성**: Core 로직을 다양한 인터페이스(CLI, API, GUI 등)에서 사용 가능
- **테스트 용이성**: 순수 함수/클래스로 테스트가 쉬워짐
- **의존성 제거**: Core 로직이 I/O에 의존하지 않음

---

### 2. 프로젝트 구조 개선

#### 변경 전
```
src/
└── arithmetic/
    ├── __init__.py
    ├── arithmetic_operations.py  (계산 로직 + I/O)
    └── exceptions.py
```

#### 변경 후
```
src/
├── arithmetic/
│   ├── __init__.py
│   ├── arithmetic_operations.py  (순수 계산 로직만)
│   └── exceptions.py
└── cli/
    ├── __init__.py
    └── demo.py  (I/O 처리)
```

**변경 위치:**
- 새 디렉토리: `src/cli/`
- 새 파일: `src/cli/__init__.py`, `src/cli/demo.py`

**변경 이유:**
- **모듈화**: CLI 관련 코드를 별도 모듈로 분리
- **확장성**: 향후 다른 인터페이스(API, GUI 등) 추가 용이
- **명확한 구조**: Core와 UI/CLI의 역할이 명확히 구분됨

---

### 3. Core 로직 순수성 유지

#### 변경 전
```python
# arithmetic_operations.py에 I/O 코드 포함
def _print_separator(...):
    print(...)  # I/O

def _run_demo():
    _print_header()  # I/O
    calculator = ArithmeticOperations()
    _run_basic_arithmetic_tests(calculator)  # I/O
    ...
```

#### 변경 후
```python
# arithmetic_operations.py: 순수 계산 로직만
class ArithmeticOperations:
    def add(self, first_number: int, second_number: int) -> int:
        return first_number + second_number
    # ... 순수 계산 메서드만
```

**변경 위치:**
- `src/arithmetic/arithmetic_operations.py`: 모든 I/O 관련 함수 제거

**변경 이유:**
- **순수 함수 원칙**: Core 로직은 부작용(side effect) 없이 동작
- **테스트 용이성**: I/O 없이 단위 테스트 가능
- **재사용성**: 다양한 환경에서 동일한 로직 사용 가능

---

### 4. CLI 인터페이스 분리

#### 변경 전
- `arithmetic_operations.py`에 데모 프로그램 포함
- Core 로직과 I/O가 혼재

#### 변경 후
- `src/cli/demo.py`: 데모 프로그램 전용 파일
- `calculator_console.py`: 사용자 입력 받는 CLI 프로그램
- `main.py`: 데모 프로그램 실행

**변경 위치:**
- 새 파일: `src/cli/demo.py`
- 수정: `main.py`

**변경 이유:**
- **책임 분리**: 각 파일이 명확한 역할을 가짐
- **유지보수성**: I/O 관련 변경 시 Core 로직에 영향 없음
- **확장성**: 새로운 인터페이스 추가 시 Core 로직 재사용 가능

---

## ✅ 검증 결과

- ✅ 모든 테스트 통과 (24/24)
- ✅ Core 로직은 순수 함수/클래스로 유지
- ✅ I/O 코드가 완전히 분리됨
- ✅ 데모 프로그램 정상 동작
- ✅ Linter 오류 없음

---

## 📊 변경 통계

| 항목 | 변경 전 | 변경 후 |
|------|---------|---------|
| `arithmetic_operations.py` 라인 수 | 273줄 | 100줄 (I/O 제거) |
| I/O 관련 함수 | Core 파일에 포함 | CLI 파일로 분리 |
| Core 로직 순수성 | I/O 의존 | 순수 함수/클래스 |
| 프로젝트 구조 | 단일 모듈 | Core + CLI 모듈 분리 |

---

## 🎯 변경 목적

이번 리팩토링은 **Core 계산 로직과 UI/CLI를 분리**하여 코드 구조를 개선하는 것을 목적으로 합니다:

1. **관심사 분리**: Core 로직과 I/O를 명확히 분리
2. **순수성 유지**: Core 로직은 부작용 없이 동작
3. **재사용성 향상**: Core 로직을 다양한 인터페이스에서 사용 가능
4. **테스트 용이성**: 순수 함수/클래스로 테스트가 쉬워짐
5. **확장성**: 새로운 인터페이스 추가 시 Core 로직 재사용

**동작 변경 없음**: 모든 기능은 기존과 동일하게 동작하며, 구조만 개선되었습니다.

---

## 📋 분리된 구조 상세

### Core 로직 (`src/arithmetic/arithmetic_operations.py`)

**특징:**
- 순수 함수/클래스 형태
- I/O 의존성 없음
- 부작용(side effect) 없음
- 재사용 가능

**포함 내용:**
- `ArithmeticOperations` 클래스
- 모든 계산 메서드 (`add`, `subtract`, `multiply`, `divide`, `divide_quotient`)
- 검증 메서드 (`_validate_divisor`)

### CLI 인터페이스 (`src/cli/demo.py`)

**특징:**
- I/O 처리 전담
- Core 로직을 사용하여 결과 출력
- 사용자 인터페이스 제공

**포함 내용:**
- 출력 함수들 (`_print_separator`, `_print_header`)
- 테스트 실행 함수들 (`_run_basic_arithmetic_tests`, etc.)
- 데모 프로그램 실행 함수 (`run_demo`)

### 사용자 입력 CLI (`calculator_console.py`)

**특징:**
- 사용자로부터 입력 받기
- 계산 수행
- 결과 출력

**포함 내용:**
- 입력 처리 함수들 (`get_integer_input`, `get_operator_input`)
- 계산 수행 함수 (`calculate`)
- 결과 출력 함수 (`display_result`)
- 메인 프로그램 (`main`)

---

## 🔍 구조 개선 효과

### Before (변경 전)
```
arithmetic_operations.py
├── ArithmeticOperations (계산 로직)
└── I/O 함수들 (출력, 테스트 실행 등)
    └── if __name__ == "__main__" (데모 실행)
```

**문제점:**
- Core 로직과 I/O가 혼재
- Core 로직이 I/O에 의존
- 재사용 어려움

### After (변경 후)
```
arithmetic_operations.py
└── ArithmeticOperations (순수 계산 로직)

cli/demo.py
└── I/O 함수들 + 데모 실행

calculator_console.py
└── 사용자 입력 CLI
```

**개선점:**
- Core 로직과 I/O 완전 분리
- Core 로직은 순수 함수/클래스
- 다양한 인터페이스에서 재사용 가능

---

## 💡 향후 확장 가능성

구조 분리로 인해 다음과 같은 확장이 용이해졌습니다:

1. **API 인터페이스 추가**
   ```python
   # src/api/calculator_api.py
   from src.arithmetic.arithmetic_operations import ArithmeticOperations
   # Flask/FastAPI 등으로 REST API 제공
   ```

2. **GUI 인터페이스 추가**
   ```python
   # src/gui/calculator_gui.py
   from src.arithmetic.arithmetic_operations import ArithmeticOperations
   # Tkinter/PyQt 등으로 GUI 제공
   ```

3. **웹 인터페이스 추가**
   ```python
   # src/web/calculator_web.py
   from src.arithmetic.arithmetic_operations import ArithmeticOperations
   # 웹 프레임워크로 웹 인터페이스 제공
   ```

모든 인터페이스는 동일한 Core 로직을 재사용할 수 있습니다.

