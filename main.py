import os,sys
import platform,subprocess
def init():
    path = []
    d = ''
    path_a = open('./config','r')
    for i in path_a:
        for c in i:
            if c == "|" or c == "\n" or c == '\r' or c == '':
                path.append(d)
                d = ''
            else:
                d = d + c
    return path
def move(path,destination):
    if platform.system() == 'windows':
        for i in path:
            subprocess.Popen("move "+i+' '+destination, shell=True)
    elif platform.system() == 'Linux':
        for i in path:
            subprocess.Popen("mv "+i+' '+destination, shell=True)