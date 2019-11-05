# Задание 6 - кластеризация k ближайших соседей
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans


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

    n_clusters = int(
        input(
            'Введите число кластеров '
            '(0 - для выхода): '
        )
    )
    if n_clusters == 0:
        break
    # Создаем объект-классификатор
    clr = KMeans(
        n_clusters
    )
    # Кластезизируем имеющиеся наборы параметров
    clr.fit(iris.data)
    # Запоминаем полученные номера кластеров
    # для каждого набора параметров
    # для использования в качестве цвета точек
    C = clr.predict(iris.data)
    # Готовим графики к отображению
    prepare_plot()
    # Отображаем графики в SciView
    plt.show()


