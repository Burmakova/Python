import os
from sklearn.datasets import load_iris

iris_dataset = load_iris()

filename = input("Введите имя файла для сохранения данных:\n")
if filename[-3:0] != "csv":
    filename += ".csv"
filedesc = open(filename, "w")

# пишем заголовок таблицы
header = ""
for i in iris_dataset['feature_names']:
    header += i + ";"
header += "Target"

filedesc.write(header + "\n")

# пишем строчки с данными в таблицу
# нам нужен именно номер строки i, потому что столбец с
# типом ириса - в отдельном списке
for i in range(len(iris_dataset['data'])):
    line = ""
    for j in iris_dataset['data'][i]:
        line += str(j).replace(".",",") + ";"
    line += str(iris_dataset['target'][i])
    filedesc.write(line + "\n")

filedesc.close()

os.startfile(filename)

