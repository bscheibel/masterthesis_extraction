import pandas
df = pandas.read_csv('text.csv', header = 0, delimiter=";")
df['Text'] = df.groupby(['X','Y'])['TEXT'].transform('sum')
df.drop_duplicates()
df.to_csv("merged.csv")