######   Write a Program to input 2 numbers & print their sum, difference, product, quotient, and remainder   #######
###     taking input in diffferent lines ###
x=int(input("Enter one number :"))
y=int(input("Enter  2nd number :"))
print("the sum of ",x, "and ",y ,"are = " ,x+y)
print("the differece of ",x, "and ",y ,"are = " ,x-y)
print("the product of ",x, "and ",y ,"are = " ,x*y)
print("the quotient of ",x, "and ",y ,"are = " ,x/y)
print("the remainder of ",x, "and ",y ,"are = " ,x%y)

### taking input in same line ###
x,y=map(int,input("Enter two number with a space between them :").split())    # here we assign two values to two varibles in one line , map(int,input().split()) here split func seprate the string fromwhite space into two strings and the map fnc converts the two strings into integerss
print("the sum of ",x, "and ",y ,"are = " ,x+y)
print("the differece of ",x, "and ",y ,"are = " ,x-y)
print("the product of ",x, "and ",y ,"are = " ,x*y)
print("the quotient of ",x, "and ",y ,"are = " ,x/y)
print("the remainder of ",x, "and ",y ,"are = " ,x%y)