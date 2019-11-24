def sayhi():
    print('Hi, this is module1 speaking.')


version = '0.1'

print(__name__)

if __name__ == '__main__':
    print('The program is being run by itself\n')
    print(__name__)
else:
    print('I am being imported from another module\n')
    print(__name__)