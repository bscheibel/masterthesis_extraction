import pandas

def merge_lines(file_out):
    df = pandas.read_csv(file_out, header = 0, delimiter=";")
    df['Text'] = df.groupby(['X','Y'])['TEXT'].transform('sum')
    df.drop_duplicates()
    df.to_csv(file_out)