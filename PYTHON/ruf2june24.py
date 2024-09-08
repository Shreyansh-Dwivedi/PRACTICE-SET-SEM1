class person:
    # name = "Shreyansh"
    # occupation = "Software Devloper"
    # net_worth = 10
    # def info(self):
    #     print(f"{self.name} is a {self.occupation}")
    def __init__(self,name,occupation):
        self.name = name
        self.occupation = occupation
        print(f"{self.name} is a {self.occupation}")


a=person("Shreyansh","Software Developer")
b=person("Kriti","HR")
# a.name="Shubham"
# a.occupation="Accountant"
# print(a.name) 
# print(a.occupation)
# a.info()