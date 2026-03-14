'''Create a list of your favorite fruits. Add one more fruit using append, then insert 
another fruit at the second position using insert(). Finally, remove the last fruit from
the list. Print the list after each step.'''

# list of fruits
print("***List of fruits***")
fruits = ['Apple', 'Cherry', 'Mango']
print(fruits)

# add one more fruit using append
print("\n***Add Fruit***")
fruits.append('Banana')
print(fruits)

# insert another fruit at the second position using insert()
print("\n***Insert Fruit***")
fruits.insert(1, 'Grapes')
print(fruits)

#remove last fruit from the list
print("\n***Remove Last Fruit***")
fruits.pop()
print(fruits)