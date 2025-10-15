# lists or arrays are mutable (changeable)
# allows to pack lots of information in one variable
# quare brackets, elements separated by comma
# lists can contain several data types

example_list = ["Here is one string", 6, 8.9, "another string 6.7"]
print(example_list)

# indexing for lists (from 0 to -1)
print(example_list[1])

# slicing
new_list = ["pizza", "banana", "cake", "coffee", "ice cream", "avocado"]
print(new_list[3:])
# it won't include the fitfh - avocado
print(new_list[2:5])


# list methods - length
print(len(new_list))

# list methods - append: adding ONE element to a list
new_list.append("something sweet")
print(new_list)


# list methods - pop: automatically removing  last element from a list (and storing it, so this wondeful element would't be lost 4ever)
x = new_list.pop()
print(new_list)
print(x)


# list methods - remove: removing  specified element from a list
new_list.remove("cake")
print(new_list)

print(type(new_list))