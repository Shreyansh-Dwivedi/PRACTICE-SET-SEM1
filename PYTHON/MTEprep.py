#Date: 07-12-2023(One day before MTE of 1st semester B.TECH) 
#1
# a=int(input("Enter the 1st no. : "))
# b=int(input("Enter the 2nd no. : "))
# print(f"Sum is : {a+b} ")
#2
# a=int(input("Enter the 1st no. : "))
# b=int(input("Enter the 2nd no. : "))
# c=int(input("Enter the 3rd no. : "))
# print("Average of the three number  is  : "+str((a+b+c)//3))
#3
# a=int(input("Enter 1st subject marks : "))
# b=int(input("Enter 2nd subject marks : "))
# c=int(input("Enter 3rd subject marks : "))
# d=int(input("Enter the 4rth marks : "))
# e=int(input("Enter the 5th subject marks :"))
# print(f"Sum of marks is : {a+b+c+d+e}")
# print("Percentage of Student is : "+str((a+b+c+d+e)/5))
#4
# r=int(input("Enter radius of the Circle : "))
# print("Are of the Circle is : "+str(3.14*(r**2)))
#5
# f=int(input("enterthe temp is farenheit : " ))
# print(f"The temperature if Celcius is : {(f-32)/1.8}")
#6
# a=int(input("Enter the 1st number : "))
# b=int(input("Enter the 2nd number : "))
# print(f"a = {a}  b = {b}")
# a=a+b
# b=a-b
# a=a-b
# print(f"The swapped numbers are  : \n a = {a} \n b = {b}")
#7
#print("Hello,Python!")
#8
# a=int(input("Enter the limiting number : "))
# for i in range(0,a):
#     print(i*i)
#8
# a=int(input("Enter the Number to chech how many times it is divisible by 3 before it is <=10 : "))
# b=a
# s=0
# while b>10:
#     b=b/3
#     s=s+1
# print(f"{s} times ")
#9
# a=int(input("Enter the  number : "))
# b=a
# rev=0
# while b>0:
#     r=b%10
#     rev = (rev*10)+r
#     b=b//10
# print("the Rev is : ", (rev))
#10
a=97
for i in range(1,5):
    a=97
    for j in range(1,i+1):
        print(chr(a),end="")
        a=a+1
    print('\n')


