import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

from func_get_symbols import get_tradeable_symbols
import pandas as pd

"""STRATEGY CODE"""
if __name__ == '__main__':

    # STEP 1 - Get list of symbols
    sym_response = get_tradeable_symbols()

# # This is a sample Python script.
#
# # Press ⌃R to execute it or replace it with your code.
# # Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm 5')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
