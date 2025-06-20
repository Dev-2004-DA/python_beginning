# ####### print numbers from 1 to 100 ###########


# i=1
# while(i<=100):
#     print(i)
#     i+=1
# print("loop ended")    


# ######## print numbers from 100 to 1 ###########

# j=100
# while(j>=1):
#     print(j)
#     j-=1
# print("loop ended")    


######## print multiplication table of a number n#########3

# x=int(input("enetr a number of your choice: "))
# i=1
# while(i<=10):
#     print(x*i)
#     i+=1
# print("table is completed")    


######### print the element of a list using a loop: [1,4,9,...,100]############

# x=[1,4,9,16,25,36,49,64,81,100]
# i=0
# while(i<10):
#     print(x[i])       # it will print element at index 0 then 1 then 2 ,,,, 9
#     i+=1
# print("loop ended ")


######### search the element x of a tupple using a loop: (1,4,9,...,100)############


# x=(1,4,9,16,25,36,49,64,81,100)
# y= 100   ## the number that need to be searched
# i=0
# while(i<=9):
#     if(x[i]==y):         ### if statement is used to print something if item is found
#         print("",y," is at index ",i)
#     i+=1

# print("item is searched")

########## print the elemnts of the following list using for loop 1,4,9,..,100###############

# lis=[1,4,9,16,25,36,49,64,81,100]
# for hehe in lis:
#     print(hehe)

########## search for a no x in this tuple    [1,4,9,16,25,36,49,64,81,100] ########

# lis=(1,4,9,16,25,36,49,64,81,100)
# y=16
# idx=0
# for x in lis:
#     if(x==y):
#         print("",y," FOUND",idx)
#         break
#     idx=idx+1
       

# ############ WAP to find the sum of first n numbers (using while ) ##############
# n=int(input("enetr the number:"))
# i=0     ## initialization
# y=0     ## a varibale that store the sum 
# while(i!=n):
#     i+=1
#     y=y+i
# print(y)    

# ############ WAP to find the sum of first n numbers (using for ) ##############

# n=int(input("enetr the number:"))
# y=0
# for z in range(1,n+1):
#     y=y+z
# print(y)    


############ WAP to find the facorial of first n numbers (using for) ##############


n=int(input("enetr the number:"))     # taking input
fact=1
for no in range(1,n+1):
    fact=fact*no 
print("the factorial is = ", fact)    

############ WAP to find the facorial of first n numbers (using while) ##############


n=int(input("enetr the number:"))     # taking input
fact=1    # variable that strores the factorial
i=1    # initailizizng 
while (i!=n+1):
    fact=fact*i
    i+=1
print(fact)    