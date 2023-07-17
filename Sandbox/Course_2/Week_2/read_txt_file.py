#!/usr/bin/env python3

def read_txt_file():
    file = open("spider.txt")
    lines = file.readlines()
    file.close()
    lines.sort()
    print(lines)

read_txt_file()