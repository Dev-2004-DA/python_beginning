print("helo ,I","dev" ,sep="-")
print("helo ,I ","dev")
print("hello","dev",end="++++")
print("good")

#  EXERCISE 1
######### CALCULATOR USING PYTHON ############
x,y=map(int,input("Enter two numbers with a space btween the : ").split())
print("ADDITION IS= ",x+y)
print("SUBTRACTION IS= ",x-y)
print("MULTIPLICATION IS= ",x*y)
print("DIVISION IS= ",x/y)
print("QUOTINT IS= ",x//y)
print("REMAINDER IS= ",x%y)

#$$$$$$$$$$$$ STRINGS $$$$$$$###

x="Dev Sagar Soni"
print(x[0:3],x[4:9] )
y=len(x[0:3])
print(y)
a="harry"
print(a[-4:-2])

##$$$$    STRINGS METHODS $$$$$###

x="dev sagar soni"
print(x.upper())
print(x.title())
print(x.capitalize())
print(x.capitalize())
print(x)
print(x.replace("dev","ved"))
print(x.capitalize().center(50))
print(x.index("dev"))


#####33 Match case ##########3
day = "Saturday"
x=20
# Match statement
match day:
    case "Monday" | "Saturday" if x==20:
        print("Start of the work week.")
    case "Friday":
        print("End of the work week.")
    case "Sunday":
        print("Rest day.")
    case _:
        print("A regular day.")

##### LOOOPSSSSSS#########

x= "DEV"
i=0
for items in x:
    if(items== "V" ):
        print("yeah , you find it")



 ### while loop taking input till user enetr valus greater than or equal to 30 #########
i=0
while(i<30):
    i=int(input("enter"))
    i+=1

print("loop ended")    


#######3 BREAK AND CONTINUE ##########33

for item in range(20):
   
    if(item==13):
        continue
    elif(item==17):
        break
    print(item)
    