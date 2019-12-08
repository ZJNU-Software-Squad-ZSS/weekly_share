"""
    数据结构：字典
"""
# 字典,键和值联系在一起，键必须是唯一的。字典是dict类的实例/对象
ab = {'Swaroop': 'swaroop@byteofpythyon.info',
      'Larry': 'larry@wall.org',
      'Mark': 'mark@163.com',
      'Spammer': 'spammer@hotmail.com'}

print("Swaroop's address is %s" % ab['Swaroop'])
ab['Mark']='Mark@163.com'
# add a key/value pair
ab['Lily'] = 'lily@python.org'
# delete a key/value pair
del ab['Spammer']
print('\nThere are %d contacts in the address-book\n' % len(ab))
for name, address in ab.items():  # 使用字典的items方法来使用字典中的每一个键/值对
    print('Contact %s at %s' % (name, address))


