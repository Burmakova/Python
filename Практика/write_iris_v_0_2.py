import os
from sklearn.datasets import load_iris


# класс "ирис"
class Iris:
    # конструктор для создания объектов по данным
    # из двух списков iris_dataset: data и target
    # или списка, получаемого при чтении файла
    def __init__(self, **info):
        # из двух списков iris_dataset: data и target
        if "data" in info and "target" in info:
            self.sepal_length = info["data"][0]
            self.sepal_width = info["data"][1]
            self.petal_length = info["data"][2]
            self.petal_width = info["data"][3]
            self.target = info["target"]
        # из одного списка строк, получаемого при чтении файла
        elif "data_and_target" in info:
            self.sepal_length = float(info["data_and_target"][0])
            self.sepal_width = float(info["data_and_target"][1])
            self.petal_length = float(info["data_and_target"][2])
            self.petal_width = float(info["data_and_target"][3])
            self.target = int(info["data_and_target"][4])


# список для объектов класса "ирис"
iris_list = []
# --- чтение файла ---
filename = input("Введите имя файла для чтения данных "
                 "(0 - для загрузки iris_dataset):\n")
if filename == "0":
    # загружаем данные из пакета sklearn
    iris_dataset = load_iris()
    # наполняем список объектами класса "ирис",
    # создаваемыми по данным из пакета
    # нам нужен именно номер строки i, потому что столбец с
    # типом ириса - в отдельном списке
    for i in range(len(iris_dataset['data'])):
        iris_list.append(
            Iris(data=iris_dataset['data'][i],
                 target=iris_dataset['target'][i]))
else:
    if filename[-3:0] != "csv":
        filename += ".csv"
    filedesc = open(filename, "r")
    # считываем весь файл как список строк
    filecontent = filedesc.readlines()
    # цикл по строкам файла
    for i in range(len(filecontent)):
        # пропускаем первую строку с заголовком
        if i > 0:
            # разбиение строки на ячейки по символу ";"
            cells = filecontent[i].split(";")
            # наполняем список объектами класса "ирис",
            # создаваемыми по данным из файла
            iris_list.append(Iris(data_and_target=cells))
    filedesc.close()

# --- фильтрация списка ---
field_num = int(input("Выберите поле для фильтрации:\n"
                      "0 - не фильтровать\n"
                      "1 - sepal length (cm)\n"
                      "2 - sepal width (cm)\n"
                      "3 - petal length (cm)\n"
                      "4 - petal width (cm)\n"
                      "5 - target\n"))

filtered_list = []
# копируем весь список
if field_num == 0:
    filtered_list = iris_list.copy()
else:
    min_num = float(input("Введите минмальное допустимое значение: "))
    max_num = float(input("Введите максмальное допустимое значение: "))
    # копируем только строки, удовлетворяющие введенному условию
    if field_num == 1:
        for i in iris_list:
            if min_num <= i.sepal_length <= max_num:
                filtered_list.append(i)
    elif field_num == 2:
        for i in iris_list:
            if min_num <= i.sepal_width <= max_num:
                filtered_list.append(i)
    elif field_num == 3:
        for i in iris_list:
            if min_num <= i.petal_length <= max_num:
                filtered_list.append(i)
    elif field_num == 4:
        for i in iris_list:
            if min_num <= i.petal_width <= max_num:
                filtered_list.append(i)
    elif field_num == 5:
        for i in iris_list:
            if min_num <= i.target <= max_num:
                filtered_list.append(i)


# --- сохранение списка ---
filename = input("Введите имя файла для сохранения данных:\n")
if filename[-3:0] != "csv":
    filename += ".csv"
filedesc = open(filename, "w")

# пишем заголовок таблицы
header = "sepal length (cm);sepal width (cm);petal length (cm);petal width (cm);target"

filedesc.write(header + "\n")

# пишем строчки с данными в таблицу
for i in filtered_list:
    line = str(i.sepal_length) + ";" + str(i.sepal_width) + \
           ";" + str(i.petal_width) + ";" + str(i.petal_width) + \
           ";" + str(i.target)
    filedesc.write(line.replace(".",",") + "\n")

filedesc.close()

os.startfile(filename)

