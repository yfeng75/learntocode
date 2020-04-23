menu=[]
menu.append(["egg","spam","bacon"])
menu.append(["egg","sausage","bacon"])
menu.append(["egg","spam"])
menu.append(["egg","bacon","spam"])
menu.append(["egg","bacon","sausage","spam"])
menu.append(["spam","bacon","sausage","spam"])
menu.append(["spam","egg","spam","spam","bacon","spam"])
menu.append(["spam","egg","sausage","spam"])

# print(menu)

# for meal in menu:
#     if not "spam" in meal:
#         for i in meal:
#             print(i)

# my_iter=iter(menu)
# for char in menu:
#     print(next(my_iter))
ingredient=[]
for meal in menu:
    for i in meal:
        if i not in ingredient:
            ingredient.append(i)
     
print(ingredient)

        

        
