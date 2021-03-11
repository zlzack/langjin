"""
print("你好！加油")
print(3%2)
a = len(input("输入a:"))
b = len(input("输入b:"))
print(a+b)

c=[8,9]
b=[c,5,6,7]
print(b)
a = {"xyz":b,"y":1,"z":2,"q":3,"w":4,"r":"好好","t":"事实"}
print(a)
a["我"]="你爹"
print(a)
"""
# # a = {"姓名":1,"年龄":2,"性别":3}
# # b=input("请输入姓名")
# # a["姓名"]=b
# # print(a)
# a = input("请输入")
# if a in "0123456789":
#     a= int(a)
#     print(a)
# else:
#     print("请输入数字")
#     exit()

# a = input("djaijd")
# if type(a) is str:
#     print("字符串")
# elif type(a) is int :
#     print("数字")
# else:
#     print("其他")



# a = 0
# b = {"张三":"zhangsan","李四":"lisi","王麻子":"wangmazi","浪晋":"langjin","流云":"liuyun","xixi":"xixi","xiaohong":"xiaohong","yasuo":"yasuo","nidie":"nidie"}
# b["张三"]= input("张三成绩：")

# b["李四"]= input("李四成绩：")

# b["王麻子"]= input("王麻子成绩：")

# b["浪晋"]= input("浪晋成绩：")

# b["流云"]= input("流云成绩：")

# b["xixi"]= input("xixi成绩：")

# b["xiaohong"]= input("xiaohong成绩：")

# b["yasuo"]= input("yasuo成绩：")

# b["nidie"]= input("nidie成绩：")
# print(b)
# while (1):
#     i=30
#     j=35
#     l=3
#     while i>0 :
#         print ("红灯还有",i,"秒",end= "  ")
#         i= i -1
#     while j >0 :
#         print("绿灯还有",j,"秒",end= "  ")
#         j = j-1
#     while l >0:
#         print("黄灯还有",l,"秒",end= "  ")
#         l=l-1

"""shuju = {}
a = input("请输入账号:")
b= len(a)
print(b)
if b >=5 and b<=8 and a[0] in "qwertyuiopasdfghjklzxcvbnm":
    c = input("请输入密码：")
    if len(c) >=6 and len(c) <= 12:
        print("注册成功！")
        shuju.update(a=c)
        print(shuju)
    else:
        print("密码长度为6-12位!")
else:
    print("账号长度为5-8位，小写字母开头！")


"""
shuju = {}

while 1>0 :
    a = input("请输入账号:")
    b= len(a)
    if b >=5 and b<=8 and a[0] in "qwertyuiopasdfghjklzxcvbnm":
        while 1>0 :
            c = input("请输入密码：")
            if len(c) >=6 and len(c) <= 12:
                print("注册成功！")
                shuju.update(a=c)
                print(shuju)
                exit()
            else:
                print("密码长度为6-12位!")
    else:
        print("账号长度为5-8位，小写字母开头！")
