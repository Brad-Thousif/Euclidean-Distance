import pandas as pd
import scipy as sp
import array as arr
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt
from scipy.spatial import distance
filepath = 'bc.csv'
ar1=[0 for x in range(18)]
df = pd.read_csv(filepath).iloc[:, [1,2,3,4,5,6,7,8]].head(20)
ar2=arr.array('i',[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])
a = df[0:1:1]
j=2
s=0
for i in range(1,19):
        b=df[i:j:1]
        dst = distance.euclidean(a, b)
        j=j+1
        print(dst)
        ar1[s]=dst
        s=s+1
plt.plot(ar1)
plt.show()        
               
