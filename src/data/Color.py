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

 
    def disable(self): # Function that disables color
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''
