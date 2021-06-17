import secrets
import time
import msvcrt
from src.data.Color import Color
from colorama import Fore, Back, Style

full_attack_moves = [{"name": "Njord's Tempest", "dmg_prcnt": 60, "accur": 80, "stamina": 15}, {"name": "Tyr's Revenge", "dmg_prcnt": 80, "accur": 90, "stamina": 40},
                     {"name": "Breath Of Thamur", "dmg_prcnt": 100, "accur": 70,  "stamina": 35} , {"name": "Hel's Touch", "dmg_prcnt": 60, "accur": 70, "stamina": 20}, 
                     {"name": "Charge Of The White Bear", "dmg_prcnt": 80, "accur": 80, "stamina": 25}, {"name": "Axe Throw", "dmg_prcnt": 70, "accur": 70, "stamina": 15}]

full_item_list = [{"name": "HP Potion", "heal":"HP", "amount": 35, "qty": 1}, {"name": "Stamina Potion", "heal":"Stamina", "amount": 20, "qty": 1}, {"name": "Large HP Potion", "heal":"HP", "amount": 60, "qty": 1},
                  {"name": "Large Stamina Potion", "heal":"Stamina", "amount": 40, "qty": 1}, {"name": "Magic Elixir", "heal":"HP and Stamina", "amount": "maximum", "qty": 1}]


class Kratos:
    
    def __init__(self, hp, stamina, atk, defense, kills, items): #Initiates the Kratos class
        self.max_hp = hp
        self.hp = hp
        self.max_stamina = stamina
        self.stamina = stamina
        self.atk = atk
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.defense = defense
        self.items = items
        self.kills = 0
        self.level = 1
        self.actions = ["Attack", "Use", "Rest"]
        self.attacks = [{"name": "Slash", "dmg_prcnt": 60, "accur": 100, "stamina": 10}]
    
    def gen_dmg(self, attack_prcnt): # Calculates the damage the player does
        gen_dmg = secrets.choice(range(self.atkl, self.atkh))     #generating random dmg value between high and low
        gen_dmg = int(float(attack_prcnt/100) * float(gen_dmg))      #determing dmg by attack type
        return gen_dmg

    def take_dmg(self, attacker): # Calculates the damage the player takes
        rand_defence = float(self.defense) * (secrets.choice(range(70,100))/100)        # generating random defence by 70%-100% of defence stats
        dmg = attacker.gen_dmg() - int(rand_defence)       #using defense to lower dmg
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return dmg
    
    def reduce_stamina(self, cost): # Reduces the stamina whenever the player attacks
        self.stamina -= cost
    
    def raise_stamina(self, amount): # Increases stamina whenever the player uses a stamina regenerating item
        if (self.stamina + amount) > self.max_stamina:
            self.stamina = self.max_stamina
        else:
            self.stamina += amount

    def raise_hp(self, amount): # Functions that raises HP
        if (self.hp + amount) > self.max_hp:
            self.hp = self.max_hp
        else:
            self.hp += amount

    def won(self): # Function that raise the player's level every 3 wins and upgrades his stats
        self.kills += 1
        if not self.kills % 3:
            upgrade_list = ["max_hp", "max_stamina", "atk", "defense"]
            upgrade_stat = secrets.choice(upgrade_list)
            upgrade_amount = secrets.choice(range(0,10))
            self.level += 1
            print("Nice work - you just leveled up to level " + Color.BLUE + Color.BOLD + str(self.level) + Color.END + " and your ", end = '')
            if upgrade_stat == "max_hp":
                print("HP stat is getting " + Color.BLUE + Color.BOLD + str(upgrade_amount) + Color.END + " points upgrade !")
            if upgrade_stat == "max_stamina":
                print("Stamina stat is getting " + Color.BLUE + Color.BOLD + str(upgrade_amount) + Color.END + " points upgrade !")
            if upgrade_stat == "atk":
                print("Attack stat is getting " + Color.BLUE + Color.BOLD + str(upgrade_amount) + Color.END + " points upgrade !")
            if upgrade_stat == "defense":
                print("Defense stat is getting " + Color.BLUE + Color.BOLD + str(upgrade_amount) + Color.END + " points upgrade !")
            print("\n")
            curr_amount = getattr(self, upgrade_stat)
            setattr(self, upgrade_stat, curr_amount + upgrade_amount)
            self.atkl = self.atk - 10
            self.atkh = self.atk + 10

    def choose_action(self): # Function that allows the choosing of actions
        i = 0
        print(Color.BOLD + Color.UNDERLINE + "Actions" + Color.END)
        for action in self.actions:
            i += 1
            print(str(i) + ": " + action)
        print("Choose action:")
        action_input = "Null"
        while not action_input.isnumeric():
            action_input = chr(msvcrt.getch()[0])
        while not action_input.isnumeric() or int(action_input) > i or int(action_input) < 1:        #overflow and numeric check
            print(Color.RED + Color.UNDERLINE + "Please choose a valid number from the list above.\n" + Color.END)
            action_input = chr(msvcrt.getch()[0])
        return self.actions[int(action_input) - 1]    #returning name of the action
    
    def choose_attack(self): # Function that allows the choosing of attack type
        if self.stamina < 10:
            print(Color.RED + "Not enough Stamina to use any attacks, try to rest instead.\n" + Color.END)
            return -1
        print(Color.RED + """
              /| ________________
        O|===|* >________________>
              \|
        """ + Color.END)
        print(Color.BOLD + Color.UNDERLINE + "Attack Moves" + Color.END)
        i = 0
        for attack in self.attacks:
            i += 1
            print(str(i) + ": " + Color.BLUE + attack.get("name")+ Color.END + " | Damage Power: " + Color.RED +
                str(attack.get("dmg_prcnt")) + "%" + Color.END + " | Stamina Cost: " + Color.GREEN + str(attack.get("stamina")) +
                    Color.END + " | Chances to miss: " + Color.YELLOW + str(100 - attack.get("accur")) + "%\n" + Color.END)
        print("\nChoose attack: ")
        attack_input = chr(msvcrt.getch()[0])
        while not attack_input.isnumeric() or (int(attack_input) > i or int(attack_input) < 1) or (self.attacks[int(attack_input) - 1].get("stamina") > self.stamina):          #overflow and stamina check
            print(Color.RED + Color.UNDERLINE + "Invaild number entered or not enough Stamina available, please choose a different attack move.\n" + Color.END)
            attack_input = chr(msvcrt.getch()[0])
        attack_move = self.attacks[int(attack_input) -1]        #get dict element of attack
        return attack_move
        

    def choose_item(self): # Function that allows the choosing of items
        print("""\n        .--[[__]]---.
        ;-----------.|
        | Inventory ||
        |    Bag    ||
        |___________|/ 
         Your Items:""")
        i = 0
        if self.items:
            for item in self.items:
                i += 1
                print(str(i) + ": " +Color.BLUE + item.get("name") + Color.END + " - restore " + Color.BLUE +str(item.get("amount")) + Color.END + " " + str(item.get("heal")) + " (" +str(item.get("qty")) + " left) ")
            print("\nChoose item: ")
            item_input = chr(msvcrt.getch()[0])
            while not item_input.isnumeric() or int(item_input) > i or int(item_input) < 1:
                print(Color.RED + Color.UNDERLINE + "Please choose a valid number from the list above.\n" + Color.END)
                item_input = chr(msvcrt.getch()[0])
            return int(item_input) - 1
        else:
            print("You don't have any items to use yet, try to attack instead.\n")
            return -1
            
    def use_item(self, item_num): # Function that allows the items to be used 
        heal = self.items[item_num].get("heal")
        amount = self.items[item_num].get("amount")
        name = self.items[item_num].get("name")
        self.items[item_num]["qty"] -= 1
        if not self.items[item_num].get("qty"):     #if ran out of potion
            self.items.pop(item_num)
        print("\nUsing " + Color.BLUE + name + Color.END + " to recover " + Color.BLUE + str(amount) + Color.END+ " points of " + heal)
        print(Color.BLUE + """ 
              (-)      
            .-'-'-.    
            |-...-| 
            |;:.._|  
            `-...-'
        """ + Color.END)
        if heal == "HP":
            self.raise_hp(amount)
        elif heal == "Stamina":
            self.raise_stamina(amount)
        else:
            self.raise_hp(self.max_hp)
            self.raise_stamina(self.max_stamina)
    
    def add_rand_item(self): # Function that generates random items
        item_dict = secrets.choice(full_item_list)
        print(Color.BOLD +"\nWow ! You just found a " + Color.UNDERLINE + Color.BLUE+ item_dict.get("name") + Color.END + "\n")
        time.sleep(2)
        if item_dict in self.items:     #if item exists for player
            for item in self.items:
                if item.get("name") == item_dict.get("name"):
                    item["qty"] += 1
                    break
        else:
            self.items.append(item_dict)
    
    def add_rand_move(self): # Function that generates random moves
        move_dict = secrets.choice(full_attack_moves)
        move_name = move_dict.get("name")
        if move_dict in self.attacks:
            dmg_prcnt = move_dict.get("dmg_prcnt")
            print(Color.BOLD + "\nYou just upgraded your " + Color.BLUE + move_dict.get("name") + Color.END + Color.BOLD + " attack move, from " + str(dmg_prcnt) + "% damage to " +
                 Color.RED + Color.BOLD + str(dmg_prcnt + 5) + "%" + Color.END + "\n")
            time.sleep(2)
            for attack in self.attacks:
                if attack.get("name") == move_name:
                    attack["dmg_prcnt"] += 5
                    break
        else:
            print(Color.BOLD + "\nYou just learned a new move ! "+ Color.UNDERLINE + Color.BLUE + move_name + Color.END + "\n")
            self.attacks.append(move_dict)
            time.sleep(2)
