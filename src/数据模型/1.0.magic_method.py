# coding=utf-8
from random import choice
from collections import namedtuple

# namedtuple 主要用于构建只有少数属性但是没有方法的对象
Card = namedtuple('Card', ['rank', 'suit'])


class FrenchDesk:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suit = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suit for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]


deck = FrenchDesk()

# 1.
# len()
# FrenchDesk 和标准python集合类型一样可以使用 len() 函数查看长度，即有多少张牌
# 2.
# slice
# 也可以通过 slicing 操作获取特定牌 deck, deck[0] 和 deck[-1] 分别获取第一张和最后一张
# 3.
# 随机取牌
# noinspection PyTypeChecker
choice(deck)
# 4.
# 也是可以迭代的
# for card in deck:
#   print(card)
# 5.
# 反向迭代也没有问题
# noinspection PyTypeChecker
# for card in reversed(deck):
#     print(card)

# 迭代通常是隐式的，譬如一个集合类型没有实现 __contains__ 方法，那么使用 in 运算符就会按照顺序做一次迭代搜索
assert Card('Q', 'hearts') in deck

# 实现排序
# 算入花色
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card_):
    rank_value = FrenchDesk.ranks.index(card_.rank)
    return rank_value * len(suit_values) + suit_values[card_.suit]


# 升序排序
for card in sorted(deck, key=spades_high):
    print(card)

# FrenchDesk 是隐式的继承了 object 类，通过 __len__ 和 __getitem__两个特殊方法，基本实现了和 python
# 只有序列数据类型一样的特性，例如迭代和切片，也可以使用标准库中 random.choice reversed sorted 等内置函数

# 首先明确一点，特殊方法的存在是为了被 Python 解释器调用的，你自己并不需要调用它们。
# 在执行 len(my_object) 的时候，如果 my_object 是一个自定义类的对象，那么 Python 会自己去调用其中由你实现的 __len__ 方法。
# 然而如果是 Python 内置的类型，比如列表（list）、字符串（str）、字节序列（bytearray）等，那么 CPython 会抄个近路，
# __len__ 实际上会直接返回 PyVarObject 里的 ob_size 属性。PyVarObject 是表示内存中长度可变的内置对象的 C 语言结构体。
# 直接读取这个值比调用一个方法要快很多。
# 很多时候，特殊方法的调用是隐式的，比如 for i in x: 这个语句，背后其实用的是 iter(x)，而这个函数的背后则是 x.__iter__() 方法。
# 当然前提是这个方法在 x 中被实现了。
