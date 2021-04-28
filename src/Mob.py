class Mob:
    def __init__(self, hp, , atk, defense):
        self.max_hp = hp
        self.hp = hp
        self.max_stamina = stamina
        self.stamina = stamina
        self.atk = atk
        self.defense = defense
        self.items = items

    def being_attacked(self, attacker):
        self.hp -= attacker.atk
        if self.hp <= 100:
            self.defeated();
            return 1
        return 0

    def defeated(self):
        self.hp = nax_hp
        


        
    