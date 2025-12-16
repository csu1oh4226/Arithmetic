# 인사관리 앱 시스템 구축 - 정산 시스템 (Arithmetic Operations)

## 프로젝트 개요

이 프로젝트는 정산 시스템의 공통 모듈로, 사칙연산(덧셈, 뺄셈, 곱셈, 나눗셈)의 정확도를 검증하는 애플리케이션입니다. 다양한 경계 조건과 예외 상황을 처리하여 견고한 산술 연산 기능을 제공합니다.

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

1. **🔴 Red (빨강)**: 실패하는 테스트를 먼저 작성
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

## 프로젝트 구조

```
ARITHMETIC/
├── README.md
├── src/
│   └── main/
│       └── java/
│           └── com/
│               └── arithmetic/
│                   └── ArithmeticOperations.java    # 사칙연산 메인 로직
├── src/
│   └── test/
│       └── java/
│           └── com/
│               └── arithmetic/
│                   └── ArithmeticOperationsTest.java # 테스트 케이스
├── build.gradle (또는 pom.xml)
└── .gitignore
```

## 환경 설정

### 요구사항
- **Java**: JDK 17 이상
- **IDE**: IntelliJ IDEA 2023.2 (권장)
- **운영 체제**: Windows 10
- **빌드 도구**: Gradle 또는 Maven
- **테스트 프레임워크**: JUnit 5

### 설치 방법

1. **JDK 17 설치 확인**
```bash
java -version
```

2. **프로젝트 클론 (이미 있는 경우)**
```bash
git clone https://github.com/csu1oh4226/Arithmetic.git
cd ARITHMETIC
```

3. **의존성 설치 (Gradle 사용 시)**
```bash
./gradlew build
```

4. **의존성 설치 (Maven 사용 시)**
```bash
mvn clean install
```

## 테스트 실행

### 전체 테스트 실행 (Gradle)
```bash
./gradlew test
```

### 전체 테스트 실행 (Maven)
```bash
mvn test
```

### 특정 테스트 실행
```bash
# Gradle
./gradlew test --tests "ArithmeticOperationsTest.testAdditionPositiveNumbers"

# Maven
mvn test -Dtest=ArithmeticOperationsTest#testAdditionPositiveNumbers
```

### 커버리지 확인
```bash
# Gradle (JaCoCo 플러그인 필요)
./gradlew test jacocoTestReport

# Maven (JaCoCo 플러그인 필요)
mvn test jacoco:report
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
- 0으로 나누기는 `ArithmeticException`을 발생시켜야 합니다.
- 음수 연산도 올바르게 처리되어야 합니다.

## 라이선스

이 프로젝트는 교육 목적으로 작성되었습니다.
