# merging dataframes

import pandas as pd 

dl = {
    'pkey': ['K0', 'K0', 'K1', 'K2'],
    'pkey2': ['K0', 'K1', 'K0', 'K1'],
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3']
}

left = pd.DataFrame(dl)

dr = {
    'pkey': ['K0', 'K1', 'K1', 'K2'],
    'pkey2': ['K0', 'K0', 'K0', 'K0'],
    'C': ['A0', 'A1', 'A2', 'A3'],
    'D': ['B0', 'B1', 'B2', 'B3']
}
right = pd.DataFrame(dr)
result1 = pd.merge(left, right, on=['pkey', 'pkey2'])
print("The default how option is \"inner\"")
print("The final DataFrame has 3 rows without any NA element")
print(result1)
print("-----------------------------------")

result1 = pd.merge(left, right, on=['pkey', 'pkey2'], how="left")
print("The final DataFrame has 5 rows")
print(result1)
print("-----------------------------------")

result1 = pd.merge(left, right, on=['pkey', 'pkey2'], how="right")
print("The final DataFrame has 4 rows")
print(result1)
print("-----------------------------------")

# appending dataframes

import pandas as pd

d1 = {"a": [1, 2], "b": [2, 4]}
df1 = pd.DataFrame(d1)
print("The first DataFrame")
print(df1)
print("------------------------")
d2 = {"a": [3, 4], "b": [6, 8]}
df2 = pd.DataFrame(d2)
print("The second DataFrame")
print(df2)
df2 = pd.DataFrame(d2)
print("------------------------")

df1 = df1.append(df2)
print("Append the second DataFrame to the first one")
print(df1)

print("Append the second DataFrame to the first one and set ignore_index=True")
df1 = df1.append(df2, ignore_index=True)
print(df1)

import pandas as pd

d1 = {"b": [1, 2], "c": [2, 4]}
df1 = pd.DataFrame(d1)
print("The first DataFrame")
print(df1)
print("------------------------")
d2 = {"c": [3, 4], "d": [6, 8]}
df2 = pd.DataFrame(d2)
print("The second DataFrame")
print(df2)
df2 = pd.DataFrame(d2)
print("------------------------")

df1 = df1.append(df2)
print("Append the second DataFrame to the first one")
print(df1)

# concat

import pandas as pd 

d1 = {"a": [1, 2], "b": [2, 4]}
df1 = pd.DataFrame(d1, index=[1, 2])
print("The first DataFrame")
print(df1)
print("------------------------")
d2 = {"c": [3, 4], "d": [6, 8]}
df2 = pd.DataFrame(d2, index=[2, 3])
print("The second DataFrame")
print(df2)
print("------------------------")
print("The outer join DataFrame")
df3 = pd.concat([df1, df2], axis=1)
print(df3)
