# select data w/ []

d = {"a": ["a", "b", "c", "d"], "b": [1, 2, 3, 4]}
df = pd.DataFrame(d)
df_filter = df[df.a == "c"]
print("select the rows whose \"a\" column is equal to \"c\"")
print(df_filter)

# using query

d = {"col1": ["a", "b", "c", "d", "a"],
     "col2": [1, 2, 3, 4, 2]}
df = pd.DataFrame(d)

df_filter = df.query('col1 == "a"')
print(df_filter)
df_filter = df.query('col1 == "a" & col2 == 1')
print(df_filter)
df_filter = df.query('col1 in ["a", "b", "c"]')
print(df_filter)
