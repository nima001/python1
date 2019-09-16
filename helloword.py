# print('helloword')
#
# a = input("请输入数据：")
# print(a)
#
# print(type(a))
#
# print(type(int(a)))
#
# m,n=input("请输入两个数字：").split(",")
#
# print(m,n,end='@')

# import math
# a=int(input())
# b=int(input())
# c=int(input())
#
# s=(a+b+c)/2
#
# area=math.sqrt(s*(s-a)*(s-b)*(s-c))
# print("三角形面积：",area,end='')

# import math

# a = int(input())
# b = int(input())
#
# s = a + b

# print("和为：", s, end='')

# import math
# a,b,c=input().split()
#
# print(int(b)*int(b)-4*int(a)*int(c))
#
# s="Python语言简单易学"
# print(s.encode('utf-8'))

# 只要有一个运算数为浮点数，结果就是浮点数
# print(6.0 / 4.0)
# print(6.0 // 4.0)
# print(6.0 % 4.0)

# 计算商和余数
# print(divmod(9, 2))
# print(divmod(9.0, 2))

# 2**2代表2的2次方

# 复数
# a=complex(4,-6)
# print(a.real)#取实部
# print(a.imag)#取虚部

# 字符串
# a="m"
# b="a"
# c="n"
#
# d=a+b+c
# print(d)
# print(c*5)

# 多行字符串，'''XXX'''或者"""XXX""",三个单引号或者三个双引号
# print('''hello python
#     '人生苦短'
# 我用Python''')
#
# print('hello python\n 人生苦短 \n 我用Python')
#
# print('\'hello python\'')

# 返回表达式的值，not运算返回一定是true或者false

# 运算符优先级  算数>比较>逻辑


# 单一列表
# list=[1,2,3]
# 混合列表
# list=[1,"python",3]
# 嵌套列表
# list=[1,"python",[True,False,1]]
# #
# # print(list[0],list[2][2])

# 列表比较，一次比较列表里面的元素大小
# [1,2,3]<[1,2,4]
# print([1,2,3]<[1,2,4])
# print([1]*10)

# 元祖与列表 数据不可变性，列表元素可变
# t1=(2,4,6,8)#元祖不可修改
# t2=[2,4,6,8]#列表可以修改
# t1[0]=10 会报错
# t2[0]=10
# print(t1)
# print(t2)

# 数学库
# import math
# print(math.pi)

# 内置转换函数

# print(bool())#没有参数，false
# print(bool(0))#除了0以外的数字都是true
# print(bool(""))#字符串，空字符串为false，非空字符串都是true
# print(bool([]))#列表，空列表为false，只要是非空列表都是true
# print(bool(None))#参数为None，false
# print(bool('str'))
#
#
# print(int(3.6))
# print(int(-7.8))
# print(int("123"))#字母字符串会报错
# print(int( 35 ))#数字中间空格会报错，两边有空格不会报错
#
# print(float("3.7"))
# #print(float("a"))#报错
#
# # 转复数
# print(complex(1,2))
# print(complex("1+2j"))
#
# # 转字符串
# print(str(123))
# print(type(str(123)))
#
# print(ord("a"))#将字符转换为Unicode编码
# print(ord("中"))
#
# print(chr(97))#将Unicode转为字符
#
# print(bin(3)) #ob  转2进制
# print(oct(10))#oo 转8进制
# print(hex(10))#ox 转16进制
#
# print(list())
# print(list("abcde"))#用参数创建列表
#
# # 序列赋值
# x,y=4,8
# print(x,y)
#
#
# a,*b="345"#扩展列表赋值，两边个数不相等，则将多余的数据以列表的形式放在*变量中
# print(a,b)

# x=int(input())
# if x%2==0:
#     print("偶数")
# else:
#     print("奇数")

# x=float(input())
# # if x<=15:
# #     y=4*x/3
# # else:
# #     y=2.5*x-17.5
# #
# # print(y)
# 循环
# for i in  [1,2,3,4]:
#     print(i)

# 输入一个数（大于10），计算1到n+1的和
# n=int(input())
# list=list(range(n+1))
# sum=0
# for i in list:
#     sum+=i
# print(sum)


# 列表推导式  取出for循环里面列表的元素进行for循环之前的计算
# list=[2*i for i in [1,2,3,4,5]]#将1,2,3,4,5取出来分别乘以2
# print(2*i for i in [1,2,3,4,5])

# list=[i for i in range(1,8) if i%2==1]#将1,2,3,4,5,6,7取出来分别判断是否为奇数，赋给i
# print(list)

# print(16-2*5>7*8/2 or "XYZ"!="xyz" and not (10-6>18/2))

# list=[1/i for i in range(1,21)]
# print(sum(list))


# 条件表达式
# 条件为true返回值  if   条件   else  条件为负返回值

# 输出1-1/2+1/3-1/4+...+1/n+1
# n=int(input())
# list=[1/i if i%2==1 else -1/i for i in range(1,n+1)]
# print(sum(list))

# 输出-1-1/3+1/5-1/7+1/9+...+1/49
# list=[1/i if i%4==1 else -1/i for i in range(1,50) if i%2==1]
# print(sum(list))

# n=int(input())
# list=[int("6"*i) for i in range(1,n+1)]
# print(list)
# print(round(123.84, 0), round(123.84, -2), float(15.5))

# 格式化输出 format
# 将数据放入{}
# print("{}的{}".format("开飞机","DJ"))
# print("{1}的{0}".format("DJ","开飞机"))
# print("{DJ1}的{DJ2}".format(DJ2="DJ",DJ1="开飞机"))

# {数据：格式}
# 保留小数后两位
# print("{:.2f}".format(2.000000))

# print("{}年实现了预计目标".format(2017))
# print("{:>10}年实现了预计目标".format(2017))#>10表示右对齐，用空格填充
# print("{:<10}年实现了预计目标".format(2017))#>10表示左对齐，用空格填充
# print("{:^10}年实现了预计目标".format(2017))#>10表示居中对齐，用空格填充
# print("{:@^10}年实现了预计目标".format(2017))#>10表示居中对齐，用@填充
# print("今年的盈利额是{:,}".format(2017))#表示用逗号隔开

# 计算分段函数
# x=float(input())
# a=(1/x if x!=0 else 0)
# print("f({:.1f})={:.1f}".format(x,a))

# 计算表达式 1 + 2 + 3 + ... + 100 的值
# list=[i for i in range(1,101)]
# print("sum = {}".format(sum(list)))

# 某省电力公司执行“阶梯电价”，安装一户一表的居民用户电价分为两个“阶梯”：
# 月用电量50千瓦时（含50千瓦时）以内的，电价为0.53元/千瓦时；超过50千瓦时的，
# 超出部分的用电量，电价上调0.05元/千瓦时。请编写程序计算电费。
#
# x=float(input())
# y=(0.53*x if x<=50 else (x-50)*0.58+0.53*x)
# if x<=50 and (x>0):
#     y = 0.53 * x
#     print("cost = {:.2f}".format(y))
# elif x>50:
#     y=(x - 50) * 0.58 + 0.53 * 50
#     print("cost = {:.2f}".format(y))
# else:
#    print("Invalid Value!")

# 计算交错序列 1-2/3+3/5-4/7+5/9-6/11+... 的前N项之和。
# x=int(input())
# list=[(j+1)/2/j if ((j+1)/2)%2==1 else -(j+1)/2/j for j in range(1,2*x,2)]
#
# print("{:.3f}".format(sum(list)))

# 输入在一行中给出一系列正整数，其间以空格分隔。当读到零或负整数时，表示输入结束，该数字不要处理
list = [int(i) for i in input().split()]
sum=0
for j in list:
    if j>0:
       if j%2==1:
           sum+=j
    else:
        break
print(sum)
# 给定两个均不超过9的正整数a和n，要求编写程序求a+aa+aaa++⋯+aa⋯a（n个a）之和
# a,n = input().split()
# while int(a) > 9:
#     a = input()
# while int(n) > 9:
#     n= int(input())
# list=[int(a*i) for i in range(1,int(n)+1)]
# print("s = {}".format(sum(list)))