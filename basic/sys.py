# parameter를 받기
import os
import time
import calendar

print(chr(97))

print(divmod(7,3))

for i, name in enumerate(['body','foo','bar']):
    print(i, name)


# filter 함수 사용법
def positive(a):
    return a > 0

print(list(filter(positive,[0,1,-3,2,4])))


print(len([1,2,3]))

# map test
def plusOne(x):
    return x + 1

print(list(map(plusOne,[1,2,3,4])))

print(ord("a"))

print(sorted("zero"))


print(os.getcwd())
print(os.system("ls"))

print(time.localtime(time.time()))

print(calendar.calendar(2018))
