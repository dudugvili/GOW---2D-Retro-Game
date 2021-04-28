import secrets
from data.Color import Color
#class Map:

#full map


object_type = ["rock", "grass", "grass"]
full_map = []
line_ctr = 0
row_ctr = 0
while line_ctr < 40:
    temp_row_list = []
    while row_ctr < 60:
        rand_cell = secrets.choice(object_type)
        if rand_cell == "rock":
            temp_row_list.append('|')
            temp_row_list.append('¯')
            temp_row_list.append('|')
            row_ctr += 3
        elif rand_cell == "grass":
            temp_row_list.append('/')
            temp_row_list.append('\\')
            row_ctr += 2 
    full_map.append(temp_row_list)
    row_ctr = 0
    line_ctr += 1

line_ctr = 0
row_ctr = 0
while line_ctr < 40:
    while row_ctr < 60:
        cell_print = full_map[line_ctr][row_ctr]
        if any(ch in "-|" for ch in cell_print):
            print(Color.DARK_GRAY + Color.BOLD, end = '')
        elif any(ch in "/\\" for ch in cell_print):
            print(Color.GREEN, end = '')
        elif any(ch in "/\\" for ch in cell_print):
            print(Color.BROWN, end = '')
        print(full_map[line_ctr][row_ctr] , end = '')
        row_ctr += 1
    row_ctr = 0
    line_ctr += 1
    print('\n')
        
                

    #mini map