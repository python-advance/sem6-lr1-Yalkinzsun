import csv
import pandas as pd
from scipy import stats

def csv_menwomen(file_obj):
    """
    Подсчёт количества мужчин и женщин, находившихся на параходе
    """
    reader = csv.reader(file_obj)
    men, women = 0, 0
    for row in reader:
        for item in row:
            if item == 'male':
                men += 1
            elif item == 'female':
                women += 1
    return men, women


def csv_port(file_obj):
    """
    Подсчёт количества пассажиров, загрузившихся на борт в различных портах
    """
    reader = csv.reader(file_obj)
    s, c, q = 0, 0, 0
    for row in reader:
        for item in row:
            if item == 'S':
                s += 1
            elif item == 'C':
                c += 1
            elif item == 'Q':
                q += 1
    return s, c, q


def csv_pclass(file_obj):
    """
    Подсчёт долей пассажиров первого, второго, третьего класса
    """
    first, second, third = 0, 0, 0
    df = pd.read_csv(file_obj)
    reader = df['Pclass']

    for row in reader:
            if row == 1:
                first += 1
            elif row == 2:
                second += 1
            elif row == 3:
                third += 1
    c = first + second + third
    return 100 * first / c, 100 * second / c, 100 * third / c


def cor_coefficient(file_obj, a, b):
    """
    Вычисление коэффициента корреляции Пирсона между
    двумя столбцами scv-таблицы
    """
    df = pd.read_csv(file_obj)
    res = df[a].corr(df[b])
    return res


def fare(file_obj):
    """
    Посчёт средней цены за билет и медианы
    """
    df = pd.read_csv(file_obj)
    return df['Fare'].mean(), df['Fare'].median()


def popular_name(file_obj):
    """
    Определение самого популярняго мужского и женского имени людей, старше 15 лет на корабле
    """
    df = pd.read_csv(file_obj)
    reader = df[['Name']]

    only_male =reader.loc[df['Sex'] == "male"]
    over15 = only_male.loc[df['Age'] > 15]
    newlist = over15['Name'].tolist()
    male_names = []
    for item in newlist:
        male_names.append(item[item.find('.') + 1:])
    men = stats.mode(male_names)

    only_female = reader.loc[df['Sex'] == "female"]
    fem_over15 = only_female.loc[df['Age'] > 15]
    newlist2 = fem_over15['Name'].tolist()
    female_names = []
    for item in newlist2:
        female_names.append(item[item.find('.') + 1:])
    women = stats.mode(female_names)

    return men, women



if __name__ == "__main__":

    with open('train.csv') as f_obj:
         print("1) Какое количество мужчин и женщин ехало на параходе?")
         a = csv_menwomen(f_obj)
         print('{} мужчин, {} женщин'.format(a[0], a[1]))

    with open('train.csv') as f_obj:
         print("2) Подсчитайте сколько пассажиров загрузилось на борт в различных портах?")
         b = csv_port(f_obj)
         print( 'S = {}, C = {}, Q = {}'.format(b[0], b[1], b[2]) )

    with open('train.csv') as f_obj:
         print("4) Какие доли составляли пассажиры первого, второго, третьего класса?")
         c = csv_pclass(f_obj)
         print('1 = {:.2f}%, 2 = {:.2f}%, 3 = {:.2f}%'.format(c[0], c[1], c[2]))

    with open('train.csv') as f_obj:
         print("5) Вычислите коэффициент корреляции Пирсона между количеством супругов (SibSp) и количеством детей (Parch)")
         print('{:.5f}'.format(cor_coefficient(f_obj, 'SibSp', 'Parch')))

    with open('train.csv') as f_obj:
         print('6.1) Выясните есть ли корреляция между возрастом и параметром survival;')
         print('{:.5f}'.format(cor_coefficient(f_obj, 'Age', 'Survived')))

    with open('train.csv') as f_obj:
         print('6.2) Выясните есть ли корреляция между полом человека и параметром survival;')
         #print('{:.5f}'.format(cor_coefficient(f_obj, 'Sex', 'Survived')))
         print('Корреляция невозможна. TypeError - разные типы данных')

    with open('train.csv') as f_obj:
         print('6.3) Выясните есть ли корреляция между пассажирским классом и параметром survival;')
         print('{:.5f}'.format(cor_coefficient(f_obj, 'Pclass', 'Survived')))  # Ty

    with open('train.csv') as f_obj:
         print("8) Посчитайте среднюю цену за билет и медиану.")
         f = fare(f_obj)
         print('средняя цена = {:.2f} у.е., медиана = {}'.format(f[0], f[1]))

    with open('train.csv') as f_obj:
         print("10) Какие самые популярные мужское и женские имена людей, старше 15 лет на корабле?")
         o = popular_name(f_obj)
         print('мужское имя - {} \nженское имя - {}'.format(o[0], o[1]))
