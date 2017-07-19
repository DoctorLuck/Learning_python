#为了引发一个异常，可以使用一个类（Exception的子类）或者实力参数调用raise语句。
#创建自己的异常类时，要确保从Exception类继承。
#class MyException(Exception):
    # pass
# try:
#     first_num=int(input("first number:"))
#     second_num=int(input("second number:"))
#     print(first_num/second_num)
# except ZeroDivisionError:
#     print("The second num can't be zero")

# try:
#     first_num=int(input("first number:"))
#     second_num=int(input("second number:"))
#     print(first_num/second_num)
# except (ZeroDivisionError,TypeError,NameError): #可以一次捕捉多个异常
#     print("The second num can't be zero")


# try:
#     first_num=int(input("first number:"))
#     second_num=int(input("second number:"))
#     print(first_num/second_num)
# except ZeroDivisionError as e:
#     print(e)

#可以使用空的except子句来捕捉所有Exceptiom类的异常

# while True:
#     try:
#         first_num = int(input("first number:"))
#         second_num = int(input("second number:"))
#         print(first_num / second_num)
#     except ZeroDivisionError as e:
#         print(e)
#     else:
#         break
