"""
Program: coupon_calculations.py
Author: Michael Skyberg, mskyberg@dmacc.edu
Last date modified: June 2020
Purpose: demonstrate the use of a nested if statement
"""

SALES_TAX = 0.06


# calculate the order total
def calculate_price(price, cash_coupon, percent_coupon):
    # calculate total with cash_coupon
    item_total = price - cash_coupon
    # calculate total with percent_coupon
    item_total = (1 - (percent_coupon/100)) * item_total
    # calculate total with shipping cost
    item_total += get_shipping_cost(item_total)
    # calculate total with tax
    item_total = (1 + SALES_TAX) * item_total
    return item_total


# get the shipping cost based on total price
def get_shipping_cost(price):
    if price < 10:
        return 5.95
    elif 10 <= price < 30:
        return 7.95
    elif 30 <= price < 50:
        return 11.95
    elif 50 <= price:
        return 0
    else:
        return 0


if __name__ == '__main__':
    cost = input("Enter Cost Of Product:")
    c_coupon = input("How Much Cash Coupon? $5 or $10:")
    p_coupon = input("How Much Percentage Coupon? 10%, 15%, 20%:")

    total = calculate_price(float(cost), int(c_coupon), int(p_coupon))
    print(f'Your Order Total Is ${total:.2f}')
