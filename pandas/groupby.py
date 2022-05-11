# iterate groupby

df = pd.read_csv("sample2.csv", sep=",")
g = df.groupby("name")

for name, gr in g:
    print("current group is {}".format(name))
    print(f"the corresponding data under group {name}")
    print("------------------------------------")
    print(gr)
    print("------------------------------------")
