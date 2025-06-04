############## WAP TO INPUT USER'S FIRST NAME AND PRINT ITS LENGTH ###############
# x=input("Enter your first name: ")
# print("The length is = " , len(x))


############## WAP TO FIND THE OCCURENCE OF $ IN A STRING ###############

# x=input("Enter any string: ")
# print("the occurence the dollar symbol in this string is : ",x.count('$'))

############## WAP TO GRADE STUDENTS BASED ON THEIR MARKS ###############

x=int(input("Enter your marks : "))
if(x>=90):
    print('GRADE ="A"')
elif(x>=80 and x<90):
    print('GRADE "B"')
elif(x>=70 and x<80 ):
    print('GRADE "C"')
else:
    print('GRADE "D"')