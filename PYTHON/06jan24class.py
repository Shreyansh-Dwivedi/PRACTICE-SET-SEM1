#date : 06-01-2023
#PPS lab work

def sum(a,b ):
    c=a+b
    return c

def sub(a,b):
    c=a-b
    return (c)

def mul(a,b):
    return a*b

# #def div(a,b):          when we write just this line it means SIGNATURE OF FUNCTION

def div(a,b):
    return a/b

# sum(1/2 ,1/2)
# sub(2,8)
# mul(8,8)
# div(2,9)

# def SUM(a,b):
#     return a+b
# print(SUM(5,5))
# print(SUM("Hello ","Jishan"))

# def f3():
#     print("Hello World")

# z=5
# def f1(a,b):
#     print(a+b+z)
#     f3()
# f1(5,5)

# def f2(w,t):
#     print(w+t+z)
#     #f3()
# f2(4,4)

# def f3():
#     print("Hello World")

# def pList():
#    my_list =[]
#    for i in range(1,6):
#      my_list.append(i)
#    print(my_list)
 
# pList()

# n=input("What do you want to perform : \n Enter '+' for Addition \n Enter '-' for Substraction ")
# a='+'
# b='-'
# if(a==n):
#     a1=int(input("enter 1st no.: "))
#     a2=int(input("enter second no. :"))
#     print(f"Answer is : {sum(a1,a2)}")

# elif (b==n):
#     a1=int(input("enter 1st no.: "))
#     a2=int(input("enter second no. :"))
#     print(f"Answer is : {sub(a1,a2)}")

n=input("Enter Task : ")
a=['+','-','*','/']
for i in a:
    if i==n:
        num1=int(input("Enter First Number : "))
        num2=int(input("Enter Second Number : "))
        if n=='+':
            print(f"{num1} + {num2} = {sum(num1,num2)}")
        elif n=='-':
            print(f"{num1} - {num2} = {sub(num1,num2)}")
        elif n=='*':
            print(f"{num1} * {num2} = {mul(num1,num2)}")
        elif n=='/':
            print(f"{num1} / {num2} = {div(num1,num2)}")




