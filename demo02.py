# shuju = {}

# while 1>0 :
#     a = input("请输入账号:")
#     b= len(a)
#     if b >=5 and b<=8 and a[0] in "qwertyuiopasdfghjklzxcvbnm":
#         while 1>0 :
#             c = input("请输入密码：")
#             if len(c) >=6 and len(c) <= 12:
#                 print("注册成功！")
#                 shuju.update(a=c)
#                 print(shuju)
#                 exit()
#             else:
#                 print("密码长度为6-12位!")
#     else:
#         print("账号长度为5-8位，小写字母开头！")


# try:
#     a=input("姓名：")
#     b=int(input("年龄："))
#     if b > 18:
#         print(a,"成年了")
#     else:
#         print(a,"未成年")
# except Exception as e :
#     print("baocuo",e)


class Fangzi():
    def __init__ (self,mingzi,huxing,daxiao,jiage):
        self.mingzi =mingzi
        self.huxing =huxing
        self.daxiao =daxiao
        self.jiage = jiage
    def gongneng(self):
        print("装逼")


mingzi =input("输入名字")
huxing = input("输入户型")
daxiao = input("输入大小")
jiage = input("输入价格")
hhh = Fangzi(mingzi,huxing,daxiao,jiage)
hhh.gongneng()
print(hhh.mingzi)