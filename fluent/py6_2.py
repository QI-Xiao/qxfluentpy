from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')


class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order: # 上下文
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


promos = []


def promotion(promo_func):
    promos.append(promo_func)
    return promo_func

@promotion
def fidelity_promo(order):
    """为积分为1000或以上的顾客提供5%折扣"""
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0

@promotion
def bulk_item_promo(order):
    """单个商品为20个或以上时提供10%折扣"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount

@promotion
def large_order_promo(order):
    distinct_items = {item.product for item in order.cart} # 这里用 set 去重
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0


def best_promo(order):
    return max(promo(order) for promo in promos)


joe = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1100)

cart = [
    LineItem('banana', 4, .5),
    LineItem('apple', 10, 1.5),
    LineItem('watermellon', 5, 5.0)
]
banana_cart = [LineItem('banana', 30, .5), LineItem('apple', 10, 1.5)]
long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]

print(
    Order(joe, cart, fidelity_promo),
    Order(ann, cart, fidelity_promo),
    Order(joe, banana_cart, bulk_item_promo),
    Order(joe, long_order, large_order_promo),
    Order(joe, cart, large_order_promo)
)

promos = [fidelity_promo, bulk_item_promo, large_order_promo]


def best_promo(order):
    return max(promo(order) for promo in promos)

# print(globals())
promos2 = [globals()[name] for name in globals() if name.endswith('_promo') and name != 'best_promo']
print(promos2)

print(best_promo)