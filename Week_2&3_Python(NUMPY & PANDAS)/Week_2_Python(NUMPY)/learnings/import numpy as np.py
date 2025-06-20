import numpy as np
from numpy import random as r
import matplotlib.pyplot as plt
import seaborn as sns





#### visualizing normal distn ######
# generating normal sample
x=r.normal(loc=0,scale=1,size=100)
#now plotting
sns.displot(x,kind='hist')
# modifying
# plt.title("NORMAL")
plt.xlabel("Data Points")
plt.ylabel("Frequency")
plt.show()