

# def my_chosen(list):  

#     print("please choose form the list below: " + list)
#     chosen='_'
#     while chosen !=0:
#         print("please choose form the list below: " + list)
#         chosen=int(input("Please make your choice: "))
#         if chosen in [1,2]:
#             print("Your choice is : {}".format(chosen))
#         else:
#             print("0.Exit")

# my_chosen(list= "1. red,2.green")

# 1.
# Create a function to calculate the "factors" and "factorial" of an int number.

# Examples
#   factors_and_factorial(6) ➞ factors = 1, 2, 3, 6; factorial= 720.

# def factors_and_factorial(k):
#     result=1
#     print("factors = ",end="")
#     for i in range (1,k+1):
#         if k>0 and k%i==0:
#             print(str(i),",",end="")
#         result=result*i
#         if i==k:
#             print(" ;factorial = " + str(result))
    
# factors_and_factorial(6)


# 2. Create a function to calculate the mean of all digits.
#   Handle both number and string cases. Convert float number to int number.

# Examples
#   mean(42) ➞ 3
#   mean('12345') ➞ 3
#   mean(666) ➞ 6
#   mean('35.9') ➞ 4
# values = "".join(char if char not in separators else " " for char in number).split()

# def func_mean(num):
#     values = "".join(char if char not in "." else "" for char in str(num))
#     sum=0
#     for i in range (0,len(values)):
#             sum=sum+ int(values[i])
#     num_mean=sum/len(values)
#     print(num_mean) 
# func_mean('77.34')

# 3.
# Create a function that performs an even-odd transform to a list, n times. Each even-odd transformation:
#     Adds two (+2) to each odd integer.
#     Subtracts two (-2) to each even integer.

# Examples
#   even_odd_transform([3, 4, 9], 3) ➞ [9, -2, 15]
#   # Since [3, 4, 9] => [5, 2, 11] => [7, 0, 13] => [9, -2, 15]
#  
#   even_odd_transform([0, 0, 0], 10) ➞ [-20, -20, -20]
#  
#   even_odd_transform([1, 2, 3], 1) ➞ [3, 0, 5]
# def even_odd_transform(num_list,times):
#     for i in range (times):
#         for j in range(0,len(num_list)):
#             if num_list[j]%2==0:
#                 num_list[j]-=2
#             else:
#                 num_list[j]+=2
#     return num_list


# print(even_odd_transform([1,2,3], 3))

# 4.Create a function that takes a string and returns the number (count) of vowels contained within it.

# Examples
#   count_vowels("Celebration") ➞ 5
#   count_vowels("Palm") ➞ 1
#   count_vowels("Prediction") ➞ 4

# Notes
#     a, e, i, o, u are considered vowels (not y).
#     All test cases are one word and only contain letters.

# def count_vowels(list):
#     count=0
#     vowel ="aeiou"
#     for i in range (0, len(list)):
#         if list[i] in vowel.casefold():
#             count+=1
#     print(count)

# count_vowels("Monday")

# 5.Additional spaces have been added to a sentence. Return the correct sentence by removing them.
# All words should be separated by one space, and there should be no spaces at the beginning or end of the sentence.

# Examples
#   correct_spacing("The film   starts       at      midnight. ")
#   ➞ "The film starts at midnight."

#   correct_spacing("The     waves were crashing  on the     shore.   ")
#   ➞ "The waves were crashing on the shore."

#   correct_spacing(" Always look on    the bright   side of  life.")
#   ➞ "Always look on the bright side of life."

# Hints
#   Use "join" and "split" functions.
def correct_space(input_string):

    separated_string=input_string.split()
    print(separated_string)

    return("*".join(separated_string))

print(correct_space("Today is    a   good day."))
# number = input("Please enter a series of numbers, using any separators you like: ")
# separators = ""

# for char in number:
#     if not char.isnumeric():
#         separators = separators +char

# # print(separators)

# values = "".join(char if char not in separators else " " for char in number).split()
# print(sum([int(val) for val in values]))





