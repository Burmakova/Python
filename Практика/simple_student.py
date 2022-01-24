import uuid
import random


# Класс реализующий студента
class Students(object):
    # Проходной балл для студента на предполагаемую специальность
    _passing_score = 289
    # Имена свойств класса в которые запишутся значения фамилии, имени и отчества
    _name_parts = {0: '_surname', 1: '_name', 2: '_fathername'}
    # Список зачётных и экзаменационных дисциплин в каждом семестре обучения
    _disciplines = {
        1: {
            'credit': [
                'History', 'Foreign language', 'Belarussian language',
                'Physical education'
            ],
            'exam': [
                'Maths', 'Physics',
                'Arithmetic and logical foundations of digital computers',
                'Fundamentals of algorithmization and programming',
                'Fundamentals of information technologies'
            ]
        },
        2: {
            'credit': [
                'Arithmetic and logical foundations of digital computers',
                'Ethics and aesthetics/History of world culture',
                'Fundamentals of General Chemistry', 'Physical education'
            ],
            'exam': [
                'Maths', 'Foreign language',
                'Fundamentals of algorithmization and programming',
                'Operation systems', 'Fundamentals of information technologies'
            ]
        },
        3: {
            'credit': [
                'Engineering geometry and graphics',
                'Equipment and basics of technology prepress and printing processes',
                'User interfaces design and usability', 'Physical education'
            ],
            'exam': [
                'Philosophy', 'Maths',
                'Fundamentals of discrete mathematics and theory of algorithms',
                'Computer networks', 'Object-oriented programming'
            ]
        },
        4: {
            'credit': [
                'Fundamentals of information security',
                'Computer multimedia systems in publishing',
                'Metrology, standardization and certification in printing production',
                'Computers, computer systems and peripherals',
                'Physical education'
            ],
            'exam': [
                'Economy', 'Mathematical programming',
                'Object-oriented programming', 'Databases',
                'Computer geometry and graphics'
            ]
        },
        5: {
            'credit': [
                'Politology',
                'Modeling and optimization processes and systems',
                'Information security and reliability information systems',
                'Physical education'
            ],
            'exam': [
                'Human life safety', 'Fundamentals of Business and Law',
                'Programming of network applications',
                'Administration of databases',
                'Computer multimedia systems in publishing'
            ]
        },
        6: {
            'credit': [
                'Fundamentals of law and human rights/Industry market theory',
                'Programming in the Internet',
                'Printing machines, machines and current lines',
                'Process automation in printing', 'Physical education'
            ],
            'exam': [
                'System programming', 'Distributed information systems',
                'Modeling and optimization processes and systems',
                'Information security and reliability information systems',
                'Administration of information systems and web portals'
            ]
        },
        7: {
            'credit': [
                'Embedded systems',
                'Administration of information systems and web portals',
                'Organization of production and enterprise management'
            ],
            'exam': [
                'Programming in the Internet',
                'Systems and technologies intelligent processing data',
                'Programming of mobile systems', 'Software testing'
            ]
        },
        8: {
            'credit': [
                'IT project management and information management',
                'Development of dynamic web-applications'
            ],
            'exam': ['Embedded systems', 'Cloud technologies']
        }
    }

    # Метод инициализации создаваемого объекта класса студента (заполнение информацией созданного в __new__ объекта)
    def __init__(self, full_name, score):
        # Создание случайного UUID версии 4 (простыми словами случайного большого идентификатора)
        self._id = uuid.uuid4()
        # Разделение строки ФИО на составные части
        # с предварительным удалением всех лишних пробелов в начале и конце строки
        # Разделение происходит по пробелам между словами
        name_parts = full_name.strip().split(' ')
        # Проверка что после разделения ФИО получилось от 2 до 3 слов
        if 3 >= len(name_parts) > 1:
            # Цикл для прохода по всем получившимся словам из строки
            for i in range(0, len(name_parts)):
                # Запись ФИО в отдельные поля класса с помошью метода __setattr__
                # Метод __setattr__(key, value) работает подобно self.key = value
                # Названия полей берутся из переменной класса (стр. 10)
                self.__setattr__(Students._name_parts[i], name_parts[i])
        # Проверка на присутствие хотя бы одного слова в строке ФИО
        elif len(name_parts) == 1:
            # Запись единственного слова в ФИО как Имени студента
            self.__setattr__(Students._name_parts[1], name_parts[0])
        # Запись набранных баллов студента
        self._score = score
        # Запись об обучении студентом в первом семестре
        self._semester = 1
        # Запись об обучении студентом на первом курсе
        self._course = 1
        # Запись о текущих дисциплинах студента
        self._current_disciplines = Students._disciplines[self._semester]

    # Метод создания объекта класса студента
    def __new__(cls, full_name, score):
        # Вывод на консоль сообщения о начале создания объекта студента
        print("Попытка поступления...")
        # Проверка параметров конструктора на соответствие нужным типам данных
        # full_name должен быть строковым типом (str)
        # score должен быть целым числом (int)
        if not isinstance(full_name, str) or not isinstance(score, int):
            # Сообщение о несоответствии типов данных и прекращении создании объекта
            print("Неудачно. Предоставлена неверная информация!")
            # Возвращаем None в качестве результата при неудачном создании
            # Для этого случая метод __init__ вызван не будет
            return None
        # Вызов родительского конструктора
        # Вызов данного метода обязателен при перегрузке метода __new__
        # Для этого объекта также будет вызван метод __del__ класса Students, если он не будет возвращен из метода __new__
        instance = object.__new__(cls)
        # Проверка хватает ли баллов абитуриента для поступления
        if score >= cls._passing_score:
            # Сообщение об успешном поступлении(создании объекта студента)
            print("Удачно поступил.")
            # Возвращение созданного объекта
            # Для него далее будет вызван метод __init__ класса Students
            return instance
        else:
            # См. пояснение в строках 149, 151-152
            print("Неудачно. Не хватило баллов!")
            return None

    # Метод использующийся при автоматическом приведении объекта студента к строке
    # Например в метода print(obj1), интерпритатор python попробует превратить obj1 в строку
    # Если данный метод не определен в классе, будет использован метод __str__ из базового/родительского класса
    def __str__(self):
        # Форматируем строку с информацией о нашем объекте (Здесь можно выводить всё что посчитаете нужным)
        return '{0}({1})'.format(self.__class__.__name__, self.__dict__)

    # Данная метод используется при использования нашего объекта студента как логической переменной
    # Например if obj1: будет вызывать данный метод
    def __bool__(self):
        # Метод должен возвращать логическое значение
        # В данном примере проверяется наличие аттрибута _id у объекта студента
        # Необходим для проверки является ли объект пустым (None)
        return hasattr(self, '_id')

    # Данный метод вызывается при уничтожении объекта класса Students сборщиком мусора
    def __del__(self):
        # Проверка не является ли объект пустым (None)
        if self:
            # Проверка является ли студент учащимся последнего семестра обучения
            if self._semester == 8:
                # Вывод сообщения о уничтожении объекта
                print(
                    f'Завершение обучения студента с личным номером {self._id}...'
                )
            else:
                # Вывод сообщения о уничтожении объекта
                print(
                    f'Перевод студента с личным номером {self._id} в следующий семестр...'
                )
        else:
            # Вывод сообщения об уничтожении объектов для которых не был вызван метод __init__
            # Данный случай будет выполняться для объектов созданных в __new__ на стр. 157,
            # но которые не были возвращены методом __new__ в стр. 164
            print('Вычёркивание абитуриента из списков...')


# Создание объекта студента с достаточным для поступления баллом
stud1 = Students('Иванов Иван Иванович', 320)
# Вывод информации об объекте с неявным использованием метода __str__
print(stud1)
if stud1:
    print('checking bool')
# Создание объекта студента с недостаточным для поступления баллом
stud2 = Students('Петров Петр Петрович', 288)
# На этом моменте будет вызван метод __del__ для объекта который мог быть записан в stud2 (см. 201-203)
# Вывод информации об объекте с неявным использованием метода __str__
print(stud2)
# На этом моменте будет вызван метод __del__ для объекта stud1

print(stud1.__bool__())