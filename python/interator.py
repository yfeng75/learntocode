string="1234567890"

# for char in string:
    # print(char)

# print(string[0])
# my_iterator = iter(string)
# print(my_iterator)
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))

# for char in string:
#     print(char)

# for char in iter(string):
#     print(char)

menu=(["spam","egg","spam","spam","bacon","spam"])
my_iter=iter(menu)
for char in menu:
    print(next(my_iter))
