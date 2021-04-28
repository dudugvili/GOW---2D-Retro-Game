import secrets


mob_names = ["Troll", "Dragon", "Fierce Ogre", "Cyclop", "Scylla", "Hydra", "Hei-Walker", "Draugr"]
class Mob:
    def __init__(self, hp, atk, defense):
        self.name = secrets.choice(mob_names)
        self.max_hp = hp
        self.hp = hp
        self.atk = atk
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.defense = defense

    def take_dmg(self, attacker, atk_move):
        rand_num = secrets.randbelow(101)
        if rand_num in range(0, atk_move.get("accur") + 1):     #if random number generated is inside the accuracy range of the attack
            player_dmg = attacker.gen_dmg(atk_move.get("dmg_prcnt"))      #generate dmg by attack move damage percent and accuracy
            self.hp -= player_dmg
            return player_dmg
        else:
            return -1



    def gen_dmg(self):
        rand_prcnt = secrets.randbelow(100)
        gen_dmg = int(float(rand_prcnt)/100 * (self.atkh - self.atkl))+(self.atkl)     #generating random dmg value between high and low
        return gen_dmg


mob_warning_text = ["Look out! ", "Over there! ", "OH NO, ", "Looks like ", "Be careful! "]
mob_fight_text = [", show it what you got!", ", have no mercy.", ", take it out!", ", defeat it!", ", dont let it stand in your way."]
mob_dead_text = [", well done !", ", good job.", ", nice work.", ", to the next challange !", ", it was a remarkable fight."]


        
    