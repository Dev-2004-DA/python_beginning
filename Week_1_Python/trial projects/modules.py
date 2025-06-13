import statistics as st ,math as m, random as r
# x=list(map(int,input("enetr the data points with a space between them :").split())) 
# print(x)
x=[78, 28, 45, 94, 6, 83, 91, 81, 23, 19, 99, 36, 52, 10, 73, 2, 69, 12, 42, 0, 30, 47]
mean=st.fmean(x)
md=st.median(x)
mz=st.multimode(x)
##y=list(r.choices(range(100),k=len(x)))##
y=[86, 52, 32, 13, 53, 21, 14, 22, 95, 29, 86, 18, 82, 41, 99, 83, 20, 39, 40, 92, 35, 7]
rho=st.correlation(x,y)
cov=st.covariance(x,y)
reg=st.linear_regression(x,y)
print(f"mean is is {mean:.2f}")
print("median is is" , md)
print("mode is is" , mz)
print("correlation is is" , rho)
print("covariance is is" , cov)
print("regression coefficient is" ,reg)
# print("mean is is" + mean)
# print("mean is is" + mean)
# print("mean is is" + mean)
