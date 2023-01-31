shopping_list = ["Milk", "eggs", "bread", "fruit", " cheese"]
# print(type(shopping_list))
# print(shopping_list)
# print(shopping_list[0])
print(shopping_list[-1])
# # rewriting a value on the list
# shopping_list[0] = "sugar"
# print(shopping_list[0])

# list methods

# add to list

# shopping_list.append("vegetables")
# print(shopping_list)
# print(shopping_list[5])
# print(len(shopping_list))
#
# # remove from a list
#
# shopping_list.remove("bread")
# print(shopping_list)
# print(len(shopping_list))
#
# # get rid of the last entry
# shopping_list.pop()
# print(shopping_list)
# print(len(shopping_list))

# mixed data type lists
# mixture = [1, 2, 3.5, "one", "two", "three"]
# print(mixture)
# #list slicing
#
# print(mixture[1:3])
# print(mixture[-2::]) # double colon reverses the order.
# print(mixture[::2]) # bounces over the amount of indexes specified
#
# #Tuples same as lists, except teh are immutable (you cant change any of the data from the list)
# # uses. they are useful for elements that you want ensuire stays the same.
#
essentials = ("bread", "eggs", "milk")
print(essentials)
print(type(essentials))
#
# # essentials[0] = "beans"