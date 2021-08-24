import pandas as pd
df = pd.read_csv("dwarf_stars.csv")
df.head()
print(df.dtypes)
df["Radius"] = 0.102763*df["Radius"]

df["Mass"] = pd.to_numeric(df["Mass"], downcast="float")
df["Mass"] = 0.000954588*df["Mass"]
print(df.dtypes)
df.to_csv("unit_converted_stars.csv")