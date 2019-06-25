import pandas
df = pandas.read_csv('text.csv', header = 0, delimiter=";")
df['Total'] = df.groupby(['x'])['Text'].transform('sum')
df.drop_duplicates()