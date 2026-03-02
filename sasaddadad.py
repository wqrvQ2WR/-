import pandas
import sys

list1 = []
log = pandas.read_csv("C:\\Users\\우리가족\\Downloads\\microbit.csv")
for i in range(len(log)) :
    print(log.iloc[i])
    list1.append(log.iloc[i])
user = ""

while user != 'q' :
    try :
        user = int(input("몇번째 데이터를 원하냐 닝겐: "))
        print(list1[user])
        if user == 'q' :
           sys.exit()
        print(list1[user])
    except ValueError :
            pass
    except IndexError :
        pass