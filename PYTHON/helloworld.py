# print("Hello World")
# print("This is My First Program ON 25Nov'23")
# age = 18
# age = age +2
# print(age)
# marks= ["Hi",97,98]
# print(marks)
# def addi(a,b):
#     return a+b
# a=8
# b=9
# print(addi(a,b))
n=int(input("Enter the Limit  : "))
a,b=0,1
if n==1:
   print("0")
elif n==2:
     print("0","\t","1",end=" ")
else:
    print(f"{a} {b}",end=" ")
    for i in range(3,n+1):
         x=a+b
         a=b
         b=x
         print(a,end=" ")