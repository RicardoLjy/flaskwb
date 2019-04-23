r'''
    自定义一个绝对值函数my_abs python内置绝对值函数abs带有参数检查
'''
def my_abs(x):
r'''
python内置绝对值函数abs带有参数检查，故此自定义函数也需要添加一个函数检查，
可以用内置函数isinstance()实现，只允许整数和浮点数类型的参数
'''
    if not isinstance(x,(int,float)):
        raise TypeError('此处添加错误提示')
    if x >= 0:
        return x
    else:
        return -x
