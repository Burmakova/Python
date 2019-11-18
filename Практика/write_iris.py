import os
from sklearn.datasets import load_iris
# НОВЫЕ импорты
import json
import numpy
import struct


# класс для конвертации объектов класса "ирис"
# в формат JSON
class MyEncoder(json.JSONEncoder):
    def default(self, o):
        # выдавало ошибку при сохранении numpy.int32
        if isinstance(o, numpy.int32):
            return format(o.__int__())
        else:
            return {'{}'.format(o.__class__.__name__): o.__dict__}


# класс "ирис"
class Iris():
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
        # НОВЫЕ if-ы для новых форматов файла
        # из словаря, полученного при чтении файла JSON
        elif "params_dict" in info:
            self.sepal_length = float(info["params_dict"]["sepal_length"])
            self.sepal_width = float(info["params_dict"]["sepal_width"])
            self.petal_length = float(info["params_dict"]["petal_length"])
            self.petal_width = float(info["params_dict"]["petal_width"])
            self.target = int(info["params_dict"]["target"])
        # из массива байт, полученного при чтении бинарного файла
        elif "bytes_read" in info:
            float_list = struct.unpack("ffffi", info["bytes_read"])
            Iris.__init__(self, data_and_target=float_list)


# ГЛАВНАЯ ПРОГРАММА
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
    # НОВЫЙ выбор формата
    select = int(input("Укажите формат файла: \n"
                       "1 - CSV\n"
                       "2 - JSON\n"
                       "3 - бинарный\n"))

    if select == 1:
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

    elif select == 2:
        filedesc = open(filename, "r")
        filecontent = json.load(filedesc)

        for i in filecontent:
            iris_list.append(
                Iris(params_dict=i["Iris"]))
        print(filecontent)
        filedesc.close()

    elif select == 3:
        filedesc = open(filename, "rb")
        while True:
            # читаем 4 набора по 4 байта,
            # необходимых для хранения float,
            # и 1 набор байт на 4 байта для int
            bytes_read = filedesc.read(20)
            # если файл кончился - прекращаем чтение
            if bytes_read == b'':
                break
            iris_list.append(
                Iris(bytes_read=bytes_read))
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
select = int(input("Выберите формат файла: \n"
                   "1 - CSV\n"
                   "2 - JSON\n"
                   "3 - бинарный\n"))

# НОВЫЙ выбор формата
if select == 1:
    filedesc = open(filename, "w")
    # пишем заголовок таблицы
    header = "sepal length (cm);sepal width (cm);petal length (cm);petal width (cm);target"

    filedesc.write(header + "\n")

    # пишем строчки с данными в таблицу
    for i in filtered_list:
        line = str(i.sepal_length) + ";" + str(i.sepal_width) + \
               ";" + str(i.petal_width) + ";" + str(i.petal_width) + \
               ";" + str(i.target)
        filedesc.write(line.replace(".", ",") + "\n")

elif select == 2:
    filedesc = open(filename, "w")
    filedesc.write(
        json.dumps(
            filtered_list,
            cls=MyEncoder,
            indent=4
        )
    )

elif select == 3:
    filedesc = open(filename, "wb")
    for i in filtered_list:
        filedesc.write(
            bytearray(
                struct.pack(
                    "ffffi", i.sepal_length, i.sepal_width,
                    i.petal_length, i.petal_width,
                    i.target)
            )
        )

filedesc.close()
os.system(filename)

