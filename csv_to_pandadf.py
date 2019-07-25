import pandas

data_df = pandas.read_csv("values.csv", sep=",")
print(data_df.head(3))

data = data_df[["X1","Y1","X2","Y2"]]
print(data)