#

## D1_1.실습- 실무 프롬프트 고치기 & 개선하기
### 나쁜 프롬프트 개선하기 

```

당신은 보안 중심 백엔드 개발자입니다.

다음 요구사항에 따라 로그인 기능을 설계하십시오.

------------------------------------------------------------
P (Purpose) — 목적
------------------------------------------------------------

사용자가 이메일과 비밀번호를 사용하여 인증할 수 있는 로그인 기능을 설계한다.
보안성과 명확한 입력/출력 계약을 갖춘 구조를 목표로 한다.

------------------------------------------------------------
C (Context) — 맥락
------------------------------------------------------------

- REST API 기반 서버 환경
- JWT 기반 인증
- 비밀번호는 해시 저장됨
- UI 구현은 제외
- DB 실제 구현은 제외 (인터페이스만 정의)

------------------------------------------------------------
T (Task) — 작업
------------------------------------------------------------

다음을 구조화하여 작성하시오:

1. 입력 계약 정의
2. 출력 계약 정의
3. 인증 처리 흐름 정의
4. 실패 시 정책 정의
5. 보안 요구사항 정의
6. 테스트 전략 정의

------------------------------------------------------------
F (Format) — 출력 형식
------------------------------------------------------------

Markdown 구조로 작성하시오.

다음 항목을 반드시 포함하시오:

- 입력 스키마
- 출력 스키마
- 에러 코드 정의
- 인증 절차 단계
- 예외 처리 정책
- 보안 체크리스트
- 테스트 케이스 목록

구현 코드는 작성하지 마시오.

```
### 7-Step Framework 작성 

```

당신은 소프트웨어 설계 전문가입니다.

이커머스 장바구니 시스템을 7-Step Framework로 구조화하십시오.

⚠️ 조건:
- UI 구현은 포함하지 않는다.
- DB 설계는 포함하지 않는다.
- 순수 도메인 로직 중심으로 작성한다.
- 입력과 출력은 명확히 정의한다.
- 모호한 표현을 사용하지 않는다.
- 구조화된 Markdown으로 작성한다.

------------------------------------------------------------
STEP 1 — 문제 인식
------------------------------------------------------------

현재 이커머스 장바구니 시스템이 해결해야 할 핵심 문제를 정의하시오.

- 장바구니의 본질적 목적은 무엇인가?
- 사용자가 기대하는 기능은 무엇인가?
- 반드시 유지되어야 하는 핵심 조건은 무엇인가?

------------------------------------------------------------
STEP 2 — 핵심 개념 정의
------------------------------------------------------------

장바구니 도메인의 핵심 개념을 정의하시오.

- Cart
- CartItem
- Product
- Quantity

각 개념의 역할을 명확히 설명하시오.

------------------------------------------------------------
STEP 3 — 불변 조건 (Invariant)
------------------------------------------------------------

다음과 같은 불변 조건을 정의하시오.

- 수량은 1 이상이어야 한다.
- 동일 상품은 중복 항목으로 존재하지 않는다.
- 총 금액은 모든 항목의 합과 일치해야 한다.

------------------------------------------------------------
STEP 4 — 주요 유스케이스 정의
------------------------------------------------------------

다음 유스케이스를 구조화하시오.

- 상품 추가
- 상품 제거
- 수량 변경
- 총 금액 계산

각 유스케이스에 대해:
- 입력
- 처리 규칙
- 출력
- 실패 조건

------------------------------------------------------------
STEP 5 — 입력/출력 계약 정의
------------------------------------------------------------

각 주요 기능에 대한 명확한 입력/출력 계약을 작성하시오.

예:
입력:
{
  productId: string,
  quantity: number
}

출력:
{
  success: boolean,
  cartTotal: number,
  error: string | null
}

------------------------------------------------------------
STEP 6 — 테스트 전략
------------------------------------------------------------

TDD 관점에서 테스트 전략을 작성하시오.

- 정상 케이스
- 경계값 테스트
- 예외 상황 테스트
- 불변 조건 검증 테스트

------------------------------------------------------------
STEP 7 — 확장 가능성 및 리스크 분석
------------------------------------------------------------

다음을 분석하시오.

- 할인 정책 추가 시 구조 영향
- 쿠폰 시스템 확장 가능성
- 동시성 문제 가능성
- 계산 오류 리스크

------------------------------------------------------------

출력은 반드시 7단계 구조를 유지하여 작성하시오.
구현 코드는 작성하지 마시오.

```

### Few-Shot 예시 작성 
```

당신은 소프트웨어 엔지니어입니다.

당신의 임무는 순수 로직 기반의 데이터 유효성 검증 함수를 생성하는 것입니다.

모든 함수는 다음 조건을 따라야 합니다:
- 입력과 출력이 명확해야 한다.
- 구조화된 결과를 반환해야 한다.
- 정상 케이스와 실패 케이스를 모두 처리해야 한다.
- UI, DB, 네트워크 로직을 포함하지 않는다.
- 오류 메시지를 명확히 반환해야 한다.

--------------------------------------------
예시 1
--------------------------------------------

요청:
이메일 주소를 검증하는 함수를 생성하시오.

입력:
- email: 문자열

규칙:
- "@" 문자가 정확히 하나 포함되어야 한다.
- "@" 뒤에 최소 하나 이상의 "."이 포함되어야 한다.
- 공백을 포함하면 안 된다.

출력 형식:
{
  "isValid": boolean,
  "error": string | null
}

--------------------------------------------
예시 2
--------------------------------------------

요청:
비밀번호를 검증하는 함수를 생성하시오.

입력:
- password: 문자열

규칙:
- 최소 길이 8자 이상
- 최소 하나 이상의 대문자 포함
- 최소 하나 이상의 숫자 포함
- 최소 하나 이상의 특수문자 포함

출력 형식:
{
  "isValid": boolean,
  "error": string | null
}

--------------------------------------------
예시 3
--------------------------------------------

요청:
나이(age) 값을 검증하는 함수를 생성하시오.

입력:
- age: 정수

규칙:
- 0 이상 120 이하
- 음수 불가
- 정수형이어야 함

출력 형식:
{
  "isValid": boolean,
  "error": string | null
}

--------------------------------------------
이제 다음 요청을 완성하시오:
--------------------------------------------

요청:
전화번호를 검증하는 함수를 생성하시오.

입력:
- phoneNumber: 문자열

규칙:
- 숫자만 포함해야 한다.
- 길이는 10자 이상 11자 이하
- 문자 또는 특수문자를 포함하면 안 된다.

출력 형식:
{
  "isValid": boolean,
  "error": string | null
}

```

## D1_2.실습- Git 기본 + Cursor 연동
### 1. 과제 이해 단계
```

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

```

### 2. 프로젝트 구조 생성 단계
```

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

```

### 3. Arithmetic 구현 단계
```

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

### 4. Git 초기화 및 브랜치 설정

```
Arithmetic 프로젝트를 Git으로 관리하려고 합니다.

다음을 단계별로 안내해 주세요:

1. Git 초기화
2. main 브랜치 생성 확인
3. 첫 커밋 수행
4. 커밋 메시지 작성 예시

OS는 Windows입니다.
```

### 5. Commit 메시지 작성 가이드

```
Arithmetic 프로젝트의 첫 커밋 메시지를 작성해 주세요.

조건:
- Conventional Commit 형식
- 변경 내용 명확
- 한 줄 요약 + 상세 설명
- 예시 3개 제공
```
### 6. GitHub Repository 생성 및 연결

```
GitHub에 Arithmetic_1004이라는 Repository를 생성했습니다.

로컬 프로젝트를 다음 조건으로 연결하고 push하는 명령어를 알려주세요.

- main 브랜치 사용
- Author: 홍길동
- Reviewer: 박철수
- description에 Author/Reviewer 포함

명령어만 단계별로 작성해 주세요.
```
일반적인 방법을 알려줌.
1. 프로젝트 폴더로 이동
cd C:\DEV\Arithmetic_1004
2. 원격 저장소 연결 (이미 origin이 있으면 생략하거나 URL만 수정)
git remote add origin https://github.com/kzfornetwork/Arithmetic_1004.git
3. 브랜치 이름을 main으로 맞춤
git branch -M main
4. 커밋이 없으면 (이미 첫 커밋이 있으면 5~6 생략)
git add .
git commit -m "chore: initial commit"
5. 원격 main에 맞춰 푸시
git push -u origin main
6. GitHub 저장소 description에 Author / Reviewer 넣기 (GitHub CLI 사용 시)
gh repo edit <USER>/Arithmetic_1004 --description "Author: 홍길동 | Reviewer: 박철수"
gh가 없으면 웹에서 저장소 About → Description에 동일 문구를 수동 입력합니다. (Git 자체 명령으로는 description을 바꿀 수 없습니다.)
```
수정된 절차
```
cd /c/DEV/Arithmetic_1004
git init
git branch -M main
git add .
git commit -m "chore: initial commit"
git remote add origin https://github.com/kzfornetwork/Arithmetic_1004.git
git push -u origin main
```

```
@https://github.com/kzfornetwork/Arithmetic_1004.git에 프로젝트 전체를 올려주세요.
```

### 7. 최종 검증 단계

```
다음 체크리스트를 검증해 주세요:

- Repository 이름이 Arithmetic_1004 형식인가?
- main 브랜치에서 작업했는가?
- 커밋 메시지가 적절한가?
- Author, Reviewer 정보가 포함되었는가?
- 원격 저장소에 push 완료되었는가?

검증 체크리스트 형태로 작성해 주세요.

````


## PRD 실습: Magic Square 프로젝트
### D1_3.실습- The Mom Test + 문제 10개 찾기
```

당신은 문제 정의 전문가입니다.

나는 4x4 Magic Square 프로그램을 만들려고 합니다.

⚠️ 하지만 바로 설계하거나 구현하지 마십시오.
먼저 문제 인식 단계부터 진행하십시오.

--------------------------------------------
STEP 1 — Observation (관찰)
--------------------------------------------

다음 질문에 답하십시오:

1. 현재 우리가 해결하려는 상황은 무엇인가?
2. 왜 4x4 마방진 문제를 다루는가?
3. 이 문제는 어떤 학습 또는 시스템 설계 맥락에서 등장하는가?

“마방진을 만든다”는 표현 대신,
상황을 관찰 관점으로 서술하십시오.

--------------------------------------------
STEP 2 — Why #1
--------------------------------------------

Q: 왜 마방진을 완성해야 하는가?

A를 가정하여 답하고,
그 답에서 드러나는 불편함 또는 구조적 문제를 분석하십시오.

--------------------------------------------
STEP 3 — Why #2
--------------------------------------------

Q: 왜 단순 계산이 아니라 프로그램으로 구현하는가?

다음 관점에서 답하십시오:
- 반복 가능성
- 검증 자동화
- 오류 방지
- 규칙 기반 사고 훈련

--------------------------------------------
STEP 4 — Why #3 (핵심 발견)
--------------------------------------------

Q: 왜 이 문제를 TDD 방식으로 설계하려 하는가?

- 무엇이 통제되어야 하는가?
- 어떤 불변 조건이 존재하는가?
- 왜 입력/출력이 명확해야 하는가?

--------------------------------------------
STEP 5 — 진짜 문제 정의
--------------------------------------------

다음을 작성하십시오:

1. 표면 문제 정의 (잘못된 정의)
2. 개선된 문제 정의 (정확한 정의)
3. 이 문제의 핵심 Invariant
4. 우리가 실제로 훈련하려는 사고 능력

--------------------------------------------

⚠️ 구현 설계는 하지 마십시오.
⚠️ 코드 언급 금지.
⚠️ 알고리즘 설명 금지.
⚠️ 구조화된 Markdown으로 작성하십시오.

```


### D1_4: 간단한 앱 설계 (3계층: Boundary-Control-Entity)
```

당신은 Dual-Track UI + Logic TDD 및 Clean Architecture 설계 전문가입니다.

프로젝트: Magic Square (4x4) — TDD 연습용
목적: 알고리즘 난이도보다 “레이어 분리 + 계약 기반 테스트 + 리팩토링” 훈련
제약:
- 구현 코드는 작성하지 마십시오. (설계/계약/테스트/통합 계획만)
- UI는 실제 화면이 아니라 “입력/출력 경계(Boundary)”로 정의
- Data Layer는 DB가 아니라 “저장/로드 인터페이스(메모리/파일 교체 가능)” 수준만
- 입력/출력은 명확히 고정

입력 계약:
- 4x4 int[][] (0은 빈칸)
- 빈칸은 정확히 2개
- 값 범위: 0 또는 1~16
- 0 제외 중복 금지
출력 계약:
- int[6]
- 좌표는 1-index
- 반환 형식: [r1,c1,n1,r2,c2,n2]
- n1,n2는 두 누락 숫자이며, (작은수→첫빈칸, 큰수→둘째빈칸) 조합이 마방진이면 그 순서로, 아니면 반대로

------------------------------------------------------------
출력 형식 (반드시 이 구조로)
------------------------------------------------------------

# 1) Logic Layer (Domain Layer) 설계
## 1.1 도메인 개념
- Entities / Value Objects / Domain Services 목록과 책임(SRP)
## 1.2 도메인 불변조건(Invariants)
- 행/열/대각선 합 일치, Magic Constant 등
## 1.3 핵심 유스케이스(도메인 관점)
- 빈칸 찾기, 누락 숫자 찾기, 마방진 판정, 두 조합 시도
## 1.4 Domain API(내부 계약)
- 메서드 시그니처 수준(코드 X) + 입력/출력/실패조건
## 1.5 Domain 단위 테스트 설계(RED 우선)
- 테스트 케이스 목록(정상/비정상/엣지)
- 각 테스트가 보호하는 invariant 명시

# 2) Screen Layer (UI Layer) 설계 (Boundary Layer)
## 2.1 사용자/호출자 관점 시나리오
- “행렬 입력 → 검증 → 결과 출력” 흐름
## 2.2 UI 계약(외부 계약)
- Input schema / Output schema / Error schema
## 2.3 UI 레벨 테스트(Contract-first, RED 우선)
- 잘못된 크기, 빈칸 개수 오류, 값 범위 오류, 중복 오류, 반환 포맷 검증
- Domain은 Mock으로 가정
## 2.4 UX/출력 규칙
- 에러 메시지 표준(정확한 문구 규칙까지)

# 3) Data Layer 설계 (Data Layer)
## 3.1 목적 정의
- “저장/로드”의 필요성과 범위(학습용)
## 3.2 인터페이스 계약
- 예: MatrixRepository.save/load (메서드 수준, 코드 X)
- 저장 대상: 입력 행렬, 실행 결과(선택)
## 3.3 구현 옵션 비교(메모리/파일)
- 옵션 A: InMemory / 옵션 B: File(JSON/CSV)
- 추천안 1개 선택 + 이유
## 3.4 Data 레이어 테스트
- 저장/로드 정합성, 예외(파일 없음/형식 오류), 불변조건(4x4 유지)

# 4) Integration & Verification (통합 및 검증)
## 4.1 통합 경로 정의
- UI → Application(선택) → Domain → Data 흐름(의존성 방향 포함)
## 4.2 통합 테스트 시나리오
- 정상 시나리오 2개 이상
- 실패 시나리오 3개 이상(입력 오류, 도메인 실패, 데이터 실패)
## 4.3 회귀 보호 규칙
- 기존 테스트 유지 정책
- 변경 금지 규칙(계약/출력 포맷)
## 4.4 커버리지 목표
- Domain Logic 95%+
- UI Boundary 85%+
- Data 80%+
## 4.5 Traceability Matrix (필수)
- Concept(Invariant) → Rule → Use Case → Contract → Test → Component

------------------------------------------------------------
추가 조건
------------------------------------------------------------
- 모호한 표현 금지(“적절히/충분히” 금지)
- 모든 규칙은 검증 가능해야 함(테스트로 확인 가능)
- 구현 코드 작성 금지
- 표/체크리스트를 적극 사용

```

### D1_5. .cursorrules 작성
#### 섹션별로 나눠서 작성하는 방법

1단계 — 뼈대 생성
```
MagicSquare 프로젝트의 .cursorrules YAML 파일 뼈대를 만들어줘.
아래 최상위 키만 포함하고 값은 비워둬:
project, code_style, architecture, tdd_rules, testing, forbidden, file_structure, ai_behavior
각 키 앞에 80자짜리 # 구분선 주석을 추가해.
YAML 내용만 출력해.
```
2단계 — 섹션별로 채우기
```
위 .cursorrules 파일의 tdd_rules 섹션을 채워줘.
  - red_phase: 테스트 먼저 작성, 실패 확인 후 다음 단계 진행 조건
  - green_phase: 최소 코드로만 테스트 통과, 이 단계에서 리팩터링 금지
  - refactor_phase: 기능 변경 없이 구조 개선, 커버리지 유지 조건
YAML 형식 유지. tdd_rules 블록만 출력해.
```
3단계 — 검토 요청
```
방금 완성한 .cursorrules 파일을 검토해줘.
아래 항목을 확인해:
1. YAML 문법 오류
2. 누락된 필수 섹션
3. tdd_rules와 forbidden 규칙 간의 충돌
4. Cursor AI가 실제로 따를 수 없는 ai_behavior 규칙
문제점만 보고해줘. 수정은 내가 요청할 때만 해.
```
4단계 — 이어서 작성하기
```
위에서 만든 .cursorrules 뼈대의 빈 섹션을 모두 채워줘.
MagicSquare 프로젝트 기준으로 작성해.

각 섹션 작성 규칙:

code_style:
  - python_version: "3.10+"
  - style_guide: PEP8 엄격 준수
  - type_hints: 모든 함수 파라미터와 반환값에 필수
  - docstring: Google 스타일, 모든 public 메서드에 필수
  - max_line_length: 88 (Black 기준)

architecture:
  ECB 패턴 3 레이어를 각각 정의해줘:
  - boundary: 외부 입출력 담당 (UI, API, CLI)
  - control: 비즈니스 로직 담당
  - entity: 도메인 데이터 및 규칙 담당
  레이어 간 의존성 방향도 명시해줘.

tdd_rules:
  지금은 문자열 1줄인데, 하위 항목으로 세분화해줘.
  각 phase마다:
    - description: 단계 설명
    - rules: 지켜야 할 규칙 목록
    - must_not: 이 단계에서 하면 안 되는 것

testing:
  - framework: pytest
  - pattern: AAA (Arrange-Act-Assert)
  - coverage_minimum: 80%
  - fixture_scope: 규칙 정의
  - naming_convention: test_ 접두사 필수

forbidden:
  항목마다 아래 구조로 작성:
    pattern: 금지 패턴
    reason: 금지 이유
    alternative: 대신 써야 할 것
  최소 포함 항목: print(), 하드코딩 상수, except 단독 사용

file_structure:
  ECB 기준 폴더 구조를 트리 형태 주석으로 작성해줘.
  boundary/, control/, entity/, tests/ 포함.

ai_behavior:
  Cursor AI가 코드 생성 전·중·후에 반드시 따라야 할 규칙.
  최소 포함:
    - 코드 작성 전 관련 테스트 파일 확인
    - ECB 레이어 경계 위반 금지
    - 타입힌트 없는 함수 생성 금지
    - tdd_rules 위반 시 경고 출력

완성된 .cursorrules 전체 파일을 출력해줘.
```

####
```
src/.cursor/rules/.cursorrules 파일을 생성해줘.

파일 내용만 출력해. 설명, 마크다운 코드블록 불필요.

--- 프로젝트 정보 ---
프로젝트명: MagicSquare
설명: [한 줄로 프로젝트 설명 작성]
방법론: Dual-Track UI + Logic TDD with MLOps

--- 반드시 포함할 섹션 ---

1. project          → 프로젝트명, 설명, 방법론
2. code_style       → PEP8 엄격 준수, 타입힌트 필수(Python 3.10+), Google 스타일 docstring
3. architecture     → ECB 패턴 (boundary / control / entity 레이어별 역할 정의)
4. tdd_rules        → red_phase / green_phase / refactor_phase 각 단계별 규칙
5. testing          → pytest AAA 패턴(Arrange-Act-Assert), fixture 규칙, 커버리지 기준
6. forbidden        → print() 디버깅 금지, 그 외 금지 패턴 목록
7. file_structure   → 레이어별 폴더 구조 예시
8. ai_behavior      → 코드 생성 시 Cursor AI가 반드시 따라야 할 행동 규칙

--- 형식 규칙 ---
- YAML 형식, 들여쓰기 2 스페이스
- 각 섹션 앞에 80자 # 구분선 + 섹션 제목 주석
- 키는 영어, 설명은 한국어로 작성
- tdd_rules 하위에 red_phase / green_phase / refactor_phase 동일 깊이로 작성
- forbidden 항목마다 reason(이유)과 alternative(대안)을 함께 명시
```

```
너는 Cursor.AI용 프로젝트 규칙 파일(.cursorrules)을 설계하는 시니어 소프트웨어 아키텍트다.

내 목표는 MagicSquare 프로젝트에 맞는 .cursorrules 파일을 만드는 것이다.
반드시 Cursor가 바로 해석하고 따를 수 있도록, 구조적이고 명확한 규칙 문서로 작성하라.

다음 조건을 반영하라.

[프로젝트 정보]
- project: MagicSquare
- style: PEP8 + 타입힌트
- testing: pytest, AAA 패턴
- architecture: ECB (boundary / control / entity)
- forbidden: print() 디버깅 금지
- methodology: Dual-Track UI + Logic TDD
- language: Python

[내가 원하는 결과]
1. 최종 출력은 .cursorrules 파일 내용만 제공한다.
2. 설명문 없이 바로 복붙 가능한 규칙 문서 형태로 작성한다.
3. 섹션은 계층형 YAML 스타일 또는 Cursor Rules에 적합한 구조적 텍스트로 작성한다.
4. 다음 항목을 반드시 포함한다:
   - project
   - core_principles
   - coding_style
   - architecture_rules
   - testing_rules
   - tdd_rules
   - ui_logic_dual_track_rules
   - forbidden_rules
   - refactoring_rules
   - file_organization
   - review_checklist
5. ECB 아키텍처를 기준으로 boundary, control, entity의 책임을 분리해서 명시한다.
6. pytest 테스트는 반드시 AAA(Arrange-Act-Assert) 패턴을 따르도록 규칙화한다.
7. print() 디버깅 금지, 대신 logging 또는 테스트로 검증하도록 규칙화한다.
8. 타입힌트는 모든 공개 함수/메서드에 필수로 강제한다.
9. PEP8 준수, 함수 길이/클래스 책임/네이밍 규칙도 포함한다.
10. TDD는 RED → GREEN → REFACTOR 순서를 강제하고, 각 단계에서 Cursor가 어떻게 행동해야 하는지 써라.
11. Dual-Track UI + Logic TDD 관점에서 UI 테스트와 로직 테스트를 분리하도록 규칙화하라.
12. MagicSquare 프로젝트에 맞게 “도메인 로직 우선, 입출력/표현 분리” 원칙을 강조하라.

[출력 형식 요구]
- 마크다운 코드블록 없이 순수 텍스트로만 출력
- 들여쓰기와 섹션 구분이 명확해야 함
- 실제 .cursorrules 파일처럼 보여야 함

이제 위 조건을 만족하는 완성형 .cursorrules를 작성하라.
```

```
project:
  name: MagicSquare_1004
  description: 4x4 매직스퀘어 문제를 해결하는 Python 프로젝트
  language: Python
  methodology: Dual-Track UI + Logic TDD

code_style:
  - PEP8 코딩 스타일을 준수한다.
  - 모든 공개 함수와 메서드에 타입 힌트를 반드시 작성한다.
  - 함수는 작고 순수한 형태로 작성하는 것을 우선한다.
  - 변수, 함수, 클래스 이름은 의미가 명확하도록 작성한다.

architecture:
  pattern: ECB
  boundary:
    - 입력과 출력(UI, API 등)만 담당한다.
    - 도메인 계산 로직을 포함하지 않는다.
  control:
    - 유스케이스 흐름을 제어하고 조합한다.
    - entity 로직과 boundary를 호출한다.
  entity:
    - 순수 비즈니스 규칙과 계산 로직만 포함한다.
    - UI나 외부 의존성 없이 테스트 가능해야 한다.

tdd_rules:
  red_phase:
    - 반드시 실패하는 테스트를 먼저 작성한다.
    - 테스트 실패를 확인하기 전에는 구현 코드를 작성하지 않는다.
  green_phase:
    - 테스트를 통과하기 위한 최소한의 코드만 작성한다.
    - 이 단계에서는 리팩토링을 수행하지 않는다.
  refactor_phase:
    - 동작 변경 없이 구조를 개선한다.
    - 모든 테스트가 통과 상태를 유지해야 한다.

testing:
  framework: pytest
  style: AAA
  rules:
    - Arrange, Act, Assert 구조를 명확하게 작성한다.
    - 정상 케이스, 경계값, 실패 케이스를 모두 테스트한다.
    - UI 테스트보다 entity(도메인 로직) 테스트를 우선한다.

forbidden:
  - print()를 이용한 디버깅을 금지한다.
  - UI 로직과 도메인 로직을 혼합하지 않는다.
  - 테스트를 우회하여 코드가 완성된 것처럼 보이게 하지 않는다.
  - 숨겨진 전역 상태(가변 상태)를 사용하지 않는다.

file_structure:
  - boundary 코드는 src/boundary에 위치한다.
  - control 코드는 src/control에 위치한다.
  - entity 코드는 src/entity에 위치한다.
  - 테스트 코드는 src 구조를 그대로 반영하여 구성한다.

ai_behavior:
  - 구현 전에 반드시 도메인 로직 테스트를 먼저 작성한다.
  - 코드 생성 시 해당 코드가 ECB의 어떤 계층인지 설명한다.
  - 코드 수정 시 아키텍처 경계를 유지한다.
  - 테스트가 통과된 이후에만 리팩토링을 제안한다.
  
```
더 잘 나오게 하는 보강 프롬프트

위 프롬프트에 이어서 아래를 붙이면 결과가 더 단단해집니다.
```
추가 요구사항:
- MagicSquare의 핵심 도메인을 반영하라:
  - 4x4 magic square
  - 입력 검증
  - 누락값 계산
  - 합 34 검증
  - 사용자 입력 UI와 순수 계산 로직 분리
- boundary는 UI/입력/출력만 담당
- control은 유스케이스 조합과 흐름 제어만 담당
- entity는 순수 규칙/검증/계산 책임만 담당
- 테스트는 entity → control → boundary 순으로 우선순위를 둔다
- UI 구현 전 순수 로직 테스트를 먼저 작성하도록 강제한다
- mock 남용 금지, 순수 함수 우선 설계를 명시하라
- 숨은 상태보다 명시적 데이터 전달을 선호하도록 규칙화하라
```

완성 후 동작 확인하는 방법
파일이 채워지면 바로 아래 프롬프트로 테스트하세요.
```
.cursorrules를 읽고
MagicSquare의 User 엔티티 클래스를 ECB 패턴으로 작성해줘.
타입힌트, Google docstring, pytest 테스트 파일도 함께 만들어줘.
```
생성된 코드에 타입힌트가 있고, 파일이 entity/ 폴더에 위치하며, 테스트 파일이 AAA 패턴으로 작성되면 .cursorrules가 정상 동작하는 것입니다.


### D1_6: 사용자 여정 작성 (Epic → User Story → Task)

Level 1: Epic (비즈니스 목표): EPIC — Business Goal
```
Magic Square를 위한 사용자 여정 작성 (Epic → User Story → Task)을 하고자 합니다.
먼저, Level 1: Epic (비즈니스 목표): EPIC — Business Goal에 대한 내용을 다음처럼 작성해 주세요.
Epic: “Invariant(불변조건) 기반 사고 훈련 시스템 구축”
목적
4x4 Magic Square 문제를 활용하여:
Invariant 중심 설계 사고 훈련
Dual-Track TDD 적용 훈련
입력/출력 계약 명확화 훈련
설계 → 테스트 → 구현 → 리팩토링 흐름 체화

성공 기준
Domain Logic 95% 이상 테스트 커버리지
입력 검증 100% 계약 테스트 통과
하드코딩 없음
매직 넘버 없음
Invariant → Test 추적 가능
```

Level 2: User Journey (사용자 여정) 例1

```
Level 2: User Journey (사용자 여정)를 다음 내용처럼 작성해 주세요.
Persona
소프트웨어 개발 학습자
TDD 훈련 중
Clean Architecture 이해 중

Journey
Step 1 — 문제 인식
“마방진을 구현한다”가 아니라

Step 2 — 계약 정의
입력 스키마 정의
출력 스키마 정의
예외 정책 정의


Step 3 — Domain 분리
BlankFinder
MissingNumberFinder
MagicSquareValidator
Solver

Step 4 — Dual-Track 진행
UI RED / Logic RED 병렬
GREEN 최소 구현
REFACTOR 통합 정리

Step 5 — 회귀 보호
엣지 케이스 추가
입력 오류 케이스 추가
조합 실패 케이스 추가

```

Level 2: User Journey (사용자 여정) 例2

# User Journey — Magic Square (4x4)

## Persona
- TDD 연습 중인 개발자
- 알고리즘이 아닌 설계 연습이 목적

## Goal
- 마방진을 정확하게 완성하고
- 로직이 invariant를 만족하는지 검증하고 싶다

---

## Stage 1: Awareness
- Action: 문제를 확인한다
- Thinking: "빈칸 2개를 채우는 문제네"
- Emotion: 가벼운 도전감
- Pain: 문제 정의가 모호할 수 있음
- Opportunity: 입력/출력 계약 명확화

---

## Stage 2: Entry
- Action: 입력 구조를 파악한다 (4x4, 0=blank)
- Thinking: "좌표와 값 반환 형식부터 정해야겠다"
- Emotion: 집중 상태
- Pain: 조건 누락 위험
- Opportunity: Contract-first 설계

---

## Stage 3: Action
- Action:
  - 빈칸 좌표 찾기
  - 누락 숫자 찾기
  - 조합 시도
- Thinking:
  - "작은 수 먼저 넣어볼까?"
- Emotion: 탐색 / 시행착오
- Pain:
  - 조합 로직 혼란
- Opportunity:
  - SRP 기반 메서드 분리

---

## Stage 4: Validation
- Action:
  - 행/열/대각선 합 검증
- Thinking:
  - "34가 맞나?"
- Emotion:
  - 긴장 → 확신
- Pain:
  - 검증 로직 중복 가능
- Opportunity:
  - Invariant 기반 설계

---

## Stage 5: Outcome
- Action:
  - 결과 반환
- Thinking:
  - "이제 테스트 통과했나?"
- Emotion:
  - 만족감
- Pain:
  - 결과 포맷 오류 가능
- Opportunity:
  - Output schema 고정

```
Level 3: User Stories

```
Level 3: User Stories를 다음 내용처럼 작성해 주세요.
Story 1 — 입력 검증
As a 학습자
I want to 입력이 정확히 4x4인지 검증되길 원한다
So that 잘못된 데이터가 Domain으로 전달되지 않도록 한다

Acceptance Criteria:
4x4가 아니면 예외
빈칸 2개 아니면 예외
중복 숫자 예외
범위 위반 예외

Story 2 — 빈칸 탐색
As a 학습자
I want to 0의 좌표를 정확히 찾고 싶다
So that 조합 시도가 가능하다

Acceptance Criteria:
row-major 순서 유지
정확히 2개 반환

Story 3 — 누락 숫자 탐색
Acceptance Criteria:
1~16 중 누락 2개
오름차순 반환

Story 4 — 마방진 판정
Acceptance Criteria:
모든 행 합 동일
모든 열 합 동일
대각선 동일

Story 5 — 두 조합 시도
Acceptance Criteria:
small→first blank 시도
실패 시 reverse
정답 배열 길이 6


```
Level 4:구현 시나리오 - Technical
```
Level 4:구현 시나리오 - Technical를 다음 내용처럼 작성해 주세요.
Feature: 4x4 마방진 완성

  불변조건 기반 로직을 검증하기 위해
  TDD를 연습하는 개발자로서
  부분적으로 채워진 4x4 마방진을 완성하고 싶다

  Background:
    Given 4x4 행렬이 주어지고
    And 0은 빈칸을 의미하며
    And 정확히 2개의 셀이 0을 포함하고 있고
    And 숫자는 1부터 16 사이여야 하며
    And 0을 제외한 중복 숫자는 허용되지 않으며
    And 4x4의 마방진 상수는 34이다

  
  Scenario: 작은 수 → 큰 수 순서로 마방진이 완성되는 경우
    Given 다음과 같은 행렬이 주어졌을 때:
      | 16 |  2 |  3 | 13 |
      |  5 | 11 | 10 |  8 |
      |  9 |  7 |  0 | 12 |
      |  4 | 14 | 15 |  0 |
    When 시스템이 빈칸 좌표를 찾고
    And 누락된 두 숫자를 찾은 뒤
    And 작은 숫자를 첫 번째 빈칸에 배치하고
    And 큰 숫자를 두 번째 빈칸에 배치하면
    Then 모든 행의 합은 34여야 하고
    And 모든 열의 합은 34여야 하며
    And 두 대각선의 합도 34여야 하고
    And 결과는 길이 6의 배열로 반환되어야 하며
    And 반환되는 좌표는 1-index 기준이어야 한다

  
  Scenario: 역순 배치 시 마방진이 완성되는 경우
    Given 다음과 같은 행렬이 주어졌을 때:
      | 16 |  2 |  3 | 13 |
      |  5 | 11 | 10 |  8 |
      |  9 |  7 |  0 | 12 |
      |  4 | 14 | 15 |  0 |
    When 작은 숫자를 첫 번째 빈칸에 배치했을 때 마방진이 되지 않고
    And 큰 숫자를 첫 번째 빈칸에 배치했을 때 마방진이 되면
    Then 시스템은 역순 배치 결과를 반환해야 하며
    And 최종 행렬은 마방진 상수 34를 만족해야 한다

  Scenario: 빈칸 개수가 올바르지 않은 경우
    Given 행렬에 빈칸이 1개만 존재할 때
    When 유효성 검증을 수행하면
    Then 오류가 발생해야 한다

  Scenario: 중복 숫자가 존재하는 경우
    Given 0을 제외한 중복 숫자가 포함된 행렬일 때
    When 유효성 검증을 수행하면
    Then 오류가 발생해야 한다

  Scenario: 값의 범위를 벗어난 경우
    Given 행렬에 16을 초과하는 숫자가 포함되어 있을 때
    When 유효성 검증을 수행하면
    Then 오류가 발생해야 한다
```
Level 5: 시나리오 검증 및 정리

```
Level 5: 시나리오 검증 및 정리를 다음 내용처럼 작성해 주세요.

시나리오 완성도 체크리스트
## ✅ 4레벨 일관성 확인

Epic → Journey
- [x] Epic의 성공 지표가 Journey에 반영됨
- [x] Journey의 모든 단계가 Epic 목표 달성에 기여
- [x] Pain Points가 명확히 정의됨

Journey → Story
- [x] Journey의 각 Stage마다 최소 1개 Story
- [x] Story가체적인 기능으로 변환됨
- [x] Acceptance Criteria가 측정 가능

Story → Technical
- [x] 모든 AC가 Gherkin 시나리오로 변환
- [x] Given-When-Then이 명확
- [x] 테스트 자동화 가능

## ✅ Edge Case 커버리지

정상 케이스
- [x] Happy Path 시나리오 존재

예외 케이스
- [x] 네트워크 오류
- [x] 권한 없음
- [x] 잘못된 입력
- [x] 중복 실행

경계 케이스
- [x] 최솟값, 최댓값
- [x] 빈 값
- [x] 특수 문자

## ✅ 사용자 중심성

실제 사용자 검증
- [ ] 현장 엔지니어 1명과 시나리오 리뷰
- [ ] 관리자 1명과 Journey 검증
- [ ] 피드백 반영

감정 흐름
- [x] 각 Journey Stage마다 감정 표시
- [x] 부정 → 긍정 전환 명확

## ✅ 구현 가능성

기술 검증
- [x] QR 스캔 라이브러리 조사 완료
- [x] 오프라인 DB 방식 결정
- [x] 자동 검증 알고리즘 설계

데이터 요구사항
- [x] 필요한 Entity 모두 정의됨 (Mission 2)
- [x] API 스펙 초안 작성



```


### D1_7: 최종 PRD 작성 (Gherkin 포함)
#### 例1

```
당신은 시니어 제품/소프트웨어 아키텍트이며 Dual-Track UI + Logic TDD 및 Concept-to-Code Traceability 전문가입니다. 
PRD 본문 골격은 Report/4를 축으로 하고, Report/1로 문제·동기를 보강하며, 기능·계약·성공 정의는 Report/2, 품질·개발 원칙은 Report/3(및 cursor 규칙) 에서 가져오는 방식으로 다음 내용을 고려해 docs 폴더에 PRD를 작성해 주세요.


프로젝트: Magic Square (4x4) — TDD 연습용
목적:
- 알고리즘 난이도보다 TDD 훈련이 목적
- Invariant 기반 설계/검증 사고를 체득
- 입력/출력 계약을 명확히 고정
- UI/DB/Web 의존성 없이 순수 로직 중심으로 구현 가능하게 PRD 작성

⚠️ 중요 규칙
- 구현 코드를 작성하지 마십시오.
- 새로운 기능을 추가하지 마십시오. (요구사항 범위 유지)
- 모호한 표현(“적절히”, “충분히” 등)을 사용하지 마십시오.
- 모든 요구사항은 테스트/검증 가능해야 합니다.
- Dual-Track(경계/도메인) 분리를 문서 구조에 반영하십시오.
- Concept → Rule → Use Case → Contract → Test → Component 추적성을 반드시 포함하십시오.
- 출력은 구조화된 Markdown으로 작성하십시오.

------------------------------------------------------------
[입력/출력 계약(고정)]
------------------------------------------------------------

입력(Input):
- 4x4 정수 행렬 int[][]
- 0은 빈칸
- 빈칸(0)은 정확히 2개
- 값 범위: 0 또는 1~16
- 0을 제외한 중복 숫자 금지
- 첫 번째 빈칸 정의: row-major(행 우선) 스캔 시 먼저 발견되는 0

출력(Output):
- int[6]
- 좌표는 1-index
- 포맷: [r1, c1, n1, r2, c2, n2]
- n1,n2는 누락 숫자 2개
- 시도 1: 작은 수 → 첫 빈칸, 큰 수 → 둘째 빈칸
  - 마방진이면 그 순서 반환
- 시도 2: (시도 1 실패 시) 큰 수 → 첫 빈칸, 작은 수 → 둘째 빈칸
  - 마방진이면 역순 반환
- 두 시도 모두 실패 시 오류 정책에 따라 처리(명시 필수)

마방진 상수(Magic Constant):
- n=4 → 34

------------------------------------------------------------
[PRD 작성 지시]
------------------------------------------------------------

아래 구조를 반드시 지켜 PRD를 작성하십시오.

# 1. Executive Summary
- 한 문단 요약
- 프로젝트가 훈련하려는 핵심 역량(불변조건/계약/TDD)

# 2. Problem Statement (문제 정의)
- “마방진을 만든다”가 아니라 “불변조건을 검증 가능한 형태로 완성한다” 관점으로 정의
- 왜 입력/출력 계약이 핵심인지 설명

# 3. Target Users
- TDD 학습자/리뷰어 관점
- 사용 목적/사용 환경(콘솔/테스트 실행)

# 4. Scope
## 4.1 In-Scope
- 빈칸 좌표 찾기
- 누락 숫자 찾기
- 마방진 판정
- 두 조합 시도 후 결과 반환
- 입력 검증(경계 레이어)
## 4.2 Out-of-Scope
- UI 화면 개발
- DB 저장/조회
- N×N 일반화(기본 PRD 범위 제외, 확장 항목으로만)
- 마방진 “생성” 알고리즘(완전 생성 문제)

# 5. Functional Requirements (기능 요구사항)
각 기능마다 아래 템플릿을 반복해서 작성하십시오:
- Feature ID
- 설명(1~2문장)
- 입력
- 처리 규칙(불변조건 포함)
- 출력
- 승인 기준(AC) — 반드시 테스트 가능 문장으로
- 관련 오류/예외 정책

필수 기능 목록:
- FR-01 입력 검증 (Boundary)
- FR-02 빈칸 탐색
- FR-03 누락 숫자 탐색
- FR-04 마방진 판정
- FR-05 해 찾기(solution): 두 조합 시도 및 반환

# 6. Business Rules (도메인 규칙)
- BR-01 ~ 형태로 나열
- “항상 참이어야 하는 규칙”으로 서술
- 예: 중복 금지, 합 규칙, 좌표 인덱스 규칙, row-major 규칙 등

# 7. Non-Functional Requirements
- 테스트 커버리지 목표:
  - Domain Logic 95%+
  - Boundary Validation 85%+
- 결정론적 실행(동일 입력 → 동일 출력)
- 부작용 금지(입력 행렬 변경 정책 명시)
- 성능 기준(선택): 4x4 기준 즉시 처리(예: 50ms 내)

# 8. Dual-Track TDD Strategy
## 8.1 Track A — Boundary(UI) TDD
- Contract-first 테스트 항목 목록
- 실패 정책(예외 타입/메시지 표준)
## 8.2 Track B — Domain(Logic) TDD
- 메서드 단위 테스트 목록
- 불변조건 테스트 목록
## 8.3 병렬 진행 규칙
- UI RED & Logic RED → UI GREEN & Logic GREEN → REFACTOR
- “도메인 먼저 다 구현 후 경계 추가” 금지

# 9. Test Plan (QA)
- 시나리오 기반 테스트 목록(정상/역순 성공/실패/입력오류)
- 회귀 테스트 정책
- 테스트 데이터(대표 4x4 예시 행렬) 포함
- Property/Invariant 기반 체크 항목

# 10. Architecture Overview (High-Level)
- 레이어 정의:
  - Boundary Layer(입력검증/출력형식)
  - Domain Layer(순수 로직)
- 책임 분리(SRP)와 확장(OCP) 전략
- 의존성 방향(도메인이 경계를 모르게)

# 11. Risks & Ambiguities
- 모호한 부분을 “결정 항목”으로 명시(예: 두 시도 모두 실패 시 정책)
- 자주 실수하는 포인트(1-index, row-major, 입력 변경 여부 등)

# 12. Traceability Matrix (필수)
다음 형식으로 표를 제공하십시오:
Concept/Invariant → Business Rule → Feature(FR) → Acceptance Criteria → Test Case → Component

------------------------------------------------------------
출력 요구사항
------------------------------------------------------------
- 전체를 Markdown으로 출력
- 번호/ID 체계 일관성 유지
- 구현 코드 작성 금지
- 모든 요구사항은 검증 가능 문장으로
```

例2

```
프로젝트: Magic Square (4x4) — TDD 연습용
목적: 알고리즘 난이도보다 “레이어 분리 + 계약 기반 테스트 + 리팩토링” 훈련
제약:
- 구현 코드는 작성하지 마십시오. (설계/계약/테스트/통합 계획만)
- UI는 실제 화면이 아니라 “입력/출력 경계(Boundary)”로 정의
- Data Layer는 DB가 아니라 “저장/로드 인터페이스(메모리/파일 교체 가능)” 수준만
- 입력/출력은 명확히 고정

입력 계약:
- 4x4 int[][] (0은 빈칸)
- 빈칸은 정확히 2개
- 값 범위: 0 또는 1~16
- 0 제외 중복 금지
출력 계약:
- int[6]
- 좌표는 1-index
- 반환 형식: [r1,c1,n1,r2,c2,n2]
- n1,n2는 두 누락 숫자이며, (작은수→첫빈칸, 큰수→둘째빈칸) 조합이 마방진이면 그 순서로, 아니면 반대로

------------------------------------------------------------
출력 형식 (반드시 이 구조로)
------------------------------------------------------------

# 1) Logic Layer (Domain Layer) 설계
## 1.1 도메인 개념
- Entities / Value Objects / Domain Services 목록과 책임(SRP)
## 1.2 도메인 불변조건(Invariants)
- 행/열/대각선 합 일치, Magic Constant 등
## 1.3 핵심 유스케이스(도메인 관점)
- 빈칸 찾기, 누락 숫자 찾기, 마방진 판정, 두 조합 시도
## 1.4 Domain API(내부 계약)
- 메서드 시그니처 수준(코드 X) + 입력/출력/실패조건
## 1.5 Domain 단위 테스트 설계(RED 우선)
- 테스트 케이스 목록(정상/비정상/엣지)
- 각 테스트가 보호하는 invariant 명시

# 2) Screen Layer (UI Layer) 설계 (Boundary Layer)
## 2.1 사용자/호출자 관점 시나리오
- “행렬 입력 → 검증 → 결과 출력” 흐름
## 2.2 UI 계약(외부 계약)
- Input schema / Output schema / Error schema
## 2.3 UI 레벨 테스트(Contract-first, RED 우선)
- 잘못된 크기, 빈칸 개수 오류, 값 범위 오류, 중복 오류, 반환 포맷 검증
- Domain은 Mock으로 가정
## 2.4 UX/출력 규칙
- 에러 메시지 표준(정확한 문구 규칙까지)

# 3) Data Layer 설계 (Data Layer)
## 3.1 목적 정의
- “저장/로드”의 필요성과 범위(학습용)
## 3.2 인터페이스 계약
- 예: MatrixRepository.save/load (메서드 수준, 코드 X)
- 저장 대상: 입력 행렬, 실행 결과(선택)
## 3.3 구현 옵션 비교(메모리/파일)
- 옵션 A: InMemory / 옵션 B: File(JSON/CSV)
- 추천안 1개 선택 + 이유
## 3.4 Data 레이어 테스트
- 저장/로드 정합성, 예외(파일 없음/형식 오류), 불변조건(4x4 유지)

# 4) Integration & Verification (통합 및 검증)
## 4.1 통합 경로 정의
- UI → Application(선택) → Domain → Data 흐름(의존성 방향 포함)
## 4.2 통합 테스트 시나리오
- 정상 시나리오 2개 이상
- 실패 시나리오 3개 이상(입력 오류, 도메인 실패, 데이터 실패)
## 4.3 회귀 보호 규칙
- 기존 테스트 유지 정책
- 변경 금지 규칙(계약/출력 포맷)
## 4.4 커버리지 목표
- Domain Logic 95%+
- UI Boundary 85%+
- Data 80%+
## 4.5 Traceability Matrix (필수)
- Concept(Invariant) → Rule → Use Case → Contract → Test → Component

------------------------------------------------------------
추가 조건
------------------------------------------------------------
- 모호한 표현 금지(“적절히/충분히” 금지)
- 모든 규칙은 검증 가능해야 함(테스트로 확인 가능)
- 구현 코드 작성 금지
- 표/체크리스트를 적극 사용
```


## D2_1.실습- Cursor AI To-Do 리스트 생성 요청 
### Ｔｏ－Ｄｏ　리스트 작성 방법
```
Ｔｏ－Ｄｏ　리스트를 작성하고 싶습니다. 작성한 문서 중 무엇을 참조해서 만들어야 할까요?
```
### Ｔｏ－Ｄｏ　리스트를 작성
```
당신은 시니어 소프트웨어 아키텍트이자 TDD 코치입니다. 할 일 목록의 항목과 완료 조건은 docs/5.PRD_MagicSquare_4x4_TDD.md를 주 소스로 두고, 스토리 단위 분해는 Report/4, 계약·오류 세부는 Report/2, 품질·TDD·ECB 준수는 Report/3와 Cursor 규칙을 참조해, 

다음 방법론을 적용하여
"Magic Square 4x4 완성 시스템"의 구현용 To-Do 구조를 작성하세요.

적용 방법론:
- Concept-to-Code Traceability
- Dual-Track UI + Logic TDD
- To-Do → Scenario → Test → Code 구조
- ECB(Entity / Control / Boundary) 모델
- RED → GREEN → REFACTOR

반드시 한국어로 작성하세요.

[시스템 목표]
부분적으로 비어 있는 4x4 Magic Square를 완성하는 시스템의 개발 To-Do를 작성합니다.

[도메인 규칙]
- 보드는 4x4이다.
- 숫자는 1~16만 사용한다.
- 0은 빈칸이다.
- 정확히 2칸이 비어 있다.
- 0을 제외한 중복 숫자는 허용되지 않는다.
- 모든 행, 열, 대각선의 합은 34여야 한다.
- 해결 가능한 경우 빈칸 값을 찾아 채운다.
- 유효하지 않은 보드는 거부한다.

[출력 형식]
다음 구조를 반드시 지켜서 작성하세요.

1. Epic
2. User Story
3. Phase별 Task 목록
4. 각 Task에는 반드시 아래 정보를 포함하세요.
   - Task ID
   - RED / GREEN / REFACTOR 여부
   - 작업 제목
   - Scenario Level (L0/L1/L2/L3)
   - 연결되는 Test 이름
   - 연결되는 Code 대상
   - ECB 스테레오타입 (Entity / Control / Boundary)
   - 필요 시 체크포인트

[표현 스타일]
- Markdown 사용
- 체크박스 형식 사용
- 실제 Cursor.AI 실습용 개발 보드처럼 작성
- 식별자는 Epic-001, US-001, TASK-001 형식 사용
- 유효한 케이스와 실패 케이스를 모두 포함
- 최소한 다음 작업을 포함
  - 보드 생성
  - 보드 유효성 검사
  - 빈칸 탐지
  - 후보값 필터링
  - 완성 로직
  - 잘못된 입력 처리
  - 테스트 커버리지 체크포인트

[Scenario Level 정의]
- L0: 기능 개요
- L1: 정상 흐름
- L2: 경계 상황
- L3: 실패 상황

[추가 제약]
- Logic 책임은 명확히 분리할 것
- UI/Boundary에는 비즈니스 규칙을 넣지 말 것
- Control은 검증과 해결 흐름을 조율할 것
- Entity는 보드 상태를 표현할 것
- 모든 To-Do는 Scenario, Test, Code로 추적 가능해야 함

이제
"Magic Square 4x4 완성 시스템"의 To-Do 구조를 생성하세요.

```

READMD.md 파일 작성
```
Ｔｏ－Ｄｏ　리스트를  포함해 READMD.md 파일을 만들고 싶습니다. 무슨 문서를 참조하면 좋을까요?
```

```
 @c:\DEV\MagicSquare _1004\ 에 있는 README 본문·To-Do·검증 기준은 docs/5.PRD_MagicSquare_4x4_TDD.md를 중심에 두고, 스토리 표현은 Report/4, 오류·계약 요약은 Report/2, 실행·ECB·TDD는 Report/3 + pyproject.toml + Cursor 규칙, 문서 관계 한 줄은 Report/5를 참조해서 To-Do 리스트를 포함한 MagicSquare를 만들기 위한 README.md 파일을 만들어줘.
```
```
Report 폴더에 작업한 내용을 보고서로 내보내줘.
```
@https://github.com/kznetwork/MagicSquare_1004.git에 @c:\DEV\MagicSquare _1004\ 프로젝트를 업로드해줘
```

## D2_4.실습- Dual-Track UI + Logic TDD
```
@c:\DEV\MagicSquare _1004\ 프로젝트를 구현하기 위한 깃 브랜치 전략을 알려줘.개발방법론은 Dual-Track TDD 이고, 다음의 순서로 진행할 거야.

- Dual-Track UI + Logic TDD
- GREEN 단계 (테스트 통과)
- Dual-Track Refactoring 
```

### 추천 브랜치 전략

main  ←── (릴리스 태그/머지, GREEN 확인)
  ↑
develop  ←── feature/dual-track-tdd
         ←── stabilize/green
         ←── refactor/refactor


```
develop 브랜치를 만들어줘.

@c:\DEV\MagicSquare _1004\ 모든 작업 내용을 깃헙에 업로드해줘.

### RED 단계 전용 (Magic Square) 답

```
feature/dual-track-tdd 브랜치를 생성해줘.

```
지금까지 작업한 내용을 Report 폴더에 리포트로 내보내줘.

```
### 
$ git branch
  develop
* feature/dual-track-tdd
  main

를 확인하고, 구현 작업을 시작합니다.

```
당신은 Dual-Track UI + Logic TDD 전문가입니다.

우리는 이미 Magic Square(4x4) 시나리오를 작성했습니다.
지금 단계는 구현이 아니라,
시나리오를 “실패하는 테스트(RED)”로 변환하는 것입니다.

중요
- 구현 코드를 작성하지 마십시오.
- GREEN 단계로 가지 마십시오.
- REFACTOR 단계로 가지 마십시오.
- 오직 RED 테스트만 작성하십시오.
- 모든 테스트는 현재 구현이 없기 때문에 실패해야 합니다.

------------------------------------------------------------
프로젝트 조건
------------------------------------------------------------

입력:
- 4x4 int[][]
- 0은 빈칸
- 정확히 2개의 0
- 값 범위 1~16
- 중복 금지 (0 제외)

출력:
- int[6]
- 좌표는 1-index
- [r1, c1, n1, r2, c2, n2]

마방진 상수:
- 4x4 → 34

------------------------------------------------------------
Dual-Track RED 단계 구조
------------------------------------------------------------

UI RED        Logic RED
   ↓              ↓
(둘 다 실패 상태)

------------------------------------------------------------
TRACK A — UI / Boundary RED
------------------------------------------------------------

다음을 실패 테스트로 변환하십시오:

1. 4x4가 아닌 입력은 예외 발생
2. 빈칸이 2개가 아니면 예외 발생
3. 값 범위 위반 시 예외 발생
4. 중복 숫자 존재 시 예외 발생
5. 반환 배열 길이는 6이어야 한다
6. 반환 좌표는 1-index여야 한다

각 테스트에 대해:
- 테스트 이름
- Given (입력)
- When (호출)
- Then (기대)
- 이 테스트가 보호하는 계약 설명

------------------------------------------------------------
TRACK B — Logic RED
------------------------------------------------------------

다음을 실패 테스트로 작성하십시오:

1. find_blank_coords()
   - row-major 순서로 정확히 2개 반환

2. find_not_exist_nums()
   - 누락 숫자 2개 반환
   - 오름차순

3. is_magic_square()
   - 모든 행 합 동일
   - 모든 열 합 동일
   - 두 대각선 합 동일
   - 34와 일치

4. solution()
   - small → first blank 시도
   - 실패 시 reverse 시도
   - 6-length 반환
   - 1-index 좌표

각 테스트는:
- 실패 상태임을 명확히 설명
- 어떤 Invariant를 검증하는지 명시

------------------------------------------------------------
출력 형식
------------------------------------------------------------

# UI RED Tests
- Test ID
- Scenario
- Invariant 보호 내용

# Logic RED Tests
- Test ID
- Scenario
- Invariant 보호 내용

------------------------------------------------------------

구현 금지
GREEN 단계 금지
REFACTOR 금지
오직 RED 테스트 설계만 수행하십시오
```
지금 작업한 내용을 추가해 @Report/9.Git_Feature_Dual_Track_TDD_Branch_Report.md 을 업데이트해줘.

```
레포 테스트 프레임워크 이름(JUnit 5, pytest 등)에 맞춰 파일/클래스 이름만 적은 테스트 스켈레톤(메서드 빈 본문, fail 또는 assertTrue(false) 한 줄)도 같은 RED 원칙으로만 적어봅니다.
```
### 테스트 해 보기
1. 한 번만: 가상환경·설치
프로젝트 루트(MagicSquare _1004)에서:

python -m venv .venv
source .venv/Scripts/activate   # PowerShell이면: .venv\Scripts\Activate.ps1
pip install -U pip
pip install -e ".[dev]"
2. 테스트 실행
전체:

cd "c:/DEV/MagicSquare _1004"
pytest

3. 커버리지
dev 옵션에는 pytest만 있고 pytest-cov는 없음이므로 커버리지 쓸 때만 추가합니다.

pip install pytest-cov
pytest --cov=magicsquare --cov-report=term-missing
pytest --cov=magicsquare --cov-report=html

생성된 htmlcov/index.html을 브라우저로 열면 됩니다.

```
깃 헙에 업로드해줘.

```

## D2_5.실습- GREEN 단계 (테스트 통과)
### GREEN TDD Cycle – 전체 개요


stabilize/green 브랜치에서 Magic Square(4x4) 커밋 단위로 Dual-Track GREEN(Logic GREEN + UI GREEN)을 진행하도록 Cursor.AI에 지시하는 프롬프트를 작성하시오.
① 첫 RED 테스트 선택 → ② 최소 구현 → ③ 테스트 실행 → ④ 통과)과 병렬 Dual-Track

1. RED 테스트 하나 선택
   ↓
2. 최소 구현 작성
   ↓
3. 테스트 실행 → 통과 확인
   ↓
4. 커밋
   ↓
5. 다음 RED 테스트로 (1번으로)


```

당신은 Dual-Track UI(Boundary/Screen) + Logic(Domain) TDD 실무 전문가입니다.
프로젝트: Magic Square 4x4 (TDD 연습용)
이번 작업은 “하나의 커밋” 단위로 진행합니다.

============================================================
중요 규칙 (반드시 준수)
============================================================
- 순서를 반드시 지키십시오: RED 선택 → GREEN 최소 구현 → 테스트 실행 → 통과 확인 → 커밋 요약
- 한 번에 많은 테스트/기능을 추가하지 마십시오. (1개 RED 테스트 묶음만)
- REFACTOR는 이번 커밋에서 하지 마십시오. (GREEN까지만)
- 하드코딩 금지 / 매직 넘버 금지
- MATRIX_SIZE 상수 사용 (Domain·Boundary·GUI에서 격자 차원은 동일 상수 또는 단일 모듈 re-export로 일치)
- Domain(magicsquare/domain.py)은 UI/DB/Web/PyQt **의존 금지**
- GUI는 PyQt 기반 **Screen 레이어**로만 구현하며, 비즈니스 규칙은 Domain에, 입출력·유효성·위임은 Boundary(magicsquare/boundary.py)에 둔다.
- Dual-Track 병렬로 진행:
  UI GREEN = Boundary 계약 + (필요 시) Screen에서의 검증 호출·에러 표시
  Logic GREEN = Domain 규칙

============================================================
고정 계약 (변경 금지)
============================================================
입력:
- 4x4 int[][]
- 0은 빈칸
- 0은 정확히 2개
- 값 범위: 0 또는 1~16
- 0 제외 중복 금지
- 첫 번째 빈칸: row-major 스캔에서 먼저 발견되는 0

출력:
- int[6]
- 좌표는 1-index
- [r1,c1,n1,r2,c2,n2]

============================================================
GUI / 실행 진입점 (이번 작업 범위에 포함)
============================================================
- 의존성: PyQt6 (또는 프로젝트 표준으로 PyQt6 고정) — pyproject.toml에 optional dependency 또는 필수 dependency로 명시
- 진입점: `python -m magicsquare` 또는 `python -m magicsquare.gui` 등 **단일 공식 경로** 1개만 문서화
- magicsquare 패키지에 **Qt를 import 하는 모듈**은 Screen 전용 하위 패키지에 둔다 (예: `magicsquare/gui/` 또는 `magicsquare/screen/`)
  - `domain.py`는 PyQt를 절대 import 하지 않는다.
- 최소 GUI 요구사항 (MVP):
  - 4×4 숫자 입력: QLineEdit 또는 QSpinBox 그리드 등, 빈칸은 0으로 표현
  - 「풀기」버튼: Boundary의 `validate` → `solve` 순으로 호출 (실패 시 ValueError 메시지를 QMessageBox 또는 상태 라벨에 표시)
  - 성공 시 길이 6 결과를 읽기 쉽게 표시 (예: 라벨 또는 읽기 전용 필드)
- GUI 동작에 대한 **자동화 테스트는 이번 커밋에서 필수 아님** (수동 체크리스트만 커밋 요약에 1~3줄). 단, 기존 pytest RED/GREEN 경로는 깨지 않게 유지.

============================================================
Step 1 — 이번 커밋에서 선택할 “첫 RED 테스트”
============================================================
(예시 — 실제 커밋마다 1묶음만 선택)

[TRACK B: Logic]
- L-RED-01: find_blank_coords()가 row-major 순서로 빈칸 좌표 2개를 반환한다.

[TRACK A: UI/Boundary]
- U-RED-01: 입력이 4x4가 아니면 예외를 발생시킨다.
- U-RED-02: 빈칸이 2개가 아니면 예외를 발생시킨다.

👉 (특정 커밋 예시) Logic: L-RED-01, UI: U-RED-01

선택 이유를 2줄로 설명하십시오.

============================================================
Step 2 — GREEN 최소 구현 (Dual-Track 병렬)
============================================================
[TRACK B — Logic GREEN]
- 선택한 Logic RED 1묶음만 통과하는 Domain 최소 구현.

[TRACK A — UI/Boundary GREEN]
- 선택한 Boundary RED 1묶음만 통과하는 validate 등 최소 구현.
- GUI 진입점 커밋은 **별도 커밋**으로 할 것: “실행 가능한 PyQt 윈도우 + pyproject 의존성 + README 실행 한 줄”만, Domain/Business 범위 확장 금지.

============================================================
Step 3 — 테스트 실행 및 통과 확인
============================================================
- 해당 커밋에서 선택한 pytest 묶음만 실행
- GUI는 수동으로 앱 실행 1회 확인 (통과/실패 요약에 한 줄)

============================================================
출력 형식 (반드시 준수)
============================================================
1) 이번 커밋 목표 (1~2문장)
2) 선택한 RED 테스트 (ID + 설명)
3) GREEN 최소 구현 범위 (Track A / Track B / GUI 여부)
4) 실행한 테스트 목록
5) 테스트 결과 요약 (PASS/FAIL)
6) 커밋 메시지 제안 (Conventional Commit)
7) 변경 파일 목록
8) 다음 커밋에서 진행할 RED 또는 GUI 보강 후보 2개

============================================================
주의
============================================================
- REFACTOR 금지
- 한 커밋에 “모든 RED 해결 + 풀 GUI”를 넣지 말 것
- PyQt는 Screen에만; Clean Architecture 경계 유지

```
####

(.venv) c:\DEV\MagicSquare _1004>pytest tests/magicsquare/ -v
================================================= test session starts =================================================
platform win32 -- Python 3.13.1, pytest-9.0.3, pluggy-1.6.0 -- C:\DEV\MagicSquare _1004\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: c:\DEV\MagicSquare _1004
configfile: pyproject.toml
plugins: cov-7.1.0
collected 16 items

tests/magicsquare/test_magic_square_logic_red.py::TestMagicSquareLogicRed::test_log_red_01_find_blank_coords_row_major_two_cells PASSED [  6%]
tests/magicsquare/test_magic_square_logic_red.py::TestMagicSquareLogicRed::test_log_red_02_find_not_exist_nums_two_sorted_ascending FAILED [ 12%]
tests/magicsquare/test_magic_square_logic_red.py::TestMagicSquareLogicRed::test_log_red_03a_is_magic_square_false_when_only_rows_match FAILED [ 18%]
tests/magicsquare/test_magic_square_logic_red.py::TestMagicSquareLogicRed::test_log_red_03b_is_magic_square_false_when_only_cols_match FAILED [ 25%]
tests/magicsquare/test_magic_square_logic_red.py::TestMagicSquareLogicRed::test_log_red_03c_is_magic_square_false_when_diagonal_wrong FAILED [ 31%]
tests/magicsquare/test_magic_square_logic_red.py::TestMagicSquareLogicRed::test_log_red_03d_is_magic_square_true_for_known_complete FAILED [ 37%]
tests/magicsquare/test_magic_square_logic_red.py::TestMagicSquareLogicRed::test_log_red_04a_solution_returns_six_elements_ordered FAILED [ 43%]
tests/magicsquare/test_magic_square_logic_red.py::TestMagicSquareLogicRed::test_log_red_04b_solution_coords_one_indexed_in_range FAILED [ 50%]
tests/magicsquare/test_magic_square_logic_red.py::TestMagicSquareLogicRed::test_log_red_04c_solution_reverse_policy_after_small_first_fails FAILED [ 56%]
tests/magicsquare/test_magic_square_logic_red.py::TestMagicSquareLogicRed::test_log_red_04d_solution_numbers_match_find_not_exist_nums FAILED [ 62%]
tests/magicsquare/test_magic_square_ui_boundary_red.py::TestMagicSquareUiBoundaryRed::test_ui_red_01_non_four_by_four_raises PASSED [ 68%]
tests/magicsquare/test_magic_square_ui_boundary_red.py::TestMagicSquareUiBoundaryRed::test_ui_red_02_blank_count_not_two_raises FAILED [ 75%]
tests/magicsquare/test_magic_square_ui_boundary_red.py::TestMagicSquareUiBoundaryRed::test_ui_red_03_value_out_of_range_raises FAILED [ 81%]
tests/magicsquare/test_magic_square_ui_boundary_red.py::TestMagicSquareUiBoundaryRed::test_ui_red_04_duplicate_non_zero_raises FAILED [ 87%]
tests/magicsquare/test_magic_square_ui_boundary_red.py::TestMagicSquareUiBoundaryRed::test_ui_red_05_solution_returns_length_six FAILED [ 93%]
tests/magicsquare/test_magic_square_ui_boundary_red.py::TestMagicSquareUiBoundaryRed::test_ui_red_06_solution_coords_are_one_indexed FAILED [100%]

====================================================== FAILURES =======================================================
__________________ TestMagicSquareLogicRed.test_log_red_02_find_not_exist_nums_two_sorted_ascending ___________________

self = <test_magic_square_logic_red.TestMagicSquareLogicRed object at 0x000002A98D256350>

    def test_log_red_02_find_not_exist_nums_two_sorted_ascending(self) -> None:
>       pytest.fail("RED")
E       Failed: RED

tests\magicsquare\test_magic_square_logic_red.py:29: Failed
_________________ TestMagicSquareLogicRed.test_log_red_03a_is_magic_square_false_when_only_rows_match _________________

self = <test_magic_square_logic_red.TestMagicSquareLogicRed object at 0x000002A98D5243E0>

    def test_log_red_03a_is_magic_square_false_when_only_rows_match(self) -> None:
>       pytest.fail("RED")
E       Failed: RED

tests\magicsquare\test_magic_square_logic_red.py:32: Failed
_________________ TestMagicSquareLogicRed.test_log_red_03b_is_magic_square_false_when_only_cols_match _________________

self = <test_magic_square_logic_red.TestMagicSquareLogicRed object at 0x000002A98D524640>

    def test_log_red_03b_is_magic_square_false_when_only_cols_match(self) -> None:
>       pytest.fail("RED")
E       Failed: RED

tests\magicsquare\test_magic_square_logic_red.py:35: Failed
_________________ TestMagicSquareLogicRed.test_log_red_03c_is_magic_square_false_when_diagonal_wrong __________________

self = <test_magic_square_logic_red.TestMagicSquareLogicRed object at 0x000002A98D564170>

    def test_log_red_03c_is_magic_square_false_when_diagonal_wrong(self) -> None:
>       pytest.fail("RED")
E       Failed: RED

tests\magicsquare\test_magic_square_logic_red.py:38: Failed
__________________ TestMagicSquareLogicRed.test_log_red_03d_is_magic_square_true_for_known_complete ___________________

self = <test_magic_square_logic_red.TestMagicSquareLogicRed object at 0x000002A98D1F8490>

    def test_log_red_03d_is_magic_square_true_for_known_complete(self) -> None:
>       pytest.fail("RED")
E       Failed: RED

tests\magicsquare\test_magic_square_logic_red.py:41: Failed
___________________ TestMagicSquareLogicRed.test_log_red_04a_solution_returns_six_elements_ordered ____________________

self = <test_magic_square_logic_red.TestMagicSquareLogicRed object at 0x000002A98D1F86B0>

    def test_log_red_04a_solution_returns_six_elements_ordered(self) -> None:
>       pytest.fail("RED")
E       Failed: RED

tests\magicsquare\test_magic_square_logic_red.py:44: Failed
____________________ TestMagicSquareLogicRed.test_log_red_04b_solution_coords_one_indexed_in_range ____________________

self = <test_magic_square_logic_red.TestMagicSquareLogicRed object at 0x000002A98D24F550>

    def test_log_red_04b_solution_coords_one_indexed_in_range(self) -> None:
>       pytest.fail("RED")
E       Failed: RED

tests\magicsquare\test_magic_square_logic_red.py:47: Failed
______________ TestMagicSquareLogicRed.test_log_red_04c_solution_reverse_policy_after_small_first_fails _______________

self = <test_magic_square_logic_red.TestMagicSquareLogicRed object at 0x000002A98D24F750>

    def test_log_red_04c_solution_reverse_policy_after_small_first_fails(self) -> None:
>       pytest.fail("RED")
E       Failed: RED

tests\magicsquare\test_magic_square_logic_red.py:50: Failed
_________________ TestMagicSquareLogicRed.test_log_red_04d_solution_numbers_match_find_not_exist_nums _________________

self = <test_magic_square_logic_red.TestMagicSquareLogicRed object at 0x000002A98D263A70>

    def test_log_red_04d_solution_numbers_match_find_not_exist_nums(self) -> None:
>       pytest.fail("RED")
E       Failed: RED

tests\magicsquare\test_magic_square_logic_red.py:53: Failed
_______________________ TestMagicSquareUiBoundaryRed.test_ui_red_02_blank_count_not_two_raises ________________________

self = <test_magic_square_ui_boundary_red.TestMagicSquareUiBoundaryRed object at 0x000002A98D256490>

    def test_ui_red_02_blank_count_not_two_raises(self) -> None:
>       pytest.fail("RED")
E       Failed: RED

tests\magicsquare\test_magic_square_ui_boundary_red.py:24: Failed
________________________ TestMagicSquareUiBoundaryRed.test_ui_red_03_value_out_of_range_raises ________________________

self = <test_magic_square_ui_boundary_red.TestMagicSquareUiBoundaryRed object at 0x000002A98D524510>

    def test_ui_red_03_value_out_of_range_raises(self) -> None:
>       pytest.fail("RED")
E       Failed: RED

tests\magicsquare\test_magic_square_ui_boundary_red.py:27: Failed
________________________ TestMagicSquareUiBoundaryRed.test_ui_red_04_duplicate_non_zero_raises ________________________

self = <test_magic_square_ui_boundary_red.TestMagicSquareUiBoundaryRed object at 0x000002A98D524770>

    def test_ui_red_04_duplicate_non_zero_raises(self) -> None:
>       pytest.fail("RED")
E       Failed: RED

tests\magicsquare\test_magic_square_ui_boundary_red.py:30: Failed
_______________________ TestMagicSquareUiBoundaryRed.test_ui_red_05_solution_returns_length_six _______________________

self = <test_magic_square_ui_boundary_red.TestMagicSquareUiBoundaryRed object at 0x000002A98D565C70>

    def test_ui_red_05_solution_returns_length_six(self) -> None:
>       pytest.fail("RED")
E       Failed: RED

tests\magicsquare\test_magic_square_ui_boundary_red.py:33: Failed
_____________________ TestMagicSquareUiBoundaryRed.test_ui_red_06_solution_coords_are_one_indexed _____________________

self = <test_magic_square_ui_boundary_red.TestMagicSquareUiBoundaryRed object at 0x000002A98D1F85A0>

    def test_ui_red_06_solution_coords_are_one_indexed(self) -> None:
>       pytest.fail("RED")
E       Failed: RED

tests\magicsquare\test_magic_square_ui_boundary_red.py:36: Failed
=============================================== short test summary info ===============================================
FAILED tests/magicsquare/test_magic_square_logic_red.py::TestMagicSquareLogicRed::test_log_red_02_find_not_exist_nums_two_sorted_ascending - Failed: RED
FAILED tests/magicsquare/test_magic_square_logic_red.py::TestMagicSquareLogicRed::test_log_red_03a_is_magic_square_false_when_only_rows_match - Failed: RED
FAILED tests/magicsquare/test_magic_square_logic_red.py::TestMagicSquareLogicRed::test_log_red_03b_is_magic_square_false_when_only_cols_match - Failed: RED
FAILED tests/magicsquare/test_magic_square_logic_red.py::TestMagicSquareLogicRed::test_log_red_03c_is_magic_square_false_when_diagonal_wrong - Failed: RED
FAILED tests/magicsquare/test_magic_square_logic_red.py::TestMagicSquareLogicRed::test_log_red_03d_is_magic_square_true_for_known_complete - Failed: RED
FAILED tests/magicsquare/test_magic_square_logic_red.py::TestMagicSquareLogicRed::test_log_red_04a_solution_returns_six_elements_ordered - Failed: RED
FAILED tests/magicsquare/test_magic_square_logic_red.py::TestMagicSquareLogicRed::test_log_red_04b_solution_coords_one_indexed_in_range - Failed: RED
FAILED tests/magicsquare/test_magic_square_logic_red.py::TestMagicSquareLogicRed::test_log_red_04c_solution_reverse_policy_after_small_first_fails - Failed: RED
FAILED tests/magicsquare/test_magic_square_logic_red.py::TestMagicSquareLogicRed::test_log_red_04d_solution_numbers_match_find_not_exist_nums - Failed: RED
FAILED tests/magicsquare/test_magic_square_ui_boundary_red.py::TestMagicSquareUiBoundaryRed::test_ui_red_02_blank_count_not_two_raises - Failed: RED
FAILED tests/magicsquare/test_magic_square_ui_boundary_red.py::TestMagicSquareUiBoundaryRed::test_ui_red_03_value_out_of_range_raises - Failed: RED
FAILED tests/magicsquare/test_magic_square_ui_boundary_red.py::TestMagicSquareUiBoundaryRed::test_ui_red_04_duplicate_non_zero_raises - Failed: RED
FAILED tests/magicsquare/test_magic_square_ui_boundary_red.py::TestMagicSquareUiBoundaryRed::test_ui_red_05_solution_returns_length_six - Failed: RED
FAILED tests/magicsquare/test_magic_square_ui_boundary_red.py::TestMagicSquareUiBoundaryRed::test_ui_red_06_solution_coords_are_one_indexed - Failed: RED
============================================ 14 failed, 2 passed in 0.26s =============================================

(.venv) c:\DEV\MagicSquare _1004>pytest tests/magicsquare/ -v
================================================= test session starts =================================================
platform win32 -- Python 3.13.1, pytest-9.0.3, pluggy-1.6.0 -- C:\DEV\MagicSquare _1004\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: c:\DEV\MagicSquare _1004
configfile: pyproject.toml
plugins: cov-7.1.0
collected 16 items

tests/magicsquare/test_magic_square_logic_red.py::TestMagicSquareLogicRed::test_log_red_01_find_blank_coords_row_major_two_cells PASSED [  6%]
tests/magicsquare/test_magic_square_logic_red.py::TestMagicSquareLogicRed::test_log_red_02_find_not_exist_nums_two_sorted_ascending FAILED [ 12%]
tests/magicsquare/test_magic_square_logic_red.py::TestMagicSquareLogicRed::test_log_red_03a_is_magic_square_false_when_only_rows_match FAILED [ 18%]
tests/magicsquare/test_magic_square_logic_red.py::TestMagicSquareLogicRed::test_log_red_03b_is_magic_square_false_when_only_cols_match FAILED [ 25%]
tests/magicsquare/test_magic_square_logic_red.py::TestMagicSquareLogicRed::test_log_red_03c_is_magic_square_false_when_diagonal_wrong FAILED [ 31%]
tests/magicsquare/test_magic_square_logic_red.py::TestMagicSquareLogicRed::test_log_red_03d_is_magic_square_true_for_known_complete FAILED [ 37%]
tests/magicsquare/test_magic_square_logic_red.py::TestMagicSquareLogicRed::test_log_red_04a_solution_returns_six_elements_ordered FAILED [ 43%]
tests/magicsquare/test_magic_square_logic_red.py::TestMagicSquareLogicRed::test_log_red_04b_solution_coords_one_indexed_in_range FAILED [ 50%]
tests/magicsquare/test_magic_square_logic_red.py::TestMagicSquareLogicRed::test_log_red_04c_solution_reverse_policy_after_small_first_fails FAILED [ 56%]
tests/magicsquare/test_magic_square_logic_red.py::TestMagicSquareLogicRed::test_log_red_04d_solution_numbers_match_find_not_exist_nums FAILED [ 62%]
tests/magicsquare/test_magic_square_ui_boundary_red.py::TestMagicSquareUiBoundaryRed::test_ui_red_01_non_four_by_four_raises PASSED [ 68%]
tests/magicsquare/test_magic_square_ui_boundary_red.py::TestMagicSquareUiBoundaryRed::test_ui_red_02_blank_count_not_two_raises FAILED [ 75%]
tests/magicsquare/test_magic_square_ui_boundary_red.py::TestMagicSquareUiBoundaryRed::test_ui_red_03_value_out_of_range_raises FAILED [ 81%]
tests/magicsquare/test_magic_square_ui_boundary_red.py::TestMagicSquareUiBoundaryRed::test_ui_red_04_duplicate_non_zero_raises FAILED [ 87%]
tests/magicsquare/test_magic_square_ui_boundary_red.py::TestMagicSquareUiBoundaryRed::test_ui_red_05_solution_returns_length_six FAILED [ 93%]
tests/magicsquare/test_magic_square_ui_boundary_red.py::TestMagicSquareUiBoundaryRed::test_ui_red_06_solution_coords_are_one_indexed FAILED [100%]

====================================================== FAILURES =======================================================
__________________ TestMagicSquareLogicRed.test_log_red_02_find_not_exist_nums_two_sorted_ascending ___________________

self = <test_magic_square_logic_red.TestMagicSquareLogicRed object at 0x000001F7AC382350>

    def test_log_red_02_find_not_exist_nums_two_sorted_ascending(self) -> None:
>       pytest.fail("RED")
E       Failed: RED

tests\magicsquare\test_magic_square_logic_red.py:29: Failed
_________________ TestMagicSquareLogicRed.test_log_red_03a_is_magic_square_false_when_only_rows_match _________________

self = <test_magic_square_logic_red.TestMagicSquareLogicRed object at 0x000001F7ADC603E0>

    def test_log_red_03a_is_magic_square_false_when_only_rows_match(self) -> None:
>       pytest.fail("RED")
E       Failed: RED

tests\magicsquare\test_magic_square_logic_red.py:32: Failed
_________________ TestMagicSquareLogicRed.test_log_red_03b_is_magic_square_false_when_only_cols_match _________________

self = <test_magic_square_logic_red.TestMagicSquareLogicRed object at 0x000001F7ADC60640>

    def test_log_red_03b_is_magic_square_false_when_only_cols_match(self) -> None:
>       pytest.fail("RED")
E       Failed: RED

tests\magicsquare\test_magic_square_logic_red.py:35: Failed
_________________ TestMagicSquareLogicRed.test_log_red_03c_is_magic_square_false_when_diagonal_wrong __________________

self = <test_magic_square_logic_red.TestMagicSquareLogicRed object at 0x000001F7AC367BF0>

    def test_log_red_03c_is_magic_square_false_when_diagonal_wrong(self) -> None:
>       pytest.fail("RED")
E       Failed: RED

tests\magicsquare\test_magic_square_logic_red.py:38: Failed
__________________ TestMagicSquareLogicRed.test_log_red_03d_is_magic_square_true_for_known_complete ___________________

self = <test_magic_square_logic_red.TestMagicSquareLogicRed object at 0x000001F7AC3CBAC0>

    def test_log_red_03d_is_magic_square_true_for_known_complete(self) -> None:
>       pytest.fail("RED")
E       Failed: RED

tests\magicsquare\test_magic_square_logic_red.py:41: Failed
___________________ TestMagicSquareLogicRed.test_log_red_04a_solution_returns_six_elements_ordered ____________________

self = <test_magic_square_logic_red.TestMagicSquareLogicRed object at 0x000001F7AC32C5A0>

    def test_log_red_04a_solution_returns_six_elements_ordered(self) -> None:
>       pytest.fail("RED")
E       Failed: RED

tests\magicsquare\test_magic_square_logic_red.py:44: Failed
____________________ TestMagicSquareLogicRed.test_log_red_04b_solution_coords_one_indexed_in_range ____________________

self = <test_magic_square_logic_red.TestMagicSquareLogicRed object at 0x000001F7AC37B550>

    def test_log_red_04b_solution_coords_one_indexed_in_range(self) -> None:
>       pytest.fail("RED")
E       Failed: RED

tests\magicsquare\test_magic_square_logic_red.py:47: Failed
______________ TestMagicSquareLogicRed.test_log_red_04c_solution_reverse_policy_after_small_first_fails _______________

self = <test_magic_square_logic_red.TestMagicSquareLogicRed object at 0x000001F7AC37B750>

    def test_log_red_04c_solution_reverse_policy_after_small_first_fails(self) -> None:
>       pytest.fail("RED")
E       Failed: RED

tests\magicsquare\test_magic_square_logic_red.py:50: Failed
_________________ TestMagicSquareLogicRed.test_log_red_04d_solution_numbers_match_find_not_exist_nums _________________

self = <test_magic_square_logic_red.TestMagicSquareLogicRed object at 0x000001F7AC38FA70>

    def test_log_red_04d_solution_numbers_match_find_not_exist_nums(self) -> None:
>       pytest.fail("RED")
E       Failed: RED

tests\magicsquare\test_magic_square_logic_red.py:53: Failed
_______________________ TestMagicSquareUiBoundaryRed.test_ui_red_02_blank_count_not_two_raises ________________________

self = <test_magic_square_ui_boundary_red.TestMagicSquareUiBoundaryRed object at 0x000001F7AC382210>

    def test_ui_red_02_blank_count_not_two_raises(self) -> None:
>       pytest.fail("RED")
E       Failed: RED

tests\magicsquare\test_magic_square_ui_boundary_red.py:24: Failed
________________________ TestMagicSquareUiBoundaryRed.test_ui_red_03_value_out_of_range_raises ________________________

self = <test_magic_square_ui_boundary_red.TestMagicSquareUiBoundaryRed object at 0x000001F7ADC60510>

    def test_ui_red_03_value_out_of_range_raises(self) -> None:
>       pytest.fail("RED")
E       Failed: RED

tests\magicsquare\test_magic_square_ui_boundary_red.py:27: Failed
________________________ TestMagicSquareUiBoundaryRed.test_ui_red_04_duplicate_non_zero_raises ________________________

self = <test_magic_square_ui_boundary_red.TestMagicSquareUiBoundaryRed object at 0x000001F7ADC602B0>

    def test_ui_red_04_duplicate_non_zero_raises(self) -> None:
>       pytest.fail("RED")
E       Failed: RED

tests\magicsquare\test_magic_square_ui_boundary_red.py:30: Failed
_______________________ TestMagicSquareUiBoundaryRed.test_ui_red_05_solution_returns_length_six _______________________

self = <test_magic_square_ui_boundary_red.TestMagicSquareUiBoundaryRed object at 0x000001F7ADC997F0>

    def test_ui_red_05_solution_returns_length_six(self) -> None:
>       pytest.fail("RED")
E       Failed: RED

tests\magicsquare\test_magic_square_ui_boundary_red.py:33: Failed
_____________________ TestMagicSquareUiBoundaryRed.test_ui_red_06_solution_coords_are_one_indexed _____________________

self = <test_magic_square_ui_boundary_red.TestMagicSquareUiBoundaryRed object at 0x000001F7AC32C490>

    def test_ui_red_06_solution_coords_are_one_indexed(self) -> None:
>       pytest.fail("RED")
E       Failed: RED

tests\magicsquare\test_magic_square_ui_boundary_red.py:36: Failed
=============================================== short test summary info ===============================================
FAILED tests/magicsquare/test_magic_square_logic_red.py::TestMagicSquareLogicRed::test_log_red_02_find_not_exist_nums_two_sorted_ascending - Failed: RED
FAILED tests/magicsquare/test_magic_square_logic_red.py::TestMagicSquareLogicRed::test_log_red_03a_is_magic_square_false_when_only_rows_match - Failed: RED
FAILED tests/magicsquare/test_magic_square_logic_red.py::TestMagicSquareLogicRed::test_log_red_03b_is_magic_square_false_when_only_cols_match - Failed: RED
FAILED tests/magicsquare/test_magic_square_logic_red.py::TestMagicSquareLogicRed::test_log_red_03c_is_magic_square_false_when_diagonal_wrong - Failed: RED
FAILED tests/magicsquare/test_magic_square_logic_red.py::TestMagicSquareLogicRed::test_log_red_03d_is_magic_square_true_for_known_complete - Failed: RED
FAILED tests/magicsquare/test_magic_square_logic_red.py::TestMagicSquareLogicRed::test_log_red_04a_solution_returns_six_elements_ordered - Failed: RED
FAILED tests/magicsquare/test_magic_square_logic_red.py::TestMagicSquareLogicRed::test_log_red_04b_solution_coords_one_indexed_in_range - Failed: RED
FAILED tests/magicsquare/test_magic_square_logic_red.py::TestMagicSquareLogicRed::test_log_red_04c_solution_reverse_policy_after_small_first_fails - Failed: RED
FAILED tests/magicsquare/test_magic_square_logic_red.py::TestMagicSquareLogicRed::test_log_red_04d_solution_numbers_match_find_not_exist_nums - Failed: RED
FAILED tests/magicsquare/test_magic_square_ui_boundary_red.py::TestMagicSquareUiBoundaryRed::test_ui_red_02_blank_count_not_two_raises - Failed: RED
FAILED tests/magicsquare/test_magic_square_ui_boundary_red.py::TestMagicSquareUiBoundaryRed::test_ui_red_03_value_out_of_range_raises - Failed: RED
FAILED tests/magicsquare/test_magic_square_ui_boundary_red.py::TestMagicSquareUiBoundaryRed::test_ui_red_04_duplicate_non_zero_raises - Failed: RED
FAILED tests/magicsquare/test_magic_square_ui_boundary_red.py::TestMagicSquareUiBoundaryRed::test_ui_red_05_solution_returns_length_six - Failed: RED
FAILED tests/magicsquare/test_magic_square_ui_boundary_red.py::TestMagicSquareUiBoundaryRed::test_ui_red_06_solution_coords_are_one_indexed - Failed: RED
============================================ 14 failed, 2 passed in 0.20s =============================================

(.venv) c:\DEV\MagicSquare _1004>pytest tests/magicsquare/test_magic_square_logic_red.py::TestMagicSquareLogicRed::test_log_red_01_find_blank_coords_row_major_two_cells tests/magicsquare/test_magic_square_ui_boundary_red.py::TestMagicSquareUiBoundaryRed::test_ui_red_01_non_four_by_four_raises -v
================================================= test session starts =================================================
platform win32 -- Python 3.13.1, pytest-9.0.3, pluggy-1.6.0 -- C:\DEV\MagicSquare _1004\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: c:\DEV\MagicSquare _1004
configfile: pyproject.toml
plugins: cov-7.1.0
collected 2 items

tests/magicsquare/test_magic_square_logic_red.py::TestMagicSquareLogicRed::test_log_red_01_find_blank_coords_row_major_two_cells PASSED [ 50%]
tests/magicsquare/test_magic_square_ui_boundary_red.py::TestMagicSquareUiBoundaryRed::test_ui_red_01_non_four_by_four_raises PASSED [100%]

================================================== 2 passed in 0.05s ==================================================

(.venv) c:\DEV\MagicSquare _1004>python -c "from magicsquare.domain import find_blank_coords; from magicsquare.boundary import validate; g=[[16,2,3,13],[5,11,10,8],[9,7,0,12],[4,14,15,0]]; validate(g); print(find_blank_coords(g))"
((3, 3), (4, 4))

(.venv) c:\DEV\MagicSquare _1004>python -m pytest tests\magicsquare\test_magic_square_logic_red.py
=================================================== test session starts ===================================================
platform win32 -- Python 3.13.1, pytest-9.0.3, pluggy-1.6.0
rootdir: c:\DEV\MagicSquare _1004
configfile: pyproject.toml
plugins: cov-7.1.0
collected 10 items

tests\magicsquare\test_magic_square_logic_red.py .FFFFFFFFF                                                          [100%]

======================================================== FAILURES =========================================================
____________________ TestMagicSquareLogicRed.test_log_red_02_find_not_exist_nums_two_sorted_ascending _____________________

self = <test_magic_square_logic_red.TestMagicSquareLogicRed object at 0x00000261CC7F2210>

    def test_log_red_02_find_not_exist_nums_two_sorted_ascending(self) -> None:
>       pytest.fail("RED")
E       Failed: RED

tests\magicsquare\test_magic_square_logic_red.py:29: Failed
___________________ TestMagicSquareLogicRed.test_log_red_03a_is_magic_square_false_when_only_rows_match ___________________

self = <test_magic_square_logic_red.TestMagicSquareLogicRed object at 0x00000261CCAC43E0>

    def test_log_red_03a_is_magic_square_false_when_only_rows_match(self) -> None:
>       pytest.fail("RED")
E       Failed: RED

tests\magicsquare\test_magic_square_logic_red.py:32: Failed
___________________ TestMagicSquareLogicRed.test_log_red_03b_is_magic_square_false_when_only_cols_match ___________________

self = <test_magic_square_logic_red.TestMagicSquareLogicRed object at 0x00000261CCAC4640>

    def test_log_red_03b_is_magic_square_false_when_only_cols_match(self) -> None:
>       pytest.fail("RED")
E       Failed: RED

tests\magicsquare\test_magic_square_logic_red.py:35: Failed
___________________ TestMagicSquareLogicRed.test_log_red_03c_is_magic_square_false_when_diagonal_wrong ____________________

self = <test_magic_square_logic_red.TestMagicSquareLogicRed object at 0x00000261CC7DBE30>

    def test_log_red_03c_is_magic_square_false_when_diagonal_wrong(self) -> None:
>       pytest.fail("RED")
E       Failed: RED

tests\magicsquare\test_magic_square_logic_red.py:38: Failed
____________________ TestMagicSquareLogicRed.test_log_red_03d_is_magic_square_true_for_known_complete _____________________

self = <test_magic_square_logic_red.TestMagicSquareLogicRed object at 0x00000261CC83BAC0>

    def test_log_red_03d_is_magic_square_true_for_known_complete(self) -> None:
>       pytest.fail("RED")
E       Failed: RED

tests\magicsquare\test_magic_square_logic_red.py:41: Failed
_____________________ TestMagicSquareLogicRed.test_log_red_04a_solution_returns_six_elements_ordered ______________________

self = <test_magic_square_logic_red.TestMagicSquareLogicRed object at 0x00000261CC7985A0>

    def test_log_red_04a_solution_returns_six_elements_ordered(self) -> None:
>       pytest.fail("RED")
E       Failed: RED

tests\magicsquare\test_magic_square_logic_red.py:44: Failed
______________________ TestMagicSquareLogicRed.test_log_red_04b_solution_coords_one_indexed_in_range ______________________

self = <test_magic_square_logic_red.TestMagicSquareLogicRed object at 0x00000261CC7EAF50>

    def test_log_red_04b_solution_coords_one_indexed_in_range(self) -> None:
>       pytest.fail("RED")
E       Failed: RED

tests\magicsquare\test_magic_square_logic_red.py:47: Failed
________________ TestMagicSquareLogicRed.test_log_red_04c_solution_reverse_policy_after_small_first_fails _________________

self = <test_magic_square_logic_red.TestMagicSquareLogicRed object at 0x00000261CC7EB250>

    def test_log_red_04c_solution_reverse_policy_after_small_first_fails(self) -> None:
>       pytest.fail("RED")
E       Failed: RED

tests\magicsquare\test_magic_square_logic_red.py:50: Failed
___________________ TestMagicSquareLogicRed.test_log_red_04d_solution_numbers_match_find_not_exist_nums ___________________

self = <test_magic_square_logic_red.TestMagicSquareLogicRed object at 0x00000261CC7FF980>

    def test_log_red_04d_solution_numbers_match_find_not_exist_nums(self) -> None:
>       pytest.fail("RED")
E       Failed: RED

tests\magicsquare\test_magic_square_logic_red.py:53: Failed
================================================= short test summary info =================================================
FAILED tests/magicsquare/test_magic_square_logic_red.py::TestMagicSquareLogicRed::test_log_red_02_find_not_exist_nums_two_sorted_ascending - Failed: RED
FAILED tests/magicsquare/test_magic_square_logic_red.py::TestMagicSquareLogicRed::test_log_red_03a_is_magic_square_false_when_only_rows_match - Failed: RED
FAILED tests/magicsquare/test_magic_square_logic_red.py::TestMagicSquareLogicRed::test_log_red_03b_is_magic_square_false_when_only_cols_match - Failed: RED
FAILED tests/magicsquare/test_magic_square_logic_red.py::TestMagicSquareLogicRed::test_log_red_03c_is_magic_square_false_when_diagonal_wrong - Failed: RED
FAILED tests/magicsquare/test_magic_square_logic_red.py::TestMagicSquareLogicRed::test_log_red_03d_is_magic_square_true_for_known_complete - Failed: RED
FAILED tests/magicsquare/test_magic_square_logic_red.py::TestMagicSquareLogicRed::test_log_red_04a_solution_returns_six_elements_ordered - Failed: RED
FAILED tests/magicsquare/test_magic_square_logic_red.py::TestMagicSquareLogicRed::test_log_red_04b_solution_coords_one_indexed_in_range - Failed: RED
FAILED tests/magicsquare/test_magic_square_logic_red.py::TestMagicSquareLogicRed::test_log_red_04c_solution_reverse_policy_after_small_first_fails - Failed: RED
FAILED tests/magicsquare/test_magic_square_logic_red.py::TestMagicSquareLogicRed::test_log_red_04d_solution_numbers_match_find_not_exist_nums - Failed: RED
=============================================== 9 failed, 1 passed in 0.13s ===============================================

(.venv) c:\DEV\MagicSquare _1004>python -m pytest tests\magicsquare\test_magic_square_ui_boundary_red.py
=================================================== test session starts ===================================================
platform win32 -- Python 3.13.1, pytest-9.0.3, pluggy-1.6.0
rootdir: c:\DEV\MagicSquare _1004
configfile: pyproject.toml
plugins: cov-7.1.0
collected 6 items

tests\magicsquare\test_magic_square_ui_boundary_red.py .FFFFF                                                        [100%]

======================================================== FAILURES =========================================================
_________________________ TestMagicSquareUiBoundaryRed.test_ui_red_02_blank_count_not_two_raises __________________________

self = <test_magic_square_ui_boundary_red.TestMagicSquareUiBoundaryRed object at 0x000002523CFC2210>

    def test_ui_red_02_blank_count_not_two_raises(self) -> None:
>       pytest.fail("RED")
E       Failed: RED

tests\magicsquare\test_magic_square_ui_boundary_red.py:24: Failed
__________________________ TestMagicSquareUiBoundaryRed.test_ui_red_03_value_out_of_range_raises __________________________

self = <test_magic_square_ui_boundary_red.TestMagicSquareUiBoundaryRed object at 0x000002523CF6C3E0>

    def test_ui_red_03_value_out_of_range_raises(self) -> None:
>       pytest.fail("RED")
E       Failed: RED

tests\magicsquare\test_magic_square_ui_boundary_red.py:27: Failed
__________________________ TestMagicSquareUiBoundaryRed.test_ui_red_04_duplicate_non_zero_raises __________________________

self = <test_magic_square_ui_boundary_red.TestMagicSquareUiBoundaryRed object at 0x000002523CF6C640>

    def test_ui_red_04_duplicate_non_zero_raises(self) -> None:
>       pytest.fail("RED")
E       Failed: RED

tests\magicsquare\test_magic_square_ui_boundary_red.py:30: Failed
_________________________ TestMagicSquareUiBoundaryRed.test_ui_red_05_solution_returns_length_six _________________________

self = <test_magic_square_ui_boundary_red.TestMagicSquareUiBoundaryRed object at 0x000002523CFABE30>

    def test_ui_red_05_solution_returns_length_six(self) -> None:
>       pytest.fail("RED")
E       Failed: RED

tests\magicsquare\test_magic_square_ui_boundary_red.py:33: Failed
_______________________ TestMagicSquareUiBoundaryRed.test_ui_red_06_solution_coords_are_one_indexed _______________________

self = <test_magic_square_ui_boundary_red.TestMagicSquareUiBoundaryRed object at 0x000002523D00BAC0>

    def test_ui_red_06_solution_coords_are_one_indexed(self) -> None:
>       pytest.fail("RED")
E       Failed: RED

tests\magicsquare\test_magic_square_ui_boundary_red.py:36: Failed
================================================= short test summary info =================================================
FAILED tests/magicsquare/test_magic_square_ui_boundary_red.py::TestMagicSquareUiBoundaryRed::test_ui_red_02_blank_count_not_two_raises - Failed: RED
FAILED tests/magicsquare/test_magic_square_ui_boundary_red.py::TestMagicSquareUiBoundaryRed::test_ui_red_03_value_out_of_range_raises - Failed: RED
FAILED tests/magicsquare/test_magic_square_ui_boundary_red.py::TestMagicSquareUiBoundaryRed::test_ui_red_04_duplicate_non_zero_raises - Failed: RED
FAILED tests/magicsquare/test_magic_square_ui_boundary_red.py::TestMagicSquareUiBoundaryRed::test_ui_red_05_solution_returns_length_six - Failed: RED
FAILED tests/magicsquare/test_magic_square_ui_boundary_red.py::TestMagicSquareUiBoundaryRed::test_ui_red_06_solution_coords_are_one_indexed - Failed: RED
=============================================== 5 failed, 1 passed in 0.08s ===============================================

(.venv) c:\DEV\MagicSquare _1004>pip install -e ".[gui]"
Obtaining file:///C:/DEV/MagicSquare%20_1004
  Installing build dependencies ... done
  Checking if build backend supports build_editable ... done
  Getting requirements to build editable ... done
  Preparing editable metadata (pyproject.toml) ... done
Requirement already satisfied: PyQt6>=6.5 in c:\dev\magicsquare _1004\.venv\lib\site-packages (from magicsquare==0.1.0) (6.11.0)
Requirement already satisfied: PyQt6-sip<14,>=13.8 in c:\dev\magicsquare _1004\.venv\lib\site-packages (from PyQt6>=6.5->magicsquare==0.1.0) (13.11.1)
Requirement already satisfied: PyQt6-Qt6<6.12.0,>=6.11.0 in c:\dev\magicsquare _1004\.venv\lib\site-packages (from PyQt6>=6.5->magicsquare==0.1.0) (6.11.0)
Building wheels for collected packages: magicsquare
  Building editable for magicsquare (pyproject.toml) ... done
  Created wheel for magicsquare: filename=magicsquare-0.1.0-0.editable-py3-none-any.whl size=1297 sha256=0e874ecb19f84148dab3c2619fb6a1563a2393052241dcd09a0319029fd6ac66
  Stored in directory: C:\Users\kz4ne\AppData\Local\Temp\pip-ephem-wheel-cache-wujc0fyz\wheels\3c\f6\b1\9b3410c13906f19976629bc760c0b99ae9a0fe21d565f00f8b
Successfully built magicsquare
Installing collected packages: magicsquare
  Attempting uninstall: magicsquare
    Found existing installation: magicsquare 0.1.0
    Uninstalling magicsquare-0.1.0:
      Successfully uninstalled magicsquare-0.1.0
Successfully installed magicsquare-0.1.0

[notice] A new release of pip is available: 24.3.1 -> 26.0.1
[notice] To update, run: python.exe -m pip install --upgrade pip

(.venv) c:\DEV\MagicSquare _1004>python -m magicsquare

(.venv) c:\DEV\MagicSquare _1004>


####

작업한 내용을 Report 폴더에 보고서로 내보내줘.
```
작업한 내용을 모두 깃헙에 업로드해줘.

```


## D2_7실습- Dual-Track Refactoring 

### 리팩토링 전 작업


kz4ne@kz4network MINGW64 /c/DEV/MagicSquare _1004 (refactor/refactor)
$ git branch
  develop
  feature/dual-track-tdd
  main
* refactor/refactor
  stabilize/green

kz4ne@kz4network MINGW64 /c/DEV/MagicSquare _1004 (refactor/refactor)
$ 

### STEP 1 — 분석 전 전제 확인 프롬프트

[Ask 모드]
```
아직 코드는 수정하지 말고 분석만 해줘.

@domain.py @boundary.py @gui/main_window.py 를 보고
아래 두 가지만 먼저 답해줘:

1. 현재 테스트 파일(test_*.py)이 존재하는지 확인하고,
   없다면 어느 파일에 대한 테스트가 필요한지 알려줘
2. 테스트 없이 리팩토링을 시작하면 안 되는 이유를 한 줄로 설명해줘

```
### STEP 2 — 코드 스멜(Code Smell) 탐지 프롬프트

[Ask 모드]

```
@domain.py @boundary.py @gui/main_window.py 의 코드 스멜(Code Smell)을 분석해줘.
코드는 절대 수정하지 말고, 문제 있는 부분만 아래 표 형식으로 정리해줘:

| 파일명 | 줄번호 | 스멜 종류 | 문제 설명 | 우선순위 |

점검 항목:
- 이해하기 힘든 이름 (함수·변수명만 봐도 의미를 알 수 없는 경우)
- 중복 코드 (같은 로직이 두 곳 이상 등장)
- 긴 함수 (20줄 초과)
- 하드코딩된 매직 넘버 (예: 34, 4, 16 등)
- 긴 매개변수 목록 (파라미터 3개 초과)
- 불필요한 주석 (코드 자체로 설명되어야 할 내용)
- 사용하지 않는 변수·함수
```

###STEP 3 — ECB 책임 분리 관점 분석 프롬프트

[Ask 모드]

```
@domain.py @boundary.py @gui/main_window.py 를 ECB(Entity-Control-Boundary) 패턴으로 분석해줘.
코드는 수정하지 말고 다음만 답해줘:

1. 각 파일이 현재 담당하는 ECB 역할
   - domain.py   → Entity(데이터) / Control(로직) 중 어느 것?
   - boundary.py → Boundary 역할을 제대로 하고 있는가?
   - gui/main_window.py → UI 로직 외에 다른 책임이 섞여 있는가?

2. 잘못된 위치에 있는 코드가 있다면
   어느 파일로 이동해야 하는지 알려줘

3. domain.py 안에 Entity(데이터 보관)와
   Control(비즈니스 규칙 실행)이 혼재한다면
   분리가 필요한 부분을 짚어줘
```
### STEP 4 — SRP / SOLID 위반 점검

[Ask 모드]
```

@domain.py @boundary.py 를 SRP(단일 책임 원칙) 관점에서
점검해줘. 코드는 수정하지 말고 위반 사항만 알려줘:

- 하나의 함수가 두 가지 이상의 역할을 하는 경우
- 하나의 클래스가 데이터 보관과 검증 로직을 동시에 담당하는 경우
- gui/main_window.py 에서 UI 외에 비즈니스 판단을 직접 하는 경우
  (예: if total == 34 처럼 UI가 직접 계산·판단하는 코드)

각 항목에 대해 파일명:줄번호 형식으로 알려줘.
```

### STEP 5 — 분석 결과 종합 및 우선순위 결정 프롬프트

[Ask 모드]
```
앞서 분석한 내용을 바탕으로 리팩토링 계획서를 작성해줘.
코드는 아직 수정하지 말고 다음 형식으로 정리해줘:

## 리팩토링 대상 목록 (우선순위 순)

| 순번 | 대상 파일 | 문제 | 적용 기법 | 우선순위 |

## 테스트 선행 필요 항목
- 리팩토링 전에 먼저 테스트를 추가해야 할 함수 목록

## 리팩토링 후 검증 방법
- 회귀 테스트(Regression Test) 실행 명령어
- 외부 동작(기능)이 바뀌지 않았음을 확인하는 방법
```   
 
### 깃 헙 업로드 후 PR 생성 후 다음 작업 진행하고
[Agent 모드]
```
지금까지 작업한 내용을 Report 폴더에 보고서로 내보내줘.
```
모든 파일을 깃헙에 업로드해줘.
```
```
### Dual-Track Refactoring 프롬프트 작성 답

[Agent 모드]
```
당신은 Dual-Track UI + Logic TDD 및 리팩토링 전문가입니다.
프로젝트: Magic Square (4x4)
이번 작업은 “커밋 1개” 단위의 Dual-Track REFACTOR만 수행합니다.

============================================================
절대 규칙 (REFRACTOR SAFETY)
============================================================
- 새 기능 추가 금지 (Feature scope change 금지)
- 외부 계약(Input/Output, 예외 타입/메시지, 배열 포맷) 변경 금지
- 테스트 삭제/완화 금지 (assert 약화 금지)
- 먼저 테스트 실행 → 리팩토링 → 테스트 재실행 (항상 GREEN 유지)
- 하드코딩 추가 금지 / 매직 넘버 추가 금지
- 파일/클래스 이동은 최소화하고, 이번 커밋 범위만 다루기
- Dual-Track 분리 유지:
  - Boundary(UI Track)는 계약/검증/포맷 책임만
  - Domain(Logic Track)은 순수 규칙/계산 책임만

============================================================
고정 계약 (변경 금지)
============================================================
입력:
- 4x4 int[][]
- 0은 빈칸, 정확히 2개
- 값 범위: 0 또는 1~16
- 0 제외 중복 금지
- 첫 번째 빈칸: row-major 스캔에서 먼저 발견되는 0

출력:
- int[6], 좌표는 1-index
- [r1, c1, n1, r2, c2, n2]
- 두 조합 시도 정책은 동일하게 유지

============================================================
커밋 단위 Dual-Track REFACTOR 절차
============================================================
Step 0) 기준선 확인
- 전체 테스트를 실행하고 “현재 GREEN 상태”임을 확인한 뒤 요약해 주세요.

Step 1) 이번 커밋에서 수행할 리팩토링 목표 1~2개만 선택
아래 후보 중 “가장 작은 단위”로 1~2개만 선택하십시오.
(선택 사유: 위험도 낮음, 변경 범위 작음, 중복 제거 효과 큼)

[Logic Track 후보]
- R-L1: Pair/배열 좌표 표현을 Coordinate(Value Object)로 교체
- R-L2: 행/열/대각선 합 계산 중복 로직을 sumRow/sumCol/sumDiag로 추출
- R-L3: Magic Constant 계산을 함수로 추출하고 MATRIX_SIZE 상수화
- R-L4: solution()에서 “조합 시도”를 tryPlacement(order)로 분리

[UI Track 후보]
- R-U1: 입력 검증 로직을 ValidationPolicy/Validator로 분리 (도메인 침투 제거)
- R-U2: 예외 메시지/코드를 상수화하고 Error Schema를 단일화
- R-U3: 출력 포맷 생성 로직을 ResultFormatter로 분리 (1-index 규칙 고정)

Step 2) 보호 테스트(안전망) 점검 및 보강(필요 시 최소 추가)
- 리팩토링 대상과 직접 연관된 테스트가 부족하면 “테스트를 강화”하십시오.
- 단, 새로운 기능 테스트를 만들지 말고, 기존 계약/동작을 더 명확히 검증하는 수준만 허용합니다.
- 예: 좌표 1-index 유지, row-major 유지, 반환 길이 6, 예외 타입/메시지 유지 등

Step 3) Dual-Track 리팩토링 수행 (최소 변경)
- 선택한 목표만 수행하십시오.
- 경계(UI) ↔ 도메인(Logic) 책임이 섞이면 분리하십시오.
- 퍼블릭 API/계약이 바뀌지 않도록 주의하십시오.

Step 4) 테스트 재실행 (회귀 확인)
- 전체 테스트를 실행하고 모두 통과해야 합니다.
- 실패 시: 리팩토링을 되돌리거나 수정하여 GREEN을 복구하십시오.

Step 5) 커밋 준비 산출물 작성
아래 형식으로 결과를 정리하십시오.

============================================================
출력 형식 (반드시 준수)
============================================================
1) 이번 커밋 리팩토링 목표 (선택한 항목 ID)
2) 변경 범위 요약 (UI Track / Logic Track 분리해서)
3) 변경 전 문제점 → 변경 후 개선점 (각 2~3줄)
4) 수정된 파일 목록 (추가/수정/이동)
5) 테스트 실행 결과 요약 (실행 명령 + PASS)
6) 위험 요소 및 롤백 포인트 (무엇을 되돌리면 되는지)
7) 커밋 메시지 제안 (Conventional Commit)
   - 예: refactor(domain): extract sum helpers and introduce Coordinate

============================================================
주의
============================================================
- 구현 기능을 바꾸지 마십시오.
- 출력 포맷을 바꾸지 마십시오.
- 테스트는 반드시 통과해야 합니다.
- 이번 커밋은 “리팩토링만” 포함해야 합니다.

```
```
작업한 내용 모두를 @11.MagicSquare_Refactoring_Readiness_Analysis_Report.md 파일에 추가해 업데이트해줘
```
작업한 내용을 모두 깃헙에 업로드해줘.
```

로컬에서:
  git checkout develop
  git pull origin develop
  git checkout -b bp/prompting_bp 
  


```

프로젝트 : Prompting_BP

발표자가 내 본인 번호로 Repository 생성, 발표 자료 작성 및 진행
Repository : 프로젝트명_개인번호 (ex: Prompting_BP _xx)
Description : Author, Reviewer 성명 -> ex: Author : 길동이, Reviewer : 박문수

발표도 포함되지만.
최종 제출물은 회고 및 개선 계획이 명확히 보이는 문서 형태여야 합니다.

Markdown (.md) 또는 자유형식 텍스트
형식 예시

# Prompting BP 회고
## 1. Keep
- 기존 코드 이해 속도 빠름
- 리팩토링 제안 품질 높음

## 2. Problem
- 프롬프트 엔지니어링 부족
- AI 제안 검증 능력 미흡
...

1장: Keep

2장: Problem

3장: Try

4장: 개인별 학습 성과

5장: 팀 차원의 개선 액션 아이템 (표 형식)

6장: 현업 적용 계획

프로젝트 전체를 돌아보며 학습과 개선점을 공유하는 세션을 기획해주세요.
1. 회고 세션 구성 
KPT 회고 (Keep, Problem, Try)
Keep (계속 유지할 것들)
- 무엇이 잘 되었는가?
- 어떤 관행을 계속 유지해야 하는가?
- 팀에게 도움이 된 것들은?

Problem (문제점들)
- 어떤 장애물이 있었는가?
- 무엇이 팀을 느리게 했는가?
- 어떤 프로세스가 비효율적이었는가?

Try (시도해볼 것들)
- 다음에는 무엇을 다르게 해볼까?
- 어떤 새로운 도구나 방법을 시도해볼까?
- 문제 해결을 위한 실험들은?

2. 개인별 학습 성과 공유 
o	각자가 배운 새로운 기술/개념
o	개인 역량 향상 부분
o	다른 팀원들과 공유하고 싶은 인사이트
o	추천하고 싶은 학습 자료

3. 팀 차원의 개선 액션 아이템 
o	구체적이고 실행 가능한 개선 계획
o	책임자 및 일정 할당
o	진행 상황 추적 방법
o	성공 기준 정의

출력 형태:
•	회고 세션 진행 가이드
•	액션 아이템 추적 템플릿
•	학습 자료 정리 문서
•	다음 프로젝트 개선 계획서

