####### WAF to print the length of a list (list is the parameter ) ###########
# def l(variable):
#     x=len(variable)
#     return x

# a="hurry"
# b=["A","B","c"]
# print("the length of",a,"is",l(a))
# print("the length of",b,"is",l(b))



####### WAF to print the elemnts of a list in a single line  ###########

def print_in_a_line(a):
    for item in a:
        print(item ,end=" ")    ## end statemnt remove the default next line feature 


x=[1,2,3,4,5,6,7,8,9,110]
print_in_a_line(x)
a="hurry"
b=["A","B","c"]
print(" ")
print_in_a_line(a)
print(" ")
print_in_a_line(b)