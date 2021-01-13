# # Python program to find largest number in a list

# # formula 1
# # A list of number is given 
# list = [1, 2, 99, 34523, 3, 999, 2345]

# # Sorting the given list 'list'
# # sort() of function sorts in ascending order

# list.sort()

# # Displaying the last element of the list
# # which is the largest number in the sorted list
# print("Largest number in the list is: ", list[-1])

# # formula 2

# # A list of numbers
# # using the max function
# lis = [22, 44, 5, 66, 1123, 4, 2, 1]

# # Max methods return the largest element in the list

# print("Largest number in the list is: ", max(lis)) 

# # formula 3
# # creating empty number
# max_n = []

# # User enter the number of element to put a list
# count = int(input("Enter the How many number: "))

# # iterating till count to append all input elements in list

# for i in range(count):
#     number = int(input("Enter The number: "))
#     max_n.append(number)

# # display the largest of number in list
# print(max("Largest number in the list is", max_n))

# formula 4

# Python program to find largest 
# number in a list 
  
def myMax(list1): 
  
    # Assume first number in list is largest 
    # initially and assign it to variable "max" 
    max = list1[0] 
   
    # Now traverse through the list and compare  
    # each number with "max" value. Whichever is  
    # largest assign that value to "max'. 
    for x in list1: 
        if x > max : 
             max = x 
      
    # after complete traversing the list  
    # return the "max" value 
    return max
  
  
# Driver code 
list1 = [10, 20, 4, 45, 99] 
print("Largest element is:", myMax(list1)) 