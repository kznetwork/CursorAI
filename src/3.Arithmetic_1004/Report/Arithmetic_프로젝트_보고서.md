# Arithmetic_1004 프로젝트 작업 보고서

## 1. 개요

본 문서는 `Arithmetic_1004` 작업 공간에서 수행한 **순수 콘솔 기반 사칙연산** 구현 내용을 정리합니다. 데이터베이스·웹 UI 없이 Python으로 핵심 연산 로직과 콘솔 입출력을 분리하고, 단위 테스트로 동작을 검증했습니다.

| 항목 | 내용 |
|------|------|
| 언어·런타임 | Python 3 |
| 주요 기능 | 덧셈, 뺄셈, 곱셈, 나눗셈(`add`, `subtract`, `multiply`, `divide`) |
| 특이 사항 | 나눗셈 시 0으로 나누기에 대한 명시적 예외 처리 |

---

## 2. 디렉터리 구조

```
Arithmetic_1004/
├── arithmetic/           # 연산 순수 로직 패키지
│   ├── __init__.py       # 공개 API 재노출
│   └── operations.py     # 사칙연산 함수 정의
├── main.py               # 콘솔 진입점(입력·출력)
├── tests/
│   └── test_operations.py
└── Report/
    └── Arithmetic_프로젝트_보고서.md   # 본 보고서
```

---

## 3. 구현 요약

### 3.1 순수 로직 (`arithmetic/operations.py`)

- `add(a, b)`, `subtract(a, b)`, `multiply(a, b)`, `divide(a, b)` 네 함수로 사칙연산을 제공합니다.
- 모든 함수는 `float` 타입 힌트를 사용하며, 콘솔·파일 등 외부 I/O에 의존하지 않습니다.
- `divide`는 제수(second operand)가 `0`인 경우 `ZeroDivisionError`를 **명시적 조건 검사** 후 발생시켜, 오류 메시지를 일관되게 유지합니다.

### 3.2 콘솔 계층 (`main.py`)

- 사용자에게 두 실수와 연산자(`+`, `-`, `*`, `/`, 곱셈은 `x`/`X` 별칭 허용)를 입력받습니다.
- 연산자 문자열을 내부 `_OPERATIONS` 맵에서 해당 함수로 매핑한 뒤 `arithmetic` 모듈의 함수를 호출합니다.
- 숫자 변환 실패는 `ValueError`로 처리하고, 0으로 나누기는 `ZeroDivisionError`로 처리하여 **입력 오류**와 **연산 오류**를 구분해 출력합니다.

### 3.3 패키지 진입 (`arithmetic/__init__.py`)

- 외부에서는 `from arithmetic import add, ...` 형태로 네 함수를 import할 수 있도록 `__all__`을 지정했습니다.

---

## 4. 예외 처리 설명

| 상황 | 처리 위치 | 동작 |
|------|-----------|------|
| 0으로 나누기 | `divide` | `b == 0`이면 `ZeroDivisionError("0으로 나눌 수 없습니다.")` 발생 |
| 0으로 나누기(사용자 메시지) | `main` | 위 예외를 포착하여 `연산 오류: ...` 형태로 출력 후 종료 |
| 숫자가 아닌 입력 | `main` | `float()` 변환 중 `ValueError` 포착 → `입력 오류: 숫자 형식이 아닙니다.` 출력 |
| 지원하지 않는 연산자 | `main` | `_OPERATIONS`에 없는 문자열이면 안내 메시지 출력 |

도메인 규칙(0 나눗셈 금지)은 **연산 모듈**에서 예외로 표현하고, **사용자에게 보여 줄 문구**는 콘솔 레이어에서 정리하는 구조입니다.

---

## 5. 단위 테스트

### 5.1 범위 (`tests/test_operations.py`)

- `unittest` 기반으로 `operations` 모듈만 직접 검증합니다(콘솔 미포함).
- `TestAdd`: 정수 합, 부동소수점 `assertAlmostEqual`.
- `TestSubtract`: 양수/음수 결과.
- `TestMultiply`: 일반 곱, 0 곱하기.
- `TestDivide`: 일반 나눗셈, **0으로 나누기 시 예외 및 메시지 부분 문자열**, 음수 제수.

### 5.2 실행 방법

프로젝트 루트(`Arithmetic_1004`)에서:

```bash
python -m unittest discover -s tests -v
```

콘솔 애플리케이션 실행:

```bash
python main.py
```

---

## 6. 설계 관점 요약

- **단일 책임**: 연산·검증은 `operations`, 사용자 대화는 `main`에 한정했습니다.
- **테스트 용이성**: 순수 함수 위주로 두어 별도 목(mock) 없이 단위 테스트가 가능합니다.
- **확장**: 새 연산(예: 나머지)은 `operations`에 함수 추가 후 `main`의 `_OPERATIONS`에 등록하는 방식으로 확장할 수 있습니다.

---

## 7. 결론

`Arithmetic_1004`에는 사칙연산 순수 함수, 콘솔 입출력 분리, 0으로 나누기 예외 처리, 그리고 `unittest` 기반 단위 테스트가 포함되어 있으며, 위 구조로 요구 기능을 충족하고 유지보수·확장에 대비했습니다.

---

*작성 기준: 저장소 내 소스 코드 및 테스트 파일 내용*
