# Create a variable and set it as an List
myList = ["Jacob", 25, "Ahmed", 80]
print(myList)

# Adds an element onto the end of a List
myList.append("Matt")
print(myList)

#find out type of myList
print(type(myList))

# Returns the index of the first object with a matching value
print(myList.index("Matt"))
print(myList.index(25))

# Changes a specified element within an List at the given index
myList[3] = 85
print(myList)

# Returns the length of the List
print(len(myList))

# Removes a specified object from an List
myList.remove("Ahmed")
print(myList)

# Removes the object at the index specified
myList.pop(1)
print(myList)

# Creates a tuple, a sequence of immutable Python objects that cannot be changed
myTuple = ("Python", )
print(myTuple)

myTuple = ("Python", "VBA", 20)
print(myTuple)