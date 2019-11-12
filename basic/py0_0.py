import os
import multiprocessing
from time import sleep

def subp():
    for i in range(5):
        print('subp\t', os.getpgid())
        sleep()

if __name__ == '__main__':
    pass
