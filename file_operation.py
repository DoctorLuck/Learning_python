# 'r' 读模式
# 'w' 写模式
# 'a' 追加模式
# 'b' 二进制模式
# '+' 读/写模式，可添加到其他模式中使用
# 通过情况，python假定处理的是文本文件。当处理二进制文件时，就需要使用'b'
# f=open('test.txt')
# print(f.read(7))        #指定字节读取
# for i in range(3):
#     print(str(i)+':'+f.readline())      #按行读且输出
# import pprint
# pprint.pprint(open('test.txt').readlines())     #一次读出多行
# f.close()

# 通过with open('filename') as name打开的文件会自动关闭
import pprint
# f=open('test.txt')
# lines=f.readlines()
# f.close()
# f=open('test.txt','a+')
# f.writelines(lines)
# f.writable()
# pprint.pprint(lines)
# f=open('test1.txt','w')
# f.write('first line\n')
# f.write('second line')
# print('666',file=f) #通过print()向文件写入内容，这种方式会自动写入换行
# print('777',file=f)

