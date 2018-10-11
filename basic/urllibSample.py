import urllib.request

fhand = urllib.request.urlopen("http://py4inf.com/code/romeo.txt")
for line in fhand:
    print(line.split())

    # words = line.split()
    # for word in words:
    #     counts[word] = counts.get(word,0) + 1
