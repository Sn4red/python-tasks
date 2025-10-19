from colorama import init, Fore, Back, Style
from datetime import datetime

# Automates resets for color changes.
init(autoreset = True)

TYPE_COLORS = {
    'INFO': Fore.GREEN,
    'DONE': Fore.GREEN,
    'CONFIRMATION': Fore.GREEN,
    'WARNING': Fore.YELLOW,
    'ERROR': Fore.RED,
}

def log(level, message):
    color = TYPE_COLORS.get(level)
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    print(
        f'{Fore.CYAN}{timestamp}{Style.RESET_ALL} '
        f'[{color}{level}{Style.RESET_ALL}] {message}'
    )

