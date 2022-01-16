#Colors within terminal:
class tcolor: #Estilos y Colores de Terminal - Different Terminal Colors and Displays
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    GREEN = '\033[92m'
    RED = '\033[31m'
    PURPLE = '\033[35m'
    ORANGE = '\033[33m'
    GREY = '\033[37m'
    DARKER = '\033\38m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    HIGHLIGHT = '\033[40m'
    REDHIGHLIGHT = '\033[41m'
    GREENHIGHLIGHT = '\033[42m'
    YELLOWHIGHLIGHT = '\033[43m'
    BLUEHIGHLIGHT = '\033[44m'
    PURPLEHIGHLIGHT = '\033[45m'
    CYANHIGHLIGHT = '\033[46m'
    REVERSE = '\033[7m'
    CROSSED = '\033[9m'
    SHADOWED = '\033[30m'

def coloredPrint(output, color): #Imprimir a color sin caer en la verborrea - Verboseless colored printing
    print(color+output+tcolor.ENDC)

