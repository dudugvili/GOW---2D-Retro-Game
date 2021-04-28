import secrets
class Kratos:
    
    def __init__(self, hp, "stamina", atk, defense, *items):
        self.max_hp = hp
        self.hp = hp
        self.max_"stamina" = "stamina"
        self."stamina" = "stamina"
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.defense = defense
        self.items = items
        self.actions = ["Attack", "Use"]
        self.attacks = [{"name": "Slash", "dmg_prcnt": 50, "accur": 100, "stamina": 10}]
    
    def gen_dmg(self):
        rand_prcnt = secrets.randbelow(100)
        gen_dmg = int(float(rand_prcnt)/100 * (self.atkh - self.atkl))+(self.atkl)     #generating random dmg value between high and low
        return gen_dmg

    def take_dmg(self, attacker):
        self.hp -= attacker.gendmg()
        if self.hp <= 100:
            self.defeated();
    
    def reduce_stamina(self, cost):
        self.stamina -= cost
    
    def raise_stamina(self, amount):
        self.stamina += amount

    def choose_action(self):
        for action in self.actions:
            print(str(action) + "action" + action)


    def defeated(self):
        print("game over")

full_attack_moves = [{"name": "Njord's Tempest", "dmg_prcnt": 60, "accur": 80, "stamina": 15}, {"name": "Tyr's Revenge", "dmg_prcnt": 80, "accur": 90, "stamina": 40},
                     {"name": "Breath Of Thamur", "dmg_prcnt": 100, "accur": 70,  "stamina": 35} , {"name": "Hel's Touch", "dmg_prcnt": 60, "accur": 70, "stamina": 20}, 
                     {"name": "Charge Of The White Bear", "dmg_prcnt": 80, "accur": 80, "stamina": 25}, {"name": "Axe Throw", "dmg_prcnt": 70, "accur": 70, "stamina": 15}]