import sys
import deep.humansize as humansize

print(sys.path)
print(humansize.approximate_size(4096,True))
# print(humansize.approximate_size(-14096,True))

'''
[
 '/Users/baguju/PycharmProjects/LearnPython/deep', 
 '/Users/baguju/PycharmProjects/LearnPython', 
 '/Users/baguju/anaconda3/envs/jweb/lib/python36.zip', 
 '/Users/baguju/anaconda3/envs/jweb/lib/python3.6', 
 '/Users/baguju/anaconda3/envs/jweb/lib/python3.6/lib-dynload', 
 '/Users/baguju/anaconda3/envs/jweb/lib/python3.6/site-packages'
]
'''


(MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY) = range(7)

print(MONDAY)


# 중복된 값은 무시됨.
a_list = ['a', 'b', 'mpilgrim', True, False, 42]
a_set = set(a_list)                           #1
print(a_set)                                  #2
## {'a', False, 'b', True, 'mpilgrim', 42}
print(a_list)                                 #3
## ['a', 'b', 'mpilgrim', True, False, 42]


a_set = {2, 4, 5, 9, 12, 21, 30, 51, 76, 127, 195}
print(30 in a_set)                                              #1
## True
print(31 in a_set)
## False
b_set = {1, 2, 3, 5, 6, 8, 9, 12, 15, 17, 18, 21}
print(a_set.union(b_set))                                       #2
## {1, 2, 195, 4, 5, 6, 8, 12, 76, 15, 17, 18, 3, 21, 30, 51, 9, 127}
print(a_set.intersection(b_set))                                #3
## {9, 2, 12, 5, 21}
print(a_set.difference(b_set))                                  #4
## {195, 4, 76, 51, 30, 127}
print(a_set.symmetric_difference(b_set))                        #5
## {1, 3, 4, 6, 8, 76, 15, 17, 18, 195, 127, 30, 51}


a_dict = {'server': 'db.diveintopython3.org', 'database': 'mysql'}
print(a_dict)
## {'server': 'db.diveintopython3.org', 'database': 'mysql'}
a_dict['database'] = 'blog'  #1
print(a_dict)
## {'server': 'db.diveintopython3.org', 'database': 'blog'}
a_dict['user'] = 'mark'      #2
print(a_dict)                #3
## {'server': 'db.diveintopython3.org', 'user': 'mark', 'database': 'blog'}
a_dict['user'] = 'dora'      #4
print(a_dict)
## {'server': 'db.diveintopython3.org', 'user': 'dora', 'database': 'blog'}
a_dict['User'] = 'mark'      #5
print(a_dict)
## {'User': 'mark', 'server': 'db.diveintopython3.org', 'user': 'dora', 'database': 'blog'}
