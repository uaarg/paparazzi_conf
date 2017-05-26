#!/usr/bin/env python
import subprocess
from shutil import copytree, copy

PPRZ_VERSION = "v5.11_devel-none-gd8285ad"

def install_custom_modifications():
    f = open("pprz_files/filelist", 'r')
    for l in f:
        l = l.split(" ")
        l[2] = l[2].split("\n")
        print("pprz_files/" + l[1])
        print(".." + l[2][0])
        if l[0] == "dir":
            copytree("pprz_files/" + l[1], ".." + l[2][0] + l[1])
        if l[0] == "merge":
            copy("pprz_files/" + l[1], ".." + l[2][0] + l[1])
        
        
if __name__ == '__main__':
    pprz_version = "null"
    try:
        process = subprocess.Popen('../paparazzi_version', stdout=subprocess.PIPE)
        for l in process.stdout:
            pprz_version = l.strip('\n')
    except:
        print("Conf has not been cloned into the proper folder")
        exit()
    
    if pprz_version == PPRZ_VERSION:
        print("Everything is awesome")
        install_custom_modifications()
    else:
        print("Paparazzi Versions do not match")
        
    
    
    
