import requests     #从网页下载文件和网页
import webbrowser   #python自带的，打开浏览器获取指定页面
from bs4 import BeautifulSoup   #解析HTML
import selenium     #启动并控制一个浏览器。能够填写表单，并模拟鼠标在这个浏览器进行点击
import re

#利用webbrowser打开浏览器并打开网页
import webbrowser
webbrowser.open('http://www.baidu.com')

# 利用requests模块
import requests
res=requests.get('http://www.baidu.com')    #返回的是一个response对象
print(type(res))
print(res.text)
# Response对象有一个status_code属性，可以检查它是否等于requests.codes.ok，了解是否下载成功。
# 可以通过response对象调用raise_for_status()方法，如果文件下载出错，就会抛出异常。
res=requests.get('http://www.jianshu.com/p/b594bf8e7e7c')
try:
    res.raise_for_status()
except Exception as exc:
    print('The problem is {}'.format(exc))
playFile=open('play.txt','wb')  #此处必须以“写二进制”模式打开该文件，这样做是为了保存该文本中的“Unicode编码”
playFile.write(res.content)   #这种方式可行
for chunk in res.iter_content():
    playFile.write(chunk)


# 通过BeautifulSoup解析HTML
res=requests.get('http://www.jianshu.com/p/a41af1501f75')
try:
    res.raise_for_status()
except Exception as exc:
    print('The problem is {}'.format(exc))
bsobj=BeautifulSoup(res.text,'lxml')
print(bsobj.prettify())
#用select（）方法寻找元素,返回一个Tag对象的列表
bsobj.select('div')     #所有名为<div>的元素
bsobj.select('#author')     #所有id为author的元素
bsobj.select('.notice')     #所有class为notice的元素
bsobj.select('div span')    #div下的所有span元素
bsobj.select('div>span')    #div下所有直接span元素
bsobj.select('input[name]')     #所有名为input,拥有name属性，其值任意的元素
bsobj.select('input[name="button"]')    #所有名为input,拥有name属性，值为button的元素
elements=bsobj.select("span")
print(elements)
print(elements[1])


html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
f=open('craw_test.html','w')
f.write(html_doc)
f.close()
bsobj=BeautifulSoup(open('craw_test.html'),'lxml')
print(bsobj.prettify())     #按照标准的缩进格式打印出来
print(bsobj.p)      #打印第一个p标签
print(bsobj.p['class'])
print(bsobj.title.string)   #打印第一个title标签的内容
print(bsobj.getText)
for link in bsobj.find_all('a'):      #获取文档中的所有a标签
    print(link)
    print(link['href'])
    print(link['class'])
print(bsobj.get_text())     #从文档中获取所有文字内容
# 字符串常被包含在tag内.Beautiful Soup用 NavigableString 类来包装tag中的字符串
print(bsobj.contents)       #将标签的子节点以列表形式列出
for child in bsobj.children:    #通过tag的.children生成器，对子节点进行循环
    print(child)

# .contents 和 .children 属性仅包含tag的直接子节点.
for des in bsobj.descendants:   #所有后代节点
    print(des)

# 如果一个tag仅有一个NavigableString 类型子节点，则可以通过.string得到子节点


# 如果tag中包含多个字符串，则可以通过.strings循环获取
for st in bsobj.strings:
    # print(repr(st))
    print(str(st).strip())


# 输出的字符串中可能包含了很多空格或空行,使用 .stripped_strings 可以去除多余空白内容
for st in bsobj.stripped_strings:
    print(st)
# 全部是空格的行会被忽略掉,段首和段末的空白会被删除

print(bsobj.find_all(href=re.compile("elsie")))
print(bsobj.find_all(href=re.compile("elsie"), id='link1'))


# 有些tag属性在搜索不能使用,比如HTML5中的 data-* 属性:
data_soup = BeautifulSoup('<div data-foo="value">foo!</div>')
# print(data_soup.find_all(data-foo="value"))
# SyntaxError: keyword can't be an expression


# 但是可以通过 find_all() 方法的 attrs 参数定义一个字典参数来搜索包含特殊属性的tag:
print(data_soup.find_all(attrs={"data-foo": "value"}))
# [<div data-foo="value">foo!</div>]

print(bsobj.find_all("a", class_="sister"))

# class_ 参数同样接受不同类型的 过滤器 ,字符串,正则表达式,方法或 True
print(bsobj.find_all(class_=re.compile(r"itl")))

# 调用tag的 find_all() 方法时,Beautiful Soup会检索当前tag的所有子孙节点,如果只想搜索tag的直接子节点,可以使用参数 recursive=False .