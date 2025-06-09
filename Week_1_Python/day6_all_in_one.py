# print("helo ,I","dev" ,sep="-")
# print("helo ,I ","dev")
# print("hello","dev",end="++++")
# print("good")

# #  EXERCISE 1
# ######### CALCULATOR USING PYTHON ############
# x,y=map(int,input("Enter two numbers with a space btween the : ").split())
# print("ADDITION IS= ",x+y)
# print("SUBTRACTION IS= ",x-y)
# print("MULTIPLICATION IS= ",x*y)
# print("DIVISION IS= ",x/y)
# print("QUOTINT IS= ",x//y)
# print("REMAINDER IS= ",x%y)

# #$$$$$$$$$$$$ STRINGS $$$$$$$###

# x="Dev Sagar Soni"
# print(x[0:3],x[4:9] )
# y=len(x[0:3])
# print(y)
# a="harry"
# print(a[-4:-2])

# ##$$$$    STRINGS METHODS $$$$$###

# x="dev sagar soni"
# print(x.upper())
# print(x.title())
# print(x.capitalize())
# print(x.capitalize())
# print(x)
# print(x.replace("dev","ved"))
# print(x.capitalize().center(50))
# print(x.index("dev"))


# #####33 Match case ##########3
# day = "Saturday"
# x=20
# # Match statement
# match day:
#     case "Monday" | "Saturday" if x==20:
#         print("Start of the work week.")
#     case "Friday":
#         print("End of the work week.")
#     case "Sunday":
#         print("Rest day.")
#     case _:
#         print("A regular day.")

# ##### LOOOPSSSSSS#########

# x= "DEV"
# i=0
# for items in x:
#     if(items== "V" ):
#         print("yeah , you find it")



#  ### while loop taking input till user enetr valus greater than or equal to 30 #########
# i=0
# while(i<30):
#     i=int(input("enter"))
#     i+=1

# print("loop ended")    


# #######3 BREAK AND CONTINUE ##########33

# for item in range(20):
   
#     if(item==13):
#         continue
#     elif(item==17):
#         break
#     print(item)
    

# def name(f_name ,m_name="sagar",l_name="soni"):
#     print("hello, ",f_name, m_name ,l_name )

# name("dev")
# name(f_name="dev")
# name("dev",m_name="kumar")

# def avg(a,b,c):
#     print("the avg is : ",(a+b+c)/3)

# avg(c=2,a=1,b=5)


# def avgs(**numbers):
#     print(type(numbers))
#     sum=0
#     for i in numbers:
#         sum=sum + i
#     print("the avg is : ",sum/(len(numbers)))   

# avgs(a=1,b=2)    



###### LISTS search for an elements ########

# x=[1,2,3,4,5,6,7]
# i=0
# ###### by if statement ######
# if 7 in x :
#     print("yes")
# else : 
#     print("No ")    

######## BY loop
# for itmes in x:  
#     if(x[i]==7):
#         print("it is present at index =",i)
#     else: 
#         print("not here")
#     i+=1
# ###########################

# z="dev sagar "
# print("ev" in z)
# print("ev" not in z)

# ########### Jump ind
# # exing ##########

# x=[1,2,3,4,5,6,7,8,9,10]
# print(x[1:len(x):2])

# ####### TUPLE #########
# x=(1,2,3,4,5,6)
# y=x.index(3,1,2)
# print(x[::2])
# print(y)

########## EXERCISE 2 CREATE A PROGRAM CAPABL OF DISPLAYING QUESTION TO THE USR LIKE KBC ###########
########## USE list data type to store the question and there correct answer #########
########## Display the final amoutnt the person is taking home afetr playing the game #####3 

print("###########Welcome to KBC##########".center(50))
que=["what is the capital of india ?".title(),"what is the capital of up ?".title()]
ans=[" New Delhi","Lucknow"]

print(que[0],"\nA. New Delhi\nB. Mumbai\nC. Kolkata\nD. Lucknow")  
x=input("your answer is : ")
A=ans[0]
print(A)
if(x==ans[0]):
    print("CORRECT !!!")
   
else:
    print("You are eliminated")    
