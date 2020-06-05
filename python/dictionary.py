fruit = {"orange": "a sweet, orange, citrus fruite",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": " asmall, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit",}
# print(fruit)
# print(fruit["lemon"])
# fruit["pear"]="an odd shaped apple"
# print(fruit)
# fruit["pear"]= "great"
# print(fruit)
# del fruit["lemon"]
# # del fruit
# # fruit.clear()
print(fruit)
print(fruit[orange])
# while True:
#     dic_key = input("please enter a fruit: ")
#     if dic_key =="quit":
#         break
#     if dic_key in fruit:
#         description = fruit.get(dic_key)
#         print(description)
#     else:
#         print("we don't have a " +dic_key)

# for snack in fruit:
#     print(fruit[snack])
# ordered_key =list(fruit.keys())
# ordered_key.sort()
# ordered_key =sorted(list(fruit.keys()))
# for f in ordered_key:
#     print(f + "-" +fruit[f])

# for f in sorted(fruit.keys()):
#     print(f +"-" +fruit[f])

# for val in fruit.values():
#     print(val)

# for key in fruit:
#     print(fruit[key])
# fruit_keys=fruit.keys()
# print(fruit_keys)
# fruit["tomato"] = "not nice with ice cream"
# print(fruit_keys)
# print(fruit.values())
print(fruit)
print('_'*20)
print(fruit.items())
f_tuple = tuple(fruit.items())
print('-'*50)
print(f_tuple)

for snack in f_tuple:
    item, description = snack
    print(item +" is " +description)

print(dict(f_tuple))
    