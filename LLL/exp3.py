"""
    数据结构：列表、元祖和字典
"""
# 列表list：处理一组有序项目的数据结构。项目应该包括在方括号中，每个项目之间用逗号分割，python以0开始计数
shoplist = ['apple', 'mango', 'carrot', 'banana']
print('I have', len(shoplist), 'items to purchase.')
print('These items are:')
for item in shoplist:
    print(item)

print('I also have to buy rice.')
shoplist.append('rice')  # append在列表尾添加一个项目
print('My shopping list is now', shoplist)

print('I will sort my list now.')
shoplist.sort()  # sort影响列表本身
print('Sorted shopping list is', shoplist)

print('The first item I will buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0]  # del语句删除列表元素
print('I bought the', olditem)
print('My shopping list is now', shoplist)

shoplist[0] = 'bana'
print('My shopping list is', shoplist)

print(help(list))

# 元祖，不可变。通过圆括号中用逗号分割的项目定义
zoo = ('wolf', 'elephant', 'penguin')
print('Number of animals in the zoo is', len(zoo))
new_zoo = ('monkey', 'dolphin', zoo)
print('Number of animals in the new zoo is', len(new_zoo))
print('ALL animals in the new zoo are', new_zoo)
print('Animals bought from old zoo are', new_zoo[2])
print('Last animal bought from old zoo is', new_zoo[2][2])

# 含有0个或者1个项目的元祖
myempty = ()
singleton = (2,)  # 单个元素的元祖必须在第一个项目后跟一个逗号，来区分元祖和表达式中一个带圆括号的对象

age = 22
name = 'Swaroop'
print('%s is %d years old' % (name, age))  # print语句可以使用跟着%符号的项目元祖的字符串，必须按照相同的顺序来定制
print('Why is %s playing with that python?' % name)
