# ##################### WAP to ask user about their three favourite movies and save them in a list ##################
# ### method 1
# User_fav_movies=[1,2,3]                            # create a list of 3 elements  then take inputs and asssig that inputs to the index
# x=input("enter your favourite movie name: ")
# y=input("enter your favourite movie name: ")
# z=input("enter your favourite movie name: ")
# User_fav_movies[0]=x
# User_fav_movies[1]=y
# User_fav_movies[2]=z
# print("user's favourite movies are = ", User_fav_movies)

# #### method 2

# User_fav_movies=[]                            # create a list of 3 elements  then take inputs and asssig that inputs to the index
# x=input("enter your favourite movie name: ")
# y=input("enter your favourite movie name: ")
# z=input("enter your favourite movie name: ")
# User_fav_movies.append(x)
# User_fav_movies.append(y)
# User_fav_movies.append(z)
# print("user's favourite movies are = ", User_fav_movies)

############################## WAP to check if a list contains a palindrome of elements ################
# x=[1,2,3,2,1]
# y=x.copy()
# y.reverse()
# if x==y :
#     print("It is palindrome")
# else:
#     print("It is not ")

############################## WAP to count the number of students with the "A" grade in the following tupple ("C","D","A","A","B","B","A") #########################
# x=("C","D","A","A","B","B","A")
# ##store the above values in a list and sort them from ascending to descending  ##
# y=list(x)
# print("the number of stdents with Grade A are = ",y.count("A"))
# y.sort()
# print(y)

############################ store the following word  meanings in a python dictionary:  table- a piece of furniture ,list of facts & figures , cat- a small animal ##########3
dicti={}                                                                # created a empty dictionary
dicti["table"]=["a piece of furniture ", "list of facts and figures"]
dicti["cat"]="a small animal"
print(dicti)
