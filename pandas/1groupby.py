# get groups in dict form

df = pd.read_csv("sample1.csv", sep=",")
g = df.groupby("name").groups
print(g)

# select one group

df = pd.read_csv("sample1.csv", sep=",")
# print(df.head())
g1 = df.groupby("category")
dict(tuple(g1))["A"]

# groupby multiple columns find mean of each group 

df = pd.read_csv("sample1.csv", sep=",")
result = df.groupby(["name", "category"]).sum()
print("Group by \"name\" and \"category\" column and sum them")
print("-------------------------------------")
print(result)

# aggregate

print(g['price'].agg(np.sum))
print("---------------------------------")
# method 2, use the native function to sum the price for each group
print(g.sum()["price"])

df = pd.read_csv("sample2.csv", sep=",")
g = df.groupby("name")
print("calculate the sum/mean/std for name group price column")
print(g["price"].agg([np.sum, np.mean, np.std]))

# iterate groupby

df = pd.read_csv("sample2.csv", sep=",")
g = df.groupby("name")

for name, gr in g:
    print("current group is {}".format(name))
    print(f"the corresponding data under group {name}")
    print(gr)
