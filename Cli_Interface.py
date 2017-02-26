from Detect_De import * # to detect Desktop Enviourment
from get_themes import *

for i in range(len(sort_themes_by_de())):
    print (str(i+1)+' : '+sort_themes_by_de()[i])
theme_number = int(input('To Apply Theme enter the Theme Number like 1 or 2 etc'))
apply(theme_number)
# add error handling here
