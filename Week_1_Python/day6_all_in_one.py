# # print("helo ,I","dev" ,sep="-")
# # print("helo ,I ","dev")
# # print("hello","dev",end="++++")
# # print("good")

# # #  EXERCISE 1
# # ######### CALCULATOR USING PYTHON ############
# # x,y=map(int,input("Enter two numbers with a space btween the : ").split())
# # print("ADDITION IS= ",x+y)
# # print("SUBTRACTION IS= ",x-y)
# # print("MULTIPLICATION IS= ",x*y)
# # print("DIVISION IS= ",x/y)
# # print("QUOTINT IS= ",x//y)
# # print("REMAINDER IS= ",x%y)

# # #$$$$$$$$$$$$ STRINGS $$$$$$$###

# # x="Dev Sagar Soni"
# # print(x[0:3],x[4:9] )
# # y=len(x[0:3])
# # print(y)
# # a="harry"
# # print(a[-4:-2])

# # ##$$$$    STRINGS METHODS $$$$$###

# # x="dev sagar soni"
# # print(x.upper())
# # print(x.title())
# # print(x.capitalize())
# # print(x.capitalize())
# # print(x)
# # print(x.replace("dev","ved"))
# # print(x.capitalize().center(50))
# # print(x.index("dev"))


# # #####33 Match case ##########3
# # day = "Saturday"
# # x=20
# # # Match statement
# # match day:
# #     case "Monday" | "Saturday" if x==20:
# #         print("Start of the work week.")
# #     case "Friday":
# #         print("End of the work week.")
# #     case "Sunday":
# #         print("Rest day.")
# #     case _:
# #         print("A regular day.")

# # ##### LOOOPSSSSSS#########

# # x= "DEV"
# # i=0
# # for items in x:
# #     if(items== "V" ):
# #         print("yeah , you find it")



# #  ### while loop taking input till user enetr valus greater than or equal to 30 #########
# # i=0
# # while(i<30):
# #     i=int(input("enter"))
# #     i+=1

# # print("loop ended")    


# # #######3 BREAK AND CONTINUE ##########33

# # for item in range(20):
   
# #     if(item==13):
# #         continue
# #     elif(item==17):
# #         break
# #     print(item)
    

# # def name(f_name ,m_name="sagar",l_name="soni"):
# #     print("hello, ",f_name, m_name ,l_name )

# # name("dev")
# # name(f_name="dev")
# # name("dev",m_name="kumar")

# # def avg(a,b,c):
# #     print("the avg is : ",(a+b+c)/3)

# # avg(c=2,a=1,b=5)


# # def avgs(**numbers):
# #     print(type(numbers))
# #     sum=0
# #     for i in numbers:
# #         sum=sum + i
# #     print("the avg is : ",sum/(len(numbers)))   

# # avgs(a=1,b=2)    



# ###### LISTS search for an elements ########

# # x=[1,2,3,4,5,6,7]
# # i=0
# # ###### by if statement ######
# # if 7 in x :
# #     print("yes")
# # else : 
# #     print("No ")    

# ######## BY loop
# # for itmes in x:  
# #     if(x[i]==7):
# #         print("it is present at index =",i)
# #     else: 
# #         print("not here")
# #     i+=1
# # ###########################

# # z="dev sagar "
# # print("ev" in z)
# # print("ev" not in z)

# # ########### Jump ind
# # # exing ##########

# # x=[1,2,3,4,5,6,7,8,9,10]
# # print(x[1:len(x):2])

# # ####### TUPLE #########
# # x=(1,2,3,4,5,6)
# # y=x.index(3,1,2)
# # print(x[::2])
# # print(y)

# ########## EXERCISE 2 CREATE A PROGRAM CAPABL OF DISPLAYING QUESTION TO THE USR LIKE KBC ###########
# ########## USE list data type to store the question and there correct answer #########
# ########## Display the final amoutnt the person is taking home afetr playing the game #####3 

# ### Let's begin ## creating list varibales of questions , options , answer
# # print("---Welocome to kaun banega cororepati---".upper().center(100))
# # que=["number of electrons in carbon atom?".title(),"no of days in a non leap year?".title(),"capital of india".title()]
# # opt=["A. 4","B. 8","C. 6","D. 12","A. 368","B. 365","C. 366","D. 356","A. New delhi".title(),"B. lucknow".title(),"C. kolkata".title(),"D. mumbai".title()]
# # ans=[opt[2],opt[5],opt[8]]

# # print("hello , ",input("Your name is :"))
# # print("Are you ready to begin?,(Y/N)" )
# # if(input()=="Y"):                                                       #   
# #     print("That's the spirit, Let's begin .")                           #        
# #     print("\n\n\nQ1.",que[0],"\n")                                      #q1 starts here
# #     for item in opt[0:4]:                                               #  used for loop to print options by using their index
# #         print(item)                                                     #
# #     C=ans[0]                                                            # assinging correct option numbeer to the correc anwer idx    
# #     if(input("Enter option=")=="C"):                                    #    runnning if statemnt 
# #         print("CORRECT".center(40))
# #         print("Lets come to next question")                                 
# #         print("\n\n\nQ2.",que[1],"\n")                                  # q2 starts here insisde a if statement
# #         for item in opt[4:8]:                                           #used for loo to print options by using their index    
# #             print(item)
# #         B=ans[1]                                                        # assinging correct option numbeer to the correc anwer idx 
# #         if(input("Enter option=")=="B"):
# #                 print("CORRECT".center(40))
# #                 print("Lets come to next question")
# #                 print("Q3.",que[2])                                      # q3 starts here           
# #                 for item in opt[8:12]:                                     # printing  its option using loops and options index 
# #                     print(item)
# #                     A=ans[2]                                                # assinging correct option numbeer to the correc anwer idx   
# #                 if(input("Enter option=")=="A"):
# #                     print("CORRECT".center(40))
# #                     print("game is ended , thankyou for playing with us".upper())
# #                 else:
# #                      print("ELIMINATED")    
# #         else:
# #                 print("ELIMINATED")        
# #     else:
# #         print("ELIMINATED")
# # else:
# #     print("LOSER")    



# # x=45/7
# # print(type(x))
# # print(f"{x:.2f}")


# # x={12:79,133:44}
# # y={"name":"dev",12:78}
# # x.update(y)
# # print(x)
# # x.pop("name")
# # print(x)
# # x.clear()
# # print(x)

# ########## exception handling  #######3
# # try:
# #     x=int(input())
# # except ValueError as e:
# #     print("you cause an error",e)

# # print("okk")

# # try:
# #     num = int(input("Enter: "))
# #     print(10 / num)
# # except Exception as e:
# #     print("Error occurred:",e)
# # age =-2
# # if age < 0:
# #     raise
# # print("hi")

# # import statistics as m
# # print(dir(m))
# # x=(1,2,3,4,5,5)
# # print(f"{m.mean(x):.2f}")

# x=[1,2,3,4,5,6]
# for it,ind in enumerate(x):
#     print("the unit is ",ind,"at the index ",it)

# # colors = ['red', 'green', 'blue']
# # for position, color in enumerate(colors, start=1):
# #     print(f"Color {position}: {color}")

# print(" correct ✅ ")
import statistics as st
print(dir(st))
norm=st.NormalDist(0,1)
sam =f"{norm.samples(5)}"
print(sam)