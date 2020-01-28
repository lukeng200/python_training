############################# Integers Explanation ##########################################
# Integers numbers can be either whole numbers or decimal numbers (or floating integer)

i = 10                              ## whole number
print (i)               

ii = int(1.2)                       ## floating integer
print(ii)

f = 1.4                 
print(f)

ii = i - f             
print(ii)

############################# Strings #######################################################
# strings are always between single or double
# double ignores any other aprostorophe within

s = 'strings'                       ## single strings ('') - cannot neglect any other aprostrophe in between otherwise use backlash
ss = "my other string"
print(s, ss)

s = 'backlash \\'                   # Backlash (\) neglect the next charater so as to avoid error
print (s)

s = 'Bob\'s cat'                    # example of backlash usage
print (s)

s = "Bob's cat and Alice's dog"     # double string ("")- neglects aprostrophe in between
print(s)

s = ''' my strings/ ' " '''         # the best (triple approstrophe) (''') = neglect every character written within
print(s)

s = 'My name is Lukman\nSoboyejo'   # \n is used to remove next character = next line
print(s)

############################## calling of variables ##############################################
name = 'Lukman'
complete_name = 'My name is %s' %name         # used to read the variable called name (method_old)
print(complete_name)

complete_name = 'My name is {}'.format(name)    # is the string object of python (method_new)
print(complete_name)

complete_name = f'My name is {name}'            # newest_method
print(complete_name)

############################## ClassWork ##########################################
# Write your complete name with age

lastname = 'Lukman'
middlename = 'Adeboye'
surname = 'Soboyejo'
Age = '27'

complete_details = f'''My name is {lastname} {surname} {middlename} and I'm {Age} old'''
print(complete_details)

############################## Boolean Operators ####################################### and conversion of sting to number and vice versa
# Almost any value is evaluated to True if it has some sort of content.
# Any string is True, except empty strings.
# Any number is True, except 0.
# Any list, tuple, set, and dictionary are True, except empty ones.
#In fact, there are not many values that evaluates to False, 
# except empty values, such as (), [], {}, "", 
# the number 0, and the value None. And of course the value False evaluates to False.

mybool = True 
mybool2 = False
print (mybool, mybool2)

s = 5                               # Boolean example
bool(5)
print(bool(s))

a = 24                             # Convert to string                           
conv = str(a)
print(str(conv))
print(type(conv))                  # how to check object you are working with

s = '1'                             # Convert to string
conv = int(s)
print(conv)
print(type(conv)) 

i = 10 
ii = 3
print(i/ii)

######################################### Types of objects such as Listing ############################################
# R = contain homogenuos list while phythos contains different integers or variables in a list

l = [1, 2, 3, 4, 5]                     # list - defined by []
print(type(l))
print(l)

ll = [1, 'A', 1.2, True]                # list of different objetcs - character, strings, integer etc..
print(ll)

l1 = [1,2,2,2,2,1,1,1,1,3,3,3,3,3,3,3]  # convert to sets 
s1 = set(l1)
print(s1)
print(type(s1))

lclean = list(s1)                       # convert to list
print(lclean)
print(type(lclean))

################################################# Indexing ######################################################
# python indexing starts from 0 and the last value can be selected with -1
# R starts from 1
# To select an index you use square bracket []

l1 = [1,2,2,2,2,1,1,1,1,3,3,3,3,3,3,3]
l1[1]                                   # Indexing
print(l1[1])

l1[0] = 'A'                             # assign value to the selected index
print(l1)
print(l1[-1])                           # indexing last value of l1
print(l1[0:3])

print(len(l1))                          # length of an objects

l = [1,2,3,4,5,6,7,8,9,10]
print(l[0])

print(l[:-2])                           # ommitting or deselecting the last two elements

############################## concatenation of objects #############################################

l1 = [1,2,3]                            # combining the list
l2 = [4,5,6,7,8]
lt = l1 + l2
print(lt)

ltt = l1 * 4                            # replicate of the list
print(ltt)

lm = [l1, l2]                           # indexing from the list above l1 and l2
print(lm[0][1])

del lm[0]                               # how to delete and delete from list - l1 and l2
print(lm)

###################################### Mutability ##############################################
# integers or float are not mutable object but list are mutable

l5 = [2, '8.5', 3, 5, 7, 8, 9]

l5[1] = 100                             # Assigned value
print(l5) 

################################### tuple ########################################################
# something that cannnot be changed e.g month 

t = (1,2,3)                             # defined with ()
print(t)
print(type(t))

#t[0] = 10                               #cannot work because it cannot be changed

######################################## Dictionary #######################################
# very robust compared to list and tupple
# it contains keys and values
# Make sure you give different names to different variables
# Dictionaries are mutable

d = {'name' : 'lukman', 'age': '27'}        # defined with curly bracket
print(d)

d['name'] = 'Adeboye'                       # overide = the values by indexing the key
print(d['name'])

d = {'names' : ['lukman', 'soboyejo', 'john']}  # You can define as many key as you want
print(d['names'][0])

d = {'names' : ['lukman', 'soboyejo', 'john'], 'number' : '30'} # also can define dictionary with various keys
print(d)