######################################### Loops and Object #############################################
# look up table 
l = [1,2,3,4,5,5,7,8,5,3,5,9,4,2]   # lookup table

for i in l:                         # i is called iterator, can use any alphabet
    print(i + 9)
print(i)

l1 = [10, 20, 30, 40]               # look up list
l2 = ['A', 'B', 'C', 'D']
lt = [l1, l2]
print(lt)

for i in lt:                        # look up in the list above; l1, l2
    print(i)

for i in lt:
    for j in i:                     # look up within i
        print(j)
    print(i)

for i, j in enumerate (l1):         # Assign numbers to the value in the list
    print(i,j)

## Example 1

val = 0
while val <= 20: 
    print(val)
    #val = val + 2 ****             # Not working
    val += 2                        # similar to previous one

## Example 2

d = {'names': ['lukman', 'adeboye', 'soboyejo'], 'age': [21, 25, 13]}

for k in d.keys():
    print(k)

for v in d.values():
    print(v)

for m, v in d.items():                  # iterating on the topple itself providing key and values #
    print(m, v)

l1 = [10, 20, 30, 40, 50, 60]

if len(l1) < 5:                              # if and else statement
    print('I am a long list')
elif len(l1) == 6:
    print('i am 6 items long')
else:
   print('i am inside the else')

d = {'names': ['lukman', 'adeboye', 'soboyejo'], 'age': [21, 25, 13]}

for k, v in d.items():
    if k == 'names':
        print(k)
    else:
       print('I dont know what to do')

############################################################################ syntax error ommission #########################
i  = 10
o = 0

try: 
    reult = i/o
except ZeroDivisionError as e: 
    print('I cannot divide by 0', e)

l1 = [1,2,3]
print(l1)

x = -10
if x < 0:
    raise Exception('the number is lower than 0')

#x = -10
#if x < 0:
    #raise Exception('the number is lower than 0')