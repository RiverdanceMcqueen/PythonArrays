# lists are constructed in one of two ways

# The constructor method: mylist = list (("apple", "banana", "pear"))

# or utilising square brackets mylist = ["apple", "banana", "pear"]

mylist = ["cars", "bikes", "boats"]

print (mylist)

# items in a list are indexed starting at 0 and can be accessed by referencing it in []

print (mylist[0])
print (mylist[1])
print (mylist[2])

# Lists can be reversed using negative indexing, which starts from the end end of the list

print (mylist[-1]) #for last in list
print (mylist[-2]) # for second last
print (mylist[-3]) # for 3rd last

# Index ranges allow you to pick between a number of elements. Works on a last but one basis so the below
# excludes bikes

print ("Selecting a range of indexes")
print (mylist[0:1])

#leaving out the start value, the range will start at the first item

print ("A range with no start value")
print (mylist[:2])

# leaving out the end value, the range will go to the end of the list

print ("A range with no end value")
print (mylist[0:])

# Using negative indexes works the same, it goes up to but excludes the last index specified

print ("A Range with negative indexesß")
print (mylist[-3:-1])

# To check if an item is in a list, use the if function

print ("checking if item is in list")
if "cars" in mylist:
    print ("Yes it exists")

# Changing values in a list
# Changing single values is done using the index of the item to change


print ("changing list values")
changelist = ["red","green","blue","orange"]
print (changelist)
changelist[1] = "purple"
print ("now the list has changed ", changelist)

#Changing a range of values

print ("changing a range of values")
print (changelist)
changelist[1:3] = ["black", "white"]
print (changelist)

#Changing more items than you replace

print ("Changing more items than you replace")
print (changelist)
changelist[2:4] = ["amber", "beige","yellow"]
print (changelist)

#Changing less items shortens the list

print ("changing less items")
print (changelist)
changelist[0:2] = ["grey"]
print (changelist)


# INSERTING ITEMS

#To insert we use the insert() method on a list

print ("inserting new items")
print (changelist)
changelist.insert(2, "Tree")
print (changelist)