# -*- coding: utf-8 -*-
# Guido van Rossum
print("1 / 1 is {}".format(1/1))
print("1 / 2 is {}".format(1/2))
print("1 // 2 is {}".format(1//2))
print("3/2 is {}".format(3.0/2.0))
print("3//2 is {}".format(3//2))
print("3//2 is {}".format(3.0//2.0))
# "/"是普通的除法运算
# "//"是整除法，就算是浮点数，结果也为整数

print("3%2 is{}".format(3%2))
# "%"是取余运算
print("2 ** 3 is {}".format(2**3))
# 变量名可以包含数字，字母，下划线。变量不能以数字开头。
time=input("Input time:")
print(time)
print(type(time))   #验证通过input()获取到的是一个字符串，所以当需要进行数值操作时，应该先转换为数值类型
print("pow(2,3) is {}".format(pow(2,3,6)))  #第一个参数x,第二个参数y，第三个参数z。pow（）是求x的y次幂，第三个参数z是可选的，如果有，则是用前面
# 求出的数值，对z求余数。
# round()会将浮点数四舍五入为最接近的整数
print("round(5.4) is {} ".format(round(5.4)))
print("round(5.5) is {} ".format(round(5.5)))
print("round(5.6) is {} ".format(round(5.6)))
import math
print(math.sqrt(9)) #用于求一个数的平方根
str1='liu dongqing'
str2=' is 20 years old'
print(str1)
print(str2)
print(str1+str2) #拼接字符串
print(str1*5)   #打印出5个str1
print("hello"+"world")
name=input('input name:')
print("hello" + name)
# 当需要写一个很长的字符串，并且需要跨行时，可以使用'''，即三引号。
# 原始字符串对于反斜线不会特殊对待。在普通字符串中，反斜线的特殊作用：转义
print('C:\nowwhere')    #普通字符串
print(r'C:\nowwhere')   #原始字符串，原始字符串的最后一个字符不能是反斜线。
# print('C:\nowwhere\')     #这种原始字符串是错误的

# 列表and元组
# python有6种内建的序列。列表、元组、字符串、Unicode字符串、buffer对象、xrange对象
# 列表可以修改，而元组不能修改
num=[1,2,3,4,5] #序列
print(num)

# 所有序列都可以进行的操作：索引、分片、加、乘、检查某元素是否属于序列的成员。
# 索引
str='liu dong qing'
print(str[0])   #第一个字符
print(str[-1])  #最后一个字符

# 分片
str='liu dong qing'
print(str[0::])
# str[x:y:z] x是分片的起始位置，y是分片的结束位置（不包含下标为y的元素），z是代表每隔几个元素取一个元素
print(str[0:2:])

# 相加
str1='liu dong qing'
str2='an ya na '
print(str1+str2)
seq1=['a','b','c']
seq2=['d','e','f']
print(seq1+seq2)

# 乘法
print('liu'*5)
print(['a'] * 5)

# 初始化一个长度为10的空列表
seq=[None]*10
print(seq)

# 为了检查某个值是否在序列中，可以使用in运算符
print('a' in 'ldq')   #打印的结果为False
print('a' in 'abc')   #打印的结果为True
print('ab' in 'abc')
# len()返回序列所包含元素的数量，min()和max()分别返回序列中的最大和最小元素

# 因为字符串不能修改，所以通过字符串创建列表时会很有用。
L=list('ldq')
print(L)

List=['a','b','c','d','e']
# 通过以下方式改变列表的值
List[0]='A'
print(List)

# 通过以下方式删除元素
del List[0]
print(List)

# 分片赋值
List[0:2]=list("AB")
print(List)

lang='Python'
Lang=list(lang) #此处要先将字符串转换为列表，因为字符串不可修改。
Lang[1:]='erl'
print(Lang)

# 列表方法
List=[1,2,3,1]
List.append(4) #向列表末尾添加新的对象
print(List.count(1)) #用于统计某个元素在列表中出现的次数
List.extend([5,6,7])    #用于向一个列表之后添加另一个序列。
print(List.index(2))    #从列表中查找出某个值第一个匹配项的位置
List.insert(3,'insert') #向列表指定位置添加一个元素
List.pop()#移除列表的一个元素，并且返回该元素的值。如果给了参数，则删除该位置的元素
print(List)
List.reverse()  #将列表元素反向存放
print(List)

List.remove(1) #移除列表中某个值得第一个匹配项
print(List)
List=[6,5,7,9,4]
List.sort() #将列表元素进行排序
print(type(List.sort()))    #验证List.sort()返回值为None
print(List)


# 元组，不可变序列
Tuple=(1,2,3)
print(Tuple)
# 只有一个元素的元组
Tuple2=(1,)
print(Tuple2)

# 字符串
str='abcdefghijklmn'
print(str.find('gh'))       #在一个字符串中查找子串。返回子串位置的左端索引。可以有第二个参数注明起始点，第三个参数注明终止点。
seq=['1','2','3','4']
sep='+'
print(sep.join(seq))
str='ABCDFGH'
lowstr=str.lower()  #返回字符串的小写字母版
print(lowstr)
str='acvfdgfd'
tstr=str.title()    #返回字符串的大写字母版
print(tstr)

import string
str='liu dong qing '
capstr=string.capwords(str)   #首字母大写
print(capstr)

str='This is a test string'
restr=str.replace('is','replace') #替换字符串中的匹配项
print(restr)

str='1+2+3+4'
print(str.split('+'))

str.strip()#去除字符串两边的空格


# 创建字典
dictionary={'name':'liudongqing','age':19}
# 键必须是不可变对象
# 可以用dict(),通过其他映射或者键值的序列创建字典
items=[('name','liudongqing'),('age','19')]
d=dict(items)
print(d)

# clear方法，清除字典中的所有项
d={'name':'liudongqing','age':19}
print(d)
d.clear()
print(d)
print(type(d.clear()))      #验证d.clear()无返回值

d1={'name':'liudongqing','age':19}
d2=d1.copy()        #这种方式为浅拷贝，当在副本中修改（原地修改，而不是替换），原始的字典会发生改变。
d2['name']='change name'
print(d2)
print(d1)


# 以下为深拷贝
from copy import deepcopy
d={}
d['names']=['ldq','zhang']
c=d.copy()
dc=deepcopy(d)
d['names'].append('append')
print(c)
print(dc)
print(d)

# fromkeys()用来使用给定的键建立新的字典，每个键都对应一个默认的值None
d={}.fromkeys(['name','age'])
print(d)

# *****************************************
# get方法是个更加宽松的访问字典的方法
d={}
print(d['name'])    #此时就会报错
print(d.get('name'))  #通过这种方法，访问一个不存在的键时，会返回一个None，而不是让你的程序报错。当运行此三行代码时，应将第二行注释掉

# *****************************************
d={'name':'ldq','age':'19','hobby':'baketball'}
print(d.items())    #d.items()将字典所有的项以列表返回，列表中的每一项都是键值对的形式。
# 结果
# dict_items([('age', '19'), ('name', 'ldq'), ('hobby', 'baketball')])

# 可以直接作用于for循环的对象统称为可迭代对象(Iterable)。
#
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器(Iterator)。

d={'name':'ldq','age':'19','hobby':'baketball'}

