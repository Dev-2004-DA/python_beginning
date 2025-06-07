####### WAF to print the length of a list (list is the parameter ) ###########
# def l(variable):
#     x=len(variable)
#     return x

# a="hurry"
# b=["A","B","c"]
# print("the length of",a,"is",l(a))
# print("the length of",b,"is",l(b))



####### WAF to print the elemnts of a list in a single line  ###########

# def print_in_a_line(a):
#     for item in a:
#         print(item ,end=" ")    ## end statemnt remove the default next line feature 


# x=[1,2,3,4,5,6,7,8,9,110]
# print_in_a_line(x)
# a="hurry"
# b=["A","B","c"]
# print(" ")
# print_in_a_line(a)
# print(" ")
# print_in_a_line(b)


########## WAF to find the factorial of n ( n is the parameter ) ############3

# def fact(n):
#     i=1         # initialization
#     y=1          # varibale that stores factorial
#     while(i!=(n+1)):
#         y=y*i
#         i+=1
#     return y    

# x=int(input("enter the number :"))
# print("the factorial of ",x, " is : ",fact(x))



############# WAF to convert usd to inr ##########3

# def usd(x):
#     inr=x*83
#     return inr
# y=100
# print("the inr value is :" , usd(y))


############# WAF that takes input number and if number is odd it reurn string odd and if even then even##############

def evod(x):
    if x%2==0:
        return "EVEN"
    else:
        return "ODD" 

y=int(input("Enterr the number : "))
print("the number is :",evod(y))