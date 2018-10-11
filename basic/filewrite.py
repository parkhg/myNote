# filewrite.py

f = open("fileTest.txt",'w')
for i in range(1,10):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

# File Read
f = open("fileTest.txt","r")

# 1번째 방법
# data = f.read()
# print(data)
# f.close()

# 2번째 방법
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

# 3번째 방법 : close 없이 사용
with open("fileTest.txt",'w') as f:
    f.write("Life is too short, you need python.")


f = open("fileTest.txt","r")

# 1번째 방법
data = f.read()
print(data)
f.close()


