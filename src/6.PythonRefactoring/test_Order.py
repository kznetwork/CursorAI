# from decimal import Decimal
# from Models import User, Menu
# from CodeSmell import calculate_order_total  # 실제 함수 import
#
# def test_calculate_order_total_with_discount():
#     user = User(id=1, name="홍길동")
#     menu = Menu(id=1, name="아메리카노", price=Decimal("4500"))
#
#     total = calculate_order_total(user, menu, quantity=3)
#
#     assert total == Decimal("12150")  # 13,500 * 0.9 = 12,150

# ======================================================================================

from decimal import Decimal
from Models import User, Menu
from CodeSmell import calculate_order_total  # 실제 함수 import

def test_calculate_order_total_with_discount():
    user = User(id=1, name="홍길동")
    menu = Menu(id=1, name="아메리카노", price=Decimal("4500"))

    total = calculate_order_total(user, menu, quantity=3)

    assert total == Decimal("12150")  # 13,500 * 0.9 = 12,150
