import os
print(os.path.join('usr','bin','spam'))  #打印出当前操作系统下由指定的字符确定的路径
myFiles=['accounts.txt','details.csv','invite.docx']
for file in myFiles:
    print(os.path.join('F:\\',file))  #打印出三个路径

print(os.getcwd())  #获得当前工作目录
# 可以通过os.chdir()改变它
os.makedirs('F:\\testfile\\')  #创建文件夹
os.path.abspath('.') #返回当前路径的绝对路径
print(os.path.abspath('.'))
os.path.relpath(path='C:\\windows',start='C:')  #返回从start到path的相对路径
print(os.path.relpath(path='C:\\windows',start='C:'))
os.path.getsize('.') #获取路径下的文件大小（字节数）
print(os.path.getsize('.'))
os.listdir('.') #获取路径下的所有文件
print(os.listdir('.'))


#获取一个目录下所有文件的大小
totalSize=0
for fileName in os.listdir('.'):
    totalSize=totalSize+os.path.getsize(fileName)
print(totalSize)

#************************************
os.path.exists('路径')   #判断文件夹或文件是否存在
os.path.isdir('路径')  #判断是否为文件夹
os.path.isfile('路径')    #判断是否为文件类型


f=open('hello.txt','w+')
len=f.write('hello world!')     #返回写入的字符个数
f.close()
print(len)