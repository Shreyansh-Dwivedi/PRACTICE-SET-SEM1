#1
# a=int(input("enter the number : "))
# for i in range(1,a):
#     print(i**2)

#2
# for i in range(1,11):
#     if i%2!=0:
#         print(i)

#3
# for i in range(1,151):
#     if i%3==0:
#         print("Fizz")
#     elif i%5==0:
#         print("Buzz")
#     elif i%3==0 and i%5==0:
#         print("FizzBuzz")
#     else:
#         print(i)

#4
# a=int(input("Enter a Number : "))
# s=0
# while a>10:
#     a=a/3
#     s+=1
# print(f"the number of times are : {s} ")

#5
# a=int(input("Enter the number to find its Factorial : "))
# f=1
# for i in range(1,a+1):
#     f=f*i
# print(f)   

#6
# a=int(input("enter the number : "))
# d=0
# i=a
# t=0
# while i>0:
#     d=i%10
#     t=t+d
#     i=i//10
# print(f"Sum  of Digits : {t}")

#7
#a=int(input("Enter a Number"))
# d=0
# i=a
# t=0
# while i>0:
#      d=i%10
#      t=t+d
#      i=i//10
# print(f"Sum  of Digits : {t}")
# rev=0
# while a>0:
#       r=a%10
#       rev=(rev*10)+r
#       a=a//10
# print(f"Reverse is : {rev}")

#8
# a=int(input("Enter a Number : "))
# b=a
# rev=0
# while a>0:
#      r=a%10
#      rev = (rev*10) + r
#      a=a//10
# if rev==b:
#      print(f"{b} is palindrome")
# else:
#      print(f"{b}is not a palindrome")

#9
# a=int(input("Enter a Number : "))
# t=0
# i=a
# while i>0:
#     t=t+1
#     i=i//10
# print(f" total number of digits : {t}")
# j=a
# sum =0
# while(j>0):
#     r=j%10
#     sum = sum + (r**t)
#     j=j//10
# if sum==a:
#     print("It is Armstrong Number ")
# else:
#     print("It is Not an Armstrong Number ")
#11
# b=0
# for i in range(2,11):
#     b=0
#     for j in range(1,i+1):
#         if(i%j==0):
#             b+=1
#     if b==2:
#       print(f"{i} is a Prime Number")

#12
# Snum=36
# a=int(input("Enter Your No. : "))
# while a!=Snum:
#     print("Ha ha! You're stuck in my loop!")
#     a=int(input("Enter Your No. : "))
# if a==Snum:
#     print("Well done muggle! You are free now.")

#13
# status_bike= ["ok","ok","ok","faulty","ok","ok"]
# for status in status_bike:
#     if status=="faulty":
#         print("Bike is faulty. Stop the Process!!!")
    
#14
# a=input("Enter your E-mail address : ")
# for ch in a:
#     if ch == '@':
#         break
#     else:
#         print(ch,end="")

#404#
#a=list(range(5))
#print(a)

#15
# num=input("Enter the Number  : ")
# num1=str(num)
# digit1=""
# for digit in num1:
#     if digit=='0':
#         digit1+='x'
#     else:
#         digit1+=digit

# print(digit1)