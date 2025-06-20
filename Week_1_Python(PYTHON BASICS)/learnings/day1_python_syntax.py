print("hello world")
print("My name is Dev Sagar Soni and I have just comapleted my bachelors in statistics hons form Banaras Hindu University ")
x=4
y=x     #  here i gave variable x the value of 4 and then assigned y to x
print(y)
z="dev"
x,y,z=5,6.0,"prod"  #here i assigned three different data types  vraibles , their values in 1 line  
print(x)
print(y)
print(z)
print(x,y,z)
fal=["apple","banana","cherry"]       # fal is a list data type
x,y,z=fal                         # here our fa variable has 3 values  that is assigned to 3 different variables in one line     

print(x,y)
x, y, z =3,4,5.8

print(x+y+z)
x=5
y="dev"
z=7.9
w="soni"
print(y,w)	
x = dict(name="John", age=36)
print(x)
print(not(2>3 or 3<2))
a="2"
b=5
#print(int(a)+str(b))                   # this  code will give an error # because we cannot concatenate int and str
#print(int(a)+b)                    # this will give an error because we cannot concatenate int and str
c=str(b)
print(type(c))



#####   Type Conversion and Type Casting #####
a=10
b=4.7
c="3" 
d=6-4j
print(int(c)+ d)
print(int(a+b-d.real))
print(int(b)+float(c)+d+complex(c))
z=int(b)+float(c)+d+complex(c)
print(type(z))
print(str(z))
print(float(z.real))
print(float(z.imag))
#print(float(z))
print(bytes(a))

x=input("age :")
print(type(x))
x, y = input("Enter two numbers: ")
print( y)
list=input("enter you 1st name and age : ").split()
print ("your name is :", list[0] , "and yur age is :",list[1] )