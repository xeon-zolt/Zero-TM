import os
from Detect_De import * # to detect Desktop Enviourment

all_theme_list = [] # empty list contaning online themes
cinnamon_themes = [] # empty list to store cinnamon themes later
tags_list = [] # store tags according to DE
all_theme_get_cmd = 'git ls-remote --tags --quiet https://github.com/xeon-zolt/ZeroThemes.git'
cinnamon_theme_get_cmd = 'git ls-remote --tags --quiet https://github.com/xeon-zolt/ZeroThemes.git \\*cinnamon '

# all_themes = os.popen(theme_get_cmd).read().strip().splitlines()

def get_cinnamon_themes():
    cinnamon_themes_raw_list = os.popen(cinnamon_theme_get_cmd).read().strip().splitlines()
    for i in range(len(cinnamon_themes_raw_list)):
        cinnamon_themes.extend([str(cinnamon_themes_raw_list[i]).split('/')[2].split('-cinnamon')[0]])
        tags_list.extend([str(cinnamon_themes_raw_list[i]).split('/')[2]])
