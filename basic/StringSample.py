str = '"Python is very Easy." he says.'
print(str)

str = "Python\'s Good Language."
print(str)

mline = "Life is a short.\nYou need Python."
print(mline)

mline = """
Life's a short.
You need Python.
"""
print(mline)    # 멀티라인 활용법

str1 = "Python is "
str2 = "simple."
print(str1+str2)    # 문자열 더하기
print(str1*2)       # 문자열 반복하기
print("="*80)       # 라인긋기

#===================================================================
# 문자열 Indexing & Slice.

str = "Life is too short, You need Python"
print(str[3])
print(str[0])
print(str[-2])      # 뒤에서부터
print(str[0:4])     # Substring (0 <= a < 3)
print(str[0:3])
print(str[19:])
print(str[:17])
print(str[19:-7])

num = 3
str = "I eat %d apples." % num
print(str)

day = "Monday"
str = "I eat {0} apples. and every {1}".format(num,day)
print(str)

str = "I eat {0} apples. and every {day}".format(num,day="Wendesday")
print(str)

print("="*3 + " Align " + "="*70)       # 라인긋기
print("{0:<10}".format("Hi"))
print("{0:^10}".format("Hi"))
print("{0:>10}".format("Hi"))

pi = 3.42134234
print("{0:0.4f}".format(pi))
print("{0:10.4f}".format(pi))

name = "박형곤"
print(f"내 이름은 {name}이다.")

d = {'name':'홍길동', 'age':30}
print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')

print("===" + " Character Function " + "="*60)


str = "I eat {0} apples. and every {day}".format(num,day="Wendesday")
print(str.count("a"))       # Count
print(str.find("a",4))      # 위치
print(str.index("t"))       # 위치(없으면 오류발생 : 사용할 필요가???)

a=","
print(a.join("abcd"))

a="abcd"
print(a.upper())
print(a.upper().lower())

a="   abcd   "
print(a.lstrip())
print(a.rstrip())

a = "Life is too short"
print(a.replace("Life", "Your leg"))
print(a.split())
a="a:b:c:d"
print(a.split(":"))

