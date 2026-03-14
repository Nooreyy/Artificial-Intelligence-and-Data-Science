'''Create a tuple with 5 numbers. Try to change the first number by converting the tuple 
into a list and back to tuple. Print both the original and modified tuple.'''

# create a tuple with 5 numbers
print("***Tuple of numbers***")
numbers_tuple = (1, 2, 3, 4, 5)
print(numbers_tuple)

# convert the tuple into a list
print("\n***Convert Tuple to List***")
number_list = list(numbers_tuple)
print(number_list)

#change the first number
print("\n***Change First Number***")
number_list[0] = 10
print(number_list)

# convert back to tuple
print("\n***Convert List back to Tuple***")
modified_tuple = tuple(number_list)
print(modified_tuple)