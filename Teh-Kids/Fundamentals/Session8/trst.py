class Hero:
    def __init__(self,strength,fed,Hp):
        self.strength=strength
        self.fed=fed
        self.Hp=Hp
    def greet (self):
        print("Strength:",self.strength,"Def",self.fed,"HP:",self.Hp)

    def attack(self,other):
        hplost= self.strength-(other.fed/2)
        other.Hp=other.Hp-hplost
        print("HP after dmg:",other.Hp)

Stats=Hero(100,125,1000)
Stats.greet()
Yso=Hero(125,100,1200)
Yso.greet()
Stats.attack(Yso)