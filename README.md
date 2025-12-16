# 소수 확인 애플리케이션 (Prime Number Checker)

## 프로젝트 개요

이 프로젝트는 0부터 1000까지의 범위에서 숫자가 소수인지 확인하는 애플리케이션입니다. 다양한 경계 조건과 예외 상황을 처리하여 견고한 소수 검사 기능을 제공합니다.

## 테스트 케이스

### 테스트 범위
- **범위**: 0 ~ 1000
- **테스트 ID**: TC-PNC-001
- **테스트 목적**: 다양한 경계 및 경계 사례를 사용하여 소수 검사 기능의 정확성을 확인

### 테스트 케이스 상세

| 입력값 | 예상 결과 | 중요도 |
|--------|----------|--------|
| "-1" | "잘못됨: 음수" | 높음 |
| "0" | "아니요" | 높음 |
| "3" | "예" | 높음 |
| "1000" | "아니요" | 높음 |
| "1001" | "잘못됨: 범위를 벗어났습니다." | 높음 |
| "27" | "아니요" | 중간 |
| "r" | "잘못됨: 숫자가 아닌 입력" | 중간 |
| " " | "잘못됨: 공백 입력" | 중간 |

## Red-Green-Refactor 방식

이 프로젝트는 **TDD (Test-Driven Development)** 방식인 **Red-Green-Refactor** 사이클을 따릅니다.

### 사이클 설명

1. **🔴 Red (빨강)**: 실패하는 테스트를 먼저 작성
   - 테스트를 작성하고 실행하여 실패하는 것을 확인
   - 실패하는 테스트가 있어야 올바른 방향으로 개발하고 있음을 보장

2. **🟢 Green (초록)**: 테스트를 통과하는 최소한의 코드 작성
   - 테스트를 통과시키기 위해 필요한 최소한의 코드만 작성
   - 복잡한 최적화나 리팩토링은 아직 하지 않음

3. **🔵 Refactor (리팩토링)**: 코드 개선
   - 테스트가 통과하는 상태를 유지하면서 코드 품질 개선
   - 중복 제거, 가독성 향상, 성능 최적화 등

### 진행 단계

#### Step 1: Red - 테스트 작성
```bash
# 테스트 파일 작성 (test_prime_checker.py)
# 모든 테스트 케이스를 작성하고 실행하여 실패 확인
python -m pytest test_prime_checker.py -v
```

#### Step 2: Green - 최소 구현
```bash
# prime_checker.py 파일에 최소한의 구현 작성
# 모든 테스트가 통과할 때까지 반복
python -m pytest test_prime_checker.py -v
```

#### Step 3: Refactor - 코드 개선
```bash
# 테스트가 통과하는 상태를 유지하면서 코드 개선
# 리팩토링 후 테스트 재실행하여 회귀 테스트
python -m pytest test_prime_checker.py -v
```

## 프로젝트 구조

```
ARITHMETIC/
├── README.md
├── prime_checker.py          # 소수 확인 메인 로직
├── test_prime_checker.py     # 테스트 케이스
└── requirements.txt          # 프로젝트 의존성
```

## 환경 설정

### 요구사항
- **Python**: 3.7 이상
- **IDE**: PyCharm (권장)
- **운영 체제**: Windows 10
- **테스트 프레임워크**: pytest

### 설치 방법

1. **가상 환경 생성 (선택사항)**
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

2. **의존성 설치**
```bash
pip install -r requirements.txt
```

3. **pytest 설치 (requirements.txt에 없을 경우)**
```bash
pip install pytest
```

## 테스트 실행

### 전체 테스트 실행
```bash
python -m pytest test_prime_checker.py -v
```

### 특정 테스트 실행
```bash
python -m pytest test_prime_checker.py::test_negative_number -v
```

### 커버리지 확인
```bash
pip install pytest-cov
python -m pytest test_prime_checker.py --cov=prime_checker --cov-report=html
```

## 개발 가이드

### 함수 시그니처 예시
```python
def check_prime(number_str: str) -> str:
    """
    주어진 문자열이 소수인지 확인합니다.
    
    Args:
        number_str: 확인할 숫자 문자열
        
    Returns:
        "예": 소수인 경우
        "아니요": 소수가 아닌 경우
        "잘못됨: {에러 메시지}": 잘못된 입력인 경우
    """
    pass
```

### 테스트 작성 예시
```python
def test_negative_number():
    assert check_prime("-1") == "잘못됨: 음수"

def test_zero():
    assert check_prime("0") == "아니요"

def test_prime_number():
    assert check_prime("3") == "예"
```

## 성공/실패 기준

### 성공 기준
- ✅ 모든 테스트 케이스가 예상한 결과를 생성
- ✅ 코드가 오류 없이 컴파일/실행됨
- ✅ 모든 종속성이 올바르게 설치되고 구성됨

### 실패 기준
- ❌ 테스트 케이스가 예상한 결과를 생성하지 않음
- ❌ 컴파일 오류 또는 런타임 오류 발생

## 특별 절차

1. **테스트 결과 기록**: 모든 테스트 실행 결과를 기록하고 문서화
2. **테스트 사례 업데이트**: 테스트 결과에 따라 테스트 케이스 문서 업데이트
3. **실패 보고**: 모든 실패 사례를 개발팀에 즉시 전달하여 해결

## 참고사항

- 소수는 1과 자기 자신으로만 나누어떨어지는 1보다 큰 자연수입니다.
- 0과 1은 소수가 아닙니다.
- 입력 범위는 0 ~ 1000으로 제한됩니다.
- 모든 입력은 문자열로 처리되며, 숫자가 아닌 입력에 대한 검증이 필요합니다.

## 라이선스

이 프로젝트는 교육 목적으로 작성되었습니다.

