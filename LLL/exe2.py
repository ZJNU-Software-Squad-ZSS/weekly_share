'''
    函数
    '''


# def定义函数，冒号结尾
def sayHello(e):
    print(e + ', Hello World!')  # e为局部变量，与函数外具有相同名称的其他变量没关系
    global name  # global定义全局变量，可指定多个全局变量，如global a,b,c
    name = 'Bian'
    print(name + ', Hello World!')


def say(message, times=1):  # 其中times，如果用户没有提供times的值，它的默认参数值为1； 申明形参时，有默认参数值的形参必须放在末尾
    print(message * times)


def func(a, b=5, c=10):
    print('a is', a, 'b is', b, 'c is', c)
    return None  # 每个函数结尾都暗含该语句，None表示没有任何东西的特殊类型


def maximum(a, b):
    if a > b:
        return a
    else:
        return b


def someFunc():
    pass        # pass语句表示一个空的语句块


def printMax(x, y):
    # 文档字符串，DocStrings，适用于模块和类
    # 惯例：一个多行字符串，首行以大写字母开始，句号结尾；第二行是空行；第三行开始是详细的描述
    """Prints the maximum of two numbers.

    The two values must be integers."""
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is the maximum')


e = 'Lisa'
name = 'Wang'
sayHello('John')
print(name)

say('Hello')
say('Baek', 5)

# 关键参数，使用名字来给函数指定实参，而不是位置
# 优势：1.不必担心参数顺序 2.假设其他参数都有默认值，我们可以只给我们想要的那些参数赋值
func(3, 7)
func(25, c=24)
func(c=50, a=100)

someFunc()
print(maximum(3, 7))

printMax(3, 5)
print(printMax.__doc__)     # 调用函数的文档字符串属性
help(printMax)      # 抓取函数的doc属性
