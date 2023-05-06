import random
from DBase import Table
import USER_utilits

class Film:
    def __init__(self, name:str, style:str, period:int):
        self.name = name
        self.style = style
        self.period = period


class User:
    def __init__(self, login:str, password:str):
        self.login = login
        self.password = password


class Hall:
    def __init__(self, name:str, num_of_rows:int, num_of_seats_in_row:int):
        self.name = name
        self.num_of_rows = num_of_rows
        self.num_of_seats_in_row = num_of_seats_in_row

"""
class Cinema_post():
    def __init__(self, num_of_date:int, count_films:int):
        self.num_of_date = num_of_date
        self.count_films = count_films
        self.date = ''
        if num_of_date == 0:
            self.date = '28.04'
        elif num_of_date == 1:
            self.date = '29.04'
        elif num_of_date == 2:
            self.date = '30.04'
        else:
            print('404 ERROR в CINEMA_POST CLASS')

        self.films_in_date = []
        self.halls_in_date = []

        for i in range(count_films):
            self.films_in_date.append(random.choice(films_list))
        for k in range(count_films):
            self.halls_in_date.append(random.choice(halls_list))
"""



films_list = list()
users_list = list()
halls_list = list()
dates = ['28.04', '29.04', '30.04']

#синема пост не трогать в csv
cinema_post_list = list()

films_for_28 = {'Соник':'Средний',
                'Москва слезам не верит':'VIP',
                'Шрэк 2':'Средний',
                'Аватар':'Малый',
                'Белый клык':'Малый'}

films_for_29 = {'Фиксики':'VIP',
                'Почему он':'Средний',
                'Убийство в Париже':'VIP',
                'Достать ножи':'Малый',
                'Шрэк 2':'Средний'}

films_for_30 = {'Достать ножи':'Малый',
                'Аватар':'Средний',
                'Белый клык':'Малый',
                'Шрэк 2':'VIP',
                'Фиксики':'VIP'}

cinema_post_list.append(films_for_28)
cinema_post_list.append(films_for_29)
cinema_post_list.append(films_for_30)



### FOR USER ###
films = []
for obj_flm in films_list:
    films.append(obj_flm.name)

film_tiles = [USER_utilits.Tile(flm) for flm in films]
date_tiles = [USER_utilits.Tile(date) for date in dates]
### FOR USER ###


### FOR BD ###
for tb in ['films', 'holls', 'users']:
    table = Table(tb).get_collection_by_index()
    for row in table:
        if tb == 'films':
            films_list.append(Film(str(row[1]), str(row[2]), str(row[3])))
        elif tb == 'holls':
            halls_list.append(Hall(str(row[1]), str(row[2]), str(row[3])))
        elif tb == 'users':
            users_list.append(User(str(row[1]), str(row[2])))
### FOR BD ###
