# age=input("enter age : ")
# new=int(age)+2
# print(new)
# age1=22
# age2=24
# print(age1+age2)

# marks=[95,98,97]
# print(marks)
# marks[1]=89
# print(marks)
# def square(x):
#     return x**2

# n=int(input("enter the number : "))
# out=square(n)
# print(f"The Square of {n} is {out}")

# i=1
# while i<18:
#     print("You are a Child")
#     i+=1
# if i>=18:
#     print("You are an Adult")

# for i in range(5):
#     print(i)

# name="Suresh"
# for i in name:
#     print(i)

# colors=["Red","Green","Blue","Yellow"]
# for color in colors:
#     print(color)
#     for i in color:
#         print(i)

# for i in range(1,11):
#     print(i)

# name=["Shreyansh","Krishna","Raj","Ramchandra"]
# name.append("Ramavatar")
# name.insert(0,"Pintu")
# for i in name:
#     print(i)
# print(name[2])
# print(len(name))

# def addnum(n1,n2):
#     print(f"The Sum of {n1} and {n2} is {n1+n2}")
# a=int(input("Enter First Number : "))
# b=int(input("Enter Second Number : "))
# addnum(a,b)

# class Car:
#     company="Toyota"
#     model="Fortuner"
#     color="White"
# c1=Car()
# print(f"The Car Company is : {c1.company} \nModel is : {c1.model} \nColour is : {c1.color} ")

# class Student:
#     def __init__(self,name,roll):
#         self.name=name
#         self.roll = roll
#         print("Adding new Students... ")
# s1=Student("Shreyansh", 56)
# print(f"Student 1 : {s1.name} \nStudent Roll No. : {s1.roll}")
# s2=Student("Shivam", 54)
# print(f"Student 2 : {s2.name} \nStudent Roll No. : {s2.roll}")

# class Student:
#     college_name="Galgotias University"
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def welcome(self):
#         print(f"Welcome Mr. {self.name}")
#     def marks_print(self):
#         print(f"Your Marks are : {self.marks}")
# s1=Student("Shreyansh",99)
# s1.welcome()
# s1.marks_print()

# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def avg_marks(self):
#         sum=0
#         for i in self.marks:
#             sum +=i
#         print(f"Your Avg Marks is {sum/3}")
# s1=Student("Shreyansh",[99,97,98])
# s1.avg_marks()

