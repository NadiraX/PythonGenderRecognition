import os.path
from pathlib import Path
from subprocess import call


def listing(path = Path('train/') ):
    train = path
    pure_list = []
    for filename in os.listdir(train):
        pure_list.append(filename)
    return(pure_list)
def main():
    music = listing()
    for i in range(len(music)):
        call(['python3', 'inf136808.py', music[i]])

if __name__ == '__main__':
    main()