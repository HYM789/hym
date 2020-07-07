
a = (1,2,3,4,5,6,7,8,9,0)


x,y,*z= a

print (x)
print (y)
print (z)

list1 = [1,2,3,4,5]
print(list1)

name = '张三'
print(name)

school="果芽"
print(school)

age = 25
price = 9.99
print(age)
print(price)

like_girl = True
like_boy = False

java_skill = None

# -------列表list------
# 存数字
list1 = [1, 2, 3, 4, 5 ]
print(list1)

# 存字符串
list2 = ['Python','API','UI','APP']
print(list2)

# 存多种类型
# list3 = ["张三", 28, 99.00,True,None,['Python'，'API','UI','APP']]
# print(list3)

# -------元组Tuple------
list1 = (1, 2, 3, 4, 5 )
print(list1)

# -------集合set------
# set1 = {'a','b','c','a','b','c'}
# set2 = set('abcabc')
# print(set1)
# print(set2)

# -------字典dict------
# list=['张三',25,'P自',18000.00]
# dict = {'姓名': '张三', '年龄': 25, '课程': 'P自','薪资':18000.00}
# print(list)
# print(dict)

# for i in range(1,100):
#     if (i % 3 != 0):
#        continue
#     print(i)
#

for i in range (1 , 100):
    if (i % 3 != 0):
        continue
    print(i)

# 定义一个求两个数商和余数的方法
def shangyushu(a,b):
    print(a // b)
    print(a % b)
shangyushu(10,3)


