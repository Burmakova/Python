# ���������� ���������� ��� ������ � ����� ������ SQLite3
import sqlite3

# � ������� ������� connect ������������ � ���� ������
# � ������ ������ ���� ������ ����� ����� �� ����� ���������� � ���������
# ���� ���� �� ����������, �� �� ����� ������
db = sqlite3.connect("./sqlite-students2.sl3")

# ����������� try-except ��������� ��������� ������������ ��� � ����������� ���������� ������
# � ����� try ������� ��� � ������� ����� ���������� ����������
try:
    # ������� �������� ������ �� ������� students
    # � ������ ���������� � ���� ������ ������ ������� ����� ������� ���������� � ���������� ������� � ���� except
    db.execute("select * from students;")
# � ����� except ������� ��� ���������� �� ��������� ��� ��� ���� ������
# � ������ ������ ����� ������������� ����� ����������
except:
    # � ������� ������� executescript ����� ��������� ���������� ������ ��� ���� ������� SQL-������
    # ������ ������ ����� �������� �� ����� � ����� SQL-�������
    # � ������ ������ ����� �������� ������ �������� � ������������� ������ students � faculties
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
    # � ������� ������� commit ����������� ���������� ���� ��������� ������������ � ���� ������
    db.commit()
    print("�������� ������ ���������!")

# ������� execute ������������� ��� ���������� ���������� SQL-�������
# � ������ ������ �������� ��� ������ �� ������� students
# ������� ���������� ��������� � ���� ���������
for row in db.execute("select * from students;"):
    # ������ ������� ����� ������������ �� ���� ������ � ������� � ��������������� ����� ������ �� �������
    print(f"{row}")

print("---------")

# ��������� �� ���� ����� ��� ������ �������
for row in db.execute("select * from faculties;"):
    print(f"{row}")

# ������ � ���� ������ �������� ��� ����������� �������
List = [("Ivan", "Ivanov", "+375292000022", "Lenina 76/1", 1),
        ("Petr", "Petrov", None, "Lenina 76/2", 2),
        ("Stepan", None, "+375292000002", "Lenina 76/3", 1)]

# � ������� ������� executemany �� ����� ��������� ���� � ��� �� SQL-������ ��������� ���
# � ������ ������ ����������� ������������ SQL-������ �� ������� ������ � ������� students
# � ������� �� ������������ ������� �� ������� ����, ������ �� ������������� �������� � ������, � ������� �� ��������
# � ������������� �� ����� ������� ? �����������
# � ������ ������ ������� �������� SQL-������ 3 ����. �� ������ ��� ������� �������� ������ List
db.executemany(
    "INSERT INTO students(name, surname, phone, address, faculty_id) VALUES (?, ?, ?, ?, ?)", List)

db.execute('''INSERT INTO students(name, surname, phone, address, faculty_id) 
                    VALUES ("Ivan", "Ivanov", "+375292000022", "Lenina 76/1", 1)''')
print("---------")

# ������� ������� students ��� �������� ���������� �������
for row in db.execute("select * from students;"):
    print(f"{row}")

print("---------")

# ��������� ������ �� ���������� ������ �� ������� students � ������� id = 2 � ���������� ���� surname � �������� Albertov
db.execute('''update students set surname = "Albertov" where id = 2;''')

# ������� �������� ���������� ������
# ��� ���� ����� ������� ��� �� ����� �������� ������ ���� ������ ���������� ������� fetchone
print(db.execute("select * from students where id = 2;").fetchone())

print("----+----")

# ��� ���� ����� ������� ��� �� ����� �������� ������ ���� ������ ���������� ������� fetchmany
print(db.execute("select * from students;").fetchmany(3))

print("------+---")



# ������� ���������� ������
db.execute("delete from students where id = 2;")

# ������� ������� students ��� �������� ���������� ��������
for row in db.execute("select * from students;"):
    print(f"{row}")

# ��������� ���������� � ����� ������
db.close()
