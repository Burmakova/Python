# Задание 3 - наивный байесовский классификатор
from sklearn.naive_bayes import GaussianNB
import matplotlib.pyplot as plt
from sklearn import datasets


def prepare_plot():
    # Зададим границы графика 1
    plt.figure(0)
    x1_min, x1_max = X1.min() - .5, X1.max() + .5
    y1_min, y1_max = Y1.min() - .5, Y1.max() + .5
    plt.xlim(x1_min, x1_max)
    plt.ylim(y1_min, y1_max)
    # Зададим границы графика 2
    plt.figure(1)
    x2_min, x2_max = X2.min() - .5, X2.max() + .5
    y2_min, y2_max = Y2.min() - .5, Y2.max() + .5
    plt.xlim(x2_min, x2_max)
    plt.ylim(y2_min, y2_max)

    # Подпишем оси графика 1
    plt.figure(0)
    plt.xlabel('Длина чашелистика')
    plt.ylabel('Ширина чашелистика')
    # Подпишем оси графика 2
    plt.figure(1)
    plt.xlabel('Длина лепестка')
    plt.ylabel('Ширина лепестка')
    # Помещаем точки исходных данных на графики
    plt.figure(0)
    plt.scatter(X1, Y1, c=C, edgecolor='k')
    plt.figure(1)
    plt.scatter(X2, Y2, c=C, edgecolor='k')


# Загрузка набора данных про ирисы
iris = datasets.load_iris()
# Сделаем 2 графика для отображения
# чашелистики
X1 = iris.data[:, 0]
Y1 = iris.data[:, 1]
# лепестки
X2 = iris.data[:, 2]
Y2 = iris.data[:, 3]
# Набор цветов точек - общий для двух графиков
C = iris.target
# Готовим графики к отображению
prepare_plot()
# Отображаем графики в SciView
plt.show()

# Создаем объект-классификатор
clf = GaussianNB()
# Обучаем классификатор имеющимися данными
clf.fit(iris.data, iris.target)
while True:
    print('Введите данные о цветке, '
          'который требуется классифицировать:')
    s_length = float(input('Длина чашелистика (0 - выход): '))
    s_width = float(input('Ширина чашелистика (0 - выход): '))
    p_length = float(input('Длина лепестка (0 - выход): '))
    p_width = float(input('Ширина лепестка (0 - выход): '))
    if s_length*s_width*p_length*p_width == 0:
        break
    # Готовим графики к отображению
    prepare_plot()
    # Помещаем точки идентифицируемого цветка на графики
    plt.figure(0)
    plt.scatter([s_length],
                [s_width],
                c=["#FF0000"])
    plt.figure(1)
    plt.scatter([p_length],
                [p_width],
                c=["#FF0000"])

    # Отображаем графики в SciView
    plt.show()
    # С помощью классификатора
    # выполняем предсказание для введенных параметров
    res = clf.predict([[s_length,
                        s_width,
                        p_length,
                        p_width]])
    # Выводим название сорта ириса по предсказанию
    print('Данный цветок классифицирован как сорт "' +
          iris.target_names[res[0]] + '"')

