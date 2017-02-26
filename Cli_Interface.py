from Detect_De import * # to detect Desktop Enviourment
from get_themes import *

def download_theme(i):
    tag = tags_list[i-1]
    cmd = 'git clone -b \''+str(tag)+'\' --single-branch \'https://github.com/xeon-zolt/ZeroThemes.git\' '+str(cinnamon_themes[i-1])
    os.system(cmd)
if get_DE() == 'cinnamon':
    get_cinnamon_themes()
    for i in range(len(cinnamon_themes)):
        print (str(i+1) +' : ' + cinnamon_themes[i])
else:
    print ('Your DE is Not Supported')
    exit()
theme_number = int(input('To Apply Theme enter the Theme Number like 1 or 2 etc\n   '))
download_theme(theme_number)
# add error handling here
