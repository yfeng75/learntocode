# 1.
# Create a function that determines whether a number is Oddish or Evenish. 
# A number is Oddish if the sum of all of its digits is odd, and a number 
# is Evenish if the sum of all of its digits is even. If a number is Oddish,
#  return "Oddish". Otherwise, return "Evenish".

# For example, oddish_or_evenish(121) should return "Evenish", since 1 + 2 + 1 = 4. 
# oddish_or_evenish(41) should return "Oddish", since 4 + 1 = 5.

# Examples
#   oddish_or_evenish(43) ➞ "Oddish"
#   oddish_or_evenish(373) ➞ "Oddish"
#   oddish_or_evenish(4433) ➞ "Evenish"
# answer:
# def oddish_or_evenish(number):
#     sum=0
#     i=1
#     while True:
#         num=number//(10**i)
#         sum+=num 
#         i+=1
#         if num==0:
#             break 
#     sum=sum+number%10
#     if sum%2 ==0:
#         print("Evenish")
#     if sum%2 ==1:
#         print('Oddish')

# oddish_or_evenish(43)
# oddish_or_evenish(373)
# oddish_or_evenish(4433)

# 2.
# In each input list, every number repeats at least once, except for two.
# Write a function that returns the two unique numbers.

# Examples
#   returnUnique([1, 9, 8, 8, 7, 6, 1, 6]) ➞ [9, 7]
#   returnUnique([5, 5, 2, 4, 4, 4, 9, 9, 9, 1]) ➞ [2, 1]
#   returnUnique([9, 5, 6, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8]) ➞ [5, 6]
def returnUnique(number_list):
    freq_count={}
    unique=[]
    for i in number_list:
        if i in freq_count:
            freq_count[i]+=1
        else:
            freq_count[i]=1
    for i in freq_count:
        if freq_count[i]==1:
            unique.append(i)
    return unique
    
    # no_dup=[]
    # for i in range(len(number_list)):
    #     number1=number_list[0]
    #     number_list.pop(0)
    #     if number1 not in number_list:
    #         no_dup.append(number1)
    #     number_list.append(number1)
    # return no_dup


print(returnUnique([1, 9, 8, 8, 7, 6, 1, 6]))
print(returnUnique([5, 5, 2, 4, 4, 4, 9, 9, 9, 1]))
print(returnUnique([9, 5, 6, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8]) )



