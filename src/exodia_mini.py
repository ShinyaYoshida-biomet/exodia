import numpy as np
import random
from collections import defaultdict



class Duel :
    def __init__(self):
        global decks, hands, normal_summon, cemetary
        self.cards = {
                    "封印されし者の左足" : 1,
                    "封印されし者の左腕" : 1,
                    "封印されし者の右腕" : 1,
                    "封印されし者の右足" : 1,
                    "封印されしエクゾディア" : 1,
                    "一時休戦" : 1,
                    "成金ゴブリン" : 3,
                    "テラ・フォーミング" : 1,
                    "チキン・レース" : 3
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

class teraforming(Duel) :
    def __init__(self) :
        self.category = "magic"
        self.name = "テラ・フォーミング"

    def activate(self) :
        global decks, hands, normal_summon, cemetary
        hands.remove(self.name)
        cemetary.append(self.name)
        hands.append('チキン・レース')
        decks.remove('チキン・レース')


class chicken_race(Duel) :
    def __init__(self) :
        self.category = "magic"
        self.name = 'チキン・レース'

    def activate(self) :
        global decks, hands, normal_summon, cemetary
        hands.remove(self.name)
        cemetary.append(self.name)
        hands.append(self.draw())



cards = {
    "封印されし者の左足" : exodia_left_leg,
    "封印されし者の左腕" : exodia_left_hand,
    "封印されし者の右腕" : exodia_right_hand,
    "封印されし者の右足" : exodia_right_leg,
    "封印されしエクゾディア" : exodia,
    "一時休戦" : rest_for_a_while,
    "成金ゴブリン" : upstart_goblin,
    "テラ・フォーミング" : teraforming,
    "チキン・レース" : chicken_race}





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
