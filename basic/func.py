# 파라미터 전달방식 : 함수내에서 i, mylist값 변경
from typing import Any, Union


def fn(i, mylist):
    i = i + 1
    mylist.append(0)


k = 10
m = [1, 2, 3]

fn(k, m)
print(k, m)  # i : 정수, mylist : mutable타입으로 값이 변경됨


# Default Parameter
def cal(i, j, factor=1):
    return i * j * factor

result = cal(10,20)
print(result)

# Named paramter
def report(name, age, score):
    print(name, age)

report(age=10, name='baguju', score=80)

# 가변길이 paramter
def total(*num):
    tot = 0
    for n in num:
        tot += n
    return tot

t = total(1,2,3)
print(t)

# return 값 : Tuple을 리턴한다고 생각하면 됨
def calc(*numbers):
    cnt = 0
    tot = 0
    for n in numbers:
        cnt += 1
        tot += n

    return cnt, tot, tot/cnt

cnt, tot, avg = calc(1,2,3,4,5)
print(cnt, tot, avg)
