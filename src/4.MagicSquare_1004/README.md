# MagicSquare (4×4)

부분적으로 비어 있는 **4×4 Magic Square**를, 고정된 입출력 계약에 따라 완성하거나(두 빈칸 `0`에 값 배치), 구조 위반·해 없음을 **표준 `code` / `message`**로 반환하는 **Python TDD 연습용** 프로젝트입니다. 그래픽 UI·웹·DB 없이 **Boundary(경계)**와 **Domain(순수 로직)**의 Dual-Track TDD로 구현 범위를 맞춥니다.

**문서 관계(한 줄):** Report 1~4·Cursor 규칙과 정렬된 요구사항 베이스라인이 `docs/`의 PRD에 수록되어 있으며, 그 근거와 산출 과정은 [`Report/5.PRD_Authoring_Docs_Baseline_Report.md`](Report/5.PRD_Authoring_Docs_Baseline_Report.md)에 정리되어 있습니다.

---

## 문서 가이드

| 목적 | 참고 문서 |
|------|------------|
| **본문·To-Do·검증 기준(원천)** | [`docs/5.PRD_MagicSquare_4x4_TDD.md`](docs/5.PRD_MagicSquare_4x4_TDD.md) — FR-01~05, AC, §8 U-/D-, §9 E2E·TQ-01·TQ-NOSOL, NFR, §12 Traceability |
| **스토리·Epic·여정 표현** | [`Report/4.UserJourney_Epic_to_TechnicalScenario_Report.md`](Report/4.UserJourney_Epic_to_TechnicalScenario_Report.md) |
| **계약·불변조건·오류 코드 요약** | [`Report/2.CleanArchitecture_DualTrack_TDD_Design_Report.md`](Report/2.CleanArchitecture_DualTrack_TDD_Design_Report.md) (PRD §8.1 문구와 문자 단위 정합) |
| **실행 환경·ECB 트리·Cursor·pytest** | [`Report/3.DevelopmentEnvironment_CursorRules_ECB_UserEntity_Report.md`](Report/3.DevelopmentEnvironment_CursorRules_ECB_UserEntity_Report.md), [`pyproject.toml`](pyproject.toml), [`.cursorrules`](.cursorrules), [`.cursor/rules/`](.cursor/rules/) |

---

## 요구사항 요약 (PRD 기준)

- **격자:** 4×4, 셀 값은 `0`(빈칸) 또는 1~16.
- **빈칸:** `0`은 정확히 2칸. 0을 제외한 1~16 **중복 없음**.
- **완성 판정:** 4행·4열·주·부 대각 **10개 선**의 합이 모두 **34**.
- **해:** 누락된 두 수를 두 빈칸에 **최대 두 번의 배치 시도**(소→대, 대→소) 후 성공 시 `int[6]` `[r1,c1,n1,r2,c2,n2]`(좌표 **1-index**), 실패 시 `NO_SOLUTION`.
- **범위 밖(Out of scope):** N×N 일반화, UI/DB, 전수 생성기 등 — PRD §4.2 참고.

---

## 계약 실패: `code` 및 `message` (요약)

문구는 **PRD §8.1** 및 **Report/2** 표와 **문자 단위 동일**해야 합니다.

| `code` | `message` |
|--------|-----------|
| `INVALID_SIZE` | `Grid must be 4x4.` |
| `INVALID_VALUE_RANGE` | `Each cell must be 0 or 1..16.` |
| `INVALID_ZERO_COUNT` | `There must be exactly two zeros (empty cells).` |
| `DUPLICATE_VALUES` | `Values 1..16 must not duplicate (excluding zeros).` |
| `NO_SOLUTION` | `No placement makes a 4x4 magic square with magic sum 34.` |

**검증 순서(BR-10):** `INVALID_SIZE` → `INVALID_VALUE_RANGE` → `INVALID_ZERO_COUNT` → `DUPLICATE_VALUES` (동시 위반 시 위에서부터 우선).

---

## 개발 환경 및 실행

### 사전 요구 사항

- **Python:** 3.10 이상 — [`pyproject.toml`](pyproject.toml)의 `requires-python`과 동일한 인터프리터를 사용합니다.
- **가상 환경(권장 기본):** 프로젝트 루트에서 의존성을 격리합니다. 시스템 전역 `pip`에 패키지를 설치하지 않는 것을 권장합니다.

### 가상 환경 만들기·활성화

프로젝트 루트(`MagicSquare _1004` 등 이 저장소의 최상위)에서:

```bash
python -m venv .venv
```

**활성화**

- **Windows — Git Bash:**

```bash
source .venv/Scripts/activate
```

- **Linux, macOS, WSL(일반적인 Linux용 Python):**

```bash
source .venv/bin/activate
```

- **Windows CMD:**

```cmd
.venv\Scripts\activate.bat
```

- **Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

프롬프트 앞에 `(.venv)`가 보이면 활성화된 상태입니다. 비활성화는 `deactivate`입니다.

### 패키지 설치

가상 환경이 **활성화된 상태**에서, 편집 가능 설치와 개발 의존성(`pytest` 등)을 한 번에 설치합니다.

```bash
python -m pip install --upgrade pip
pip install -e ".[dev]"
```

### 그래픽 UI (PyQt6, 선택)

```bash
pip install -e ".[gui]"
python -m magicsquare
```

### 테스트 실행

```bash
pytest
```

특정 파일·노드만 돌릴 때 예시:

```bash
pytest tests/entity/models/test_user.py -v
pytest -k "test_user" --tb=short
```

### 커버리지(선택, PRD NFR 대비)

PRD는 Domain **≥ 95%**, Boundary **≥ 85%**를 목표로 합니다. 측정에는 `pytest-cov`가 필요합니다(현재 `[project.optional-dependencies].dev`에는 없음).

```bash
pip install pytest-cov
pytest --cov=magicsquare --cov-report=term-missing
```

레이어별로 경로를 나눠 측정하려면 구현 후 `boundary` / `domain` 등 실제 모듈 경로에 맞춰 `--cov` 인자를 조정하면 됩니다.

### TDD·리팩터링 워크플로(요약)

프로젝트 규칙은 **`.cursor/rules/magicsquare-tdd-testing.mdc`**와 PRD §8(Dual-Track)에 맞춥니다.

| 단계 | 할 일 | 하지 말 것 |
|------|--------|------------|
| **RED** | 요구사항을 **실패하는 테스트** 하나로 번역하고, 의도한 이유로 실패하는지 확인한다. | 프로덕션 코드를 먼저 넣어 통과시키기, 실패 원인 불명확한 채 다음 단계로 넘어가기. |
| **GREEN** | 그 테스트를 통과시키는 **최소** 구현만 작성한다. | 이 단계에서 구조 리팩터링·범위 밖 기능 추가. |
| **REFACTOR** | 동작(테스트 결과)은 그대로 두고 이름·중복·ECB 경계 등을 정리한다. | 새 기능·새 공개 동작 추가, 테스트 삭제·약화로만 Green 맞추기. |

**Dual-Track:** Boundary(계약·U- 시리즈)와 Domain(로직·D- 시리즈) 쪽에 **서로 다른 RED**를 두고 같은 스프린트 단위에서 GREEN까지 맞추는 방식을 권장합니다(PRD §8.3).

**리팩터링 시 커버리지:** Cursor 규칙상 리팩터링 후에도 **전체 최소 80%**를 깨지 않도록 유지하는 것을 전제로 합니다(세부 목표는 PRD NFR-01·02).

### 소스 레이아웃·아키텍처

- **코드:** `src/magicsquare/` — `pyproject.toml`의 `pythonpath = ["src"]`로 `pytest`가 패키지를 import합니다.
- **ECB:** 권장 디렉터리·의존성 방향은 **Report/3** 및 **`.cursor/rules/magicsquare-ecb-architecture.mdc`**를 따릅니다.

---

## 검증 기준 (PRD 중심)

구현이 “완료”로 간주되려면 다음을 충족하는 것이 목표입니다(세부 AC·TC-ID는 PRD 본문).

- [ ] **FR-01** 입력 검증(I1~I4): 실패 시 Domain 해 결정 진입점 **0회**(AC-FR-01-01 등).
- [ ] **FR-02** 행 우선 스캔으로 빈칸 두 좌표(AC-FR-02-01~03, TQ-01).
- [ ] **FR-03** 누락 두 수 `{a,b}`(TQ-01 → `{1,6}`, TQ-NOSOL → `{15,16}`).
- [ ] **FR-04** 0 없는 완전 격자에 대한 마방진 판정(AC-FR-04-01~03).
- [ ] **FR-05** 두 시도·`int[6]`·`NO_SOLUTION`·입력 비변형(AC-FR-05-01~04).
- [ ] **§9.3** 착수 전: `TQ-NOSOL`에 대해 두 배치 모두 FR-04가 `false`임을 **자동 테스트로 증명**.
- [ ] **Dual-Track:** §8.1 Boundary 계약 테스트(U-01 등)와 §8.2 Domain 테스트(D-01 등) **병렬** 진행(한 트랙만 끝내지 않기).
- [ ] **NFR-01 / NFR-02:** Domain 라인 커버리지 **≥ 95%**, Boundary **≥ 85%**(도구: `pytest-cov` 등).
- [ ] **NFR-03 / NFR-04:** 결정론·호출자 `grid` 비변형.

Cursor 에이전트·로컬 개발 시 **Red → Green → Refactor** 및 금지 패턴은 **`.cursor/rules/magicsquare-tdd-testing.mdc`**, **`magicsquare-forbidden.mdc`**를 참고합니다.

---

## 구현 To-Do (PRD FR·트랙 정렬)

아래 항목은 [`docs/5.PRD_MagicSquare_4x4_TDD.md`](docs/5.PRD_MagicSquare_4x4_TDD.md)의 기능·테스트 ID와 대응하도록 구성했습니다. 스토리 문맥은 **Report/4**, 컴포넌트 이름·듀얼 트랙 상세는 **Report/2**를 함께 보세요.

### Phase 0 — 기준 데이터·게이트

- [ ] `TQ-01`, `TQ-NOSOL` 픽스처 상수 및 §9.3 자동 검증(두 시도 모두 실패).
- [ ] §12 Traceability에 맞춰 테스트·모듈에 TC-ID / FR 주석(팀 규칙에 맞게).

### Phase 1 — Entity / 보드 표현

- [ ] 4×4 불변(또는 방어적 복사) **Grid** 등 Entity — 외부 리스트 변이와 분리(NFR-04).

### Phase 2 — Track A · Boundary (FR-01)

- [ ] `INVALID_SIZE`, `INVALID_VALUE_RANGE`, `INVALID_ZERO_COUNT`, `DUPLICATE_VALUES` + §8.1 메시지.
- [ ] 무효 입력 시 Domain `resolve` **미호출**(U-01~U-06, AC-FR-01-01).

### Phase 3 — Track B · Domain (FR-02~05)

- [ ] 빈칸 탐색 `EmptyCellLocator`(D-12 등).
- [ ] 누락 두 수 `MissingNumbersResolver`(D-01, AC-FR-03).
- [ ] 완성 판정 `MagicSquareValidator`(D-14, D-13, PI-01).
- [ ] 두 시도 해 찾기 + 내부 `NO_MAGIC_SOLUTION` → Boundary `NO_SOLUTION`(D-11, U-09, AC-FR-05).

### Phase 4 — Control · 진입점 조율

- [ ] 검증 통과 시에만 Domain 호출, 응답 매핑(유스케이스 / Control 레이어).
- [ ] 공개 API: `int[][]` / `list[list[int]]` 수용, 성공 시 `int[6]`.

### Phase 5 — E2E·품질

- [ ] §9.1 E2E-OK-01, E2E-NO-01, E2E-ERR-01~04.
- [ ] PI-01~03, NFR-03 반복 실행, NFR-01·02 커버리지 게이트(CI 권장).

---

## 현재 저장소 상태

- **패키지:** `magicsquare` (`src/magicsquare/`) — ECB 예시로 **User** 엔티티 및 테스트가 일부 포함되어 있습니다(**Report/3** 참고). Magic Square 본 기능은 PRD에 맞추어 위 To-Do대로 확장하면 됩니다.

---

## 라이선스

미정 — 필요 시 `LICENSE` 파일을 추가하세요.
