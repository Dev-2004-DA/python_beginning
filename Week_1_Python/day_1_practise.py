# ######   Write a Program to input 2 numbers & print their sum, difference, product, quotient, and remainder   #######
# ###     taking input in diffferent lines ###


# x=int(input("Enter one number :"))
# y=int(input("Enter  2nd number :"))
# print("the sum of ",x, "and ",y ,"are = " ,x+y)
# print("the differece of ",x, "and ",y ,"are = " ,x-y)
# print("the product of ",x, "and ",y ,"are = " ,x*y)
# print("the quotient of ",x, "and ",y ,"are = " ,x/y)
# print("the remainder of ",x, "and ",y ,"are = " ,x%y)


#  ### taking input in same line ###

# x,y=map(int,input("Enter two number with a space between them :").split())    # here we assign two values to two varibles in one line , map(int,input().split()) here split func seprate the string fromwhite space into two strings and the map fnc converts the two strings into integerss
# print("the sum of ",x, "and ",y ,"are = " ,x+y)
# print("the differece of ",x, "and ",y ,"are = " ,x-y)
# print("the product of ",x, "and ",y ,"are = " ,x*y)
# print("the quotient of ",x, "and ",y ,"are = " ,x/y)
# print("the remainder of ",x, "and ",y ,"are = " ,x%y)


#   ### WAP to input side of a square and print its perimeter and area ###

# side=int(input("Enter the integer value of a side of a square:"))
# print("The perimeter and the area of the square of side ",side,"are ",4*side,"and ",side**2," respectively")



############ WAP to input 2 floaring point numbers & print their averages ############

# x,y=map(float,input("Enter two numbers with a space between them :").split())
# print("the average of ",x," and ",y,"is = ",(x+y)/2)



####### Wap to input 2 int numbers , a and b . Print true if a is greater than or equal to b , if not then False #######

a,b=map(int,input("Enter two integers wuth a space between them :").split())
print(a>=b)