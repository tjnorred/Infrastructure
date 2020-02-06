from pathlib import Path
import os

folder_name = 'chapter'
folder_count = 10
dir = Path('/path/to/file/')

for i in range(1, folder_count + 1):
    new_folder = folder_name + str(i)
    try:
        os.mkdir(os.path.join(dir, new_folder))
        print('Creating directory {}'.format(new_folder))
    except:
        print("Directory {} already exists".format(new_folder))
