import os
from pathlib import Path
paths = sorted(Path('./').iterdir(), key=os.path.getmtime)

output = ''
counter = 0
for f_name in paths:
    if counter == (len(paths) - 1):
        print(f_name)
    else:
        print(f_name, ',')
        counter += 1

