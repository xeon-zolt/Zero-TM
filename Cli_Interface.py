from Detect_De import *
from get_themes import *

def themes_avaliable():
    number_of_themes = count_themes()
    for i in range(number_of_themes - 1): # because count is reduced cause of removing master check get_theme.py
        print (str(i+1)+' : ' + get_theme()[i])

def apply_theme():
    get_selection = int(input('enter the theme number coresponding to theme to apply\n like 1 or 2\n'))
    # write a if to exit and a else for everything below
    selected_theme = get_theme()[get_selection-1]
    print(selected_theme)
if get_DE()=='cinnamon':
    themes_avaliable()
    apply_theme()
else:
    print ('Your Desktop Enviourment is not supported')
