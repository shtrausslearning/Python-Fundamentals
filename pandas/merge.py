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
