# 1.
# Create a function to calculate the "max", "min", and "mean" of a list.

# Examples
#   max_min_mean([6,1,5,3,4,2]) ➞ max = 6; min = 1; mean = 3.5.

# def max_min_mean(value):
#     min=value[0]
#     max=value[0]
#     sum=value[0]
#     for i in value:
#         if i<min:
#             min=i
#         if i>max:
#             max=i
#         sum=sum+i
#     mean=sum/len(value)
#     print("max= {}".format(max),"min={}".format(min),"mean={}".format(mean) )

# max_min_mean(value=[6,1,5,3,4,2])
# 2.
# Given an unsorted list, create a function that returns the nth smallest element (the smallest element is the first smallest, the second smallest element is the second smallest, etc).

# Examples
#   nth_smallest([1, 3, 5, 7], 1) ➞ 1
#   nth_smallest([1, 3, 5, 7], 3) ➞ 5
#   nth_smallest([1, 3, 5, 7], 5) ➞ None
#   nth_smallest([7, 3, 5, 1], 2) ➞ 3

# Notes
#     n will always be >= 1.
#     Each number in the array will be distinct (there will be a clear ordering).
# #     Given an out of bounds parameter (e.g. a list is of size k), and you are asked to find the m > k smallest element, return None.
# def nth_smallest(value,n):
#     value_sorted=sorted(value)
#     if n<=len(value_sorted):
#         print(value_sorted[n-1])
#     else:
#         print("none")
#     print(value)
# nth_smallest(value=[7, 3, 5, 1], n=2)
#sorted() change the list order, .sort() is an object
#  3.
# Write a function that takes a list and a number as arguments. Add the number to the end of the list, then remove the first element of the list. The function should then return the updated list.

# Examples
#   next_in_line([5, 6, 7, 8, 9], 1) ➞ [6, 7, 8, 9, 1]
#   next_in_line([7, 6, 3, 23, 17], 10) ➞ [6, 3, 23, 17, 10]
#   next_in_line([1, 10, 20, 42 ], 6) ➞ [10, 20, 42, 6]
#   next_in_line([], 6) ➞ "No list has been selected"
# def next_in_line(value,add):
#     if len(value)>0:
#         value.append(add)
#         value=value[1:]
#         print(value)
#     else:
#         print("No list has been selected")
# next_in_line([5, 6, 7, 8, 9], 1)
# next_in_line([], 1)

# 4.
# Create a function that takes a list of numbers between x1 and x2 and returns the missing numbers.
#   Case 1 : Only one number will be missing.
#   Case 2 : More than one number will be missing.

# Examples (assume x1=1, and x2=10)
#   missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10]) ➞ 5
#   missing_num([7, 2, 3, 6, 5, 9, 1, 4, 8]) ➞ 10
#   missing_num([10, 5, 1, 2, 6, 8, 3, 9]) ➞ 4, 7

# Notes
#     The list of numbers will be unsorted (not in order).

# def missing_num(value):
#     x1= min(value)
#     x2= max(value)
#     for i in range(x1,x2):
#         if i not in value:
#             print(i)

# missing_num(value=[10, 5, 1, 2, 6, 8, 3, 9])

# 5.
# Given two lines, determine whether or not they are parallel.
# Lines are represented by a list [a, b, c], which corresponds to the line ax+by=c.

# Examples
#   lines_are_parallel([1, 2, 3], [1, 2, 4]) ➞ true
#     # x+2y=3 and x+2y=4 are parallel.
#   lines_are_parallel([2, 4, 1], [4, 2, 1]) ➞ false
#     # 2x+4y=1 and 4x+2y=1 are not parallel.
#   lines_are_parallel([0, 1, 5], [0, 2, 15]) ➞ true
#     # Lines are parallel to x axis.

# Notes
#     All the test cases use valid input (so no lists of the wrong size, for example).
#     All the coefficients will be integers (whole numbers).
#     Coefficients can be 0.
# def lines_are_parallel(line1,line2):
#     if line1[1]!=0 and line2[1]!=0:
#         slope1=line1[0]/line1[1]
#         slope2=line2[0]/line2[1]
#         if slope1==slope2: 
#             print("Lines are parallel")
#         else:
#             print("lines are not parallel")
#     elif line1[1]==0 and line2[1]==0:
#         print("Lines are parallel")
#     else:
#         print("lines are not parallel")
# lines_are_parallel([1, 2, 3], [1, 2, 4])
# lines_are_parallel([2, 4, 1], [4, 2, 1])    
# lines_are_parallel([0, 1, 5], [0, 2, 15]) 
# lines_are_parallel([2, 0, 1], [4, 0, 1])  
# lines_are_parallel([2, 1, 1], [4, 0, 1]) 
   
# 6. AMC8 2017 Problem 20
# An integer between 1000 and 9999, inclusive, is chosen at random. How may ways that it is an odd integer whose digits are all distinct? 
def count_ways():
    count=0
    for i in range(1000,9999):
        if i%2==1:
            x=str(i)
            is_unqiue=True
            for j in range(0,len(x)):
                for k in range (j+1,len(x)):
                    if x[j]==x[k]:
                        is_unqiue=False
                        break
                if (is_unqiue==False):
                    break
          
            if is_unqiue==True:
                count+=1
    print(count)


    count=0
    for i in range(1000,9999):
        if i%2==1:
            x=str(i)
            is_unique=True
            for j in range(0,len(x)):
                if (x[j] in x[j+1:len(x)]):
                    is_unique=False
            if is_unique==True:
                count+=1        
    print(count)

count_ways()






                    
                 















