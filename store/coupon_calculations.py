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


if __name__ == '__main__':
    pass
