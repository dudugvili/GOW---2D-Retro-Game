import secrets
import os
import time
from src.Kratos import Kratos, full_attack_moves, full_item_list
from src.Mob import Mob, mob_warning_text, mob_fight_text, mob_dead_text
from src.data.Color import Color

def set_game():    #saved file
    curr_dir = os.path.dirname(__file__)
    full_path = os.path.join(curr_dir, "src\\data\\save_file.txt")
    if False: #Need to add a saved game optionwyt
        print("Welcome back, here are your stats - ")
    else:
        new_game_text()
        return Kratos(100, 35, 35, 15, 0, [full_item_list[0], full_item_list[1]])
        

def new_game_text():
    print(Color.RED + Color.UNDERLINE + Color.BOLD + "\n              GOD OF WAR              " + Color.END + "\n")
    print("                                  "+ Color.CYAN + Color.BOLD + " O  " + Color.END)
    print(Color.UNDERLINE + Color.BOLD +"Welcome, this is your player -" + Color.END + "    " + Color.CYAN + Color.BOLD + "/|\\" + Color.END)
    print("                                  "+ Color.CYAN + Color.BOLD + "/ \\" + Color.END)
    print(Color.BOLD + "To move use the 'WASD' keys")
    print("To choose an action type in the chosen number\n" + Color.END)
    print(Color.UNDERLINE + Color.BOLD +"When encountering an enemy you will act in turns, in your turn you can choose to:"+ Color.END)
    print("1: " + Color.RED + "Attack" + Color.END + " the enemy - throughout the game you will achieve new attack moves.")
    print("2: " + Color.GREEN + "Use" + Color.END + " a potion to restore HP or Stamina - you can get Potions from killing enemies or finding them around the map.")
    print("3: " + Color.CYAN + "Rest" + Color.END + ", use this to restore 15 Stamina without potions - after each fight Stamina is fully restored.")
    print(Color.BOLD + "\n===============================================\n" + Color.END)
    ready = input(Color.UNDERLINE + Color.BOLD +"Ready to begin? (Y/N) -" + Color.END)
    if ready == 'Y' or ready == 'y':
        print("Good luck. (you will need it)\n")
    else:
        print("Too late, good luck !\n")

def lottery_win(chance):        #function to randomly win attack moves and items
    rand_num = secrets.randbelow(101)
    if rand_num in range(0, chance):
        return True
    return False


def print_health(player, enemy):
    #HP print
    if int(player.hp/100):
        print("                        _________________________")
    elif int(player.hp/10):
        print("                        _________________________")
    else:
        print("                        _________________________")
    bar_blocks = ""
    blank_blocks = ""
    player_bar_blocks = (player.hp/player.max_hp) * 100 / 4
    for i in range(0,int(player_bar_blocks)):
        bar_blocks += "█"
    for j in range(0, 25-int(player_bar_blocks)):
        blank_blocks += " "
    print("HP: " + Color.GREEN + str(player.hp) + "/" + str(player.max_hp) + Color.END, end = '')
    if player.hp < 10:
        print("              |" + Color.GREEN + bar_blocks + Color.END + blank_blocks + "|")
    elif player.hp < 100:
        print("             |" + Color.GREEN + bar_blocks + Color.END + blank_blocks + "|")
    else:
        print("            |" + Color.GREEN + bar_blocks + Color.END + blank_blocks + "|")

    #Stamina print
    if int(player.stamina/100):
        print("                        _________________________")
    elif int(player.stamina/10):
        print("                        _________________________")
    else:
        print("                        _________________________")
    bar_blocks = ""
    blank_blocks = ""
    player_bar_blocks = (player.stamina/player.max_stamina) * 100 / 4
    for i in range(0,int(player_bar_blocks)):
        bar_blocks += "█"
    for j in range(0, 25-int(player_bar_blocks)):
        blank_blocks += " "
    print("Stamina: " + Color.YELLOW + str(player.stamina) + "/" + str(player.max_stamina) + Color.END, end = '')
    if player.stamina > 9:
        print("         |" + Color.YELLOW + bar_blocks + Color.END + blank_blocks + "|\n")
    else:
        print("          |" + Color.YELLOW + bar_blocks + Color.END + blank_blocks + "|\n")
    
    #Stats print
    print("attack range: " + Color.BLUE + Color.BOLD + str(player.atkl) + "~" +str(player.atkh) + Color.END +
          " defense: " + Color.BLUE + Color.BOLD + str(player.defense) + Color.END )
    print("______________________________________________")

    #Enemy's HP print
    if int(enemy.hp/100):
        print("                        _________________________")
    elif int(enemy.hp/10):
        print("                       _________________________")
    else:
        print("                      _________________________")
    bar_blocks = ""
    blank_blocks = ""
    player_bar_blocks = (enemy.hp/enemy.max_hp) * 100 / 4
    for i in range(0,int(player_bar_blocks)):
        bar_blocks += "█"
    for j in range(0, 25-int(player_bar_blocks)):
        blank_blocks += " "
    print("Enemy's HP: " + Color.RED + str(enemy.hp) + "/" + str(enemy.max_hp) + Color.END, end = '')
    if enemy.max_hp < 10:
        print("     |" + Color.RED + bar_blocks + Color.END + blank_blocks + "|")
    else:
        print("    |" + Color.RED + bar_blocks + Color.END + blank_blocks + "|")
    



player = set_game()
while player.hp:
    move = input("Choose movement (WASD) - ")
    print("\n")
    #move by map
    if True:        #if encountered a monster
        rand_mob_atk = int(float(player.atk) * (secrets.choice(range(70,130))/100))     #random mob dmg from (-30%) to (+30%) by player's atk
        rand_mob_hp = int(float(player.hp) * (secrets.choice(range(70,130))/100))     #random mob HP from (-30%) to (+30%) by player's HP
        rand_mob_def = int(float(player.defense) * (secrets.choice(range(70,130))/100))     #random mob defense from (-30%) to (+30%) by player's defense
        enemy = Mob(100, rand_mob_atk, rand_mob_def)
        print(Color.GREEN + secrets.choice(mob_warning_text) + Color.END + "It's a " + Color.BOLD + Color.RED + enemy.name + Color.END + secrets.choice(mob_fight_text) + "\n")
        turn_ctr = 0        #switching turns
        time.sleep(1.5)
        while player.hp > 0 and enemy.hp > 0:
            if not turn_ctr%2:      #player's turn
                print(Color.BOLD + "\n===============================================\n" + Color.END)
                print_health(player, enemy)
                time.sleep(2)
                print(Color.BLUE + Color.BOLD + "\n                 -YOUR TURN-                     " + Color.END)
                player_action = player.choose_action()
                #using potions
                if player_action == "Use":
                    player_item_num = player.choose_item()       #get an index of the item
                    if player_item_num == -1:       #if no items available move on to an attack
                        player_action = "Attack"
                    else:
                        player.use_item(player_item_num)
                        
                #attacking
                if player_action == "Attack":
                    player_atk_dict = player.choose_attack()        #get a dict of the attack move
                    if player_atk_dict == -1:        #if no stamina available to attack
                        player_action = "Rest"
                    else:   
                        player_dmg = enemy.take_dmg(player, player_atk_dict)
                        player.reduce_stamina(player_atk_dict.get("stamina"))
                        if player_dmg == -1:
                            print("You missed !\n")
                        else:
                            print(Color.BOLD + "\nsuccessfuly attacked with " + Color.BLUE + player_atk_dict.get("name") + Color.END + " and caused " + 
                                  Color.BLUE + Color.BOLD + str(player_dmg) + " damage !" + Color.END + "\n")

                #rest
                if player_action == "Rest": 
                    print(Color.BLUE + "Resting ZzzzZ - (+15 Stamina)" + Color.END)
                    player.raise_stamina(15)
            else:       #enemy's turn
                print(Color.BOLD + "\n===============================================\n" + Color.END)
                print(Color.RED + Color.BOLD + "                 -ENEMY'S TURN-                     " + Color.END)
                enemy_dmg = player.take_dmg(enemy)
                print("            " + Color.RED + enemy.name + Color.END + " ATTACKS ! " + Color.RED + Color.BOLD + "-" + str(enemy_dmg) + " HP" + Color.END+ "\n")

            turn_ctr += 1
            time.sleep(2)

        if enemy.hp <= 0:
            print(Color.BLUE + Color.BOLD + Color.UNDERLINE + "You've defeated " + enemy.name + secrets.choice(mob_dead_text) + Color.END + "\n")
            if lottery_win(30):             #30% chance to win a new attack move/potion after winning
                player.add_rand_move()      #adds a random attack move
            if lottery_win(30):
                player.add_rand_item()      #adds a random potion
            player.won()
            player.raise_stamina(player.max_stamina)
            player.raise_hp(player.max_hp)
            
        else:
            print(Color.RED + Color.BOLD + Color.UNDERLINE + "---------------------YOU'VE DIED---------------------" + Color.END)
            print(Color.RED + Color.BOLD + Color.UNDERLINE + "----------------------GAME OVER----------------------" + Color.END)



        
