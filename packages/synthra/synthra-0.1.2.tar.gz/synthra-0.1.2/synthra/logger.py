import colorama, os
from colorama import Fore, Style
from datetime import datetime
from threading import Lock
import sys

colorama.init()

class Logger:
    l = Lock()

    @staticmethod
    def timestamp() -> str:
        """Get the current timestamp."""
        return datetime.now().strftime("%H:%M:%S")

    @staticmethod
    def log(tag: str, content: str):
        """General log function."""
        color = Logger.get_color(tag)
        time_stamp = Logger.timestamp()
        tag_formatted = f"{tag:<5}"
        
        with Logger.l:
            print(f"{Style.BRIGHT}{Fore.BLACK}{time_stamp} {Fore.WHITE}| {color}{tag_formatted} {Fore.WHITE}| {Fore.BLACK}{content}")

    @staticmethod
    def get_color(tag: str) -> str:
        """Determine the color based on the log tag."""
        if tag.lower().startswith('s'):
            return Fore.GREEN
        elif tag.lower().startswith('e') or tag.lower().startswith('f'):
            return Fore.RED
        elif tag.lower().startswith('w'):
            return Fore.YELLOW
        elif tag.lower().startswith('d') or tag.lower().startswith('i'):
            return Fore.BLUE if tag.lower().startswith('d') else Fore.CYAN
        else:
            return Fore.MAGENTA

    @staticmethod
    def info(content: str):
        """Log an info level message."""
        Logger.log("Info", content)

    @staticmethod
    def debug(content: str):
        """Log a debug level message."""
        Logger.log("Debug", content)

    @staticmethod
    def fail(content: str):
        """Log a fail/error level message."""
        Logger.log("Fail", content)

    @staticmethod
    def warn(content: str):
        """Log a warning level message."""
        Logger.log("Warn", content)

    @staticmethod
    def success(content: str):
        """Log a success level message."""
        Logger.log("Suc", content)
    
    @staticmethod
    def clear():
        """Clear the console."""
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def input(content: str):
        """Capture user input with a timestamp."""
        input_color = Fore.BLUE
        success_color = Fore.GREEN
        time_stamp = Logger.timestamp()
        input_tag_formatted = "Input"

        with Logger.l:
            sys.stdout.write(f"{Style.BRIGHT}{Fore.BLACK}{time_stamp} {Fore.WHITE}| {input_color}{input_tag_formatted} {Fore.WHITE}| {Fore.BLACK}{content} {Fore.BLUE}")
            sys.stdout.flush()
            user_input = input()
            sys.stdout.write("\033[F\033[K")
            success_tag_formatted = "Suc  "
            print(f"{Style.BRIGHT}{Fore.BLACK}{Logger.timestamp()} {Fore.WHITE}| {success_color}{success_tag_formatted} {Fore.WHITE}| {Fore.BLACK}{user_input}")
        
        return user_input

