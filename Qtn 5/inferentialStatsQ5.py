import pandas as pd
df = pd.read_csv("C:/Users/hp/Desktop/inferentialStatsQ5.csv")

#dropping first column 
df = df.iloc[:,1:]

#defining range function:
def minmax(val):
    min_val = min(val)
    max_val = max(val)
    range_val = max_val-min_val
    print("min:",min_val)
    print("max:",max_val)
    print("range:",range_val)
    return ' '
print("\n----------- Calculate Mean -----------\n")
print(df.mean())
 
print("\n----------- Calculate Median -----------\n")
print(df.median())
 
print("\n----------- Calculate Mode -----------\n")
print(df.mode())

print("\n----------- Calculate Variance -----------\n")
print(df.var())

print("\n----------- Calculate Standard Deviation -----------\n")
print(df.std())

print("\n----------- Calculate Range -----------\n")
print(minmax(df.Points))
print(minmax(df.Score))
print(minmax(df.Weigh))
