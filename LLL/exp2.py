"""
    模块: 一个包含了所有你定义的函数和变量的文件，以.py为扩展名
    """
# 标准库模块
# sys模块
import sys  # sys是system的缩写

print('The command line arguments are:')
for i in sys.argv:  # sys.argv变量是一个字符串的列表，包含命令行参数的列表。
    print(i)  # 执行python exp2.py we are students时，sys.argv[0]='exp2.py',sys.argv[1]='we'...

print('\n\nThe PYTHONPATH is', sys.path, '\n')  # sys.path包含输入模块的目录名列表

# 字节编译的文件，以.pyc作为扩展名，以便输入模块更加快一点

# from...import 语句
# 如果想直接输入argv变量 或 所有sys模块使用的名字
from sys import argv
from sys import *


# 模块的name,每个模块都有自己的name，如果是main说明这个模块被用户单独运行
if __name__ == '__main__':
    print('The program is being run by itself\n')
else:
    print('I am being imported from another module\n')


# 创建自己的模块module1.py,在同一个目录里，或者在sys.path所列目录之一
import module1

module1.sayhi()
print('Version', module1.version)

from module1 import *

sayhi()
print('Version', version)


# dir函数，来列出模块定义的标识符。标识符有函数、类和变量
print(dir(sys))
print(dir(module1))
# print(dir())    # 返回当前模块的属性列表
a = 5
print(dir())