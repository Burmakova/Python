import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Kalkpro(unittest.TestCase):
    # https://kalk.pro/finish/wallpaper/
    def setUp(self):
        # запуск Firefox при начале каждого теста
        self.driver = webdriver.Firefox()
        # открытие страницы при начале каждого теста
        self.page = self.driver.get('https://kalk.pro/finish/wallpaper/')

    def tearDown(self):
        # закрытие браузера при окончании каждого теста
        self.driver.close()

    # вспомогательный метод для заполнения размеров комнаты
    def input_walls_data(self, hei, wid, len):
        driver = self.driver
        # высота
        # находим элемент страницы по ID
        elem = driver.find_element_by_id("js--roomСeiling_height")
        # очищаем элемент от старого значения
        elem.clear()
        # вносим новое значение
        elem.send_keys(hei)
        # ширина
        elem = driver.find_element_by_id("js--roomSizes_width")
        elem.clear()
        elem.send_keys(wid)
        # длина
        elem = driver.find_element_by_id("js--roomSizes_length")
        elem.clear()
        elem.send_keys(len)

    # метод для проверки работы калькулятора при различных
    # размерах комнаты, в т. ч. проверка отображения ошибок
    # при вводе некорректных данных
    def test_walls(self):
        driver = self.driver
        # пробуем ввести размер 1х1х1
        self.input_walls_data(1, 1, 1)
        # запускаем расчет
        elem = driver.find_element_by_class_name(
            "js--calcModelFormSubmit"
        )
        elem.click()
        # проверяем наличие результатов расчета
        self.assertIn('Результаты расчета', driver.page_source)
        # проверяем, что площадь четырех стех размером 1х1 равна 4
        elem = driver.find_element_by_css_selector(
            "ul.data-list li:nth-child(4) strong"
        )
        self.assertEqual('4 м²', elem.text)

        # пробуем ввести размер 0х1х1
        self.input_walls_data(0, 1, 1)
        # запускаем расчет
        elem = driver.find_element_by_class_name(
            "js--calcModelFormSubmit"
        )
        elem.click()
        # проверяем наличие сообщения об ошибке
        self.assertIn('Ошибки', driver.page_source)
        # проверяем наличие одной ссылки на поле ввода
        elems = driver.find_elements_by_css_selector(
            "a.js--onclick-goToField"
        )
        self.assertEqual(len(elems), 1)

        # пробуем ввести размер aхbхc (буквы вместо цифр)
        self.input_walls_data('a', 'b', 'c')
        # запускаем расчет
        elem = driver.find_element_by_class_name(
            "js--calcModelFormSubmit"
        )
        elem.click()
        # проверяем наличие сообщения об ошибке
        self.assertIn('Ошибки', driver.page_source)
        # проверяем наличие трех ссылок на поля ввода
        elems = driver.find_elements_by_css_selector(
            "a.js--onclick-goToField"
        )
        self.assertEqual(len(elems), 3)

    # метод для проверки работы калькулятора
    # при добавлении окон и дверей
    def test_windows(self):
        driver = self.driver
        # пробуем ввести размер 1х1х1
        self.input_walls_data(1, 1, 1)
        # добавляем окно
        elem = driver.find_element_by_css_selector(
            "fieldset[name=windows] button"
        )
        elem.click()
        # задаем размеры окна 1х1 - во всю стену, кол-во окон - 1
        elem = driver.find_element_by_id("js--windows_height_0")
        elem.clear()
        elem.send_keys(1)
        elem = driver.find_element_by_id("js--windows_width_0")
        elem.clear()
        elem.send_keys(1)
        elem = driver.find_element_by_id("js--windows_count_0")
        elem.clear()
        elem.send_keys(1)
        # запускаем расчет
        elem = driver.find_element_by_class_name(
            "js--calcModelFormSubmit"
        )
        elem.click()
        # проверяем наличие результатов расчета
        self.assertIn('Результаты расчета', driver.page_source)
        # проверяем, что площадь трех стен размером 1х1 равна 4
        elem = driver.find_element_by_css_selector(
            "ul.data-list li:nth-child(4) strong"
        )
        self.assertEqual('3 м²', elem.text)

        # добавляем дверь
        elem = driver.find_element_by_css_selector(
            "fieldset[name=doors] button"
        )
        elem.click()
        # задаем размеры двери 1х1 - во всю стену, кол-во дверей - 1
        elem = driver.find_element_by_id("js--doors_height_0")
        elem.clear()
        elem.send_keys(1)
        elem = driver.find_element_by_id("js--doors_width_0")
        elem.clear()
        elem.send_keys(1)
        elem = driver.find_element_by_id("js--doors_count_0")
        elem.clear()
        elem.send_keys(1)
        # запускаем расчет
        elem = driver.find_element_by_class_name(
            "js--calcModelFormSubmit"
        )
        elem.click()
        # проверяем наличие результатов расчета
        self.assertIn('Результаты расчета', driver.page_source)
        # проверяем, что площадь двух стен размером 1х1 равна 4
        elem = driver.find_element_by_css_selector(
            "ul.data-list li:nth-child(4) strong"
        )
        self.assertEqual('2 м²', elem.text)

    # вспомогательный метод для заполнения данных из таблиц
    def input_from_tables(self, hei, sq, rw):
        driver = self.driver
        # высота
        # находим элемент страницы по ID
        elem = driver.find_element_by_id("js--roomСeiling_height")
        # очищаем элемент от старого значения
        elem.clear()
        # вносим новое значение
        elem.send_keys(str(hei))
        # ширину и длину вычислим из площади в таблице:
        # воспользуемся тем, что в таблице площадь четная,
        # ширину будем считать равной 2
        elem = driver.find_element_by_id("js--roomSizes_width")
        elem.clear()
        elem.send_keys(2)
        # длина
        elem = driver.find_element_by_id("js--roomSizes_length")
        elem.clear()
        elem.send_keys(str(sq/2))
        # ширина рулона
        elem = driver.find_element_by_id("js--wallpaperSizes_rollWidth")
        elem.clear()
        elem.send_keys(rw)

    # метод для проверки работы калькулятора
    # на таблице с шириной 53
    def test_width_53(self):
        driver = self.driver
        # добавляем окно
        elem = driver.find_element_by_css_selector(
            "fieldset[name=windows] button"
        )
        elem.click()
        # задаем стандартный размер окон 1.17х1.46
        elem = driver.find_element_by_id("js--windows_height_0")
        elem.clear()
        elem.send_keys('1.17')
        elem = driver.find_element_by_id("js--windows_width_0")
        elem.clear()
        elem.send_keys('1.46')
        # добавляем дверь
        elem = driver.find_element_by_css_selector(
            "fieldset[name=doors] button"
        )
        elem.click()
        # задаем стандартный размер дверей 2.07х0.87
        elem = driver.find_element_by_id("js--doors_height_0")
        elem.clear()
        elem.send_keys('2.07')
        elem = driver.find_element_by_id("js--doors_width_0")
        elem.clear()
        elem.send_keys('0.87')
        # задаем счетчик окон и дверей, который будет увеличиваться
        # вместе с увеличением площади комнаты
        windows_count = 0

        # открываем сохраненную таблицу
        filedesc = open("test53.csv", "r")
        # считываем весь файл как список строк
        filecontent = filedesc.readlines()
        # цикл по строкам файла
        for i in range(len(filecontent)):
            # пропускаем первую строку с заголовком
            if i > 0:
                # разбиение строки на ячейки по символу ";"
                cells = filecontent[i].split(";")
                # увеличиваем значение счетчика окон и дверей
                windows_count += 1
                # вводим число окон
                elem = driver.find_element_by_id("js--windows_count_0")
                elem.clear()
                elem.send_keys(windows_count)
                # вводим число дверей
                elem = driver.find_element_by_id("js--doors_count_0")
                elem.clear()
                elem.send_keys(windows_count)

                # проверка корректности вычислений
                # по первым двум столбцам (высота 2,25 м)
                self.input_from_tables(float(cells[0]), float(cells[1]), 53)
                # запускаем расчет
                elem = driver.find_element_by_class_name(
                    "js--calcModelFormSubmit"
                )
                elem.click()
                # проверяем наличие результатов расчета
                self.assertIn('Результаты расчета', driver.page_source)
                # проверяем, что площадь совпадает с табличной
                elem = driver.find_element_by_css_selector(
                    "ul.data-list li:nth-child(1) strong"
                )
                print("Проверка для площади ", cells[1], ": ")
                self.assertEqual(cells[2]+' шт', elem.text)
                print("OK")
        filedesc.close()

    # тестируем кнопочный калькулятор
    def test_calc(self):
        driver = self.driver
        # открываем калькулятор
        elem = driver.\
            find_element_by_css_selector(".js--onclick-callCalc")
        elem.click()
        # ждем, пока калькулятор откроется
        time.sleep(5)
        # перебиваем цифры от 0 до 9 (ноль не будет отображаться перед 1)
        for i in range(10):
            print("Нажатие кнопки ", str(i), ": ")
            elem = driver.find_element_by_name(str(i))
            elem.click()
            print("OK")
        # проверяем изображение на дисплее
        # (ноль не будет отображаться перед 1)
        elem = driver.find_element_by_class_name("display-indicator-ceils")
        self.assertEqual(elem.text, '123456789')

    # тестируем кнопочный калькулятор
    def test_calc2(self):
        driver = self.driver
        # открываем калькулятор
        elem = driver.find_element_by_css_selector(".js--onclick-callCalc")
        elem.click()
        # ждем, пока калькулятор откроется
        time.sleep(5)
        # перебиваем цифры от 1 до 3 (ноль не будет отображаться перед 1)
        for i in range(1, 4):
            print("Нажатие кнопки ", str(i), ": ")
            elem = driver.find_element_by_name(str(i))
            elem.click()
            print("OK")
        elem = driver.find_element_by_name("+")
        elem.click()

        # перебиваем цифры от 1 до 3 (ноль не будет отображаться перед 1)
        for i in range(4, 7):
            print("Нажатие кнопки ", str(i), ": ")
            elem = driver.find_element_by_name(str(i))
            elem.click()
            print("OK")

        elem = driver.find_element_by_name("Result")
        elem.click()
        # проверяем изображение на дисплее
        # (ноль не будет отображаться перед 1)
        elem = driver.find_element_by_class_name("display-indicator-ceils")
        self.assertEqual(elem.text, str(123 + 456))

if __name__ == '__main__':
    unittest.main()
