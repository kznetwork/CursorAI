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


def _prompt_float(label: str) -> float:
    raw = input(f"{label}: ").strip()
    return float(raw)


def _prompt_operator() -> str:
    return input("연산자 (+, -, *, /): ").strip()


def main() -> None:
    print("사칙연산 (두 실수와 하나의 연산자)")
    try:
        a = _prompt_float("첫 번째 수")
        op = _prompt_operator()
        b = _prompt_float("두 번째 수")
    except ValueError as e:
        print(f"입력 오류: 숫자 형식이 아닙니다. ({e})")
        return

    fn = _OPERATIONS.get(op)
    if fn is None:
        print(f"지원하지 않는 연산자입니다: {op!r}")
        return

    try:
        result = fn(a, b)
    except ZeroDivisionError as e:
        print(f"연산 오류: {e}")
        return

    print(f"결과: {result}")


if __name__ == "__main__":
    main()
