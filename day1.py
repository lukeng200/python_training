# integers
#i = 10 
#print (i)

#ii = int(1.2)
#print(ii)

# floating
#f = 1.4
#print(f)

#ii = i - f
#print(ii)

# strings_are always between single or double, double ignores any other aprostorophe

#s = 'strings'
#ss = "my other string"

#print(s, ss)

#s = 'backlash \\' # Baclash escape the next word or character
#print (s)

#s = 'Bob\'s cat'
#print (s)

#s = "Bob's cat and Alice's dog"
#print(s)

#s = ''' my strings/ ' " ''' # best

#s = 'My name is Lukman \n Soboyejo' #\n is used to remove next character 
#print(s) 

#name = 'Lukman'
#complete_name = 'My name is %s' % name # %s - used to read the variable called name
#print(complete_name)

#complete_name = 'My name is {}'.format(name) # is the string object of python
#print(complete_name)

#complete_name = f'My name is {name}'
#print(complete_name)

# Class Work 1

#name = 'Lukman' 
#surname = 'Soboyejo'
#Age = '27'

#complete_name = f'My name is {name}'
#print(complete_name)

#complete_surname = f'My surname is {surname}'
#print(complete_surname)

#complete_Age = f'My Age is {Age}'
#print(complete_Age)

#complete_details = f'My details are shown as follows; Name, Surname, Age {name, surname, Age}'
#print(complete_details)

#complete_details = f'''My name is {name} {surname} and I'm {Age} old'''
#print(complete_details)

#Boolean and conversion of sting to number and vice versa

#mybool = True 
#mybool2 = False
#print (mybool, mybool2)

#i=1
#print(str(i))

#s = '1'
#conv = int(s)

#s = 'False'
#bool(s)
#print(bool(s))

#type of object you can work woth

#print(type(i))

#i = 10 
#ii = 3
#print(i/ii)
 
######### Object = List an example of an object... R = contain homogenuos list, phythos contains different integers in a list
l = [1, 2, 3, 4, 5]
#print(type(l))
#print(l)

ll = [1, 'A', 1.2, True]
#print(ll)

print(l != ll)

#Arbitrary 
#l1 = [1,2,2,2,2,1,1,1,1,3,3,3,3,3,3,3]
#print(l1)

#s1 = set(l1)
#print(s1)
#print(type(s1))

#lclean = list(s1)
#print(lclean)
#print(type(lclean))

# Indexing
#l1[1]
#print(l1[1])

#l1[0] = 'A'
#print(l1)
#print(l1[-1])
#print(l1[0:3])
#print(len(l1)) # length of the words

#l = [1,2,3,4,5,6,7,8,9,10]
#print(l[0])

#print(l[:-2]) # ommitting the last two elements

#concatenation of values
#l1 = [1,2,3]
#l2 = [4,5,6,7,8]
#lt = l1 + l2
#print(lt)

#ltt = l1 * 4
#print(ltt)

# list inside list 
#lm = [l1, l2]
#print(lm[0][1])
#del lm[0]
#print(lm)

#Mutability = integers or float are not mutable object but list are mutable


#tuple cannnot be changed e.g month defined with ()
#t = (1,2,3)
#print(t)
#print(type(t))

# t[0] = 10 #cannot work

#Dictionary very complex compared to list it contains keys and values
# Give different name different name
#Dictionaries are mutable
#d = {'name' : 'lukman', 'age': '33'}
#print(d)

#d['name'] = 'Adeboye'
#print(d['name'])

#overide = dictionary and the key
#You can define as many key
#d = {'names' : ['lukman', 'soboyejo', 'john']}
#print(d['names'][0])

#define dictionary with  various keys
#d = {'names' : ['lukman', 'soboyejo', 'john'], 'number' : '30'}
#print(d)