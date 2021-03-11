import time
a = time.strftime("%y-%m-%d %H:%M:%S")
text = input("输入今天的趣事：")
with open ("Z:\日记.txt","a" , encoding="utf8")as f:
    f.write(a+"\n")
    f.write(text+"\n")
    
