############## WAP TO INPUT USER'S FIRST NAME AND PRINT ITS LENGTH ###############
# x=input("Enter your first name: ")
# print("The length is = " , len(x))


############## WAP TO FIND THE OCCURENCE OF $ IN A STRING ###############

# x=input("Enter any string: ")
# print("the occurence the dollar symbol in this string is : ",x.count('$'))

############## WAP TO GRADE STUDENTS BASED ON THEIR MARKS ###############

# x=int(input("Enter your marks : "))
# if(x>=90):
#     print('GRADE ="A"')
# elif(x>=80 and x<90):
#     print('GRADE "B"')
# elif(x>=70 and x<80 ):
#     print('GRADE "C"')
# else:
#     print('GRADE "D"')


################ WAP to check if a number is entered by user is odd or even ################    

# x=int(input("Enter an integer number : "))
# if(x%2 ==0):
#     print("The number is EVEN.")
# else:
#     print("The number is ODD.")    


################# WAP to find the greatest of 3 numbers entered by the user #################

x,y,z= map(float,input("enter three distinct number with a blank space after each number :").split())
if(x>y and x>z): print("the greatest among the thr45ee is :",x)
elif(y>x and y>z): print("the greatest among the three is :",y)
else: print("the greatest among the three is: ",z)