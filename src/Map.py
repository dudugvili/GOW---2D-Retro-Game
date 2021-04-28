import secrets
#import data.Color
class Color:
    HEADER = '\033[95m'
    GREEN = '\033[92m'
    BROWN = "\033[0;33m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    BLUE = '\033[94m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    PURPLE = '\033[95m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    CROSSED = "\033[9m"
    UNDERLINE = '\033[4m'
    END = '\033[0m'


 
    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

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
        for line_ctr in range(y_axis - 15, y_axis + 1):
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