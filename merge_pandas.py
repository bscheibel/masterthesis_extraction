import pandas
df = pandas.read_csv('text.csv', header = 0)
df['Total'] = df.groupby(['Name', 'Age'])['Salary'].transform('sum')
df.drop_duplicates(take_last=True)