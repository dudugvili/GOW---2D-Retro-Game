import secrets
import src.data.Color

class Map:
    def __init__(self, max_x, max_y, kratos_x, kratos_y):
        object_type = ["rock", "grass", "grass", "grass"]
        full_map = []
        line_ctr = 0
        row_ctr = 0
        while line_ctr <= max_y:
            temp_row_list = []
            while row_ctr <= max_x:
                rand_cell = secrets.choice(object_type)
                if rand_cell == "rock" and line_ctr < (max_y - 2):
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
        self.full_map = full_map
        self.kratos_cord = {'X':kratos_x ,'Y':kratos_y}
        self.max_x = max_x
        self.max_y = max_y

    def print_cell(self, line_ctr, row_ctr):
        cell_print = self.full_map[line_ctr][row_ctr]
        if any(ch in "-|" for ch in cell_print):
            print(Color.DARK_GRAY , end = '')
        elif any(ch in "/\\" for ch in cell_print):
            print(Color.GREEN, end = '')
        print(self.full_map[line_ctr][row_ctr] , end = '')

    def print_map(self):
        y_axis = self.kratos_cord['Y']
        x_axis = self.kratos_cord['X']
        if(y_axis - 15 < 0):
            map_print_range = (0, 15)
        else:
            map_print_range = range(y_axis - 15, y_axis + 1)
        for line_ctr in map_print_range:
            for row_ctr in range(0,71):
                if line_ctr in range (y_axis - 2, y_axis + 1) and row_ctr in range(x_axis - 1, x_axis + 2):
                    if line_ctr == (y_axis - 2):
                        if row_ctr == x_axis:
                            print(Color.RED + Color.BOLD + "O" + Color.END, end='')
                        else:
                            self.print_cell(line_ctr, row_ctr)
                    #if above - prints head of player

                    elif line_ctr == (y_axis - 1):
                        if row_ctr == (x_axis - 1):
                            print(Color.RED + Color.BOLD + "/" + Color.END, end='')
                        if row_ctr == x_axis:
                            print(Color.RED + Color.BOLD + "|" + Color.END, end='')
                        if row_ctr == (x_axis + 1):
                            print(Color.RED + Color.BOLD + "\\" + Color.END, end='')
                    #if above - prints arms of player

                    elif line_ctr == (y_axis):
                        if row_ctr == (x_axis - 1):
                            print(Color.RED + Color.BOLD + "/" + Color.END, end='')
                        if row_ctr == x_axis:
                            print(" ", end='')
                        if row_ctr == (x_axis + 1):
                            print(Color.RED + Color.BOLD + "\\" + Color.END, end='')
                    #if above - prints legs of player

                else:
                    self.print_cell(line_ctr, row_ctr)

            print('')
