import os
def apply(a):
    change_dir_cmd = 'cd '+ a + '&& ls Wallpaper'
    wallpaper = os.popen(change_dir_cmd)
    current_Dir = os.popen('pwd') 
#Go into theme after downlading
    wallpaper_cmd = 'gsettings set org.cinnamon.desktop.background picture-uri  "file:///Wallpaper/'+str(wallpaper)+'"'
# cinnamon wallpaper
    os.system(wallpaper_cmd)
apply('Monochrome')
