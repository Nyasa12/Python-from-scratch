'''with open("wipe.txt", "r") as f :
    data = f.read()

wipe.txt renamed_by_python.txt                       
'''

import os

old_name ="wipe.txt"
new_name ="renamed_by_python.txt"

os.rename(old_name, new_name)
