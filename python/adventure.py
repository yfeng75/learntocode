# available_exits = ["north","south","east","west"]

# chosen_exit = ""
# while chosen_exit not in available_exits:
#     chosen_exit = input("Please choose a diection: ")
#     if chosen_exit.casefold() == "quit":
#         print("game over")
#         break 

# print("aren't you glad you got out of there")

# i=0
# while i%11 !=0 or i==0:
#     print(i)
#     i+=7
#     print(i)
    
for i in range(0, 21):
    if i%3!=0 and i%5!=0:
        print(i)
       