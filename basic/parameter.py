# parameter를 받기
# 사용예 : python sys.py life is short


import sys

args = sys.argv[1:]
for i in args:
    print("Param %d : %s", i, i.upper(), end=' ')
