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
x=[1,2,3,2,1]
y=x.copy()
y.reverse()
if x==y :
    print("It is palindrome")
else:
    print("It is not ")