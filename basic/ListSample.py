print("===" + " List Sample " + "="* 60)

# List = Array로 생각하면 됨.

odd = [1,3,5,7,9]
print(odd)
print(odd[2])
print(odd[-1])
print(odd[0:2])

#  List include List.
a = [1,2,3,['a','b','c']]
print(a[-1][0])

b = [4,5,6]
print(a[0:3]+b)
print(b*2)

b[1] = 7
print(b)

del(b[1])
print(b)

b.append(2)
b.append(1)
print(b)

b.sort()
print(b)

b.reverse()
print(b)

b.insert(0,9)
print(b)

b.remove(1)   # 첫번째 나오는 값을 삭제
print(b)

# 리스트 값을 삭제하는 방법
# 1. remove : value
# 2. pop    : index
# 3. del    : index

print("=== " + "{0:<15}".format("tuple") + "="*60)

# tuple은 list와 구조는 동일하지만 값을 변경할 수 없다.
t1 = (1,2,3,4)
print(t1)
print(t1[3])
print(t1 * 2)

print()
print("=== " + "{0:<15}".format("Dictionary") + "="*60)
# Dictionary : hash와 같음.  key=value구조
d1 = {"name":"baguju","age":"50","sex":"male"}
print(d1)

d1["habit"] = "photo"
print(d1)
del d1["habit"]
print(d1)

print(d1["age"])
d1["age"] = "20"

print(d1)

print(d1.keys())         # dict_keys 라는 객체가 만들어짐(sort, insert 등 적용불가)
vl = list(d1.keys())
print(vl)                # key값만 list에 적용함


print(d1.values())

for k in d1.keys():
    print("{0}:".format("{0:<10}".format(k)), d1.get(k))

# Key가 dictionary안에 있는지?
print("age" in d1)

msg = "set"
print("\n=== " + f"{msg:<15}" + "=" * 60)

# set(집합자료형)은 중복을 허용하지 않으며, 순서가 없다
# 자료의 중복을 제거하기 위한 필터로 활용된다.

s1= {1,2,3,1,2}
print(s1)
s2 = {3,4,5,6,7}

print(s1&s2)    # 교집합
print(s2.intersection(s1))
print(s1|s2)    # 합집합
print(s2.union(s1))
print(s2-s1)    # 차집합
print(s2.difference(s1))

s1.update([7,8,8,10])
print(s1)

l1 = list(s1)       # 자료에 접근하기 위하여 리스트나 튜플로 변환
t1 = tuple(s1)
print(l1)
print(t1)


# Bool
if (bool([])):
    print("True")
else:
    print("False")
