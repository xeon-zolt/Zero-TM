import os
from Detect_De import * # to detect Desktop Enviourment

theme_list = [] # empty list contaning online themes
cinnamon_themes = [] # empty list to store cinnamon themes later
cmd = 'git ls-remote --tags --quiet https://github.com/xeon-zolt/ZeroThemes.git'
themes = os.popen(cmd).read().strip().splitlines()
def count_themes():
    count_themes = 0
    for i in themes:
        count_themes = count_themes + 1
    return count_themes
def get_theme():
    number_of_themes = count_themes()
    for i in range(number_of_themes):
        theme = (str(themes).split('/tags/')[i+1].split('\'')[0])
        if theme != 'master':
            theme_list.extend([theme])
    return (theme_list)
def sort_themes_by_de():
    for i in range(count_themes()):
        if get_DE()=='cinnamon':
            if '-cinnamon' in get_theme()[i]: # it can be with De too but this prevent naming theme starting with de name
                cinnamon_themes.extend([get_theme()[i].split('-cinnamon')[0]])
