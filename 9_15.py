# 字面量
# 被写在代码中固定的值

# 第二节 ：注释
"""" Python文件 ，类，方法"""

# 第三节 ：变量
money = 300
print("钱包的钱还有：",money)
"""买了冰淇凌"""
money = money - 10
print("钱包的钱还有：",money)

my_love = 999
ex_love = my_love
my_love = 777
print(my_love)
print(ex_love)
# 第四节：数据类型
print(type("今天要努力"))
print(type(999))
print(type(789.9))

ILY = "我爱你"
print(type(ILY))

# 第五节 ：数据类型转换

"""int(),float(),str()"""
"""万物皆可转字符串"""
"""浮点数转整数，丢失精度"""

# 第六节 ：标识符与关键字

# 第七节 ：算术运算符 和 赋值运算符
# 第八节 ；字符串的三种定义

print('She says:"Let\'s go !"')

#第九节 ： 字符串的拼接

name = "胡歌"
tel = 1234
print("我是"+name+"，我的电话是："+str(tel))
"""整数没办法拼接，先转化类型"""

# 第十节 ：字符串格式化

first = "天青色等烟雨"
second = "而我在等你"
message = "青花瓷中最有名的两句词分别是:%s,%s"%(first,second)
print(message)

# 第十一节：字符串快速格式化

first1 = "该怎么去形容你最贴切"
second2 = "拿什么做比较才算特别"
t3 = "对你的感觉强烈，却又不太了解，全凭直觉"
all1 = f"1{first1}+2{second2}+3{t3}"
print(all1)

# 第十二节：表达式的格式化

print("1*1的结果是：%d"%(1*1))
print(f"1*1的结果是：{1*1}")

name1= "Tesla"
stock_price = 19.99
stock_code = 12345
stock_price_daily_growth_factor = 1.2
growth_days = 5
print(f"公司；{name1},股票代码：{stock_code},当前股价；{stock_price}")
five_days_later = stock_price*stock_price_daily_growth_factor**growth_days
print("今日增长系数是：%s,经过%d天的增长后，股票价格达到了；%0.2f"%(stock_price_daily_growth_factor,growth_days,five_days_later))

# 第十四小节 ；input

#name2 = input("告诉我你是谁？")
#print(name2)

# """第三章"""
# print("欢迎来到儿童游乐场，儿童免费，成人收费")
# age = int(input("请输入您的年龄："))
# if age >= 18:
#     print("您已成年，游玩需补票10元")
# print("祝你游玩愉快！")
#
# if int(input("请输入您的身高:(cm)")) >= 180:
#     print("恭喜你!")
# elif int(input("请输入您的会员等级:")) >= 3:
#     print("恭喜你")
# elif int(input("请输入您的心情指数:")) >= 30:
#     print("恭喜你")
# else:
# #     print("算了")
# age = int(input("请输入您的年龄:(岁)"))
# if  age >= 18 :
#     if age <30 :
#         if int(input("请输入您的入职年龄:")) > 2:
#             print("您可以领取礼物")
#         elif int(input("等级大于3,也可以领取哦,请输入您的入职年龄:"))>3:
#             print("您可以领取礼物")
#         else:
#             print("很遗憾,您不能领取")
# else:
#     print("未成年不可以领取哦")
#
#
# import random
# num1 = random.randint(1,10)
# print(num1)
# guess_num = int(input("请输入您猜的数字:"))
# if guess_num == num1:
#     print("恭喜你,第一次就猜对了")
# else:
#     if guess_num > num1:
#         print("您猜大了")
#     else:
#         print("您猜小了")
#     guess_num = int(input("请输入您猜的数字:"))
#     if guess_num == num1:
#         print("恭喜你,第二次就猜对了")
#     else:
#         if guess_num > num1:
#             print("您猜大了")
#         else:
#             print("您猜小了")
#
#         guess_num = int(input("请输入您猜的数字:"))
#         if guess_num == num1:
#             print("恭喜你,第三次就猜对了")
#         else:
#             print("三次机会用完了哦")

# # 第四章 while
# i = 0
# while i < 40:
#     print("我喜欢你!")
#     i += 1
# i = 0
# sum = 0
# while i <= 100:
#     sum += i
#     i += 1
# # print(sum)
# import random
# num2 = random.randint(1,100)
# a = 1
# print(num2)
# guess_num1 = int(input("请输入您猜的数"))
# if guess_num1 == num2:
#     print("恭喜你,第一次就猜对了")
#     print(f"您一共猜了{a}次")
# else:
#     while guess_num1 != num2:
#          if guess_num1 > num2:
#             print("您猜大了")
#             print(f"您一共猜了{a}次")
#             a += 1
#
#             guess_num1 = int(input("请输入您猜的数"))
#
#
#          else:
#             print("您猜小了")
#             print(f"您一共猜了{a}次")
#             a += 1
#             guess_num1 = int(input("请输入您猜的数"))
#
# import random
# num3 = random.randint(1,100)
# print(num3)
# b = 0
# flag = True
# while flag:
#     guess_num4 = int(input("请输入您猜的数:"))
#     b +=1
#     if guess_num4 == num3:
#         print("恭喜你第一次就猜对了!")
#         flag = False
#     else:
#         if guess_num4 > num3:
#             print("您猜大了!")
#
#         else:
#             print("您猜小了!")
# print(f"您一共猜了{b}次")
# #表白一百天,每天送十支玫瑰花
# i = 0
# while i< 100:
#     print(f"今天第{i}天,准备表白了")
#     j = 1
#     while j <= 10:
#         print(f"送给你的第{j}只玫瑰")
#         j += 1
#     i += 1
# #     print(f"离目标还差{100-i}天")
# print("||||||||||||||||||||||||||||||||||||||||||||||||||||")
# print("hello",end='')
# print("world",end='')
#
# print("hello\tworld")
# print("hello\tmr.yong")

# #控制外层循环
# i = 1
# while i <= 9:
#     #控制内层循环
#     j = 1
#     while j<=i:
#         print(f"{j}*{i}={i*j}\t",end='')
#         j+=1
#     i+=1
#     print()
#
# name3 = "itheima"
# for c in name3:
#     print(c)
#
# name4 = "itheima is a brand of itcast"
# jishu = 0
# for d in name4:
#     if d == "a":
#         jishu += 1
# # print(jishu)
# d = 0
# num11 = int(input("请输入一个数字"))
# for x in range(num11):
#     if x % 2 ==0:
#         d +=1
# print(d)
#
# #for 双循环
# """表白一百天，每天十支玫瑰花"""
# i = 1
# n = 1
# for i in range(1,101):
#     print(f"今天是表白的第{i}天")
#     for n in range(1,11):
#         print(f"这是送给小美的第{n}只玫瑰")
# print(f"表白了{i}次，终于成功了！")
# #for 循环 9x9乘法表
# i = 1
# j = 1
# f = 2
# for i in range(1,10):
#     for j in range(1,f):
#         print(f"{j}*{i}={i*j}\t",end='')
#     print()
#     f += 1

#contine 和 break
#
# for x in range(1,6):
#     print("语句1")
#     continue
#     print("语句2")
#
# for x in range(1,6):
#     print("语句1")
#     break
#     print("语句2")
# print("语句3")
#
# #发工资
# _money = 10000
# for x in range(1,21):
#     if _money >0:
#         import random
#         score = random.randint(1,10)
#         print(score)
#         if score >= 5:
#             _money-=1000
#             print(f"员工{x}发放工资1000元,账户余额还剩{_money}元")
#         else:
#             print(f"员工{x},绩效分{score},不发工资,下一位")
#     else:
#         break
# print("工资发完了,下月再来领取吧")

# #函数
# name111 = "heimachengxuyuan"
# print(type(len(name111)))

# #自创函数
# def my_len(date):
#     count = 0
#     for i in date:
#         count += 1
#     print(f"字符串{date}长度是{count}")
# str1 = " woaini"
# str2 = "wofeichangaini"
# my_len(str2)
# my_len(str1)
#
# def say_hello():
#     print("我是一个打招呼的函数")
# say_hello()

# #写一个两数相加的函数
# def add(x,y):
#     sum = x + y
#     print(f"{x}+{y}= {x+y}")
# add(1,1)
# add(1,4)

# #自动查验核酸函数
# def tem_check(x):
#     print("请出示您的健康码及72小时核酸证明,并配合测量体温!")
#     if x>=37.5:
#         print("您需要立马隔离!!!!")
#     else:
#         print("您的体温正常!")
# tem_check(35)
#
# def check_age(x):
#     """
#     check_age函数可以用来检测是否可以进入网吧
#     :param x:形参
#     :return:返回值
#     """
#     if x > 18:
#         print("SUCCESS")
#     else:
#         return None
# if not check_age(13):  None 与 False  一样
#     print("未成年不可以进入网吧哦!")

# #函数的调用
# def fun1():
#     print("111")
# def fun2():
#     print("222")
#     fun1()
#     print("333")
# # fun2()
# Atm
# the_money = 0
# def money_check():
#     print(f"周杰伦,您好,您的余额剩余:{the_money}元")
# def in_money():
#     a = int(input("请输入您存入的金额:(元)"))
#     global the_money
#     the_money += a
#     print(f"周杰伦,您好,您存款{a}元成功")
#     print(f"周杰伦,您好,您的余额剩余:{the_money}")
# def out_money():
#     a = int(input("请输入您取出的金额:(元)"))
#     global the_money
#     the_money -= a
#     print(f"周杰伦,您好,您{a}取款元成功")
#     print(f"周杰伦,您好,您的余额剩余:{the_money}")
# def quit():
#     print("感谢您的使用!")
# def hello():
#     print("周杰伦,您好,欢迎使用ATM取款机")
#     print("查询余额[输入1]\n存款[输入2]\n取款[输入3]\n退出[输入4]")
# hello()
# ainput_num = int(input("请选择您的服务"))
# if ainput_num == 1:
#     money_check()
#     hello()
# elif ainput_num == 2:
#     in_money()
#     hello()
# elif ainput_num == 3:
#     out_money()
#     hello()
# else:
#     quit()
# if ainput_num ==4:
#     quit()
# else:
#     while ainput_num != 4:
#
#         if ainput_num == 1:
#             money_check()
#         elif ainput_num == 2:
#             in_money()
#         elif ainput_num == 3:
#             out_money()
#
#
# quit()
# #
# if ainput_num == 4:
#     quit()
# else:
#     flag = True
#     while flag :
#         if ainput_num ==1:
#             money_check()
#         elif ainput_num ==2:
#             in_money()
#         elif ainput_num ==3 :
#             out_money()
#         hello()
        # if ainput_num == 4:
#         #     flag == False
# the_money = 5000
# num = 0
# #余额查询函数
# def money_check(head_master):
#     if head_master:
#         print("-------------查询余额------------------")
#     print(f"您好,您的余额剩余{the_money}元")
# def in_money():
#     global the_money
#     num = int(input("请输入您要存入的金额:"))
#     the_money += num
#     print(f"您好,你存款{num}元成功")
#     #调用一下查询函数
#     money_check(False)
#
# def out_money():
#         global the_money
#         num = int(input("请输入您取出的金额:"))
#         the_money -= num
#         print(f"您好,你取款{num}元成功")
#         # 调用一下查询函数
#         money_check(False)
# def main():
#     print("您好,欢迎使用ATM取款机,请选择操作:")
#     print("查询余额 [输入1]")
#     print("存款\t\t[输入2]")
#     print("取款\t\t[输入3]")
#     print("退出\t\t[输入4]")
#     global  num
#     num = input("请输入您的选择:")
# while True:
#     main()
#     if num == "1":
    #     money_check(True)
    #     continue
    # elif num == "2":
    #     in_money()
    #     continue
    # elif num =="3":
    #     out_money()
    #     continue
    # else:
    #     print("谢谢您的使用")
    #     break
#列表
# list_1 = ["蔡徐坤","章子怡","王俊凯"]
# print(list_1)
# print(type(list_1))
# list_2 = ["我爱你",666,True]
# print(list_2)
# print(type(list_2))
#列表内元素无限制,故可以列表嵌套

#列表下表索引
# my_list = [[1,2],[3,4]]
# print(my_list[1])
# print(my_list[-1])
# # print(my_list[0][1])
# my_list = [1,2,3]
# print(my_list.index(1))
# my_list.insert(1,"我爱你")
# print(f"修改后的列表是{my_list}")
# my_list.append("我真的非常爱你")
# print(my_list)
# my_list2 = ["天天送花","每天打电话"]
# my_list.extend(my_list2)
# print(my_list)
# #删除下标
# del my_list[6]
# element = my_list.pop(5)#有返回值,先拿出来给您看看,再去除
# print(f"剩余的元素{my_list},取出的的元素{element}")

# #remove 只能删除一个指定元素(从左至右开始搜索)
# my_list.append(2)
# my_list.remove(2)
# print(my_list)
# my_list.append(2)
# my_list.append(2)
# #清空列表
# my_list.clear()
# print(my_list)
# #统计某个元素的数量
# print(my_list.count(2))
# print(len(my_list))

# #学生年龄列表
# student_age = [21,25,21,23,22,20]
# student_age.append(31)
# new_student_age = [29,33,30]
# student_age.extend(new_student_age)
# first_element = student_age.pop(0)
# print(first_element)
# last_element = student_age.pop(int(len(student_age)-1))
# print(last_element)
# student_age.index(31)
# print(student_age)
#
#
# my_list = ["周杰伦","王力宏","林俊杰"]
# #for while 循环遍历或者迭代列表
#
# def list_for_func():
#     index = 0
#     while index < len(my_list):
#         element = my_list[index]
#         print(element)
#         index += 1
# list_for_func()

my_list = [1,2,3,4,5,6,7,8,9,10]
#偶数列表
list1 = []
# index = 0
# while index < len(my_list):
#     if int(my_list[index]) % 2 == 0:
#         list1.append(my_list[index])
#     index += 1
# print(f"通过while循环,从列表{my_list}中,取出的新列表是:{list1}")

# for element in my_list:
#     if element % 2 == 0:
#         list1.append(element)
# print(f"通过for循环,从列表{my_list}中,取出的新列表是:{list1}")

#元组 tuple
#仅仅定义一个元组,要有逗号
# t1 = ("我爱你",)
# print(t1)
# print(type(t1))
# #元组嵌套
# t2 = ((1,3),(4,5))
# print(t2[1][1])
# t4 = ("我","你","他")
# print(t4.index("我"))
# print(t4.count("我"))
# print(len(t4))
# #while循环遍历元组
# def tuple_for_func():
#     index = 0
#     while index < len(t4):
#         print(t4[index])
#         index += 1
# tuple_for_func()
#for循环遍历元组
# def tuple_for_func():
#     for element in t4:
#         print(element)
# tuple_for_func()
#tuple 中嵌套列表,就可以修改列表
#
# t5 = ("我爱你",["I","LOVE","YOU"])
# print(f"原元组是\t\t:{t5}")
# t5[1][1] = "LIKE"
# print(f"修改后的元组是:{t5}")

# #再识字符串
# str3 = "I LOVE YOU"
# #寻找起始下标
# print(str3.index("LOVE"))
# #替换形成新的字符串
# new_str3 = str3.replace("LOVE","Like")
# print(f"原字符串是:{str3},新字符串是:{new_str3}")
#字符串的切割,变成元组
# str4 = "hello the furture i wanna be the best"
# new_str4 = str4.split(" ")
# print(new_str4)
# print(type(new_str4))
# #strip 去除收尾空格(不传参)
# # 传参(去除收尾指定参数)
# print(str4.count("a"))
# print(len(str4))
#
# str5 = "wo wanna be the best"
# print(str5.count("w"))
# new_str6 = str5.replace(" ","|")
# print(f"修改后的字符串是:{new_str6}")
# new_str5 = new_str6.split("|")
# print(f"{new_str5},{type(new_str5)}")

#集合
my_set = {"I Love You","I","she","he","she","he"}
print(f"{my_set},{type(my_set)}")
my_empty_set = set()
print(type(my_empty_set))
#添加新元素
my_set.add("python")
print(my_set)
my_set.remove("I")
print(my_set)
#随机取出来一个
element = my_set.pop()
print(element)
my_set.clear()
print(my_set)
#取两个集合差
set1 = {1,2}
set2 = {1,5}
set3 = set1.difference(set2)
print(f"{set3},{set2},{set1}")
#消除两个集合的差
print("--------------------")
set1.difference_update(set2)
print(f"{set1},{set2}")
print(set1.union(set2))

#定义字典
my_dict = {"王力宏":99,"周杰伦":88,"林俊杰":77}
print(my_dict["王力宏"])
#字典的嵌套
my_dict2 = {"王力宏":{"语文":99,"数学":88,"英语":77}}
print(my_dict2)
#调出王力宏的数学成绩
print(my_dict2["王力宏"]["数学"])
#拿到全部key
print(my_dict.keys())
#遍历字典
for keys in my_dict.keys():
    print(f"字典中所以的key有:{keys}")
    print(f"字典中value的值分别是:{my_dict[keys]}")
#也可以直接 for key in my_dict:

#练习
staff_information = {"王力宏":{"部门":"科技部","工资":3000,"级别":1},"周杰伦":{"部门":"市场部","工资":5000,"级别":2},"林俊杰":{"部门":"市场部","工资":7000,"级别":3},"张学友":{"部门":"科技部","工资":4000,"级别":1}}
for key in staff_information:
    if staff_information[key]["级别"] == 1:
        staff_information[key]["工资"] += 1000
        staff_information[key]["级别"] += 1
print(staff_information)
#函数返回多个值
def return1():
    return 1,2
x,y = return1()
print(f"{y},{x}")
def users_infor(name,age,gender):#位置参数

    print(f"名字:{name},年龄:{age},性别:{gender}")
users_infor("jesse",19,"男")
# lambda x,y: print(f"{x+y}")
# lambda