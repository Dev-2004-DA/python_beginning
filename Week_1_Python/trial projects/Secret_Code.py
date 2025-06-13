# # # # Write a python program to translate a msg into scret code languaeg . Use the rules below to translate norml English into secret code language

# # # #Codeing:
# # # if the word conatins at leats 3 characters , removve the first letter and append it at the end 
# # #  now append three random charcters at the starting and the end
# # #else:
# # #   simple reverse the string 

# # #Decoding:
# # #if the word contains less than 3 characters , reverse it 
# # #else:
# # #   remove 3 random characters from start and the end. Now reverse the last letter and append it to the beginning 

# # # Your program should ask whether you want to code or decode 
# # import random as r
import random as r 
ran="abcdefghijklmnopqrstuvwxyz"     # characters that will add to the end and the beginning 
a=(r.choices(ran,k=3))                      
b=(r.choices(ran,k=3))
at_end="".join(a)                    #3 characters that will add to the end   
at_beg="".join(b)                    #3 characters that will add to the beg.           
# personal info.
name=input("Enter your name ").upper()
gender=input("enter your gender (m/f):").lower()

if(gender=="m"):
    title="Mr."
elif(gender=="f"):
    title="Mrs."    

print(f"hello, {title} {name}, welcome to the secret language translator".center(30))

#asking user what he want to do code / decode
print("What would you like to do Encode/Decode -")
ans=input().lower() 


#Encoding

if(ans=="encode"):
    word=input("Enter the word to get is its translation:").strip()      # use strip method to remove spaces 
    if(len(word)<3):                                                     ##  for length of word less than 3 
        print("the code language of your word is = "+ word[::-1])        ## using negative index to convert string into reverse string        
    else:
        print(f"the code language of your word is ={at_beg}{word[::-1]}{at_end}")


#Decoding

if(ans=="decode"):
    word=input("Enter the word to get is its translation:").strip()      # use strip method to remove spaces 
    if(len(word)<3):                                                     ##  for length of word less than 3 
        print("the code language of your word is = "+ word[::-1])        ## using negative index to convert string into reverse string        
    else:
        a=word[3:(len(word)-3)]                     #remove 3 charac frrom last and beg.
        b=a[::-1]                                   # reverse the remaining part 
        print(f"the decoding of your word is ={b.upper()}")

print("thank you for using".upper())
   






# ###  decoing in short to understand
# word="abdihsirjkl"
# x=word[3:(len(word)-3)]
# y=x[::-1]
# print(y)
