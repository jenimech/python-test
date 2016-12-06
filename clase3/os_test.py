from os import walk

for root, folders, files in walk('.'):
    for file in files:
        print(file)

#os.path.isfile('os_test.py') 
#os.path.isfolder('clase3')
#os.path.isdir('clase3')