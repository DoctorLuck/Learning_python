# -*- coding:utf-8 -*-
# 2017-7-18
# DoctorLuck

# 斐波那契数列
fibs=[0,1]
for i in range(8):
    fibs.append(fibs[-2]+fibs[-1])
print(fibs)
# 用户输入数字范围
fibs=[0,1]
x=int(input("Input num:"))
# x=input("Input num:")   #返回的是一个字符串，需要将其转换为数值
x=int(input("Input num:"))
for i in range(x):
    fibs.append(fibs[-2]+fibs[-1])
print(fibs)
# 创建一个函数
def hello(name):
    return 'hello '+name+'!'
print(hello('ldq'))
# 文档化函数
# 如果在函数的开头写下字符串，它就会作为函数的一部分进行存储，这称作文档字符串
def hello(name):
    '打印hello ...'
    return 'hello '+name+'!'
print(hello('ldq'))
print(hello.__doc__)    #获取文档字符串
print(help(hello))      #help(函数名) 可以获取函数的相关信息

# 参数
# 在函数内部对参数进行的修改，不会影响外部的变量
def change(name):
    name='changed name'
name='ldq'
change(name)
print(name)
# 注意别的数据类型
# 当在序列上做切片的时候，返回的切片是一个副本。
storage={}
def init(data):
    data['first']={}
    data['middle']={}
    data['third']=[]
init(storage)
print(storage)

# 当从函数返回多个值时，以元组的形式返回


# 关键字参数：提供参数名的参数

# 可传多个位置参数
def print_params(*params):
    print(params)
print_params('ldq','zhang','haha')  #注意运行结果是一个元组
# 运行结果
# ('ldq', 'zhang', 'haha')

# 传多个关键字参数
def print_params2(**params):
    print(params)
print_params2(x=1,y=2,z=3)      #结果为一个字典
# 运行结果
# {'x': 1, 'z': 3, 'y': 2}

# 多种参数混合使用
def print_params(x,y,z=3,*pospar,**keypar):
    print(x,y,z)
    print(pospar)
    print(keypar)
print_params(1,2,3,4,5,6,foo=1,bar=2)

# 全局变量：global x

# recursion 递归



