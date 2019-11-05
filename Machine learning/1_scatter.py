# Задание 1 - отображение данных на плоскости,
# метод главных компонентов
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.decomposition import PCA

# Загрузка набора данных про ирисы
iris = datasets.load_iris()
# На плоскости мы можем отложить только 2 из 4 параметров:
# один - по высоте, второй - по ширине.
# Например, возьмем из набора данных первых 2 параметра:
# по ширине (X) будем отклыдывать длину чашелистика
# (столбец 0)
# по высоте (Y) будем отклыдывать ширину чашелистика
# (столбец 1)
X = iris.data[:, 0]
Y = iris.data[:, 1]
# Цветом точек будем отображать их принадлежность
# к определенному сорту ирисов
C = iris.target

# Создаем плоскость для отображения с идентификатором 0
plt.figure(0)
plt.clf()

# Помещаем точки на плоскость
# edgecolor='k' - обводка точек черным
plt.scatter(X, Y, c=C, edgecolor='k')

# Зададим границы отображаемой области
# по 0.5 см больше минимума и максимума
x_min, x_max = X.min() - .5, X.max() + .5
y_min, y_max = Y.min() - .5, Y.max() + .5

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)

# Подпишем оси
plt.xlabel('Длина чашелистика')
plt.ylabel('Ширина чашелистика')

# Отображаем плоскость в окошке SciView
plt.show()

# Аналогичным образом можно построить рисунки
# для оставшихся 5 сочетаний по 2 параметра:
# 1
X = iris.data[:, 0]
Y = iris.data[:, 2]
plt.figure(1)
plt.scatter(X, Y, c=C, edgecolor='k')
x_min, x_max = X.min() - .5, X.max() + .5
y_min, y_max = Y.min() - .5, Y.max() + .5
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xlabel('Длина чашелистика')
plt.ylabel('Длина лепестка')
plt.show()
# 2
X = iris.data[:, 0]
Y = iris.data[:, 3]
plt.figure(2)
plt.scatter(X, Y, c=C, cmap=plt.cm.Set1,
            edgecolor='k')
x_min, x_max = X.min() - .5, X.max() + .5
y_min, y_max = Y.min() - .5, Y.max() + .5
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xlabel('Длина чашелистика')
plt.ylabel('Ширина лепестка')
plt.show()
# 3
X = iris.data[:, 1]
Y = iris.data[:, 2]
plt.figure(3)
plt.scatter(X, Y, c=C, edgecolor='k')
x_min, x_max = X.min() - .5, X.max() + .5
y_min, y_max = Y.min() - .5, Y.max() + .5
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xlabel('Ширина чашелистика')
plt.ylabel('Длина лепестка')
plt.show()
# 4
X = iris.data[:, 1]
Y = iris.data[:, 3]
plt.figure(4)
plt.scatter(X, Y, c=C, edgecolor='k')
x_min, x_max = X.min() - .5, X.max() + .5
y_min, y_max = Y.min() - .5, Y.max() + .5
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xlabel('Ширина чашелистика')
plt.ylabel('Ширина лепестка')
plt.show()
# 5
X = iris.data[:, 2]
Y = iris.data[:, 3]
plt.figure(5)
plt.scatter(X, Y, c=C, edgecolor='k')
x_min, x_max = X.min() - .5, X.max() + .5
y_min, y_max = Y.min() - .5, Y.max() + .5
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xlabel('Длина лепестка')
plt.ylabel('Ширина лепестка')
plt.show()

# Один из способов упрощения анализа визуальных данных
# является метод главных компонент
# (PCA – principal component analysis)
# позволяющий сократить кол-во параметров, а значит -
# кол-во их сочетаний и рисунков для анализа
# (хотя и не без потери данных).
# При этом исходные параметры заменяются
# вычесленными из них ЭЙГЕНпараметрами.
# В ЭЙГЕНпараметры могут объединяться
# плотно взаимосвязанные параметры .
transformer = PCA(n_components=2)
eigenparams = transformer.fit_transform(iris.data)
X = eigenparams[:, 0]
Y = eigenparams[:, 1]
plt.figure(6)
plt.scatter(X, Y, c=C, edgecolor='k')
x_min, x_max = X.min() - .5, X.max() + .5
y_min, y_max = Y.min() - .5, Y.max() + .5
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xlabel('1-ый эйгенпараметр (мб, площадь лепестка)')
plt.ylabel('2-ой эйгенпараметр (мб, площадь чашелистика)')
plt.show()


