import pandas

log = pandas.read_csv("C:\\Users\\우리가족\\Downloads\\microbit.csv")
for i in range(len(log)) :
    print(log.iloc[0])