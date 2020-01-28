# Any kind of object in python is treated as object oriented program... any kind of object
########################################## help and dir function ###########################################

s = 'john'
s.upper()                               # by typing obj.method
print(s)
print(help(s.upper))                    # help function used to show the details on the application of method... 
print(help(s.title))                    # cannot take an objetc
print(s.upper())
print(s.tittle())

# Example 1

l = [1,2,3,4,5]
print(dir(l))                           # dir is used to show the available method/functions
print(help(l.append))
l.append(100)
print(l)

# Example 2

help(l.insert)  
#l.insert(0,100)
print(l)

# Example 3
l = [1,2,3,4,5]
help(l.pop)                             # remove the last element of the list
l.pop(l[3])
print(l)                                

#Example 4

l = [1,2,3,4,4,5,6,6,7,7,100,66,99]
help(l.sort)
l.sort()
print(l)


# Example 5 for dictionary

d = {'Nigeria':'Lagos', 'Ethopia': 'Addis Ababa', 'Cameroun' : 'Yaounde'}      # create dictionary
print(d)                                                                       # Most are not taking values
print(dir(d))
print(d.keys())
print(d.values())
print(d.items())