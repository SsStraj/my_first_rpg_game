"""
Герой ищет приключения, каждый ход у него генерируется коффицент удачи

как рассчитывается коффициент удачи и что влиет на него и на что влияет он
коффициент удачи это как бросок кубиков

коффициент удачи влияет на условия в событии

если коффициент плохой когда у нас монстр
то он атакует вас первым


и выпадают разные события
какие?


У героя есть характеристики
сила
ловкость
интелект
жизни

чем больше сила тем больше урон
чем больше ловкость тем больше вероятноть уклонения от аттаки
чем больше интелект тем больше сила способности обмануть

главному герою не на что жить
он бедный авантюрист пошел искать приключения
голод
жажда
устлость
деньги

улучшения снаряжения

нужен сюжет и квесты
квесты побочные и основные

локации
NPC
Карта
события случайные
добавить очищение консоли

идея для локации
болото
нужен спрей от комаров или каждый ход будут отниматься жизни.

пустыня (зыбучий песок)
город
деревня (спавн)
тундра

1 квест дойти до города
найти работу и деньги

он  должен выпонить квесты в деревне
чтобы заработать денег на повозку в город или на коня.

в город можно попасть через тундру.
дома лесника


на каждой локации будут добавлятся события соответсвующие этой локации.


продумать систему локаций и квестов

система плоских координат
ячейки с чем то с домами
людьми и так далее

у тебя есть карта
там туман войны
ты можешь ввести координату
как в шахматах
чтобы переместиться к определенной ячейке


Деревня

[
[дерево, C , дом, камень, деревенщина],
[дерево "",дом, камень, деревенщина],
[дерево "",дом, камень, деревенщина],
[дерево "", "", "", квест],
[дерево "",дом, камень, деревенщина],
]


"""

from random import choice, randint

from marketeer import start_meeting_with_marketeer
from quests import start_quest
from monster import start_meeting_with_monster
from find_item import get_item

events_on_the_way = ['monster', 'quest', 'marketeer', 'item']


def start_event(type_event):
    if type_event == 'monster':
        start_meeting_with_monster()
    elif type_event == 'quest':
        start_quest()
    elif type_event == 'marketeer':
        start_meeting_with_marketeer()
    elif type_event == 'item':
        get_item()


hp_hero = 100
pow_hero = 3

luck_factor = None
player_move = input(f"Однажды вы проснулись и ошутили неприодалимое желание поискать приключений на свою пятую точку.\n"
                    f"И вот вы стоите перед зеркалом в своих блестящих, порваной одежде и трусах и понимаете что для\n"
                    f"геройвств вам рановато. По этим обстоятельвствам вы решаете посмотреть под кроватью на наличие\n"
                    f"хотябы 5 рублёв. Так как вы всю жизнь полагались на удачу вы нашли аж целых 10 рублёв.\n"
                    f"Осознав что вы полный бомж, вы решаете отправиться в путешествии хотябы за 50 рублёв чтобы\n"
                    f"купить такому альфа-самцу одежду, доспехи, еду, ваду, и доблестный меч.\n"
                    f"Чтобы начать своё доблестное путешествие напишите окей летсгоу:")

while True:
    luck_factor = randint(1, 5)

    print("Коффицент удачи:", luck_factor)

    # todo: сделать больше выбор, в начале вывести локацию, и возможные дейтствия.
    # todo: у нас будут локации, на каждой локации будут квесты побочные и сюжетные.
    # todo: не все квесты можно взять с определенного уровня
    # todo: не в каждую локацию можно сразу попасть вас там убьют комары

    input("Искать приключений: ")
    random_event = choice(events_on_the_way)
    start_event(random_event)