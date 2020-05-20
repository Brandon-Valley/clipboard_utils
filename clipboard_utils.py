# from tkinter import Tk
from ctypes import windll
from pyperclip import copy
from pyperclip import paste


if __name__ == "__main__": 
#     from   usms.exception_utils import exception_utils as eu 
    pass
else:
#     from . usms.exception_utils import exception_utils as eu
    pass



def get_clipboard():
#     return(Tk().clipboard_get())
    return(paste())

def set_clipboard(i):
    copy(i)

def clear_clipboard():
    if windll.user32.OpenClipboard(None):
        windll.user32.EmptyClipboard()
        windll.user32.CloseClipboard()



if __name__ == '__main__':
    print('In Main:  clipboard_utils')
#     a = read_from_clipboard_input()
    print(get_clipboard())


















    print('End of Main:  clipboard_utils')        