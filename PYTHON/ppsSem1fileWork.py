#date : 28-12-2023
#Q1.a.
# a=int(input("Enter the number : "))
# s=0
# b=a
# while b>0:
#     s = s + (b%10)
#     b//=10
# print(f"Sum of Digits of {a} is  : {s}")

#Q1.b.
# a=int(input("Enter Radius of a Circle : "))
# print(f"Area of the Circle with Radius {a} is {3.14*(a**2)}")

#Q1.c.
# m1=int(input("Enter 1st TEST marks : "))
# m2=int(input("Enter 2nd TEST marks : "))
# m3=int(input("Enter 3rd TEST marks : "))
# m=min(m1,m2,m3)
# M=((m1+m2+m3)-m)/2
# print("The Best of the Two Avg marks of the Three Test marks are : "+str(M))

#Q1.d.
# a=int(input("Enter the Number :  "))
# print("Answer when "+str(a)+" is multipied to 4 is : "+str(a<<2))

#Q2.a.
# a=input("enter the CHARACTER : ")
# v=['a','e','i','o','u','A','E','I','O','U']
# if a in v:
#     print("Vowel")
# else:
#     print("Consonant")

#Q2.b.
# a=int(input("Enter the 1st Number : "))
# b=int(input("Enter the 2nd Number : "))
# c=int(input("Enter the 3rd Number : "))
# d=0
# if a>b:
#     d=a
# elif b>a:
#     d=b
# if d>c:
#     d=d
# elif c>d:
#     d=c
# print("The Greatest of the Three Inputed Number is  : "+str(d))

#Q2.c.
# yr=int(input("Enter the Year : "))
# if (yr%4==0 and yr%100!=0) or (yr%400==0) :
#     print(f"{yr} is a Leap Year.")
# else:
#     print(f"{yr} is not a Leap Year")

#Q2.d.
# ch1=input("Enter 1st Character : ")
# ch2=input("Enter 2nd Character : ")
# if ch1==ch2:
#     print(f"{ch1} and {ch2} both are the Same Characters")
# else:
#     print(f"{ch1} and {ch2} both are Different Characters")

#Q3.a.
# a=int(input("Enter The Number : "))
# while a>=0:
#     print(a)
#     a-=1

#Q3.b.
# a=int(input("Enter the Number of Lines of Pattern : "))
# x=1
# while x<=a:
#     print(x*'*')
#     x+=1

#Q3.c.
# a=int(input("Enter Number to be Reversed : "))
# rev=0
# b=a
# while b>0:
#     rev = rev *10 +(b%10)
#     b//=10
# print(f"Reverse of {a} is : {rev}")

#Q3.d.
# a,b=0,1
# while a<=50:
#     print(a,end=" ")
#     a,b=b,a+b

#Q3.e.
# a=int(input("Enter Your Limit : "))
# b=a
# term =2
# total = 0
# for i in range(a):
#     total +=term
#     term= term*10+2
# print(total)

#Q4.a.
# my_list=[3,4,5,6,7,8]
# listSUM=sum(my_list)
# print(f"Sum of {my_list} is {listSUM}")

#Q4.b.
# n=int(input("Enter Number of Elements in the LIST : "))
# my_list=[]
# for i in range(n):
#     element=int(input(f"Enter the Element {i+1} : "))
#     my_list.append(element)
# print(f"The Original list is : {my_list}")
# s,e=0,n-1
# while s<=e:
#     py=my_list[s]
#     my_list[s]=my_list[e]
#     my_list[e]=py
#     s+=1
#     e-=1
# print(f"The Reversed List is : {my_list}")

#Q4.c.
# l1=["M","NA"]
# l2=["Y","ME"]
# result = [x+y for x,y in zip(l1,l2)]
# print(result)

#Q5.a.
# w="welcome to my code"
# #indexing
# print(w[0])
# print(w[11])
# #slicing
# print(w[1:9])

#5.b.
# w=input("Enter the String : ")
# W=""

# print(len(w))
# for i in w:
#     if i in "aeiouAEIOU":
#         W+="_"
#     else:
#         W+=i
# print(W)
        
#Q5.c.
# w=input("Enter the Word : ")
# s=0
# p=0
# e=len(w)-1
# while s<=e:
#     if w[s]!=w[e]:
#         print("Not a Palindrome")
#         p+=1
#         break
#     s+=1
#     e-=1
# if p==0:
#     print("Palindrome")

#ruf work
a=9
for i in range(1,a):
    print(f"i is :  {i}")

