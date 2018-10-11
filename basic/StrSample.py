path = r"C:\temp\test.csv"
print(path)


# str.join()
s = "".join(["가나","다라","마바"])
print(s)

s = "-".join(["가나","다라","마바"])
print(s)

# str.split
s = "가나,다라,마바".split(",")
print(s)

#str.partition
defarture,_,arrival = "Seattle-Seoul".partition("-")
print(defarture)
print(arrival)

# format
# 1.위치를 기반으로
s = "Name :{0}, Age :{1}".format("박형곤","50")
print(s)

# 2.필드명을 기반으로
s = "Name :{name}, Age :{age}".format(name="박형곤",age="50")
print(s)

# 3.object's index or key
info = ("박형곤","50")
s = "Name :{x[0]}, Age :{x[1]}".format(x=info)
print(s)


# byte Class
text1 = b"byte"
text2 = "byte"

for c in text1:
    print(c)


for c in text2:
    print(c)
