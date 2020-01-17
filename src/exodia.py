import numpy as np
import random
from collections import defaultdict


# class Deck :

class Duel :
    def __init__(self):
        global decks, hands, normal_summon, cemetary
        self.cards = {"コスモクイーン" : 1,
                    "封印されし者の左足" : 1,
                    "封印されし者の左腕" : 1,
                    "封印されし者の右腕" : 1,
                    "封印されし者の右足" : 1,
                    "封印されしエクゾディア" : 1,
                    "ブルーアイズ・トゥーン・ドラゴン" : 1,
                    "魔道化リジョン" : 3,
                    "召喚僧サモンプリースト" : 3,
                    "王立魔法図書館" : 1,
                    "トゥーンのもくじ" : 3,
                    "魔法石の採掘" : 2,
                    "一時休戦" : 1,
                    "成金ゴブリン" : 3,
                    "リロード" : 2, #"打ち出の小槌" : 2,
                    "黄金色の竹光" : 3,
                    "ダーク・バースト" : 2,
                    "トレード・イン" : 2,
                    "妖刀竹光" : 3,
                    "折れ竹光" : 2,
                    "ワンダー・ワンド" : 3
                    }

    def start(self) :
        global decks, fields, hands, normal_summon, cemetary
        cemetary = []
        normal_summon = 1
        fields = []
        decks = sum([[k]*self.cards[k] for k in self.cards], [])
        hands =  [self.draw() for i in range(5)]
        #self.Deck_num = len(self.Decks)


    def draw(self) :
        global decks, hands, normal_summon, cemetary
        draw_card = random.choice(decks)
        decks.remove(draw_card)
        return(draw_card)

class Monster(Duel) :
    def summon(self) :
        global decks, hands, normal_summon, cemetary
        normal_summon -= 1
        fields.append(self.name)
        hands.remove(self.name)


class cosmo_queen(Monster) :
    def __init__(self) :
        self.category = "monster"
        self.tribe = "magician"
        self.level = 8
        self.attribute = "darkness"
        self.name = "コスモクイーン"
        self.atk = 2900
        self.dfc = 2450

class exodia(Monster) :
    def __init__() :
        self.category = "monster"
        self.tribe = "magician"
        self.level = 3
        self.attribute = "darkness"
        self.name = "封印されしエクゾディア"
        self.atk = 1000
        self.dfc = 1000

class exodia_left_hand(Monster) :
    def __init__(self) :
        self.category = "monster"
        self.tribe = "magician"
        self.level = 1
        self.attribute = "darkness"
        self.name = "封印されし者の左手"
        self.atk = 200
        self.dfc = 300

class exodia_right_hand(Monster) :
    def __init__(self) :
        self.category = "monster"
        self.tribe = "magician"
        self.level = 1
        self.attribute = "darkness"
        self.name = "封印されし者の右手"
        self.atk = 200
        self.dfc = 300

class exodia_left_leg(Monster) :
    def __init__(self) :
        self.category = "monster"
        self.tribe = "magician"
        self.level = 1
        self.attribute = "darkness"
        self.name = "封印されし者の左足"
        self.atk = 200
        self.dfc = 300


class exodia_right_leg(Monster) :
    def __init__(self) :
        self.category = "monster"
        self.tribe = "magician"
        self.level = 1
        self.attribute = "darkness"
        self.name = "封印されし者の右足"
        self.atk = 200
        self.dfc = 300


class blue_eyes_toon(Monster) :
    def __init__(self) :
        self.category = "monster"
        self.tribe = "dragon"
        self.level = 8
        self.attribute = "lightness"
        self.name = "ブルーアイズ・トゥーン・ドラゴン"
        self.atk = 3000
        self.dfc = 2500


class rigion(Monster) :
    def __init__(self) :
        global decks, hands, normal_summon, cemetary
        self.category = "monster"
        self.tribe = "magician"
        self.level = 4
        self.attribute = "darkness"
        self.name = "魔道化リジョン"
        self.atk = 1300
        self.dfc = 1500
        if self.name in fields :
            normal_summon += 1
    # def summon(self) :
    #     global decks, hands, normal_summon, cemetary
    #     #normal_summon -= 1

class summon_priest(Monster) :
    def __init__(self) :
        self.category = "monster"
        self.tribe = "magician"
        self.level = 4
        self.attribute = "darkness"
        self.name = "召喚僧サモンプリースト"
        self.atk = 800
        self.dfc = 1600

    def activate(self, target1, target2) :
        summoned = self.name in fields
        if not summoned :
            print("error")
        elif len([cards[k]().level==4 if cards[k]().category =="monster" else False for k in decks]) == 0 :
            print("No monsters in the deck")
        elif cards[target2].category != "magic" :
            print("error : This is not the magic card")
        elif cards[target2].category != "monster" or cards[target2].level != 4:
            print("error : This is not the monster card")
        else :
            hands.remove(target2)
            cemetary.append(target2)
            decks.remove(targer1)
            fields.append(target1)


class magic_library(Monster) :
    def __init__(self) :
        self.category = "monster"
        self.tribe = "magician"
        self.level = 4
        self.attribute = "lightness"
        self.name = "王立魔法図書館"
        self.atk = 0
        self.dfc = 2000


class toon_content(Duel) :
    def __init__(self) :
        self.category = "magic"
        self.name = "トゥーンのもくじ"

    def activate(self, target) :
        global decks, hands, normal_summon, cemetary
        tf = "トゥーン" in cards[target]().name
        if tf :
            decks.remove(target)
            cemetary.append(self.name)
            hands.append(target)
            hands.remove(target)
        else :
            print("It's not toon card")
            print("Error !")


class magic_excavation(Duel) :
    def __init__(self) :
        self.category = "magic"
        self.name = "魔法石の採掘"

    def activate(self, hand1, hand2, name) :
        global decks, hands, normal_summon, cemetary
        if len(self.hands) < 3 :
            text = f"Error : There are not enough self.hands to activate {name}"
            print(text)

        if "magic" not in [k.category for k in self.cemetary] :
            text = f"There are no magic in self.cemetary"
            print(text)

        hands.remove(name)
        hands.remove(hand1).remove(hand2)
        cemetary.append(name)


class rest_for_a_while(Duel) :
    def __init__(self) :
        self.category = "magic"
        self.name = "一時休戦"

    def activate(self) :
        global decks, hands, normal_summon, cemetary
        hands.remove(self.name)
        cemetary.append(self.name)
        hands.append(self.draw())


class upstart_goblin(Duel) :
    def __init__(self) :
        self.category = "magic"
        self.name = "成金ゴブリン"

    def activate(self) :
        global decks, hands, normal_summon, cemetary
        hands.remove(self.name)
        cemetary.append(self.name)
        hands.append(self.draw())


class reload(Duel) :
    def __init__(self) :
        self.category = "magic"
        self.name = "リロード"

    def activate(self) :
        global decks, hands, normal_summon, cemetary
        hands.remove(self.name)
        cemetary.append(self.name)
        l = len(hands)
        decks.extend(hands)

        hands = []
        hands.extend([self.draw() for i in range(l)])

class golden_takemitsu(Duel) :
    def __init__(self) :
        self.category = "magic"
        self.name = "黄金色の竹光"

    def activate(self) :
        global decks, hands, normal_summon, cemetary, fields
        n_takemitsu = sum(["竹光" in k for k in fields])
        if n_takemitsu < 1 :
            print("Cannot activate : There are no takemitsu card")
        else :
            hands.remove(self.name)
            cemetary.append(self.name)
            hands.append([self.draw() for i in range(2)])


class dark_barst(Duel) :
    def __init__(self) :
        self.category = "magic"
        self.name = "ダーク・バースト"

    def activate(self, target) :
        global cards,  decks, hands, normal_summon, cemetary, fields
        tf1 = [ cards[k]().attribute == "darkness" if cards[k]().category=="monster"  else False for k in fields ]
        tf2 = [ cards[k]().atk <= 1500 if cards[k]().category=="monster"  else False for k in fields ]
        targets = cemetary[(tf1 and tf2)==True]
        if targets :
            cemetary.remove(target)
            hands.append(target)
            hands.remove(self.name)
            cemetary.append(self.name)
            hands.append([self.draw() for i in range(2)])
        else :
            print("No target in the cemetary")


class trade_in(Duel) :
    def __init__(self) :
        self.category = "magic"
        self.name = "トレード・イン"

    def activate(self, target) :
        global cards, decks, hands, normal_summon, cemetary, fields
        tf = [cards[k]().level==8 if cards[k]().category=="monster"  else False for k in fields ]
        targets = hands[tf==True]
        if targets :
            hands.remove(target)
            hands.remove(self.name)
            cemetary.append(self.name)
            hands.append([self.draw() for i in range(2)])
        else :
            print("No target in the hands")


class cursed_takemitsu :
    def __init__(self) :
        self.category = "magic"
        self.name = "妖刀竹光"

    def activate(self, target) :
        global cards, decks, hands, normal_summon, cemetary, fields
        tf = [True if cards[k]().category=="monster"  else False for k in fields]
        targets = fields[tf==True]
        if targets :
            hands.remove(self.name)
            fields.append(self.name)

        else :
            print("No target in the fields")

class cursed_takemitsu :
    def __init__(self) :
        self.category = "magic"
        self.name = "妖刀竹光"

    def activate(self, target) :
        global cards, decks, hands, normal_summon, cemetary, fields
        tf = [True if cards[k]().category=="monster"  else False for k in fields]
        targets = fields[tf==True]
        if targets :
            hands.remove(self.name)
            fields.append(self.name)

        else :
            print("No target in the fields")

class broken_takemitsu :
    def __init__(self) :
        self.category = "magic"
        self.name = "折れ竹光"

    def activate(self, target) :
        global cards, decks, hands, normal_summon, cemetary, fields
        tf = [True if cards[k]().category=="monster"  else False for k in fields]
        targets = fields[tf==True]
        if targets :
            hands.remove(self.name)
            fields.append(self.name)

        else :
            print("No target in the fields")

class wonder_wand :
    def __init__(self) :
        self.category = "magic"
        self.name = "ワンダー・ワンド"

    def activate(self, target) :
        global cards, decks, hands, normal_summon, cemetary, fields
        tf = [cards[k]().category=="magician" if cards[k]().category=="monster"  else False for k in fields]
        targets = fields[tf==True]
        if targets :
            hands.remove(self.name)
            fields.append(self.name)
            target_monster = target
            self.activated = True

        else :
            print("No target in the fields")


    def effect_activate(self) :
        global cards, decks, hands, normal_summon, cemetary, fields
        fields.remove(self.target_monster)
        fields.remove(self.name)
        cemetary.append(self.name)
        cemetary.append(target_monster)
        hands.append([self.draw() for i in range(2)])


cards = {"コスモクイーン" : cosmo_queen,
            "封印されし者の左足" : exodia_left_leg,
            "封印されし者の左腕" : exodia_left_hand,
            "封印されし者の右腕" : exodia_right_hand,
            "封印されし者の右足" : exodia_right_leg,
            "封印されしエクゾディア" : exodia,
            "ブルーアイズ・トゥーン・ドラゴン" : blue_eyes_toon,
            "魔道化リジョン" : rigion,
            "召喚僧サモンプリースト" : summon_priest,
            "王立魔法図書館" : magic_library,
            "トゥーンのもくじ" : toon_content,
            "魔法石の採掘" : magic_excavation,
            "一時休戦" : rest_for_a_while,
            "成金ゴブリン" : upstart_goblin,
            "リロード" : reload, #"打ち出の小槌" : 2,
            "黄金色の竹光" : golden_takemitsu,
            "ダーク・バースト" : dark_barst,
            "トレード・イン" : trade_in,
            "妖刀竹光" : cursed_takemitsu,
            "折れ竹光" : broken_takemitsu,
            "ワンダー・ワンド" : wonder_wand}



duel = Duel()
duel.start()
hands
upstart_goblin().activate()
hands, fields, cemetary
rest_for_a_while().activate()
trade_in().activate("ブルーアイズ・トゥーン・ドラゴン")
upstart_goblin().activate()
hands, fields, cemetary
rigion().summon()
hands, fields, cemetary
wonder_wand().activate("魔道化リジョン")
hands, fields, cemetary
wonder_wand().effect_activate()
summon_priest().activate("王立魔法図書館", "ダーク・バースト")
hands, fields, cemetary
toon_content().activate("トゥーンのもくじ")
toon_content().activate("トゥーンのもくじ")
toon_content().activate("ブルーアイズ・トゥーン・ドラゴン")
hands, fields, cemetary


rigion().summon()
hands, fields, cemetary
broken_takemitsu().activate("魔導化リジョン")


toon_content().activate("トゥーンのもくじ")
toon_content().activate("トゥーンのもくじ")
toon_content().activate("ブルーアイズ・トゥーン・ドラゴン")
hands, fields, cemetary
upstart_goblin().activate()
magic_library().summon()
hands
fields
toon_content().activate("トゥーンのもくじ")
reload().activate()
hands, fields
toon_content().activate("トゥーンのもくじ")

magic_library().summon()

upstart_goblin().activate()
hands
cemetary
summon_priest().summon()
summon_priest().activate("王立魔法図書館", "ダークバースト")

upstart_goblin().activate()
hands
upstart_goblin().activate()
hands


decks
summon_priest().summon()
summon_priest().activate("王立魔法図書館", "黄金色の竹光")
summon_priest()
fields
hands
summon_priest().activate("王立魔法図書館", 'ブルーアイズ・トゥーン・ドラゴン')

toon_content().activate("トゥーンのもくじ")
upstart_goblin().activate()
hands

toon_content().activate()
toon_content().activate()
toon_content().activate()

reload().activate()
summon_priest().summon()
rigion().summon()
hands
