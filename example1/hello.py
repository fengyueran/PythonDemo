#coding:utf-8

#1.hello world
print "hello world"

#2.注释
# 单行注释
#‘’‘块注释
'''
请计算：19+2
'''
a = 19 + 2
print a

#3.函数
def myFunction(a,b):
    c = a + b
    print c

if __name__=="__main__":
    myFunction(1,2)

#4.if语句
a = 3
if a == 3:
    print "it is three"
else:
    print "it is not three"

#5.数组
a = [1, 2, "hello", 3]
print a

#6.for循环

for i in a:
    print i

#7.字典
mydict = { "a":3, "b":4 }
mydict["c"] = 5
print mydict['c']
print mydict


#8.import
import random
print random.randint(0,10)
