import secrets
import os
import time
import subprocess
import msvcrt
from src.Kratos import Kratos, full_attack_moves, full_item_list
from src.Mob import Mob, mob_warning_text, mob_fight_text, mob_dead_text
from src.Map import Map
from src.data.Color import Color

def set_game():    #saved file
    curr_dir = os.path.dirname(__file__)
    full_path = os.path.join(curr_dir, "src\\data\\save_file.txt")
    if False: #Need to add a saved game option
        print("Welcome back, here are your stats - ")
    else:
        new_game_text()
        return Kratos(100, 35, 50, 15, 0, [full_item_list[0], full_item_list[1]])
        

def new_game_text(): # Introduction text 
    print(Color.RED + Color.UNDERLINE + Color.BOLD + "\n              GOD OF WAR              " + Color.END + "\n")
    print("                                  "+ Color.CYAN + Color.BOLD + " O  " + Color.END)
    print(Color.UNDERLINE + Color.BOLD +"Welcome, this is your player -" + Color.END + "    " + Color.CYAN + Color.BOLD + "/|\\" + Color.END)
    print("                                  "+ Color.CYAN + Color.BOLD + "/ \\" + Color.END)
    print(Color.BOLD + "To move use the 'WASD' keys")
    print(Color.BOLD + "You can move freely on grass without encountering monsters, the grass looks like this - " + Color.GREEN + "/\\/\\" + Color.END)
    print(Color.BOLD + "When moving through shrubs you have a chance of getting into a fight, the shrubs looks like this - " + Color.DARK_GRAY + "|-|" + Color.END)
    print("To choose an action type in the chosen number\n" + Color.END)
    print(Color.UNDERLINE + Color.BOLD +"When encountering an enemy you will act in turns, in your turn you can choose to:"+ Color.END)
    print("1: " + Color.RED + "Attack" + Color.END + " the enemy - throughout the game you will achieve new attack moves.")
    print("2: " + Color.GREEN + "Use" + Color.END + " a potion to restore HP or Stamina - you can get Potions from killing enemies or finding them around the map.")
    print("3: " + Color.CYAN + "Rest" + Color.END + ", use this to restore 15 Stamina without potions - after each fight Stamina is fully restored.")
    print(Color.BOLD + "\n===============================================\n" + Color.END)
    print(Color.UNDERLINE + Color.BOLD +"Ready to begin? (Y/N) -" + Color.END)
    ready = chr(msvcrt.getch()[0])
    if ready == 'Y' or ready == 'y':
        print("Good luck. (you will need it)\n")
    else:
        print("Too late, good luck !\n")
    time.sleep(1.5)

def lottery_win(chance):        #function to randomly win attack moves and items
    rand_num = secrets.randbelow(101)
    if rand_num in range(0, chance):
        return True
    return False


def print_health(player, enemy): #Prints the health of both the player and the enemy
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
    
def move(map): Controls movement
    move_dict = {'W':-1 , 'A':-1, 'S':1, 'D':1, 'w':-1, 'a':-1, 's':1, 'd':1}
    move = chr(msvcrt.getch()[0])
    full_map = map.full_map
    x_cord = map.kratos_cord['X']
    y_cord = map.kratos_cord['Y']
    while move not in move_dict.keys():
        print(Color.RED + Color.BOLD + "Choose a valid movement please (WASD) - " + Color.END)
        move = chr(msvcrt.getch()[0])
    moving = move_dict[move]
    if move in ['W', 'w', 'S', 's']:
        if (y_cord + moving) not in range (2, map.max_y + 1):
            print(Color.RED + Color.BOLD + "Invaild movement, outside map boreders." + Color.END)
            return -1
        else:
            map.kratos_cord["Y"] += (moving*2)
            for i in range(0,3):
                if any(ch in "-|" for ch in (full_map[y_cord -2 + moving: y_cord + 1 + moving][i])[x_cord - 1: x_cord + 2]): 
                    return lottery_win(20)
            else:
                return False
    elif move in ['A', 'a', 'D', 'd']:
        if (x_cord + moving) not in range (1, map.max_x):
            print(Color.RED + Color.BOLD + "Invaild movement, outside map boreders." + Color.END)
            return -1
        else:
            map.kratos_cord["X"] += (moving*2)
            for i in range(0,3):
                if any(ch in "-|" for ch in (full_map[y_cord -2: y_cord + 1][i])[x_cord - 1 + moving: x_cord + 2 + moving]): 
                    return lottery_win(20)
            else:
                return False



subprocess.call(['tput', 'reset'])
player = set_game()
map = Map(70, 70, 35,70)
while player.hp:
    subprocess.call(['tput', 'reset'])
    map.print_map()
    encounter = -1
    while encounter == -1:
        encounter = move(map)
    print("\n")
    #move by map
    if encounter:        #if encountered a monster
        rand_mob_atk = int(float(player.atk) * (secrets.choice(range(70,115))/100))     #random mob dmg from (-30%) to (+15%) by player's atk
        rand_mob_hp = int(float(player.hp) * (secrets.choice(range(70,115))/100))     #random mob HP from (-30%) to (+15%) by player's HP
        rand_mob_def = int(float(player.defense) * (secrets.choice(range(70,115))/100))     #random mob defense from (-15%) to (+30%) by player's defense
        enemy = Mob(100, rand_mob_atk, rand_mob_def)
        print(Color.GREEN + secrets.choice(mob_warning_text) + Color.END + "It's a " + Color.BOLD + Color.RED + enemy.name + Color.END + secrets.choice(mob_fight_text) + "\n")
        turn_ctr = 0        #switching turns
        time.sleep(2.5)
        while player.hp > 0 and enemy.hp > 0:
            if not turn_ctr%2:      #player's turn
                subprocess.call(['tput', 'reset'])
                print(Color.BOLD + "\n===============================================\n" + Color.END)
                print_health(player, enemy)
                time.sleep(1.5)
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
            time.sleep(1.5)

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



        
