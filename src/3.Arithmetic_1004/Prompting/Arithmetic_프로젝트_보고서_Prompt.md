# Assignment structure for Git push
_Exported on 4/19/2026 at 16:17:36 GMT+9 from Cursor (3.1.15)_

---

**User**

다음 과제 내용을 구조적으로 정리해 주세요.

과제:
- Arithmetic Git Push하기
- Repository 이름: Arithmetic_XX (예: Arithmetic_01)
- Author, Reviewer 이름을 description에 포함
- main 브랜치에서 commit 후 push

정리 항목:
1. 수행 절차
2. 명명 규칙
3. 필수 제출 요소
4. 실수하기 쉬운 부분

---

**Cursor**

# Arithmetic 과제 요약

## 1. 수행 절차

1. **저장소 준비**  
   - GitHub(또는 과제에서 지정한 원격)에 `Arithmetic_XX` 형식의 새 저장소를 만든다.  
   - 로컬 프로젝트와 원격을 연결한다(`git remote add origin ...` 등).

2. **작업 브랜치**  
   - **`main` 브랜치**에서 작업한다.  
   - 다른 브랜치에서만 커밋한 뒤 `main`에 머지하지 않은 상태로 제출하면 요구사항과 어긋날 수 있다.

3. **커밋**  
   - 과제 범위에 맞게 코드/파일을 수정한 뒤 `main`에서 스테이징·커밋한다.

4. **설명(description) 반영**  
   - 저장소 **설명(description)** 필드(또는 과제에서 말하는 “description”이 README/PR이면 그에 맞춤)에 **Author**, **Reviewer** 이름을 넣는다.

5. **푸시**  
   - `main`의 커밋을 원격에 `git push`한다.  
   - 제출 링크·스크린샷 등 과제 안내에 맞게 제출한다.

---

## 2. 명명 규칙

| 대상 | 규칙 |
|--------|------|
| **저장소 이름** | `Arithmetic_XX` — `XX`는 지정 번호(예: `Arithmetic_01`). 과제에서 준 번호와 **정확히** 일치해야 함. |
| **브랜치** | 기본 작업·제출 기준은 **`main`**. |
| **설명(description)** | **Author**(작성자)·**Reviewer**(리뷰어) **이름**을 포함. 형식은 과제 예시가 있으면 그대로 따르고, 없으면 예: `Author: 홍길동, Reviewer: 김철수`처럼 한 줄에 명확히. |

---

## 3. 필수 제출 요소

- **`Arithmetic_XX` 이름의 원격 저장소**가 존재할 것.  
- **`main` 브랜치**에 반영된 **커밋**이 있을 것.  
- 해당 커밋이 **원격에 push**되어 있을 것.  
- 저장소 **description**(또는 지정된 위치)에 **Author·Reviewer 이름**이 포함될 것.  
- (과제지에 있다면) **저장소 URL**, **커밋 해시**, **스크린샷** 등 추가 제출물도 함께 충족.

---

## 4. 실수하기 쉬운 부분

- **`main`이 아닌 브랜치**에서만 커밋하고 push — 채점은 `main` 기준이면 불합격 처리될 수 있음.  
- **저장소 이름 오타** (`Arithmetic_1` vs `Arithmetic_01` 등) — 과제에 적힌 `XX` 자릿수·형식 그대로 사용.  
- **description 누락** — GitHub 저장소 상단 **About**의 Description에 넣는 경우가 많음; README만 수정하고 Description은 비워 두는 실수.  
- **첫 push 전 기본 브랜치 이름** — 로컬이 `master`인데 원격은 `main`만 있는 경우, 브랜치 이름·upstream 설정 혼동.  
- **원격 미연결·잘못된 URL** — `git remote -v`로 확인하지 않고 push 실패.  
- **Reviewer 미기재 또는 영문/한글 혼용으로 식별 어렵게** — 채점자가 **누가 Author/Reviewer인지** 한눈에 보이게 쓰기.

---

요약하면, **`Arithmetic_XX` 저장소 + `main`에서 커밋 후 push + description에 Author·Reviewer`** 세 가지를 동시에 만족시키는지 최종 점검하면 됩니다.

---

**User**

Arithmetic 프로젝트의 기본 폴더 구조를 설계해 주세요.

조건:
- 순수 콘솔 기반
- UI, DB 없음
- 사칙연산 기능 포함
- 단일 책임 원칙 고려
- 추후 확장 가능하도록 구조 설계

출력:
- 폴더 구조
- 각 파일 역할 설명
- 클래스 책임 정의

---

**Cursor**

# Arithmetic 프로젝트 기본 폴더 구조 설계

순수 콘솔·DB/UI 없음·사칙연산·SRP·확장(새 연산, 새 입력 형식, 검증 규칙 분리)을 전제로 한 구조입니다. 언어는 C#·Java·TypeScript 등 패키지 단위가 있는 경우를 기준으로 했고, Python이면 `src/arithmetic/` 패키지로 1:1 대응하면 됩니다.

---

## 폴더 구조

```
Arithmetic/
├── src/
│   ├── ConsoleHost/                 # 실행 진입점 (콘솔 I/O만)
│   │   └── Program.cs               # 또는 main.py, Program.java 등
│   │
│   ├── Application/                 # 애플리케이션 서비스 (유스케이스)
│   │   ├── CalculatorAppService.cs  # “입력 문자열 → 계산 결과” 흐름 조율
│   │   └── Ports/                   # (선택) 인터페이스만 두고 구현은 Domain
│   │       └── ICalculatorAppService.cs
│   │
│   ├── Domain/                      # 비즈니스 규칙의 핵심
│   │   ├── Operations/              # 연산 단위 (SRP: 연산 하나 = 클래스 하나)
│   │   │   ├── IArithmeticOperation.cs
│   │   │   ├── AdditionOperation.cs
│   │   │   ├── SubtractionOperation.cs
│   │   │   ├── MultiplicationOperation.cs
│   │   │   ├── DivisionOperation.cs
│   │   │   └── IOperationResolver.cs  # 기호/토큰 → 연산 인스턴스 (확장 시 여기만 수정)
│   │   ├── OperationResolver.cs     # 위 인터페이스 구현 (맵 또는 팩토리)
│   │   │
│   │   ├── Parsing/                   # “문자열 → 구조화된 표현”만 담당
│   │   │   ├── IExpressionParser.cs
│   │   │   └── SimpleBinaryExpressionParser.cs  # 예: 두 피연산자 + 한 연산자
│   │   │
│   │   ├── Evaluation/              # (선택) 파싱 결과 → 숫자 계산만
│   │   │   ├── IExpressionEvaluator.cs
│   │   │   └── BinaryExpressionEvaluator.cs
│   │   │
│   │   └── Models/                    # 값 객체 / 결과 타입
│   │       ├── ParsedExpression.cs    # 좌/우 피연산자, 연산자 종류 등
│   │       └── CalculationResult.cs   # 성공 값 또는 오류 코드/메시지
│   │
│   └── Shared/                        # (선택) 여러 레이어에서 쓰는 순수 유틸
│       └── NumberFormatter.cs         # 표시 형식만 담당 시
│
├── tests/                             # 단위 테스트 (Domain 우선)
│   ├── Domain.Tests/
│   │   ├── Operations/
│   │   ├── Parsing/
│   │   └── Evaluation/
│   └── Application.Tests/
│
└── Arithmetic.sln                     # 또는 pyproject.toml, pom.xml 등
```

**확장 시 예시**

- 괄호·다항식: `Domain/Parsing/`에 `AdvancedExpressionParser.cs` 추가, `IExpressionParser` 구현만 교체·조합.
- 로깅·설정 파일: `Infrastructure/` 추가 후 `Application`에서 주입.
- CLI 인자 모드: `ConsoleHost/`에 `CommandLineRunner.cs`만 추가하고 서비스는 재사용.

---

## 각 파일(또는 모듈) 역할

| 위치 | 역할 |
|------|------|
| **ConsoleHost/Program** | 프로세스 시작, DI(또는 수동 조립), 표준 입출력 읽기/쓰기, 종료 코드. **계산 규칙 없음.** |
| **Application/CalculatorAppService** | “한 줄 입력 받기 → 파싱 → 평가 → 결과 DTO 반환” 순서만 조율. 연산 구현·파싱 알고리즘은 직접 들고 있지 않음. |
| **Domain/Operations/** | 각 사칙연산의 **의미**(예: 나눗셈 0으로 나누기 금지). 외부 I/O 없음. |
| **Domain/OperationResolver** | `+`, `-`, `*`, `/` 등 **토큰 → `IArithmeticOperation`**. 새 연산 추가 시 이곳(또는 등록 테이블)만 확장. |
| **Domain/Parsing/** | 문자열 검증·토큰화·`ParsedExpression` 생성. **숫자가 아닌지, 형식 오류** 등은 여기서 정의 가능. |
| **Domain/Evaluation/** | 이미 파싱된 표현에 대해 **Resolver로 연산을 고르고 실행**. 파싱과 분리하면 “같은 AST, 다른 평가 전략” 확장이 쉬움. |
| **Domain/Models/** | 불변 값 객체, 성공/실패 구분. UI/콘솔에 의존하지 않음. |
| **tests/** | 연산·파서·평가·앱 서비스를 각각 단위 테스트. |

초기에는 **Evaluation을 AppService 안에 두어도** 되지만, 위처럼 나누 두면 SRP와 테스트가 분명해집니다.

---

## 클래스 책임 정의

| 클래스(인터페이스) | 단일 책임 |
|--------------------|-----------|
| **Program** | 콘솔 루프, 사용자 메시지 출력, 서비스 호출. |
| **ICalculatorAppService / CalculatorAppService** | 유스케이스 오케스트레이션(파서 → 평가기 호출, 예외를 `CalculationResult`로 매핑 등). |
| **IExpressionParser / SimpleBinaryExpressionParser** | 입력 문자열 → `ParsedExpression`. 연산 실행 안 함. |
| **IExpressionEvaluator / BinaryExpressionEvaluator** | `ParsedExpression` → 숫자 결과(또는 도메인 오류). |
| **IArithmeticOperation** | “두 숫자를 받아 결과를 내는” 계약만 정의. |
| **AdditionOperation … DivisionOperation** | 각 연산 **한 종류**만 구현. |
| **IOperationResolver / OperationResolver** | 연산자 기호에 맞는 구현체 선택. |
| **ParsedExpression** | 파싱 결과 데이터 보관(좌/우 값, 연산자 식별자). |
| **CalculationResult** | 성공 값 또는 실패 이유(0으로 나누기, 잘못된 형식 등). 콘솔은 이 객체를 문자열로만 표현. |

이렇게 두면 **콘솔은 입출력**, **앱 서비스는 흐름**, **파서는 문법**, **연산 클래스는 의미**, **리졸버는 매핑**으로 역할이 겹치지 않고, 이후 **모듈러·단위 변환·새 연산자**를 넣을 때도 수정 범위가 작습니다.

---

**User**

Arithmetic_1004폴더를 만들고, 
사칙연산 기능을 구현해 주세요.

조건:
- add, subtract, multiply, divide 함수 포함
- 0으로 나누기 예외 처리
- 입력/출력 명확
- 순수 로직 중심
- 단위 테스트 포함

출력:
1. 구현 코드
2. 테스트 코드
3. 예외 처리 설명

---

**Cursor**

워크스페이스 상태를 확인한 뒤 `Arithmetic_1004` 폴더에 구현과 테스트를 추가합니다.



워크스페이스가 비어 있습니다. Python으로 순수 로직 모듈·콘솔 진입점·단위 테스트를 추가합니다.



`c:\DEV\Arithmetic_1004` 아래에 패키지 `arithmetic`, 콘솔 `main.py`, `tests`를 두었습니다. 테스트 9개 모두 통과했습니다.

---

## 1. 구현 코드

**순수 로직** (`arithmetic/operations.py`):

```1:32:c:\DEV\Arithmetic_1004\arithmetic\operations.py
"""사칙연산 순수 함수. 입출력·콘솔 의존 없음."""


def add(a: float, b: float) -> float:
    """두 수의 합을 반환합니다."""
    return a + b


def subtract(a: float, b: float) -> float:
    """a에서 b를 뺀 값을 반환합니다."""
    return a - b


def multiply(a: float, b: float) -> float:
    """두 수의 곱을 반환합니다."""
    return a * b


def divide(a: float, b: float) -> float:
    """
    a를 b로 나눈 값을 반환합니다.

    b가 0이면 ZeroDivisionError를 발생시킵니다.
    (명시적 검사로 메시지를 통일합니다.)
    """
    if b == 0:
        raise ZeroDivisionError("0으로 나눌 수 없습니다.")
    return a / b
```

**입출력 분리** (`main.py` — 숫자/연산자 입력, 결과·오류 메시지 출력):

```1:48:c:\DEV\Arithmetic_1004\main.py
"""
콘솔 진입점: 입력/출력만 담당합니다. 계산은 arithmetic.operations를 사용합니다.
"""

from arithmetic import add, divide, multiply, subtract

_OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "x": multiply,
    "X": multiply,
    "/": divide,
}
# ... _prompt_float, _prompt_operator, main ...
```

패키지 진입: `arithmetic/__init__.py`에서 `add`, `subtract`, `multiply`, `divide`를 재노출합니다.

---

## 2. 테스트 코드

```1:48:c:\DEV\Arithmetic_1004\tests\test_operations.py
"""arithmetic.operations 단위 테스트."""

import unittest

from arithmetic.operations import add, divide, multiply, subtract


class TestAdd(unittest.TestCase):
    def test_integers(self) -> None:
        self.assertEqual(add(2, 3), 5)

    def test_floats(self) -> None:
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=7)
# ... TestSubtract, TestMultiply, TestDivide ...
```

실행:

```bash
cd c:/DEV/Arithmetic_1004
python -m unittest discover -s tests -v
```

---

## 3. 예외 처리 설명

| 구분 | 처리 |
|------|------|
| **0으로 나누기** | `divide`에서 `b == 0`이면 `ZeroDivisionError("0으로 나눌 수 없습니다.")`를 **명시적으로** 발생시킵니다. 언어 기본 `/`만 쓰지 않고 조건을 두어, 메시지와 실패 조건을 한곳에서 관리합니다. |
| **콘솔에서의 후속 처리** | `main()`은 `divide` 호출을 `try/except ZeroDivisionError`로 감싸 사용자에게 `연산 오류: ...`로 출력하고 종료합니다. |
| **잘못된 숫자 입력** | `_prompt_float`에서 `float()` 변환 실패 시 `ValueError`를 잡아 `입력 오류`로 안내합니다(로직 모듈과 분리). |

요약하면, **도메인 규칙(0 나눗셈 금지)**은 `operations.divide`에서 예외로 표현하고, **사용자에게 보여 줄 문구**는 콘솔 레이어에서 한 번 더 정리하는 형태입니다.

---

콘솔 실행: `python main.py` 후 안내에 따라 두 수와 연산자를 입력하면 됩니다.

---

**User**

Report 폴더를 만들고 지금 작업한 내용에 대한 보고서를 작성해줘.

---

**Cursor**

프로젝트 파일을 확인한 뒤 `Report` 폴더에 보고서를 작성합니다.



작업을 반영해 **`Report`** 폴더를 만들고 아래 파일에 보고서를 두었습니다.

- **`Report/Arithmetic_프로젝트_보고서.md`**

포함 내용은 다음과 같습니다.

1. **개요** — 목적, Python·콘솔·사칙연산 범위  
2. **디렉터리 구조** — `arithmetic/`, `main.py`, `tests/`, `Report/`  
3. **구현 요약** — `operations.py`, `main.py`, `__init__.py` 역할  
4. **예외 처리** — 0으로 나누기, 잘못된 숫자, 미지원 연산자 표  
5. **단위 테스트** — 검증 범위, `unittest` 실행·`main.py` 실행 명령  
6. **설계 관점** — 책임 분리, 테스트 용이성, 확장 방법  
7. **결론** — 요구사항 충족 요약  

필요하면 같은 폴더에 **Author / Reviewer** 줄이나 과제용 표지 정보를 넣을 수 있으니 원하시는 형식을 알려주시면 됩니다.

