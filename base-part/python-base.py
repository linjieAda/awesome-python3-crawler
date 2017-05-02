# _*_ coding: utf-8 _*_

"""类型和运算----类型和运算----类型和运算----类型和运算----类型和运算----类型和运算----类型和运算----类型和运算----类型和运算----类型和运算----类型和运算"""

# -- 寻求帮助
class Obj(object):

    def __init__(self, name):
        self.name = name

    def study(self):
        print('%s is like study' % self.name)
dir(Obj)
help(Obj.study)

# --测试类型
L = [1,2,3]
if isinstance(L, list):
    print('L is list')

#-- 整数可以利用bit_length函数测试所占的位数
a = 1
b = 1024
print(a.bit_length(), b.bit_length())

#--
