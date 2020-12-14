import os

# список для строк
line_list = []
# --- чтение файла ---
F1 = input("Введите имя файла для чтения данных F1:\n")
if F1[-3:0] != "txt":
    F1 += ".txt"
filedesc = open(F1, "r")
N1 = int(input("Введите номер первой строки N1:\n"))
N2 = int(input("Введите номер последней строки N2:\n"))
A = input("Введите первую букву для отбора строк A:\n")
# считываем весь файл как список строк
filecontent = filedesc.readlines()
# цикл по строкам файла
for i in range(len(filecontent)):
    if N1 <= i+1 <= N2 and \
            filecontent[i][0] == A[0]:
        line_list.append(filecontent[i])
filedesc.close()

# --- запись файла ---
F2 = input("Введите имя файла для сохранения данных F2:\n")
if F2[-3:] != "txt":
    F2 += ".txt"
filedesc = open(F2, "w")
# пишем строчки
for i in line_list:
    filedesc.write(i)
filedesc.close()
os.startfile(F2)

