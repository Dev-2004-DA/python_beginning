# print("hello")
# print('hello')
# #print("hello "dev"")                   # this will give error bcz the quostes inside and outside the string are same
# print("hello 'dev ' ")
# print('hello "dev" ')
# #print('hello 'dev'')                  # this will give error bcz the quostes inside and outside the string are same


#                          ########## Assign string to variable #########
# x='my name \nis dev'                                ##using escape sequence
# y="his name is "
# z="""hlelo sjkhsh """                                           
# w="""hello , my name is dev .                           
# how are you all , i thoought you all are good ,
# nice to see you all """                                             # using triple qutes to print multiline string
# print(x)
# print(y)
# print(z)
# print(w)


########################### BASIC OPERTAIONS ON STRING ######################
########### CONCATEATION
x="hello dev"
y='sagar soni'
z=""" good
morning """
print(x+y+z)
print(x+" "+y+z)
############ LENGTH OF STRING 
print(len(x))
############ INDEXING
print(x[0])
############SLICING OF STRING
x="Hello World"
print(x[:3])
print(x[1:3])
print(x[3:])
print(x[-5:-1])

################ string functions##################
x="hello i am dev sagar soni"
print(x.upper())
print(x.capitalize())
print(x.title())
print(x.replace("dev sagar soni","rishi soni").title())     ### chain function
print(x.replace('i','you'))
print(x.startswith('hell'))
print(x.count("a"))



####################  CONDITIONALS STATEMENT #####################
score=55
if (score > 40):
    print("You passed!")