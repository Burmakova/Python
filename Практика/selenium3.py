import unittest
from selenium import webdriver
import time
# для работы с сохраненными файлами
import os
# в именах сохраненных файлов ставится дата
import datetime
# классы для обработки PDF
import textract
# для очистки папки с сохраненными файлами после теста
import shutil
# классы для обработки русского текста в PDF
import io
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage


class PriceTestCase(unittest.TestCase):
    # подготовка к каждому тесту
    def setUp(self):
        # папка для сохранения файлов
        self.savePath = "c:\\testDownloads\\"
        # очистка папки с сохраненными файлами
        if os.path.isdir(self.savePath):
            shutil.rmtree(self.savePath)
        # создание папки для сохранения файлов
        os.mkdir(self.savePath)
        # профиль для сохранения файлов
        profile = webdriver.FirefoxProfile()
        profile.set_preference(
            "browser.download.dir",
            self.savePath
        )
        profile.set_preference("browser.download.folderList", 2)
        profile.set_preference(
            "browser.helperApps.neverAsk.saveToDisk",
            "application/pdf;application/x-pdf"
        )
        profile.set_preference(
            "browser.helperApps.alwaysAsk.force",
            False
        )
        # запуск Firefox при начале каждого теста
        self.driver = webdriver.Firefox(firefox_profile=profile)
        # открытие страницы при начале каждого теста
        self.page = self.driver.get(
            "https://service-online.su/forms/cenniki/"
        )
        # открытие окна авторизации
        elem = self.driver.find_element_by_id("enter")
        elem.click()
        # 5 сек ожидания открытия окна
        time.sleep(5)
        # ввод логина и пароля
        elem = self.driver.find_element_by_name("login")
        elem.send_keys("<Ваш логин>")
        elem = self.driver.find_element_by_name("password")
        elem.send_keys("<Ваш пароль>")
        # нажатие кнопки "Войти"
        elem = self.driver.find_element_by_name("test_enter")
        elem.click()
        # закрытие сообщения об успешном входе
        elem = self.driver.find_element_by_class_name("mfp-close")
        elem.click()

    # окончание каждого теста
    def tearDown(self):
        # выход с сайта во избежание блокировки
        # системой защиты от подбора пароля
        ul = self.driver.find_element_by_id("menu")
        lis = ul.find_elements_by_tag_name("li")
        li = lis[-1]
        li.click()
        # закрытие браузера при окончании каждого теста
        self.driver.close()

    # тест на наличие ссылки "Личный кабинет" в меню
    def testAuthorization(self):
        elem = self.driver.find_element_by_id("menu")
        self.assertIn("Личный\nкабинет", elem.text)

    # тест сохранения одного ценника на английском
    def testOnePrice(self):
        elem = self.driver.find_element_by_id("comp_name")
        elem.send_keys("Eurotorg")
        # английский формат даты год/месяц/день
        elem = self.driver.find_element_by_id("date")
        elem.clear()
        elem.send_keys("2020/01/13")
        # выбор белорусского рубля в выпадающем списке валют
        elem = self.driver.find_element_by_name("valyuta")
        elem.click()
        options = elem.find_elements_by_tag_name("option")
        for option in options:
            if option.text == "Белорусский рубль, 974":
                option.click()
                break

        elem = self.driver.find_element_by_id("tovar_ed_default")
        elem.send_keys("kg")
        elem = self.driver.find_element_by_id("tovar_country_default")
        elem.send_keys("RB")

        # таблица с товарами
        elem = self.driver.find_element_by_id("tab1")
        tbody = elem.find_element_by_tag_name("tbody")
        tr = tbody.find_element_by_tag_name("tr")
        # название товара
        td = tr.find_element_by_class_name("tovar_name")
        field = td.find_element_by_tag_name("textarea")
        field.send_keys("Candy Southern Night")
        # цена товара - английский формат с точкой
        td = tr.find_element_by_class_name("tovar_cena")
        field = td.find_element_by_tag_name("input")
        field.send_keys("10.55")

        # жмем ссылку "Скачать"
        elem = self.driver.find_element_by_id("download")
        elem.click()
        # 10 сек ожидания
        # на случай, если Firefox спросит, сохранять файл
        time.sleep(10)

        # проверяем наличие сохраненного файла по названию
        today = datetime.date.today()
        fullpath = (self.savePath +
                "cenniki-new-" +
                today.strftime("%Y-%m-%d") +
                ".pdf"
        )
        self.assertEqual(
            os.path.isfile(fullpath),
            True
        )

        # получаем текст из сохраненного файла
        page = textract.process(fullpath)
        # проверяем наличие введенных значений в тексте файла
        #print(page)
        self.assertIn(b"Eurotorg", page)
        self.assertIn(b"2020/01/13", page)
        self.assertIn(b"kg", page)
        self.assertIn(b"RB", page)
        self.assertIn(b"Candy Southern Night", page)
        # цена
        self.assertIn(b"10", page)
        self.assertIn(b"55", page)

    # тест сохранения одного ценника на русском
    def testOnePriceRu(self):
        elem = self.driver.find_element_by_id("comp_name")
        elem.send_keys("ООО Евроторг")
        elem = self.driver.find_element_by_id("date")
        elem.send_keys("13.01.2020")
        # выбор белорусского рубля в выпадающем списке валют
        elem = self.driver.find_element_by_name("valyuta")
        elem.click()
        options = elem.find_elements_by_tag_name("option")
        for option in options:
            if option.text == "Белорусский рубль, 974":
                option.click()
                break

        elem = self.driver.find_element_by_id("tovar_ed_default")
        elem.send_keys("кг")
        elem = self.driver.find_element_by_id("tovar_country_default")
        elem.send_keys("РБ")

        # таблица с товарами
        elem = self.driver.find_element_by_id("tab1")
        tbody = elem.find_element_by_tag_name("tbody")
        tr = tbody.find_element_by_tag_name("tr")
        # название товара
        td = tr.find_element_by_class_name("tovar_name")
        field = td.find_element_by_tag_name("textarea")
        field.send_keys("Конфеты Южная ночь")
        # цена товара
        td = tr.find_element_by_class_name("tovar_cena")
        field = td.find_element_by_tag_name("input")
        field.send_keys("10,55")

        # жмем ссылку "Скачать"
        elem = self.driver.find_element_by_id("download")
        elem.click()
        # 10 сек ожидания
        # на случай, если Firefox спросит, сохранять файл
        time.sleep(10)

        # проверяем наличие сохраненного файла по названию
        today = datetime.date.today()
        fullpath = (self.savePath +
                "cenniki-new-" +
                today.strftime("%Y-%m-%d") +
                ".pdf")
        self.assertEqual(
            os.path.isfile(fullpath),
            True
        )

        # получаем текст из сохраненного файла
        # открываем файл
        fh = open(fullpath, 'rb')
        # открываем первую страницу
        page_obj = PDFPage.get_pages(fh,
                                  caching=True,
                                  check_extractable=True
        ).__next__()

        resource_manager = PDFResourceManager()
        # создаем объект для вывода текста
        fake_file_handle = io.StringIO()
        # создаем конвертер для извлечения текста из PDF
        converter = TextConverter(resource_manager, fake_file_handle)
        # создаем интерпретатор страницы
        page_interpreter = PDFPageInterpreter(resource_manager, converter)
        # извлекаем текст страницы
        page_interpreter.process_page(page_obj)
        # забираем текст страницы в переменную page
        page = fake_file_handle.getvalue()
        # уничтожаем созданные объекты
        converter.close()
        fake_file_handle.close()

        # проверяем наличие введенных значений в тексте файла
        print(page)
        self.assertIn("ООО Евроторг", page)
        self.assertIn("13.01.2020", page)
        self.assertIn("кг", page)
        self.assertIn("РБ", page)
        self.assertIn("Конфеты Южная ночь", page)
        # цена
        self.assertIn("10", page)
        self.assertIn("55", page)


if __name__ == '__main__':
    unittest.main()
