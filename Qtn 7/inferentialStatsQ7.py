import pandas as pd
data = pd.read_excel("C:/Users/hp/Desktop/inferentialStatsQ7.xlsx")

#plotting a boxplot
import matplotlib.pyplot as plt
plt.boxplot(data.iloc[:,1])
plt.show()
#there are some outliers also right skewed 

#finding mean variance and standard deviation
print("\n_____________Mean___________\n")
data.iloc[:,1].mean()

print("\n_____________Variance___________\n")
data.iloc[:,1].var()

print("\n_____________Standard Deviation___________\n")
data.iloc[:,1].std()

print("\n_____________Measures of centarlity___________\n")
data.describe()
data.iloc[:,1].median()

print("\n_____________Measures of spread___________\n")
data.iloc[:,1].var()
