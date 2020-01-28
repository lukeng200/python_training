#Loops and Object

#l = [1,2,3,4,5,5,7,8,5,3,5,9,4,2]

# for i in l: # i is called iterator, can use any object
    #print(i + 9)

#print(i)

#l1 = [10, 20, 30, 40]
#l2 = ['A', 'B', 'C', 'D']
#lt = [l1, l2]

#for i in lt:
    #print(i)

#for i in lt:
    #for j in i:
        #print(j)
    #print(i)

#for i, j in enumerate(l1):
    #print(i,j)

#val = 0

#while val <= 20: 
    #print(val)
    #val = val + 2
    # val += 2 similar to previous one

# d = {'names': ['lukman', 'adeboye', 'soboyejo'], 'age': [21, 25, 13]}

#for k in d.keys():
    #print(k)

#for v in d.values():
    #print(v)

# iterating on the topple itself providing key and values
#for m, v in d.items():
    #print(m, v)

#l1 = [10, 20, 30, 40, 50, 60]

#if len(l1) < 5:
    #print('I am a long list')
#elif len(l1) == 6:
    #print('i am 6 items long')
#else:
   # print('i am inside the else')

d = {'names': ['lukman', 'adeboye', 'soboyejo'], 'age': [21, 25, 13]}

for k, v in d.items():
    if k == 'names':
        for i in v:
            print(i)
    else:
       print('I dont know what to do')

### syntax error
#i  = 10
#o = 0

#try: 
    #reult = i/o
#except ZeroDivisionError as e: 
    #print('I cannot divide by 0', e)

#l1 = [1,2,3]
#print(l1)

#x = -10
#if x < 0:
    #raise Exception('the number is lower than 0')