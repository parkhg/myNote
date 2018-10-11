"""
Dir의 파일리스트를 구함
"""
import os

def get_file_list(path):
    fp = open(path + "/filelist.txt",'wt')
    filelist = os.listdir(path)
    for x in filelist:
        fp.write(x + '\n')
    fp.close()

get_file_list("/Users/baguju")


