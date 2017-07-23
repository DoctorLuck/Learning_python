import re
# '\d' 表示以为0-9的数字
# '\D'除0到9的数字以外的任何字符。
# '\w' 任何字母，数字或下划线字符。
# '\W'除字母，数字和下划线以外的任何字符

# '\s'可以用来匹配空格
# '*' 0次或多次
# '+' 一次或多次
# '.'通配符
# 用花括号匹配特定次数  {3,} 3次或者多次  {,3}匹配0次到5次
# 向re.compile()传入一个字符串值，表示正则表达式，它将返回一个regex模式对象。
# Regex对象的search()方法查找传入的字符串，寻找该正则表达式的所有匹配。如果匹配到则返回Match对象，否则返回None。Match对象有一个group()方法，返回被查找字符串实际匹配的文本。
# phoneNumberRegex=re.compile(r'\d{3}-\d{4}-\d{4}')
# ma=phoneNumberRegex.search('My number is 157-9768-5592')
# print("Phone number is : {}".format(ma.group()))

# 分组
# phoneNumberRegex=re.compile(r'(\d{3})-(\d{4}-\d{4})')
# ma=phoneNumberRegex.search('My number is 157-9768-5592')
# print(ma.group(0))      #此时与不传入参数一样，返回的是整个匹配的文本
# print(ma.group(1))      #第一组
# print(ma.group(2))      #第二组\
# print(ma.groups())      #获得所有分组
# print(ma.string)
# print(ma.groupdict())
# print(ma.groups())

# '|'称为管道，当希望匹配许多表达式中的一个时，可以使用。
# nameRegex=re.compile(r'l(iu|ang|ai)')
# ma=nameRegex.search('liu and lang and li and lai')
# print(ma.group())

# '?'实现可选匹配
# nameRegex=re.compile(r'[a-z\s]+(like)?[a-z]+')
# ma1=nameRegex.search('liu like you')
# ma2=nameRegex.search('liu disgusting you')
# print(ma1.group())
# print(ma2.group())

# 贪婪模式和非贪婪模式
# python的正则表达式默认是贪婪模式，这以为会尽可能匹配长的字符串。

# Regex对象还有findall()方法。search()返回一个Match对象，包含被查找的字符串的“第一次”匹配的文本。而findall()方法将返回一组字符串，包含被查找
# 字符串中的所有匹配。

# newLineRegex=re.compile('.*')
# print(newLineRegex.search('''I am a boy!
#                           Next Line'''
#                           ).group())

# 通过传入re.DOTALL作为re.compile()的第二个参数，可以让'.'匹配所有字符，包括换行符。
# newLineRegex=re.compile('.*',re.DOTALL)
# print(newLineRegex.search('''I am a boy!
#                           Next Line'''
#                           ).group())

# 当在匹配需要忽略字母大小写时，可向re.compile()的第二个参数传re.IGNORECASE或re.I。
# nameRegex=re.compile('ldq',re.IGNORECASE)
# print(nameRegex.findall('ldq is small and LDQ is big'))