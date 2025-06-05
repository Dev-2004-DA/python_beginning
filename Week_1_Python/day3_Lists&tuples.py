################## LISTS ####################
# marks = [1,2,3,4,5]
# print(marks[0])
# marks[0]=0                   # change particular data in a list 
# print(marks[0])
# print(len(marks))            # length of the list

# x=["dev",21,"22220STA018",23.5]      # list contain different data types together 
# print(x[0]+x[2]+str(x[1]))
# x[0]=34                              # change particular data in a list
# print(x[0])
# print(x)
# print(x[1:])                         # this is list slicing 

######################  LISTS METHODS #######################
# x=[2,1,3]
# x.append(4)          # add one element to the list 
# print(x)
# x.sort(reverse=True)                            # sorting in descending order
# print(x)
# x.insert(2,"dev")
# print(x)
# x.pop(3)                                        # remove the element at index 3 
# print(x)

# ########################### TUPLES #############################
# x=(2,4,2,"dev")
# print(x[2])
# y=list(x)
# print(y)
# z=tuple(y)
# print(z)


############################ DICTIONARIES #####################

# bio={"name": "dev sagar soni",
#      "age": 21 ,
#      "subjects":[ 'maths','physics','statistics'],
#      "college":"BHU"}
# print(type(bio))                            
# print(len(bio))                         # length of dict
# bio["subjects"].append("python")         # adding elemnt in key subject
# bio["year"]=2025

# print(bio)
# print(bio.keys())
# print(bio.items())
# print(bio.get("subjects"))
# bio.update({"b.g.":["A","B"]})          #update items to dictionary ie key:value
# print(bio)


###################### SETS ############################

x={1,2,3,4,4,4,3,3,"dvev"}
# print(x)
# print(len(x))
# y=[]
# z=set()
# print(type(y))
# x.pop()
# x.pop()
# print(x.pop())
x={1,2,3,4,5,6}
y={3,4,5,"dev","soni"}
z=x.union(y)
print(z)
w=x.intersection(y)
print(w)