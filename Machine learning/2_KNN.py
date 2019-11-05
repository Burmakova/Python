# Задание 2 - метод k ближайших соседей
import matplotlib.pyplot as plt
from numpy import ndarray
from sklearn import neighbors, datasets


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

while True:

    n_neighbors = int(
        input(
            'Введите число учитываемых соседей '
            '(0 - для выхода): '
        )
    )
    if n_neighbors == 0:
        break
    # Создаем объект-классификатор
    clf = neighbors.KNeighborsClassifier(
        n_neighbors
    )
    # Обучаем классификатор имеющимися данными
    clf.fit(iris.data, iris.target)
    print('Введите данные о цветке, '
          'который требуется классифицировать:')
    s_length = float(input('Длина чашелистика: '))
    s_width = float(input('Ширина чашелистика: '))
    p_length = float(input('Длина лепестка: '))
    p_width = float(input('Ширина лепестка: '))

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

    res = clf.predict([[s_length, s_width, p_length, p_width]])

    print('Данный цветок классифицирован как сорт "' +
          iris.target_names[res[0]] + '"')

