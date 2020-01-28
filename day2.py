# r = range (1, 100, 2)          # range definition
# print(r)

# l = list(r)
# print(l)

# d = {'a': range(1,50), 'b': range(1,20)}        #creating dictionary

# ra = list(range(1,50))                          # creating list
# rb = list(range(1,20))
# d = {'a': ra, 'b': rb}

# for k, v in d.items():                          # looping
#     if k == 'a':
#         for i in v:
#             if i > 25:
#                 print(i)
#             else:
#                 print('no values')
#     if k == 'b':
#     # else
#         for i in v:
#             if i < 10:
#                 print(i)

# print(d['a'])

# l = []                          # empty list for creating a new list

# for i in d['a']:
#     if i > 25:
#         l.append(i)
# print(l)

########################################### function #######################################

# def my_function():
#     print('Hi Python')
#     '''
#     This function prints something
#     This function is shit
#     '''

# my_function()

# print(help(my_function))

# def my_function2(s):
#      print(s)

# my_function2('Lukman')

# def my_function3(name, age= 27):
#     print(name, age)

# my_function3('Matteo')

# def multiply(x, y):
#     result = x * y
#     print(result)

# multiply(10, 12)

# l = [10,2,3,5]

# def multiply2(*args):            # *args tells python to read more than one argumensts INDIVIDUALLY
#      v = 1
#      for i in args:
#          v = v * i
#      return v
  
# mynumber = multiply2(*l)
# # multiply2(1,30,90,4,3)
# # multiply2(*l)                   # Unpack the list - it takes single elements in the list

# L = 4
# B = 6

# def rect_area(length, breadth):
#     calculation = length * breadth

#     return calculation

# my_area = rect_area(10, 19)
# print(my_area)


# def shape_area(shape, width, height):
#     if shape == 'rectangle':
    
#         calculation = width * height
        
#     if shape == 'triangle':
    
#         calculation = width * height / 2

#     else:
#         print('I dont know the shape')
        
#     return calculation

# area = shape_area('triangle', 100, 3)
# print(area)


# def fah_temp(celcius):
#     f = (celcius * 9 / 5) + 32
#     return f

# a = fah_temp(100)
# print(a)

# lc = [10, 0, 100, 50]

# def fah_temp2(*args):
#     l = []
#     for c in args:
#         calculation = (c * 9 / 5) + 32
#         l.append(calculation)
#     return l

# lc = [10, 0, 100, 50]
# my_f = fah_temp2(2, 5)
# print(my_f)

# my_f = fah_temp2(*lc)
# print(my_f)