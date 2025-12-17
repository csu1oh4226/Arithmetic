# arithmetic_operations.py 실행 가이드

## 📁 파일 위치 정보

### 절대 경로 (Absolute Path)
```
C:\OEV\Cursor_pro\ARITHMETIC\src\arithmetic\arithmetic_operations.py
```

### 상대 경로 (프로젝트 루트 기준)
```
src/arithmetic/arithmetic_operations.py
```

### 현재 작업 디렉토리
```
C:\OEV\Cursor_pro\ARITHMETIC
```

---

## ⚠️ 중요 사항

`arithmetic_operations.py` 파일은 **클래스 정의 파일**이므로 직접 실행할 수 없습니다.  
이 파일은 다른 Python 스크립트에서 **import**하여 사용해야 합니다.

---

## 🚀 실행 방법

### 방법 1: Python 모듈로 import하여 사용 (권장)

#### 프로젝트 루트에서 실행
```bash
# 현재 위치 확인
cd C:\OEV\Cursor_pro\ARITHMETIC

# Python 인터프리터에서 import
python
>>> from src.arithmetic.arithmetic_operations import ArithmeticOperations
>>> calc = ArithmeticOperations()
>>> calc.add(5, 3)
8
```

#### 또는 한 줄로 실행
```bash
python -c "from src.arithmetic.arithmetic_operations import ArithmeticOperations; calc = ArithmeticOperations(); print(calc.add(5, 3))"
```

---

### 방법 2: main.py 실행 (가장 쉬운 방법)

프로젝트 루트에서:
```bash
python main.py
```

**경로**: `C:\OEV\Cursor_pro\ARITHMETIC\main.py`

---

### 방법 3: 테스트 실행

프로젝트 루트에서:
```bash
pytest tests/test_arithmetic_operations.py -v
```

**경로**: `C:\OEV\Cursor_pro\ARITHMETIC\tests\test_arithmetic_operations.py`

---

### 방법 4: 직접 실행 가능하도록 파일 수정 (선택사항)

만약 파일을 직접 실행하고 싶다면, 파일 끝에 다음 코드를 추가:

```python
if __name__ == "__main__":
    calc = ArithmeticOperations()
    print("사칙연산 시스템")
    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"10 - 4 = {calc.subtract(10, 4)}")
    print(f"6 * 7 = {calc.multiply(6, 7)}")
    print(f"15 // 3 = {calc.divide(15, 3)}")
    print(f"15 / 3 = {calc.divide_quotient(15, 3)}")
```

그 후 실행:
```bash
# 프로젝트 루트에서
python src/arithmetic/arithmetic_operations.py

# 또는 절대 경로로
python C:\OEV\Cursor_pro\ARITHMETIC\src\arithmetic\arithmetic_operations.py
```

---

## 📝 경로 요약

| 항목 | 경로 |
|------|------|
| **프로젝트 루트** | `C:\OEV\Cursor_pro\ARITHMETIC` |
| **arithmetic_operations.py** | `C:\OEV\Cursor_pro\ARITHMETIC\src\arithmetic\arithmetic_operations.py` |
| **main.py** | `C:\OEV\Cursor_pro\ARITHMETIC\main.py` |
| **테스트 파일** | `C:\OEV\Cursor_pro\ARITHMETIC\tests\test_arithmetic_operations.py` |

---

## ✅ 권장 실행 순서

1. **프로젝트 루트로 이동**
   ```bash
   cd C:\OEV\Cursor_pro\ARITHMETIC
   ```

2. **main.py 실행** (가장 간단)
   ```bash
   python main.py
   ```

3. **또는 테스트 실행**
   ```bash
   pytest tests/test_arithmetic_operations.py -v
   ```

---

## 🔍 현재 위치 확인 방법

```bash
# PowerShell에서
pwd

# Python에서
python -c "import os; print(os.getcwd())"
```

---

## 💡 팁

- **항상 프로젝트 루트(`C:\OEV\Cursor_pro\ARITHMETIC`)에서 실행**하는 것이 가장 안전합니다.
- 상대 경로를 사용할 때는 현재 작업 디렉토리를 확인하세요.
- `main.py`를 사용하면 경로 문제 없이 쉽게 실행할 수 있습니다.

