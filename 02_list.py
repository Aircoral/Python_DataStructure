#coding = utf-8
#list 操作测试
from timeit import Timer
# 两个list相加操作
# li1 = [1,2]
# li2 = [23,5]
# #产生新的列表三种方法
# #1.两个列表相加
# li = li1 + li2
# #2.列表生成器
# li = [i for i in range(10000)]
# #3.将range（10000）转换成列表
# li = list (range(10000))

def test1():
    li = []
    for i in range (10000):
        li.append(i)

def test2():
    li = []
    for i in range (10000):
        li = li+[i]   #li +=[i]在时间复杂度上优于前者，和append操作相当。

def test3():
    li =[i for i in range(10000)]

def test4():
    li = list(range(10000))

def test5():
    li = []
    for i in range(10000):
        li.extend(i) #extend与+操作的区别是：+操作产生新list，extend在原列表进行操作，接收列表或可遍历对象，append只能添加一个元素

#构造测算timer类
timer1 = Timer("test1()", "from __main__ import test1") #传参数时只接受字符串，不能传函数名
print("append:", timer1.timeit(1000))

timer2 = Timer("test2()", "from __main__ import test2") #传参数时只接受字符串，不能传函数名
print("+:", timer2.timeit(1000))

timer3 = Timer("test3()", "from __main__ import test3") #传参数时只接受字符串，不能传函数名
print("[i for i in range:]", timer3.timeit(1000))

timer4 = Timer("test4()", "from __main__ import test4") #传参数时只接受字符串，不能传函数名
print("list(range():", timer4.timeit(1000))

timer5 = Timer("test5()", "from __main__ import test5") #传参数时只接受字符串，不能传函数名
print("extend:", timer4.timeit(1000))
#执行结果：
# append: 1.244506514
# +: 199.144434223
# [i for i in range:] 0.453316424999997
# list(range(): 0.20962478900000292
# extend: 0.20680837499998006


def test6():
    li = []
    for i in range(10000):
        li.append(i)#append只往表尾加

def test7():
    li = []
    for i in range(10000):
        li.insert(0, i) #0代表往列表头追加

timer6 = Timer("test6()", "from __main__ import test6") #传参数时只接受字符串，不能传函数名
print("append:", timer6.timeit(1000))

timer7 = Timer("test7()", "from __main__ import test7") #传参数时只接受字符串，不能传函数名
print("insert:", timer7.timeit(1000))

#执行结果：
# append: 1.004758061
# insert: 28.37967281
