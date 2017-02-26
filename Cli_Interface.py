from Detect_De import * # to detect Desktop Enviourment
from get_themes import *
from apply_cinnamon import *
def download_theme(i):
    tag = tags_list[i-1]
    cmd = 'git clone -b \''+str(tag)+'\' --single-branch \'https://github.com/xeon-zolt/ZeroThemes.git\' '+str(cinnamon_themes[i-1])
    os.system(cmd)
    return cinnamon_themes[i-1] # here cause it will be returned if its downloaded

if get_DE() == 'cinnamon':
    get_cinnamon_themes()
    for i in range(len(cinnamon_themes)):
        print (str(i+1) +' : ' + cinnamon_themes[i])
    theme_number = int(input('To Apply Theme enter the Theme Number like 1 or 2 etc\n   '))
    apply(download_theme(theme_number))
else:
    print ('Your DE is Not Supported')
    exit()

# add error handling here
