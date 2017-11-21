import os

for file in os.listdir('.'):
    if file.__len__() <= 3 or file.__len__() < 6:
        print file
