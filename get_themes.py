import os
theme_list = []
cmd = 'git ls-remote --heads https://github.com/xeon-zolt/ZeroThemes.git'
themes = os.popen(cmd).read().strip().splitlines()
def count_themes():
    count_themes = 0
    for i in themes:
        count_themes = count_themes + 1
    return count_themes
def get_theme():
    number_of_themes = count_themes()
    for i in range(number_of_themes):
        theme = (str(themes).split('/heads/')[i+1].split('\'')[0])
        if theme != 'master':
            theme_list.extend([theme])
    return (theme_list)
