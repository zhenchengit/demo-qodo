"""Checkout rules:
- SAVE10 gives 10% off orders of at least $100.
- Tax is 10% of the amount after discount.
"""


def checkout(subtotal, coupon=None):
    discount = 0

    if coupon == "SAVE10" and subtotal > 100:
        discount = subtotal * 0.10

    tax = subtotal * 0.10
    return round(subtotal - discount + tax, 2)


print(checkout(100, "SAVE10"))
print(checkout(200, "SAVE10"))
