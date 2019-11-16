# стол
class Table:
    __mass = 0

    def __init__(self, mass0):
        self.__mass = mass0

    # чтение инкапсулированной массы
    def get_mass(self):
        return self.__mass

#журнальный стол
class JournalTable(Table):
    storage = 0


# обеденный стол
class DinnerTable(Table):
    __places = 0

    def __init__(self, mass0):
        Table.__init__(self, mass0)
        self.__places = mass0//5

    # чтение инкапсулированного числа мест
    def get_places(self):
        return self.__places


class Truck:
    __maxMass = 0
    __tables = []

    def __init__(self, max_mass):
        self.__maxMass = max_mass

#расчет всех погруженных столов
    def __current_mass(self):
        s = 0
        for i in self.__tables:
            s += i.get_mass()
        return s

#расчет оставшейся доступности массы для погрузки столов
    def reserved_mass(self):
        return self.__maxMass - self.__current_mass()

    def add_table(self, new_table):
        if new_table.get_mass() < self.reserved_mass():
            self.__tables.append(new_table)
            print("Стол массой  " +
                  str(new_table.get_mass()) +
                  " загружен!")
        else:
            print("Стол массой " +
                  str(new_table.get_mass()) +
                  " Не влазит!\nОсталось только " +
                  str(self.reserved_mass()) + " кг!")


newTable = [
    DinnerTable(10),
    DinnerTable(20),
    DinnerTable(30)]

newTruck = Truck(50)
newTruck.add_table(newTable[0])
newTruck.add_table(newTable[1])
newTruck.add_table(newTable[2])
