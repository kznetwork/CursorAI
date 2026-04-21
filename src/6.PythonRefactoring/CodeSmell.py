# def p(u, m, q):  # 의미 없는 변수명
#     if u and m:
#         t = m.price * q
#         if t > 10000:  # 매직 넘버
#             t = t * 0.9
#         return t
#     return 0

# ======================================================================================

# from decimal import Decimal
#
# from Models import User
# from Models import Menu
#
#
# def calculate_order_total(user: User, menu: Menu, quantity: int) -> Decimal:
#     """주문 총액 계산 (10,000원 이상 10% 할인)"""
#     DISCOUNT_THRESHOLD = Decimal("10000")
#     DISCOUNT_RATE = Decimal("0.9")
#
#     if not user or not menu:
#         raise ValueError("User and Menu are required")
#     subtotal = menu.price * quantity
#
#     if subtotal >= DISCOUNT_THRESHOLD:
#         return subtotal * DISCOUNT_RATE
#     return 0

# ======================================================================================

# from decimal import Decimal
#
# from Models import User
# from Models import Menu
#
#
# def calculate_order_total(
#         user: User,
#         menu: Menu,
#         quantity: int,
#         discount_threshold: Decimal = Decimal("10000"),
#         discount_rate: Decimal = Decimal("0.9")
# ) -> Decimal:
#     """주문 총액 계산
#
#     Args:
#         user: 주문 사용자
#         menu: 주문 메뉴
#         quantity: 수량
#         discount_threshold: 할인 기준 금액
#         discount_rate: 할인율
#
#     Returns:
#         Decimal: 최종 주문 금액
#
#     Raises:
#         ValueError: user 또는 menu가 None인 경우
#     """
#     if not user or not menu:
#         raise ValueError("User and Menu are required")
#
#     subtotal = menu.price * quantity
#
#     if subtotal >= discount_threshold:
#         return subtotal * discount_rate
#
#     return subtotal

# ======================================================================================

# from decimal import Decimal
#
# from Models import User
# from Models import Menu
#
#
# def calculate_order_total(user: User, menu: Menu, quantity: int) -> Decimal:
#     """주문 총액 계산 (10,000원 이상 10% 할인)"""
#     DISCOUNT_THRESHOLD = Decimal("10000")
#     DISCOUNT_RATE = Decimal("0.9")
#
#     if not user or not menu:
#         raise ValueError("User and Menu are required")
#     subtotal = menu.price * quantity
#
#     if subtotal >= DISCOUNT_THRESHOLD:
#         return subtotal * DISCOUNT_RATE
#     return 0

# ======================================================================================

from decimal import Decimal
from typing import Optional
from Models import User, Menu


def calculate_order_total(
        user: User,
        menu: Menu,
        quantity: int,
        discount_threshold: Decimal = Decimal("10000"),
        discount_rate: Decimal = Decimal("0.9")
) -> Decimal:
    """주문 총액 계산

    Args:
        user: 주문 사용자
        menu: 주문 메뉴
        quantity: 수량
        discount_threshold: 할인 기준 금액
        discount_rate: 할인율

    Returns:
        Decimal: 최종 주문 금액

    Raises:
        ValueError: user 또는 menu가 None인 경우
    """
    if not user or not menu:
        raise ValueError("User and Menu are required")

    subtotal = menu.price * quantity

    if subtotal >= discount_threshold:
        return subtotal * discount_rate

    return subtotal
