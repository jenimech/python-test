import os

def list_files(path):
    for root, dirs, files in os.walk(path):
        level = root.replace(path, '').count(os.sep)
        # print(level)
        ind   = ' ' * 4 * (level)
        foldername = os.path.basename(root)
        print('{}{}'.format(ind, foldername))
        print('{}{}'.format(ind, '|___'))
        subind = ' ' * 4 * (level + 1)
        for f in files:
             print('{}|{}'.format(subind, f))

list_files('../')