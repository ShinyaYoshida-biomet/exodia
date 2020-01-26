class Gremlin :
    def __init__(self) :
        self.atack = 1300
        self.defence = 1400
        self.card_type = "モンスター"
        self.attribute = "闇"
        self.tribe = "悪魔"
        self.name = "グレムリン"
        self.level = 4


class BlackMagicianGirl :
    def __init__(self) :
        self.atack = 2000
        self.defence = 1700
        self.card_type = "モンスター"
        self.attribute = "闇"
        self.tribe = "魔法使い"
        self.name = "ブラック・マジシャン・ガール"
        self.level = 6

    def effect(self) :
        n_master = sum(["ブラック・マジシャン" in k for k in cemetary])
        self.atack += 300*n_master


class Tosshinn :
    def __init__(self) :
        self.card_type = "magic"

    def activate(self, target) :
        target.atack += 700


class DianKeto :

    def activate(self) :
        new_life = life + 1000
        return(new_life)

life = 4000
print(f"ライフポイント : {life}")
keto = DianKeto()
life = keto.activate()
print(f"ライフポイント : {life}")


class DianKeto :

    def activate(self) :
        life += 1000
        return(life)

life = 4000
print(f"ライフポイント : {life}")
keto = DianKeto()
life = keto.activate()
print(f"ライフポイント : {life}")


class DianKeto :

    def activate(self) :
        global life
        life += 1000
        return(life)

life = 4000
print(f"ライフポイント : {life}")
keto = DianKeto()
life = keto.activate()
print(f"ライフポイント : {life}")
```
cemetary = ["グレムリン", "ブラック・マジシャン"]
BMG = BlackMagicianGirl()
print(f"攻撃力 : {BMG.atack}")
BMG.effect()
print(f"攻撃力 : {BMG.atack}")
```

```
print(BlackMagicianGirl().atack)
```
gremlin = Gremlin()
print(f"カード名 : {gremlin.name}")
print(f"属性 : {gremlin.attribute}")
print(f"種族 : {gremlin.tribe}")
print(f"レベル : {gremlin.level}")


BMG = BlackMagicianGirl()
print(f"カード名 : {BMG.name}")
print(f"属性 : {BMG.attribute}")
print(f"種族 : {BMG.tribe}")
print(f"レベル : {BMG.level}")

BMG = BlackMagicianGirl()
print(f"攻撃力 : {BMG.atack}")
Tosshinn().activate(BMG)
print(f"攻撃力 : {BMG.atack}")
