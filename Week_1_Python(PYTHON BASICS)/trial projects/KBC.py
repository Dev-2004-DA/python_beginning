########## EXERCISE 2 CREATE A PROGRAM CAPABL OF DISPLAYING QUESTION TO THE USR LIKE KBC ###########
########## USE list data type to store the question and there correct answer #########
########## Display the final amoutnt the person is taking home afetr playing the game #####3 

### Let's begin ## creating list varibales of questions , options , answer
print("---Welocome to kaun banega cororepati---".upper().center(100))
que=["number of electrons in carbon atom?".title(),"no of days in a non leap year?".title(),"capital of india".title()]
opt=["A. 4","B. 8","C. 6","D. 12","A. 368","B. 365","C. 366","D. 356","A. New delhi".title(),"B. lucknow".title(),"C. kolkata".title(),"D. mumbai".title()]
ans=[opt[2],opt[5],opt[8]]

print("hello , ",input("Your name is :").upper())
print("Are you ready to begin?,(Y/N)" )
if(input().upper()=="Y"):                                                       #   
    print("That's the spirit, Let's begin .")                           #        
    print("\n\n\nQ1.",que[0],"\n")                                      #q1 starts here
    for item in opt[0:4]:                                               #  used for loop to print options by using their index
        print(item)                                                     #
    C=ans[0]                                                            # assinging correct option numbeer to the correc anwer idx    
    if(input("Enter option=").upper()=="C"):                                    #    runnning if statemnt 
        print("CORRECT".center(40))
        print("Lets come to next question")                                 
        print("\n\n\nQ2.",que[1],"\n")                                  # q2 starts here insisde a if statement
        for item in opt[4:8]:                                           #used for loo to print options by using their index    
            print(item)
        B=ans[1]                                                        # assinging correct option numbeer to the correc anwer idx 
        if(input("Enter option=").upper()=="B"):
                print("CORRECT".center(40))
                print("Lets come to next question")
                print("Q3.",que[2])                                      # q3 starts here           
                for item in opt[8:12]:                                     # printing  its option using loops and options index 
                    print(item)
                    A=ans[2]                                                # assinging correct option numbeer to the correc anwer idx   
                if(input("Enter option=").upper()=="A"):
                    print("CORRECT".center(40))
                    print("game is ended , thankyou for playing with us".upper())
                else:
                     print("ELIMINATED")    
        else:
                print("ELIMINATED")        
    else:
        print("ELIMINATED")
else:
    print("LOSER")    