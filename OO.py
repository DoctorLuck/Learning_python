#面向对象
#封装 多态 继承
# __metaclass__=type
#
# class Person:
#     def setName(self,name):
#         self.name=name
#     def getName(self):
#         return self.name
#     def greet(self):
#         print("hello" + self.name)
#
# p=Person()
# p.setName('liudongqing')
# p.greet()

# class Class:
#     def method(self):
#         print("I have a self")
# def function():
#     print("I don't")
#
# instance=Class()
# instance.method()
# instance.method=function
# instance.method()

#为了让方法或者属性变为私有，只要在它的名字前面加上双下划线即可。
# class Secretive:
#     def __inaccesible(self):    私有方法iikm
#         print("Can't get me")
#     def accesible(self):
#         print('The secret message is:')
#         self.__inaccesible()
# s=Secretive()
# # s.__inaccesible() 错误
# s.accesible()

# class Fiter:
#     def put(self):
#         print("I am parent")
# class ZI(Fiter):
#     def put(self):
#         print("I am child")
#
# f=Fiter()
# f.put()
# f=ZI()
# f.put()
#
# class Bclass:
#     def put(self):
#         print("I am B")
#
# class Aclass:
#     def put(self):
#         print("I am A")
#
# class Subclass(Bclass,Aclass):  此处如果将Aclass放在之前，则打印出来的是A
#     pass
# Sub=Subclass()
# Sub.put()


