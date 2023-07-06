import random
import time


def start_meeting_with_monster():
    print('Вы встретили человека в капюшоне, почуяв смердячий запах монстра, вы решили помочь человеку, препупредив\n'
          'его об опасности, но, когда он скинул капюшон стало понятно что он не человек...')


possible_rarity = ["обычный", "редкий", "легендарный"]

hero_hp = 100
hero_damage = 9
hero_level = 1

monster1_rarity = random.choice(possible_rarity)

if monster1_rarity == "обычный":
    monster1_hp = 50
    monster1_damage = 10
    monster1_lvl = 1

if monster1_rarity == "редкий":
    monster1_hp = 80
    monster1_damage = 15
    monster1_lvl = 2

if monster1_rarity == "легендарный":
    monster1_hp = 100
    monster1_damage = 30
    monster1_lvl = 3

print("Вы встретили монстра и он", monster1_rarity, "уровень", hero_level)

while hero_hp > 0 and monster1_hp > 0:
    print("Здоровье монстра:", monster1_hp)
    print("Максимальный урон монстра", monster1_damage)
    print("Здоровье героя:", hero_hp)
    print("Максимальный урон героя", hero_damage)

    choice_user = input("Введите действие 1 - Атака, 2 - Уклонение, 3 - Блок: ")

    choice_monster = random.choice(["1", "2", "3"])

    if choice_user == "1" and choice_monster == "1":
        time.sleep(0.7)
        print("Вы берете свой меч... ")
        time.sleep(0.7)
        print("и бросаетесь на монстра... ")
        time.sleep(0.5)

        hero_damage_the_fight = random.randint(int(hero_damage / 2), hero_damage)
        monster1_hp = monster1_hp - hero_damage_the_fight
        print("Ваш урон по монстру", hero_damage_the_fight)
        time.sleep(0.4)
        print("У монстра осталось ", monster1_hp, "здоровья")

        time.sleep(0.7)
        print("монстр издает истошный вопль... ")
        time.sleep(0.7)
        print("и и кусает героя... ")
        time.sleep(0.5)

        monster_damage_the_fight = random.randint(int(monster1_damage / 2), monster1_damage)
        hero_hp = hero_hp - monster_damage_the_fight
        print("урон монстра", monster_damage_the_fight)
        time.sleep(0.4)
        print("У героя осталось ", hero_hp, "здоровья")
    # если герой выбрал атаку а монстр выбрал уклониться
    elif choice_user == "1" and choice_monster == "2":
        hero_damage_the_fight = random.randint(int(hero_damage / 2), hero_damage)
        choice_monster = random.choice(["1", "2"])
        if choice_user == "1":
            print("Монстр уклоняется от вашего удара, вы не наносите урона")
        elif choice_user == "2":
            print("монстр спотыкается о свои ноги и получает двойной урон")
            monster1_hp = monster1_hp - hero_damage_the_fight * 2
    elif choice_user == "2" and choice_monster == "1":
        monster_damage_the_fight = random.randint(int(monster1_damage / 2), monster1_damage)
        choice_user = random.choice(["1", "2"])
        if choice_user == "1":
            print("Герой уклоняется от удара, монстр не наносит урона")
        elif choice_user == "2":
            print("Герой спотыкается на банановой кожуре и получает двойной урон")
            hero_hp = hero_hp - monster_damage_the_fight * 2
    elif choice_user == "2" and choice_monster == "2":
        print("Герой и монстр решили станцевать танго и вальс ")
    elif choice_user == "3" and choice_monster == "1":
        print("Вы ставите блок как в фильме про звёздные войны, но он вам толком не помог")
        time.sleep(0.4)
        hero_hp = hero_hp - 5
        print("Монстр сбивает вас с ног сокрушительным ударом")
        time.sleep(0.4)
        print("Вы успели встать прямо перед добиванием монстра")
    elif choice_user == "3" and choice_monster == "2":
        print("Так как у обоих гениев в этой битве было 5 iq один поставил блок как в звёздных войнах, а другой решил"
              "стать кабанчиком")
    elif choice_user == "3" and choice_monster == "3":
        print("С каждой секундой становилось понятно что это больше походит на интелектуальную битву,"
              "так как оба простояли в блоке всего лишь 2 часа")
    elif choice_user == "1" and choice_monster == "3":
        print("Вы увидели что монстр к чему то готовится и вы решили нанести сокрушительный удар")
        time.sleep(0.4)
        print("Монстр упал от вашего удара")
        monster1_hp = monster1_hp - 5
    elif choice_user == "2" and choice_monster == "3":
        print("Один гений решил потанцевать танго, а другой решил понаблюдать из укрытия")
