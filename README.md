# pyhon_DataStructure
<<<<<<< HEAD
## 01时间复杂度
### 若a+b+c=1000,且a^2+b^2=c^2(a,b,c为自然数)，如何求出所有a、b、c的组合？两种解法的程序执行时间差别巨大
### 机器执行时间=基本运算数量*每个基本步骤执行的时间
### 时间复杂度:假设存在函数g，使得算法A处理规模为n的问题示例所用时间为T(n)=0(g()),则称(n)为算法A的渐近时间复杂度，简称时间复杂度，记为T(n)
### 例如：枚举法中有三个for循环，每个for循环执行次数是1000次，if执行1次，print执行一次，则T(n)=N^3+2。
### 时间复杂度的几条基本计算规则
#### 1.基本操作，即只有常数项，认为其时间复杂度为0(1)
#### 2.顺序结构，时间复杂度按加法进行计算
#### 3.循环结构，时间复杂度按乘法进行计算
#### 4.分支结构，时间复杂度取最大值
#### 5.判断-个算法的效率时，往往只需要关注操作数量的最高次项，其它次要项和常数项可以忽略
#### 6.在没有特殊说明时，我们所分析的算法的时间复杂度都是指最坏时间复杂度
### 时间复杂度比较：O(1) < O(logn) < O(n) < O(nlogn) < O(n^2) < O(n^3) < O(2^n) < O(n!) < O(n^n)
### 函数是对基本步骤的封装，其复杂度要看函数体里面的基本操作数，例如比较list.append()和list.insert()的时间效率。
## 02Python内置类型性能分析
### timeit模块
### timeit模块可以用来测试一小段Python代码的执行速度。
### class timeit. Timer(stmt='pass', setup='pass', timer= <timer function>)
### Timer是测量小段代码执行速度的类。
### stmt参数是要测试的代码语句(statment) ;
### setup参数是运行代码时需要的设置;
### timer参数是一个定时器函数， 与平台有关。
### timeit.Timer.timeit(number=1000000)
### Timer类中测试语句执行速度的对象方法。number参 数是测试代码时的测试次数，默认为1000000次。 方法
### 返回执行代码的平均耗时，一个float类 型的秒数。
### list内置操作的时间复杂度


| Operation | Big-O Efficiency|
| ------ | ------ |
| indexx[] | O(1) |
| index assignment | O(1) |
| append | O(1)|
| popO | O(1) |
| pop(i) | O(n)|
| insert(i,item)| O(n)|
| del operator | O(n)|
| iteration | O(n)|
| contains (in) | O(n)|
| get slice [x:) | O(k)|
| del slice | O(n)|
| set slice | O(n+ k)|
| reverse | O(n)|
| concatenate | O(k)|
| sort | O(n logn)|
| multiply | O(nk)

### dict内置操作的时间复杂度
| Operation | Big-O Efficiency|
| ------ | ------ |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |

=======
>>>>>>> 60593db7f464e2c7c0f6a88b87b4b445a586ce79
#python_DataStructure
