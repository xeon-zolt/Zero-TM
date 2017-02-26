import os
def get_DE():
    return os.environ.get('DESKTOP_SESSION')
# record reading on different Desktop Enviourments
# for cinnamon its --> 'cinnamon'
# for gnome its --> 'gnome'
# or improve a method in future
