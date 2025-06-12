i=0
while(i>=0):  ### using while loop for multiple time asking user 
    while True:
        try:
            data = list(map(float, input("Enter your data with space between each data point: ").split()))
            print("Entered data is:", data)
            break
        except ValueError as v:
            print("Invalid input! Please enter only numbers separated by spaces.")

     ###### importing module 
      
    import math as m,statistics as st

    ##ABOUT DATA SET , defining a fnc##

    def about(k):
        count=len(k)
        print("NO OF ELEMENTS IN DATA SET IS :",count)
        if(count%2==0):
            print("DATA HAS EVEN NO OF ELEMENTS")
        else:
            print("DATA HAS ODD NO OF ELEMENTS")    

    #MEASURE OF CENTRAL TENDANCIES , definin a fnc
   
    def MOCT(a):
        mean=st.fmean(a)
        median=st.median(a)
        modes=st.multimode(a)
        print("mean:                                  ".upper(),mean)
        print("MEDIAN:                                ",median)
        if len(modes)==1:
            print("unique mode:                           ".upper(),modes)
        else:
            print("Multiple mode:                         ".upper(),modes)
   
   
    #MEASURE OF DISPERSION, defining a fnc 
   
   
    def MOD(b):
        Var=st.pvariance(b)
        var=st.variance(b)
        SD=st.pstdev(b)
        sd=st.stdev(b)
        print(f"population variance:                    {Var:.2f}".upper())
        print(f"sample variance:                        {var:.2f}".upper())
        print(f"population standard deviation:          {SD:.2f}".upper())
        print(f"sample standard deviation:              {sd:.2f}".upper())
    
    
    
    #MEASURES of Range
    
    
    minima=min(data)
    maxima=max(data)
    range=maxima-minima 


    #MEASURE OF POSITION

    Q=st.quantiles(data,n=4)
    iqr=Q[2]-Q[0]                                       # q1=Q[0], q3=Q[2] , due o indexing starts form 0 


    #MILD OUTLIARS

    outliars=[]                                             # creating a empy list of outliars  
    for item in data:
        if((item<Q[0]-1.5*iqr)or (item>Q[2]+1.5*iqr)):
            outliars.append(item)                           # adding element in the list outliar                                                 

    print("-----for the given data the following statistics are calculated and are listed below----".title(),end="\n\n")
    print("ABOUT THE DATA , ",data)
    about(data)

    print("\n"'SECTION-1 "__measure of central tendancies__"'.upper().center(80),end="\n\n")
    MOCT(data)                                              #calling fnc
    print("\n"'SECTION-2 "__measure of dispersion__"'.upper().center(80),end="\n\n")
    MOD(data)                                                #calling fnc
    print("\n"'SECTION-3 "__measure of range __"'.upper().center(80),end="\n\n")
    print("MAXIMUM VALUE OF THE DATA SET:         ",maxima)
    print("MINIMUM VALUE OF THE DATA SET:         ",minima)
    print("RANGE OF THE DATA SET:                 ",range) 
    print("\n"'SECTION-4 "__measure of position__"'.upper().center(80),end="\n\n")
    print("QUARTILE 1:                            ",Q[0])
    print("QUARTILE 2:                            ",Q[1]) 
    print("QUARTILE 3:                            ",Q[2])
    print("INTER QUARTILE RANGE:                  ",iqr)          

    
    if(len(outliars)==0):
        print("NO OUTLIARS")
    else:
        print("OUTLIARS:                            ",outliars)


    i+=1
    print("\nDo you want to do it for another data set ?(y/n)")
    if(input().lower()=="y"):
        continue
    else:
        print("THANK YOU ,EXIT")
        break    
