#USAGE:
# from varian_utils.mystyle import mystyle, styles_overview
#
# print(f"Testing {mystyle.bright}bright{mystyle.done} text output"")

from colorama import init, Fore, Style
class mystyle:
    good = Fore.GREEN + Style.BRIGHT
    bad = Fore.RED + Style.BRIGHT
    bright = Fore.YELLOW + Style.BRIGHT
    green = Fore.GREEN
    done = Style.RESET_ALL
    init(autoreset=True)

def styles_overview():
    print(f"{mystyle.good}good{mystyle.done}\n"
            f"{mystyle.bad}bad{mystyle.done}\n"
            
            f"{mystyle.bright}bright{mystyle.done}\n"
            #f"{mystyle.white}white{mystyle.done}\n"
            f"{mystyle.green}green{mystyle.done}\n")