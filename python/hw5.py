# answer 1
# import time
# def makebox(col,symbol):
    
#     for i in range(col+1):
#         if i==1 or i== col:
#             print(symbol*col,) 
#         elif i>1 and i<col:
#             print(symbol + ' '*(col-2) +symbol,)
# start_time=time.time()
# makebox(5,"#")
# print(time.time()-start_time)
# # makebox(3,"@")
# makebox(2,'$')
# makebox(1,'%')

#answer 2
import math
import time
start_time=time.time()
def sastry(number):
    nxt_number=number+1
    number_concat=str(number)+str(nxt_number)
    square_root= math.sqrt(int(number_concat))
    return square_root.is_integer()
    

i=1
while not sastry(i):
    i+=1
print(i)
print(time.time()-start_time)
# 3.
# Make a function that encrypts a given input with these steps:

# Input: "apple"

# Step 1: Reverse the input: "elppa"
# Step 2: Replace all vowels using the following chart:
#           a => 0
#           e => 1
#           o => 2
#           u => 3
#         # "1lpp0"
# Step 3: Add "aca" to the end of the word: "1lpp0aca"

# Output: "1lpp0aca"

# Examples
#   encrypt("banana") ➞ "0n0n0baca"
#   encrypt("karaca") ➞ "0c0r0kaca"
#   encrypt("burak") ➞ "k0r3baca"
# def encrypt(val_orign):
#     val_new=''
#     val_reverse=val_orign[::-1]
#     for i in val_reverse:
#         if i == 'a':
#             i='0'
#         elif i== 'e':
#             i='1'
#         elif i== 'o':
#             i='2'
#         elif i== 'u':
#             i='3'
#         else:
#             i = i
#         val_new+=i
#     val_new=val_new+'aca'
#     return val_new

# print(encrypt(val_orign='banana'))
# print(encrypt(val_orign="burak"))  
# print(encrypt(val_orign="alpaca"))

# 4.answer
# import timeit

# def encrypt(val_orign):
#     val_new=''
#     val_no_tail=val_orign[:-3]
#     for i in val_no_tail:
#         if i == '0':
#             i='a'
#         elif i== '1':
#             i='e'
#         elif i== '2':
#             i='0'
#         elif i== '3':
#             i='u'
#         else:
#             i = i
#         val_new+=i
#     val_new=val_new[::-1]
#     return val_new

# import time
# start_time=time.time()
# print(encrypt('0n0n0baca'))
# print(time.time()-start_time)
# print(encrypt(val_orign="0n0n0baca"))  
# print(encrypt(val_orign="0c0pl0aca"))

#print(encrypt("dsd"))
#execution_time = timeit.timeit('print(val_orign)', setup='val_orign="0n0n0baca"',number=1)
#execution_time = timeit.timeit('encrypt(val_orign)', setup='val_orign="0n0n0baca"',number=1)
#execution_time = timeit.timeit(encrypt("0n0n0baca"))
#print(execution_time)