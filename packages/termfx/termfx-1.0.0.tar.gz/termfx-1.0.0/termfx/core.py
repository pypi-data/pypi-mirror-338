#!/usr/bin/env python3
from colorama import Fore, init
import sys
import shutil
import json
import time
import getpass

init(autoreset=True)
sys.stdout.reconfigure(encoding='utf-8')


# ======= Centered Output =======

def printCentered(text, mode="banner"):
    """
    Prints text centered in terminal.
    Mode: 'banner' = no prefix, 'line' = with [>] prefix
    """
    width = shutil.get_terminal_size().columns
    lines = text.split('\n')
    for line in lines:
        centered = line.center(width)
        if mode == "line":
            print(Fore.LIGHTCYAN_EX + "[>] " + centered)
        else:
            print(Fore.LIGHTCYAN_EX + centered)


# ======= Centered Input =======

def inputCentered(text, mode="banner"):
    """
    Gets centered input from user.
    Mode: 'banner' = no prefix, 'line' = with [>] prefix
    """
    width = shutil.get_terminal_size().columns
    lines = text.split('\n')
    prompt = ""
    for line in lines:
        if mode == "line":
            prompt += ("[>] " + line).center(width) + '\n'
        else:
            prompt += line.center(width) + '\n'
    return input(Fore.LIGHTCYAN_EX + prompt.strip() + " ")


# ======= Shortcut Print Functions =======

def printInfo(text):
    print(Fore.LIGHTCYAN_EX + "[>] " + str(text))

def printSuccess(text):
    print(Fore.LIGHTGREEN_EX + "[+] " + str(text))

def printError(text):
    print(Fore.LIGHTRED_EX + "[!] " + str(text))

def printWarning(text):
    print(Fore.LIGHTYELLOW_EX + "[-] " + str(text))

def printBanner(text):
    print(Fore.LIGHTCYAN_EX + str(text))


# ======= Shortcut Input Functions =======

def inputInfo(text):
    return input(Fore.LIGHTCYAN_EX + "[>] " + str(text))

def inputSuccess(text):
    return input(Fore.LIGHTGREEN_EX + "[+] " + str(text))

def inputError(text):
    return input(Fore.LIGHTRED_EX + "[!] " + str(text))

def inputWarning(text):
    return input(Fore.LIGHTYELLOW_EX + "[-] " + str(text))


# ======= Utility Functions =======

def printDivider(char="-", length=50):
    """
    Print a horizontal divider.
    """
    print(Fore.LIGHTBLACK_EX + char * length)

def askYesNo(question):
    """
    Ask a yes/no question and return True/False
    """
    while True:
        answer = input(Fore.LIGHTCYAN_EX + f"[?] {question} (y/n): ").strip().lower()
        if answer in ["y", "yes"]:
            return True
        elif answer in ["n", "no"]:
            return False

def inputHidden(prompt):
    """
    Hidden input (e.g. password)
    """
    return getpass.getpass(Fore.LIGHTCYAN_EX + "[*] " + prompt + ": ")

def printJsonPretty(obj):
    """
    Print JSON nicely formatted
    """
    print(Fore.LIGHTWHITE_EX + json.dumps(obj, indent=4, ensure_ascii=False))

def printTable(headers, rows):
    """
    Print a basic table with headers and rows.
    """
    col_widths = [max(len(str(x)) for x in col) for col in zip(*([headers] + rows))]
    header_row = " | ".join(str(val).ljust(col_widths[i]) for i, val in enumerate(headers))
    separator = "-+-".join('-' * w for w in col_widths)
    print(Fore.LIGHTBLUE_EX + header_row)
    print(Fore.LIGHTBLUE_EX + separator)
    for row in rows:
        print(" | ".join(str(val).ljust(col_widths[i]) for i, val in enumerate(row)))


def progressBar(iteration, total, prefix='', suffix='', length=40, fill='█'):
    """
    Print a progress bar in terminal.
    """
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{Fore.LIGHTMAGENTA_EX}{prefix} |{bar}| {percent}% {suffix}', end='\r')
    if iteration == total:
        print()
