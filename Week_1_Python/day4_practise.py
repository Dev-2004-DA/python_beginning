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


x=(1,4,9,16,25,36,49,64,81,100)
y= 100
i=0
while(i<=9):
    if(x[i]==y):         ### if statement is used to print something if item is found
        print("",y," is at index ",i)
    i+=1

print("item is searched")