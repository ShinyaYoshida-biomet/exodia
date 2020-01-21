import numpy as np
import random
import copy
import traceback
import pandas as pd
from collections import defaultdict


alpha = 0.2
gamma = 0.9
states_key = ["hands", "fields", "cemetary", "normal_summon"]

class Duel :
    def __init__(self):
        global decks, hands, normal_summon, cemetary
        hands, cemetary, fields = [], [], []
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


class Monster(Duel) :
    def __init__(self) :
        self.category = "monster"

    def summon(self) :
        global decks, hands, normal_summon, cemetary
        normal_summon -= 1
        if normal_summon < 0 :
            raise Exception("ImplementError")

        else :
            fields.append(self.name)
            hands.remove(self.name)




class exodia(Monster) :
    def __init__(self) :
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
        self.name = "封印されし者の左腕"
        self.atk = 200
        self.dfc = 300

class exodia_right_hand(Monster) :
    def __init__(self) :
        self.category = "monster"
        self.tribe = "magician"
        self.level = 1
        self.attribute = "darkness"
        self.name = "封印されし者の右腕"
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
        if 'チキン・レース' not in decks :
            raise Exception("ImplementError")
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


def complete_exodia() :
    global hands
    win_hands = np.array(["封印されし者の左足", "封印されし者の左腕",
        "封印されし者の右足", "封印されし者の右腕", "封印されしエグゾディア"])
    tf = (len(hands) >= 5) and (set(win_hands) in set(hands))
    return(tf)


def get_rewards() :
    global decks, win_hands
    reward = 13 - len(decks) + len(hands) + normal_summon
    if complete_exodia() :
        print(f"This is the hands {hands}")
        reward += 100
        print("Win")
    return(reward)

def get_states() :
    global hands, fields, cemetary, decks, normal_summon
    states = defaultdict()
    states["hands"] = hands
    states["fields"] = fields
    states["cemetary"] = cemetary
    states["normal_summon"] = normal_summon
    states["decks"] = decks
    return(states)



def reverse_states(original_states) :
    global hands, fields, decks, normal_summon, cemetary, states_key

    hands = original_states["hands"]
    fields = original_states["fields"]
    decks = original_states["decks"]
    normal_summon = original_states["normal_summon"]
    cemetary = original_states["cemetary"]
    states = get_states()
    return(states)


def get_actions() :
    global hands, cards
    action_dict = defaultdict()
    for k in hands :
        card = cards[k]()
        if card.category == "magic" :
            action = cards[k]().activate
        elif card.category == "monster" :
            action = cards[k]().summon
        else  :
            action = none
        action_dict[card.name] = action
    return(action_dict)


def get_index(original_states) :
    ind = ""
    global states_key
    #for i in range(len(states)) :\
    for k in states_key :
        original_states["normal_summon"] = str(original_states["normal_summon"])
        ind += f"{k}_" + "_".join(original_states[k])
    return(ind)


def get_Qval(states, action) :
    global Q_table
    ind = get_index(states)
    if ind in list(Q_table.index) :
        q = Q_table.loc[ind, action]
    else  :
        s = pd.Series([0]*Q_table.shape[1], index=Q_table.columns, name=ind)
        Q_table = Q_table.append(s)
        q = 0
    return(q)


def get_Qmax(action_dict) :
    global Q_table
    qs = []
    for l in action_dict :
        print(l)
        save_original_states()
        action_dict[l]() # action
        new_states = get_states()
        q = get_Qval(new_states, l)
        reverse_states()
        qs.append(q)
    best_action = list(action_dict.keys())[np.argmax(qs)]
    return(best_action, max(qs))


def decide_action(states) :
    global Q_table
    ind = get_index(states)
    actions = get_actions()
    if ind  in list(Q_table.index) :
        s = Q_table.loc[ind, :]
    else  :
        s = pd.Series([0]*Q_table.shape[1], index=Q_table.columns, name=ind)
        Q_table = Q_table.append(s)
    # best_action = s[actions].argmax()
    cands = np.argmax(s[actions])
    if type(cands) == str :
        best_action = cands
    else :
        i = np.random.randint(0, len(cands))
        best_action = cands.index[i]

    return(best_action, s.max())



def renew_Q(best_action, prev_val) :
    global Q_table, alpha, gamma, decks
    reward = get_rewards()
    original_states = copy.deepcopy(get_states())
    action_dict = get_actions()

    action_dict[best_action]()

    new_states = get_states()
    #states = reverse_states(original_states)
    best_action_next, Qmax = decide_action(new_states)
    new_val = (1 - alpha) * prev_val + alpha * (reward + gamma * Qmax)

    ind = get_index(original_states)
    if ind in list(Q_table.index) :
        Q_table.loc[ind, best_action] = new_val
    else :
        s = pd.Series([0]*Q_table.shape[1], index=Q_table.columns, name=ind)
        s[best_action] = new_val
        Q_table = Q_table.append(s)






Q_tables = []
Q_table = pd.DataFrame(columns = cards.keys())
n_success = 0
for i in range(10000) :
    try :
        duel = Duel()
        duel.start()
        tf = True
        j = 0
        while tf :
            states = get_states()
            actions = get_actions()
            best_action, prev_val = decide_action(states)
            renew_Q(best_action, prev_val)
            actions[best_action]()
            tf = not(complete_exodia() or len(decks) == 0 or j >= 30)
            j += 1
        Q_tables.append(Q_table)
        n_success += 1

    except :
        pass

Q_table.index.nunique()
Q_tables[0]
Q_table.sum()
actions = get_actions()
states = get_states()
actions, states
best_action, prev_val = decide_action(states)
states
renew_Q(best_action, prev_val)
Q_table
get_states()




#### Duel simulation
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
