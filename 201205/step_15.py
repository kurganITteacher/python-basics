DISCOUNT = 15


def apply_discount(price, discount):
    return price * (100 - discount) / 100


# def discount_product(price):
#     pass


basket = [5985.58, 4789.6, 14593.5, 4751.3]
basket_sum = sum(basket)
print(basket_sum)

basket_sum_discounted = 0
discount_1 = 7
for product in basket:
    # print(product, apply_discount(product, 15))
    # basket_sum_discounted = basket_sum_discounted + apply_discount(product, discount_1)
    basket_sum_discounted += apply_discount(product, discount_1)
print(basket_sum_discounted)
# print(basket_sum * (100 - discount_1) / 100)
