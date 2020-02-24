#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob

def pharse_my_hh(filepath):
        
    fin = open(filepath, "rt")
    fout = open("temp.txt", "wt")

    for line in fin:
        fout.write(line.replace(u'¥', u'$'))

    fin.close()
    fout.close()
        
    fin1 = open("temp.txt", "rt")
    newfilepath = filepath.replace(".txt", "_converted.txt")
    fout1 = open(newfilepath, "wt")

    for line in fin1:
        fout1.write(line.replace(u'Â', ''))

    fin1.close()
    fout1.close()

    print("convert done")

if __name__ == "__main__":

    filenamelist = (glob.glob("D:\\Funspaces\\2\\pokerking\\2020\\2\\*\\*.txt"))
    # filenamelist = (glob.glob("D:\\Funspaces\\2\\pokerking\\2020\\2\\21\\PKNG103426509.txt"))
    # print(filenamelist)
    for file in filenamelist:
        pharse_my_hh(file)
