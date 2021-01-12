# coding=utf-8
# 利用特殊方法，可以让自定义对象通过加号进行运算

# 实现一个二维向量（vector）类
# 1.
# abs 是一个内置函数，如果输入是整数或者浮点数，它返回的是输入值的绝对值；如果输入是复数（complex number），那么返回这个复数的模。
# 为了保持一致性，在碰到 abs 函数的时候，也应该返回该向量的模
# 2.
# 还可以利用 * 运算符来实现向量的标量乘法（即向量与数的乘法，得到的结果向量的方向与原向量一致，模变大）

from math import hypot


class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # 1.
    # repr，它能把一个对象用字符串的形式表达出来以便辨认，这就是“字符串表示形式”
    # repr 就是通过 __repr__ 这个特殊方法来得到一个对象的字符串表示形式的。
    # 在 __repr__ 的实现中，用到了 %r 来获取对象各个属性的标准字符串表示形式
    # 因为 Vector(1, 2) 和 Vector('1', '2') 是不一样的
    # __repr__ 和 __str__ 的区别在于，后者是在 str() 函数被使用，
    # 或是在用 print 函数打印一个对象的时候才被调用的，并且它返回的字符串对终端用户更友好。
    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    # 2.

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)




