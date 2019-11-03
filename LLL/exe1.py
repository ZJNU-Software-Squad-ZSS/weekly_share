from twisted.python.compat import raw_input

"""
    字符串，不可变
    """
# ''与""用法相同
print('hello world')
print("hello World")

# '''与"""可以指示多行的字符串，在三引号里面可以自由的使用单引号和双引号
e = '''hello pip "install" flask'!' '''
print(e)

# 转义符\
print('What\'s your name')
print("What's your name")
# 行末\表示在下一行继续,不是开始新的行
print("This is one." \
      "This is two.")
print("This is one."
      "This is two.")
print("This is one.\
This is two.")
print('''This is one.
This is two.''')

# 自然字符串，指示某些不需要如转义符那样特别处理的字符串。加前缀r或者R
# 正则表达式一定要使用自然字符串
print(r"Newlines are indicated by \n")

# Unicode字符串，书写国际文本的标准方法。加前缀u或者U
# 处理文本文件的时候用Unicode字符串，特别是文件含有非英语语言的文本
print(u"This is 中国")

# 按字面意义级连字符串
print('What\'s''your name?')  # 这只是将两个字符串拼接
print('What\'s', 'your name?')  # 自动转成What's your name?


"""
    标识符
    """
# 第一个字符必须是字母表的字符（大小写）或者下划线('_')
# 其他部分可以由字母、下划线、数字组成
# 区分大小写


'''
    分号；
    '''
# 分号表示一个逻辑行/语句的结束，可以用但是避免使用分号
i = 5
print(i)

i = 5;
print(i);
# i = 5;print(i);
# i = 5;print(i)
# 可以并排，但是不推荐，且python会要求你format


'''
    控制流，冒号结尾
    '''
# if..elif..else
number = 23
guess = int(raw_input('Enter an integer: '))  # raw_input将字符串打在屏幕上，等待用户输入

if guess == number:
    print('''Congratulation!
    (but you don't win any prizes!)''')
elif guess < number:
    print('No, it is a little higher than that')
else:
    print('No, it is a little lower than that')
print('Done')

# while循环,有一个可选的else从句
number = 23
running = True

while running:
    guess = int(raw_input('Enter an integer: '))  # raw_input将字符串打在屏幕上，等待用户输入

    if guess == number:
        print('''Congratulation!
        (but you don't win any prizes!)''')
    elif guess < number:
        print('No, it is a little higher than that')
    else:
        print('No, it is a little lower than that')
        running = False
    print('Done')
else:
    print('You are loser!')

# for..in循环,使用于任何种类、任何对象的序列
for i in range(1, 5):  # range左闭右开为[1,2,3,4]; range(1,5,2)中2为步长,为[1,3]
    print(i)
else:
    print('The for loop is over!')

# break语句，如果你从for或while循环中终止，任何对于的循环else将不执行
# continue语句，跳过该循环，进行下一轮循环



