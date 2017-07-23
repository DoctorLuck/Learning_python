#构造方法 在一个对象被创建后，会立即调用构造方法。
# class FooBar:
#     def __init__(self): #构造方法
#         self.name='ldq'
# f=FooBar()
# print(f.name)

# class Bird:
#     def __init__(self):
#         self.hungry=True
#     def eat(self):
#         if self.hungry:
#             print("eating")
#             self.hungry=False
#         else:
#             print('No thanks')
# class SongBird(Bird):
#     def __init__(self):
#         # Bird.__init__(self)
#         super(SongBird,self).__init__()
#         self.sound='haha'
#     def sing(self):
#         print(self.sound)
#
# B=Bird()
# B.eat()
# SB=SongBird()
# SB.sing()
# SB.eat()

