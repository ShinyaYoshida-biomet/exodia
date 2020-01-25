# /bin/python
import random
import multiset as ms
import numpy as np
import copy
import traceback
import pandas as pd
from collections import defaultdict
from tqdm import tqdm

alpha = 0.9
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
                    "封印されしエグゾディア" : 1,
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
        self.name = "封印されしエグゾディア"
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
    "封印されしエグゾディア" : exodia,
    "一時休戦" : rest_for_a_while,
    "成金ゴブリン" : upstart_goblin,
    "テラ・フォーミング" : teraforming,
    "チキン・レース" : chicken_race}



def complete_exodia() :
    global hands
    win_hands = ["封印されし者の左足", "封印されし者の左腕",
        "封印されし者の右足", "封印されし者の右腕", "封印されしエグゾディア"]
    tf = (len(hands) >= 5) and (set(win_hands) <= set(hands))
    return(tf)


def get_rewards() :
    global decks, win_hands
    reward = 13 - len(decks) + len(hands) + normal_summon
    reward += sum(["封印されし" in k for k in hands])
    reward -= sum(["テラ・フォーミング" in k for k in hands])
    if complete_exodia() :
        print("big rewards")
        reward += 1000
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



def existed_state(states, Q_table) :
    hands = ms.Multiset(states["hands"])
    fields = ms.Multiset(states["fields"])
    cemetary = ms.Multiset(states["cemetary"])
    cond = f"hands=='{hands}'"
    cond += f" & fields=='{fields}'"
    cond += f" & cemetary=='{cemetary}'"

    tf = (Q_table.hands == hands) * (Q_table.fields == fields) * (Q_table.cemetary == cemetary)
    if tf.sum() == 0 :
        return(False)
    else :
        ind = Q_table.index[tf.values][0]
        return(ind)



def add_states_toQ(states, Q_table) :
    array = [ms.Multiset(states["hands"]), ms.Multiset(states["fields"]),
        ms.Multiset(states["cemetary"])]
    array += [0]*(Q_table.shape[1]-3)
    s = pd.Series(array, index=Q_table.columns)
    Q_table = Q_table.append(s, ignore_index=True)
    return(Q_table)


def decide_action(states, Q_table) :
    ind = existed_state(states, Q_table)
    actions = get_actions()
    if type(ind) == np.int64 and not Q_table.empty :
        s = Q_table.iloc[ind, :]
        cands = np.argmax(s[actions])
        max_ = cands.max()
    else  :
        Q_table = add_states_toQ(states, Q_table)
        n_actions = len(actions)
        if n_actions >=1 :
            cands = list(actions)[np.random.randint(n_actions)]
        else :
            raise Exception("ImplementError")
        max_ = 0


    if type(cands) == str :
        best_action = cands
    else :
        i = np.random.randint(0, len(cands))
        best_action = cands.index[i]
    return(best_action, max_, Q_table)

#decide_action(states, Q_table)[2]


def renew_Q(best_action, prev_val, Q_table, original_states, new_states) :
    global alpha, gamma, decks
    reward = get_rewards()
    best_action_next, Qmax, Q_table = decide_action(new_states, Q_table)
    new_val = (1 - alpha) * prev_val + alpha * (reward + gamma * Qmax)

    ind = existed_state(original_states, Q_table)
    if type(ind)==np.int64  :
        Q_table.loc[ind, best_action] = new_val
    else :
        Q_table = add_states_toQ(original_states, Q_table)
        Q_table.loc[Q_table.index[-1], best_action] = new_val

    return(Q_table)



#normal_summon
Q_tables = []
colQ = ["hands", "fields", "cemetary"] + list(cards.keys())
Q_table = pd.DataFrame(columns =colQ)
n_success = 0
for i in tqdm(range(2000)) :
    try :
        duel = Duel()
        duel.start()
        if complete_exodia() :
             n_success += 1
             pass
        tf = True
        j = 0
        while tf :
            states = get_states()
            original_states = copy.deepcopy(states)
            actions = get_actions()
            best_action, prev_val, Q_table = decide_action(states, Q_table)
            actions[best_action]()
            if complete_exodia() :  n_success += 1
            new_states = get_states()
            Q_table = renew_Q(best_action, prev_val,
                Q_table, original_states, new_states)
            tf = not(complete_exodia() or len(decks) == 0 or j >= 30)
            j += 1
        Q_tables.append(Q_table)

    except :
        pass

print(n_success)

Q_table.sum()
Q_table.shape

sum(Q_table.hands == ms.Multiset(["チキン・レース",
    "テラ・フォーミング", "チキン・レース", "成金ゴブリン", "封印されしエグゾディア"]))


Q_table.loc[Q_table.hands == ms.Multiset(["チキン・レース", "テラ・フォーミング", "チキン・レース", "成金ゴブリン", "封印されしエグゾディア"]), :]
Q_table.drop(columns=["hands", "fields", "cemetary"]).sum(axis=1).sort_values()
Q_table.iloc[2491,]["hands"]
Q_table.iloc[690,]["hands"]
Q_table.iloc[1422,]["hands"]
Q_table.iloc[4153,]
Q_table.iloc[56, ]
Q_table.query("テラ・フォーミング >= 10")
Q_table[Q_table["テラ・フォーミング"]>=10]


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
