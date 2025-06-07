###### functions ###########
def hi():
    print("hello")

hi()
######### function with arguments #######
def sum(a:int ,b:int):
    x=a+b
    return x 


print("the sum is ", sum(4.5,5.5))


def greet(name:str):
    print("Hello, ",name)

greet("dev")
greet("div")
greet(4)



def greet(name , age ):
    print("Hello, you are ",name, "and your age is ",age)

greet("div",20)
greet("dev",21)

########## function with return statement ############

def sum(a,b):
    x=a+b
    return xs

print(sum(2,3))

def get_details():
    name = "Dev"
    age = 21
    return name, age
x,y=get_details()
print(x,y)
print(x)
print(get_details())

def student(firstname, lastname):
    print(firstname, lastname)


# Keyword arguments
student('Geeks', 'Practice')
student(lastname='Practice', firstname=21)


##### creating a function of calculatingg avg of 3 values ######

def avg(a,b,c):
    x=(a+b+c)/3
    return x

g,h,i=map(int,input("enetr three numbber with a space between them:").split())
print("the avg is : ",avg(g,h,i))