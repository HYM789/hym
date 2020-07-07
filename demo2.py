# def shang_yu(a,b):
#     if(b == 0):
#         return None
#     else:
#         return (a//b,a%b)
#
# res = shang_yu(20,2)
#
# if res is None:
#     print("参数错误")
# else:
#     print("商为: ",res[0],"余数为:",res[1])
#
# res = shang_yu(b=2,a=20)
#
# if res is None:
#     print(res)
#     print("参数错误")
# else:
#     print(res)
#
# c = 1,2,3,4
# a,*b = (1,2,3,4)
#
# print(b)
#
# #
# def sum1(name,*args,**kwargs):
#     print(kwargs)
#     print(name)
#     s = 0
#     for i in  args:
#         s+=i
#     return s
# print(sum1(1,2,3,56,7,8,9,0,3,3,4,4,7))
# print(sum1(name="薛小磊"))

#class calc():
#   a = None
#   b = None
#     res = None
#      def input(self,a,b):
#         self.a=a
#         self.b=b
#     def div(self):
#         self.res = self.a / self.b
#     def sum(self):
#          self.res = self.a + self.b
#     def get_result(self):
#         print(self.res)

# c = calc()
# c.input(10,20)
# c.sum()
# c.get_result()
# c.div()
# c.get_result()

# class calc():
#     res = None
#
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def div(self):
#         self.res = self.a / self.b
#     def sum(self):
#          self.res = self.a + self.b
#     def get_result(self):
#         print(self.res)
#
# c = calc(29,39)
# c.sum()
# c.get_result()

# for i in range(1,10):
#     for j in range(1,i+1):
#         # print(j,"x",i,"=",i*j,end="\t")
#         # print("{}*{}={}".format(i,j,i*j),end="\t")
#         print(("%d*%d=%d")%(i,j,i*j),end=" ")
#     print()
#
# l = [7,8,9,4,6,9,2,3,78,65,1264,42]

# length = len(l)
# for i  in range(length-1,0,-1):
#     for j in range(i):
#         if(l[j] > l[j+1]):
#             l[j],l[j+1] = l[j+1],l[j]
#
# print(l)

# l = [7,8,9,4,6,9,2,3,78,65,1264,42]
# length = len(l)
# for i in range(len(l)-1):
#     for j in range(len(l)-i-1):
#         if (l[j] > l[j+1]):
#             l[j],l[j+1] = l[j+1],l[j]
# print(l)
#
# class Parent():
#
#     money = 99999999
#     house = 9999
#     _yi_wu = "裙子"
#
#     def shou_yi(self):
#         print("点石成金")
#
# class Child(Parent):
#     ai_hao = "享受"
#
#
# c = Child()
# print(c.ai_hao)
# print(c.money)正确

# p = Parent(123)
# print(p.a)
#
# class Child(Parent):
#     ai_hao = "享受"
#     def __init__(self,*args,**kwargs):
#         super() ._init(*args,**kwargs)
#
# def shou_yi(self):
#     print("影分身之术")
#
#
# c = Child(123)
# print(c.ai_hao)
# print(c.money)
# c.shou_yi()
# print(c.a)错误

# class Test():
#     name="我是模块2中的Test"
#
# if _name_=="main":
#     name()
#     print(Test.name)错误

# l=[1,2,3,5,6,9,8,45,78]
# s={1,6,9,0,5,6,98}
# #
# # 打开模式：r 读取 w 清空写入 a 追加写入 b 二进制模式
# #  f = open("aaa.txt",'w') #打开文件
# # f.write("hello Kitty")   #输出
# # f.close()

# f = open("aaa.txt",'w') #打开文件
# f.write("hello Kitty\n你大爷还是你大爷\n黑山老妖齐姥姥\n")   #输出
# f.writelines({"黑山老鸭\n齐姥姥是也\n没有神的光环\n"})
# print(f.writable())
# f.close()
#
# f = open("abc.txt",'r')
# print(f.read())
# print(f.read(10))
# print(f.readline())
# print(f.readlines())
# f.close()

# a="你是不是狗，我不知道，但你是真的狗"
# print(a)
#
# b="天才是我强哥"
# print(b)
#
# for i in a:
#     print(i)
#
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%d x %d = %d"%(j,i,i*j),end="\t")
#     print()
#
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("{} x {} = {}".format(j,i,i*j),end="\t")
#     print()
#
# l=[1,34,67,85,2,0,2]
#
# l[0]=20
# print(1)
# l[1:3]=20,30
# print(l)
#
# l=[7,8,9,10]
# l.append("仙女")
# l.append("仙女姐姐")
# l.extend({'987',456})
# l.insert(1,"小仙女")
# print(l)
#
# print(l.pop())
# print(1)
#
# l.remove(456)
# print(1)
#
# # 字典的操作
# d = {"name":"小明","age":18,"sex":"男"}
#
# for key in d:      #只能遍历key值
#     print(d[key])
#
# d.items()
# print(d.items())
#
# for k,v in d.items():
#     print(k,v)

def div(a,b):
    try:
        return a / b
    except:
        return

print(div(10,5))

try:
    f = open("bbbb.txt",'r')
    print(f.read())
    f.close()
except:
    print("文件不存在")

print("操作完文件")

def div(a,b):
    try:
        print(a/b)
    except ZeroDivisionError as e:
        print(e)
    else:
        print("除法执行成功")
    finally:
        print("不管try中是否报错，都会被执行")

class CustomException(Exception):
    def __init__(self,value = "值不能为0"):
        self.value = value

    def __str__(self):
        return  self.value

a = 0

try:
    if a == 0:
        print("a = {}触发异常",format(a))
except CustomException as e:
    print(e)



