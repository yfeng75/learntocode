name=input("What is your name? ")
age = int(input("How old are you?"))

#if age >= 16 and age <= 65:
# if 18<= age  <=30 and name !="":
if age in range(16,66) and name != "":
    print("Welcome to the holiday, {}".format(name))
else:
    print("Sorry, you are not in the right age")

# print("-" * 80)

# if age <16 or age >65:
#      print("Enjoy your free time")
# else:
#     print("Have a good day at work")


