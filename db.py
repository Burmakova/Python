# Подключаем библиотеку для работы с базой данных SQLite3
import sqlite3

# С помощью команды connect подключаемся к базе данных
# В данном случае база данных будет взята из файла указанного в параметре
# Если файл не существует, то он будет создан
db = sqlite3.connect("./sqlite-students2.sl3")

# Конструкция try-except позволяет выполнять небезопасный код с последующей обработкой ошибок
# В блоке try пишется код в котором может возникнуть исключение
try:
    # Попытка получить данные из таблицы students
    # В случае отсутствия в базе данных данной таблицы будет вызвано исключение и управление перейдёт в блок except
    db.execute("select * from students;")
# В блоке except пишется код отвечающий за обработку той или иной ошибки
# В данном случае будут отлавливаться любые исключения
except:
    # С помощью команды executescript можно выполнить переданную строку как один большой SQL-скрипт
    # Данный скрипт может состоять из одной и более SQL-команды
    # В данном случае будет выполнен скрипт создания и инициализации таблиц students и faculties
    db.executescript("""
        CREATE TABLE faculties(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        );

        INSERT INTO faculties(name)
        VALUES ("Information technologies");
        INSERT INTO faculties(name)
        VALUES ("Print technologies and media communications");

        CREATE TABLE students(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            surname TEXT,
            phone TEXT,
            address TEXT NOT NULL,
            faculty_id INTEGER NOT NULL,
            FOREIGN KEY (faculty_id)
            REFERENCES faculties (id)
            ON DELETE CASCADE
            ON UPDATE NO ACTION
        );

        INSERT INTO students (name, surname, phone, address, faculty_id) 
        VALUES ("Ivan", "Ivanov", "+375292000002", "Lenina 75/1", 1);
        INSERT INTO students (name, address, faculty_id)
        VALUES ("Albert", "Lenina 75/2", 1);
        INSERT INTO students (name, surname, address, faculty_id)
        VALUES ("Petr", "Albertov", "Lenina 75/3", 2);
        INSERT INTO students (name, phone, address, faculty_id)
        VALUES ("Roman", "+375292000001", "Lenina 75/4", 2);
    """)
    # С помощью команды commit выполняется сохранение всех изменений произошедших в базе данных
    db.commit()
    print("Создание таблиц завершено!")

# Команда execute предназначена для выполнения одиночного SQL-запроса
# в данном случае получаем все записи из таблицы students
# Команда возвращает результат в виде итератора
for row in db.execute("select * from students;"):
    # Каждый элемент будет представлять из себя кортеж с данными и соответствовать одной строке из таблицы
    print(f"{row}")

print("---------")

# Повторяем всё тоже самое для второй таблицы
for row in db.execute("select * from faculties;"):
    print(f"{row}")

# Данные в виде списка кортежей для последующей вставки
List = [("Ivan", "Ivanov", "+375292000022", "Lenina 76/1", 1),
        ("Petr", "Petrov", None, "Lenina 76/2", 2),
        ("Stepan", None, "+375292000002", "Lenina 76/3", 1)]

# С помощью команды executemany мы можем выполнтиь один и тот же SQL-запрос несколько раз
# В данном случае выполняется динамический SQL-запрос на вставку данных в таблицу students
# В отличие от статического запроса из скрипта выше, данные не подставляются напрямую в строку, а берутся из кортежей
# и подставляются на место символа ? динамически
# В данном случае команда выполнит SQL-запрос 3 раза. По одному для каждого элемента списка List
db.executemany(
    "INSERT INTO students(name, surname, phone, address, faculty_id) VALUES (?, ?, ?, ?, ?)", List)

db.execute('''INSERT INTO students(name, surname, phone, address, faculty_id) 
                    VALUES ("Ivan", "Ivanov", "+375292000022", "Lenina 76/1", 1)''')
print("---------")

# Выводим таблицу students для проверки успешности вставки
for row in db.execute("select * from students;"):
    print(f"{row}")

print("---------")

# Выполняем запрос на обновление записи из таблицы students у которой id = 2 с установкой поля surname в значение Albertov
db.execute('''update students set surname = "Albertov" where id = 2;''')

# Выводим значение обновлённой строки
# Для того чтобы указать что мы хотим получить только одну строку используем функцию fetchone
print(db.execute("select * from students where id = 2;").fetchone())

print("----+----")

# Для того чтобы указать что мы хотим получить только одну строку используем функцию fetchmany
print(db.execute("select * from students;").fetchmany(3))

print("------+---")



# Удаляём обновлённую строку
db.execute("delete from students where id = 2;")

# Выводим таблицу students для проверки успешности удаления
for row in db.execute("select * from students;"):
    print(f"{row}")

# Закрываем соединение с базой данных
db.close()
