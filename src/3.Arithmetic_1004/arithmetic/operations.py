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
