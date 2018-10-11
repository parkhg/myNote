# -*- coding: utf-8 -*-
import re

s = '100 NORTH MAIN ROAD'
print(re.sub('ROAD$','RD.', s))    # $ 문자열의 끝부분과 일치


s = '100 NORTH BROAD ROAD APT. 3'
print(re.sub('ROAD$','RD.',s))

print(re.sub(r'\bROAD\b','RD.',s))  # 정규식 표현에 r문자를 사용하라
