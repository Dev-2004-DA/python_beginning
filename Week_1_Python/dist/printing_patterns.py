## Square of Asterisks                                      
for i in range(0,4,1):                             
    for j in range(0,4,1):                             
        print("*",end="")                                   
    print(" ")                                          

    
## Right-Angled Triangle of Asterisks
## Pattern (for height = 5)                                       
for i in range(6):
    n=i
    for j in range(n):
        print("*",end="")
    print(" ")                                                            
            

## Example 3: Inverted Right-Angled Triangle of Asterisks
## Pattern (for height = 5):

for i in range(6):
    n=5-i
    for j in range(n):
        print("*",end="")
    print("")    


## Example 4: Pyramid of Asterisks
## This pattern involves printing spaces before the asterisks to center them.

for i in range(0,5,1):
    a=5-i
    b=6+i
    for j in range(a,b):
        print("*",end="")
    print("")        
