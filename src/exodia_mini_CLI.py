# /bin/python
import os
import random
import multiset as ms
import numpy as np
import copy
import traceback
import pandas as pd
from collections import defaultdict
from tqdm import tqdm
import sys



class Duel :
    def __init__(self):
        global decks, hands, normal_summon, cemetary
        hands, cemetary, fields = [], [], []
        self.cards = {
                    "封印されし者の左足" : 1,
                    "封印されし者の左腕" : 1,
                    "封印されし者の右腕" : 1,
                    "封印されし者の右足" : 1,
                    "封印されしエグゾディア" : 1,
                    "ブルーアイズ・トゥーン・ドラゴン" : 1,
                    "魔導書士バテル" : 1,
                    "一時休戦" : 1,
                    "ルドラの魔導書" : 1,
                    "トゥーンのもくじ" : 3,
                    "トレード・イン" : 1,
                    "成金ゴブリン" : 3,
                    "テラ・フォーミング" : 1,
                    "チキン・レース" : 3,
                    "擬似空間" : 3
                    }
        self.win_hands = np.array(["封印されし者の左足", "封印されし者の左腕",
            "封印されし者の右足", "封印されし者の右腕", "封印されしエグゾディア"])

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
        # if self.win_hands in np.array(hands) :
        #     print("Win! Exodia was completed")
        return(draw_card)

    def choose_target(self, targets) :
        if len(targets) == 0 :
            #print(chr(27) + "[2J")
            print("===========================================")
            print("There are no targets")
            sys.exit()

        #print(chr(27) + "[2J")
        print("===========================================")
        print("Choose the target card")
        for i in range(len(targets)) : print(f"{i} : {targets[i]}")
        index = int(input())
        target = targets[index]
        return(target)

    def search(self, target) :
        hands.append(target)
        decks.remove(target)



class Monster(Duel) :
    def __init__(self) :
        self.name = None
        self.category = "monster"

    def summon(self) :
        global decks, hands, normal_summon, cemetary
        normal_summon -= 1
        if normal_summon < 0 :
            #print(chr(27) + "[2J")
            print("=============================")
            raise Exception("ImplementError")

        elif self.level <= 4 :
            fields.append(self.name)
            hands.remove(self.name)

        self.summoned_effect()

    def summoned_effect(self) :
        print("")


class NormalMagic(Duel) :
    def __init__(self) :
        self.name = None
        self.category = "magic"
        self.magic_type = "normal"

    def activate(self) :
        hands.remove(self.name)
        self.normal_effect()
        cemetary.append(self.name)


    def normal_effect(self) :
        print("")



class FieldMagic(Duel) :
    global cards, hands, fields, cemetary, decks
    def __init__(self) :
        self.name = None
        self.category = "magic"
        self.magic_type = "field"

    def activate(self) :
        for k in fields :
            c = cards[k]()
            if c.category == "magic" :
                if c.magic_type == "field" :
                    fields.remove(k)
                    cemetary.append(k)

        hands.remove(self.name)
        fields.append(self.name)
        self.fields_effect()

    def fields_effect(self) :
        print("")


class exodia(Monster) :
    def __init__(self) :
        super(exodia, self).__init__()
        self.tribe = "magician"
        self.level = 3
        self.attribute = "darkness"
        self.name = "封印されしエグゾディア"
        self.atk = 1000
        self.dfc = 1000

class exodia_left_hand(Monster) :
    def __init__(self) :
        super(exodia_left_hand, self).__init__()
        self.tribe = "magician"
        self.level = 1
        self.attribute = "darkness"
        self.name = "封印されし者の左腕"
        self.atk = 200
        self.dfc = 300

class exodia_right_hand(Monster) :
    def __init__(self) :
        super(exodia_right_hand, self).__init__()
        self.category = "monster"
        self.tribe = "magician"
        self.level = 1
        self.attribute = "darkness"
        self.name = "封印されし者の右腕"
        self.atk = 200
        self.dfc = 300

class exodia_left_leg(Monster) :
    def __init__(self) :
        super(exodia_left_leg, self).__init__()
        self.tribe = "magician"
        self.level = 1
        self.attribute = "darkness"
        self.name = "封印されし者の左足"
        self.atk = 200
        self.dfc = 300


class exodia_right_leg(Monster) :
    def __init__(self) :
        super(exodia_right_leg, self).__init__()
        self.tribe = "magician"
        self.level = 1
        self.attribute = "darkness"
        self.name = "封印されし者の右足"
        self.atk = 200
        self.dfc = 300



class blue_eyes_toon(Monster) :
    def __init__(self) :
        super(blue_eyes_toon, self).__init__()
        self.tribe = "dragon"
        self.level = 8
        self.attribute = "lightness"
        self.name = "ブルーアイズ・トゥーン・ドラゴン"
        self.atk = 3000
        self.dfc = 2500


class spellbook_of_magician_of_prophecy(Monster) :
    def __init__(self) :
        super(spellbook_of_magician_of_prophecy, self).__init__()
        self.tribe = "magician"
        self.level = 2
        self.attribute = "water"
        self.name = "魔導書士バテル"
        self.atk = 500
        self.dfc = 200

    def summoned_effect(self) :
        global decks, hands, normal_summon, cemetary
        targets = []
        for k in decks :
            if "魔導書" in cards[k]().name :
                targets.append(k)

        if len(targets) == 0 :
            print("There are no cards to search")

        else :
            target = self.choose_target(targets)
            self.search(target)


class rest_for_a_while(NormalMagic) :
    def __init__(self) :
        super(rest_for_a_while, self).__init__()
        self.name = "一時休戦"

    def normal_effect(self) :
        global decks, hands, normal_summon, cemetary
        hands.append(self.draw())


class upstart_goblin(NormalMagic) :
    def __init__(self) :
        super(upstart_goblin, self).__init__()
        self.name = "成金ゴブリン"

    def normal_effect(self) :
        global decks, hands, normal_summon, cemetary
        hands.append(self.draw())


class teraforming(NormalMagic) :
    def __init__(self) :
        super(teraforming, self).__init__()
        self.name = "テラ・フォーミング"

    def normal_effect(self) :
        global cards, decks, hands, normal_summon, cemetary
        targets = []
        for k in decks :
            c = cards[k]()
            if c.category == "magic" :
                if c.magic_type == "field" :
                    targets.append(k)
            #raise Exception("ImplementError")
        target = self.choose_target(targets)
        self.search(target)


class toon_content(NormalMagic) :
    def __init__(self) :
        super(toon_content, self).__init__()
        self.name = 'トゥーンのもくじ'

    def normal_effect(self) :
        global decks, hands, normal_summon, cemetary
        toon_cards = list(set([k for k in decks if "トゥーン" in cards[k]().name]))
        target = self.choose_target(toon_cards)
        self.search(target)


class trade_in(NormalMagic) :
    def __init__(self) :
        super(trade_in, self).__init__()
        self.name = 'トレード・イン'

    def normal_effect(self) :
        global cards, decks, hands, normal_summon, cemetary

        targets = []
        for k in hands :
            if cards[k]().category == "monster" :
                if cards[k]().level == 8 :
                    targets.append(k)

        target = self.choose_target(targets)
        hands.remove(target)
        hands.append(self.draw())
        hands.append(self.draw())



class chicken_race(FieldMagic) :
    def __init__(self) :
        super(chicken_race, self).__init__()
        self.name = 'チキン・レース'

    def fields_effect(self) :
        global decks, hands, normal_summon, cemetary
        hands.append(self.draw())


class pseudo_space(FieldMagic) :
    def __init__(self) :
        super(pseudo_space, self).__init__()
        self.name = '擬似空間'

    def fields_effect(self) :
        global cards, decks, hands, normal_summon, cemetary
        targets = []
        for k in cemetary :
            c = cards[k]()
            if c.category == "magic" :
                if c.magic_type == "field" :
                    targets.append(k)

        target = self.choose_target(targets)
        cards[target]().fields_effect()
        cemetary.remove(target)



class spellbook_of_knowledge(NormalMagic) :
    def __init__(self) :
        super(spellbook_of_knowledge, self).__init__()
        self.category = "magic"
        self.name = 'ルドラの魔導書'

    def normal_effect(self) :
        global decks, hands, normal_summon, cemetary

        targets = []
        hands_fields = []
        for k in fields :
            if cards[k]().category == "monster" :
                if cards[k]().tribe == "magician" :
                    targets.append(k)
                    hands_fields.append("fields")

        for k in hands :
            if "魔導書" in cards[k]().name :
                targets.append(k)
                hands_fields.append("hands")

        for i in range(len(targets)) : print(f"{i} : {targets[i]}")
        index = int(input())
        target = targets[index]
        if hands_fields[index] == "hands" :
            hands.remove(target)
        elif hands_fields[index] == "fields" :
            fields.remove(target)
            cemetary.append(target)

        hands.append(self.draw())
        hands.append(self.draw())


cards = {
    "封印されし者の左足" : exodia_left_leg,
    "封印されし者の左腕" : exodia_left_hand,
    "封印されし者の右腕" : exodia_right_hand,
    "封印されし者の右足" : exodia_right_leg,
    "封印されしエグゾディア" : exodia,
    "擬似空間" : pseudo_space,
    "ブルーアイズ・トゥーン・ドラゴン" : blue_eyes_toon,
    "魔導書士バテル" : spellbook_of_magician_of_prophecy,
    "ルドラの魔導書" : spellbook_of_knowledge,
    "一時休戦" : rest_for_a_while,
    "トレード・イン" : trade_in ,
    "トゥーンのもくじ" : toon_content,
    "成金ゴブリン" : upstart_goblin,
    "テラ・フォーミング" : teraforming,
    "チキン・レース" : chicken_race}



def complete_exodia() :
    global hands
    win_hands = ["封印されし者の左足", "封印されし者の左腕",
        "封印されし者の右足", "封印されし者の右腕", "封印されしエグゾディア"]
    tf = (len(hands) >= 5) and (set(win_hands) <= set(hands))
    return(tf)


def get_actions() :
    global hands, cards, normal_summon
    action_dict = defaultdict()

    for k in hands : #k=hands[0]
        action = None
        card = cards[k]()
        if card.category == "magic" :
            action = cards[k]().activate
        elif card.category == "monster" :
            if normal_summon >= 1 :
                action = cards[k]().summon

        if action : action_dict[card.name] = action
        else  : continue
    return(action_dict)



def show_actions(action_dict) :
    keys = list(action_dict.keys())
    for i in range(len(keys)) :
        print(f"{i} : {keys[i]}")



def get_states() :
    global hands, fields, cemetary, decks, normal_summon
    states = defaultdict()
    states["hands"] = hands
    states["fields"] = fields
    states["cemetary"] = cemetary
    states["normal_summon"] = normal_summon
    states["decks"] = decks
    return(states)


def main() :
    duel = Duel()
    duel.start()

    tf = True
    while tf :
        print("The states : ")
        states = get_states()

        for k in states :
            if k!= "decks" :
                print(f" {k} : {states[k]}")
        if complete_exodia() :
            #print(chr(27) + "[2J")
            print("====================================================")
            print("Exodia Completed !")
            print(hands)
            sys.exit()

        action_dict = get_actions()
        keys = list(action_dict.keys())
        if len(keys) == 0 :
            #print(chr(27) + "[2J")
            print("====================================================")
            print("There are no actions")
            sys.exit()

        #print(chr(27) + "[2J")
        print("====================================================")
        print("Choose the action : ")
        show_actions(action_dict)
        action = int(input())

        if complete_exodia() :
            #print(chr(27) + "[2J")
            print("====================================================")
            print("Exodia Completed !")
            print(hands)
            sys.exit()

        key = keys[action]
        action_dict[key]()
        tf = len(decks) != 0



if __name__ == '__main__' :
    main()
