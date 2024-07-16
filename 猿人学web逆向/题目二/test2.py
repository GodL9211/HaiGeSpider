from functools import partial


def apply_discount(price, discount_rate):
    return price * discount_rate


# 电子产品折扣率
electronics_discount = partial(apply_discount, discount_rate=0.95)
# 服装折扣率
clothing_discount = partial(apply_discount, discount_rate=0.9)
# 图书折扣率
books_discount = partial(apply_discount, discount_rate=0.85)


def calculate_discounted_price(cart_items, discount_func):
    total_price = sum(item['price'] * item['quantity'] for item in cart_items)
    return discount_func(total_price)


# 示例购物车商品
cart_items = [
    {'name': 'Laptop', 'category': 'electronics', 'price': 1200, 'quantity': 1},
    {'name': 'Jeans', 'category': 'clothing', 'price': 200, 'quantity': 2},
    {'name': 'Python Book', 'category': 'books', 'price': 50, 'quantity': 3},
]

# 根据商品类别应用折扣
discounted_price_electronics = calculate_discounted_price(
    [item for item in cart_items if item['category'] == 'electronics'],
    electronics_discount
)

discounted_price_clothing = calculate_discounted_price(
    [item for item in cart_items if item['category'] == 'clothing'],
    clothing_discount
)

discounted_price_books = calculate_discounted_price(
    [item for item in cart_items if item['category'] == 'books'],
    books_discount
)

print(f"Discounted Price for Electronics: {discounted_price_electronics}")
print(f"Discounted Price for Clothing: {discounted_price_clothing}")
print(f"Discounted Price for Books: {discounted_price_books}")
