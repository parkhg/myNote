# 정규식 표현
import re


data = """
park 690223-1528114
kim  700905-1059119
"""

pat = re.compile("(\d{6})[-]\{7}")
print(pat.sub("\g<1>-*******",data))


result = []
for line in data.split("\n"):
    word_result = []
    for word in line.split(" "):
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + "-" + "*******"
        word_result.append(word)

    result.append(" ".join(word_result))

print("\n".join(result))


# 정규표현식의 기초

# 1. 문자클래스 [] : 문자들과 매치
# [a-zA-Z] : 알파벳 모두
# [0-9] : 숫자 모드
# [^0-9] :  Not 숫자

# \d - 숫자와 매치, [0-9]와 동일한 표현식이다.
# \D - 숫자가 아닌 것과 매치, [^0-9]와 동일한 표현식이다.
# \s - whitespace 문자와 매치, [ \t\n\r\f\v]와 동일한 표현식이다. 맨 앞의 빈 칸은 공백문자(space)를 의미한다.
# \S - whitespace 문자가 아닌 것과 매치, [^ \t\n\r\f\v]와 동일한 표현식이다.
# \w - 문자+숫자(alphanumeric)와 매치, [a-zA-Z0-9]와 동일한 표현식이다.
# \W - 문자+숫자(alphanumeric)가 아닌 문자와 매치, [^a-zA-Z0-9]와 동일한 표현식이다.

p = re.compile("[a-z]+")   # 첫글자가 소문자인가???
m = p.match("Python")
m = p.match("python")
if m:
    print("Match found : ", m.group())
else:
    print("No Match.")

print(m)

m = p.search("Python")     # 전체에서 소문자를 찾음
if m:
    print("Match found : ", m.group())
else:
    print("No Match.")


result = p.findall("Life is short")    # List로
print(result)

result = p.finditer("life is short")
print(result)


# group() : match된 문자열을 리턴
# start() : match된 문자열의 시작위치를 리턴
# end()   : match된 문자열의 끝 위치를 리턴
# span()  : match된 문자열의 (시작,끝) 튜플로 리턴

m = p.search("4 python")
print(m.group())
print(m.start())
print(m.span())

