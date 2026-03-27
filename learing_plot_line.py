import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
 
 
dfMPEG=pd.read_csv('auto-mpg.csv')
 
 
dfMPEG['log_weight'] = np.log(dfMPEG['weight'])
dfMPEG['log_mpg'] = np.log(dfMPEG['mpg'])
 
#print(dfMPEG)
# creating a line
m = -1
b = 8.5
 
#x = list(range(0, 4, 0.01))
x = np.linspace(0, 4, 1000)
y = [m * xi + b for xi in x]
 
 
print(y)
# end on the line
 
 
 
#plt.scatter(dfMPEG['mpg'], dfMPEG['weight'])
plt.scatter(dfMPEG['log_mpg'], dfMPEG['log_weight'])
plt.plot(x, y)
 
 
plt.xlabel('Miles Per Gallon')
plt.ylabel('Weight')
plt.title('MPG vs Weight')
plt.show()
