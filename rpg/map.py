import os
import time
import random
from rich import print

# todo: Сделать на карте разные объекты на карте,
#  н-р: Деревня, лес, болото, предметы, торговцы, монстры и т.д.
#  А также к каждому объекту добавить свой 'индекс',
#  н-р: 1 - Деревня, 2 - Лес и т.д.
#  когда персонаж переходит на какое либо поле он окрашивается в цвет этого поля
# 1 Деревня - место ивентов, где игрок может остановиться за деньги или найти лут;
# 2 Лес - место ивентов, также поле в котором даётся дебаф к скорости;
# 3 Болото - место ивентов, также поле в котором даётся дебаф к скорости;
# 4 Лут - поле в котором выдаётся случайно сгенерированный лут;
# 5 Торговец - человек который спавниться в рандомной локации, у которого можно что то купить или продать за деньги;
# 6 Монстр - враг гг;
# 7 Дом персонажа(спавн) - место где гг может отдохнуть или выложить свой инвентарь.

objection = [1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6]
hero_name = input("Как вы назовёте своего персонажа:")
hero_hp = 100
hero_lvl = 1
hero_power_attack = 15
hero_inventory = ["бинт", "бинт", "бинт"]
hero_coord_y = 2
hero_coord_x = 2
# Карта разработчика
game_map_inside = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 7, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]


def random_object():
    while objection:
        random_x = random.randint(0, 4)
        random_y = random.randint(0, 4)
        random_objection = random.choice(objection)
        index_random_objection = objection.index(random_objection)
        objection.pop(index_random_objection)
        while game_map_inside[random_y][random_x] != 0:
            random_x = random.randint(0, 4)
            random_y = random.randint(0, 4)
        game_map_inside[random_y][random_x] = random_objection


# Карта игрока
game_map = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 7, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]  # 0 - означает что клетка на карте пустая
random_object()


# Проверка игрока в границах карты
def chek_move():
    global hero_coord_x
    global hero_coord_y
    if hero_coord_x == 5:
        print('Бро, ты не можешь выходить за границу карты!')
        hero_coord_x = 4
        time.sleep(1.3)
    elif hero_coord_x == -1:
        print('Бро, ты не можешь выходить за границу карты!')
        hero_coord_x = 0
        time.sleep(1.3)
    elif hero_coord_y == -1:
        print('Бро, ты не можешь выходить за границу карты!')
        hero_coord_y = 0
        time.sleep(1.3)
    elif hero_coord_y == 5:
        print('Бро, ты не можешь выходить за границу карты!')
        hero_coord_y = 4
        time.sleep(1.3)


def chek_object():
    global hero_coord_x
    global hero_coord_y


def show_map(coord_x, coord_y):
    os.system('cls')

    for y in range(len(game_map)):
        for x in range(len(game_map)):
            if y == coord_y and x == coord_x:
                print("[green]@", end=' ')
            else:
                print(game_map[y][x], end=' ')
        print()


# Карта
def hero_map():
    global hero_coord_x
    global hero_coord_y

    show_map(hero_coord_x, hero_coord_y)

    print("Чтобы переместить персонажа вверх, вниз, влево или вправо введите w, s, a или d.")
    player_answer = input("Введите w, s, a или d:")

    if player_answer == 's' or player_answer == 'S':
        hero_coord_y = hero_coord_y + 1
        hero_coord_x = hero_coord_x
        chek_move()
        game_map[hero_coord_y][hero_coord_x] = game_map_inside[hero_coord_y][hero_coord_x]
        hero_map()
    elif player_answer == 'W' or player_answer == 'w':
        hero_coord_y = hero_coord_y - 1
        hero_coord_x = hero_coord_x
        chek_move()
        game_map[hero_coord_y][hero_coord_x] = game_map_inside[hero_coord_y][hero_coord_x]
        hero_map()
    elif player_answer == 'A' or player_answer == 'a':
        hero_coord_y = hero_coord_y
        hero_coord_x = hero_coord_x - 1
        chek_move()
        game_map[hero_coord_y][hero_coord_x] = game_map_inside[hero_coord_y][hero_coord_x]
        hero_map()
    elif player_answer == 'd' or player_answer == 'D':
        hero_coord_y = hero_coord_y
        hero_coord_x = hero_coord_x + 1
        chek_move()
        game_map[hero_coord_y][hero_coord_x] = game_map_inside[hero_coord_y][hero_coord_x]
        hero_map()
    else:
        print('Введите вверх, вниз, влево или право.')
        time.sleep(1.3)
        hero_map()


hero_map()
