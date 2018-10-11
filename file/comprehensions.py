import os

'''
1. 현재 Dir
2. Dir와 File 분리
3. File과 확장자 분리
'''
# dir chanage
print(os.getcwd())
os.chdir('/Users/baguju/PycharmProjects/LearnPython/ctrl')
print(os.getcwd())

# file & dir 분리
pathname = '/Users/baguju/PycharmProjects/LearnPython/deep/sysinfo.py'
print(os.path.split(pathname))
(dirname, filename) = os.path.split(pathname)
print(dirname, filename)

# file과 확장자 분리
(shortname, extension) = os.path.splitext(filename)
print(shortname, extension[1:])

'''
4. Dir 내 file조회(Wild Card 활용)
'''
import glob

print(glob.glob('*.py'))

'''
5. File Meta 정보
'''
print(os.getcwd())

metadata = os.stat('wjparser.py')
print(metadata)

import time

# st_mtime : 19700101부터 현재까지의 시간(초) Epoch
print(time.localtime(metadata.st_mtime))
# time.struct_time(tm_year=2018, tm_mon=7, tm_mday=18, tm_hour=22, tm_min=30, tm_sec=27, tm_wday=2, tm_yday=199, tm_isdst=1)

print(os.path.realpath('wjparser.py'))

# File Size
print(metadata.st_size)

import deep.humansize as humansize
print(humansize.approximate_size(metadata.st_size))


'''
------------------------------------------------
List : 모든 List에 일괄적용
'''

a_list = [2,5,3,7]
b_list = [elem * 2 for elem in a_list]
print(a_list, b_list)

# 파일에 일괄적
print([os.path.realpath(f) for f in glob.glob('*.py')])


# 파일에 일괄적용 (if 문을 추가하여 필터링할 수 있다)
print([os.path.realpath(f) for f in glob.glob('*.py') if os.stat(f).st_size > 2000])

# File Size와 함께 처리
print([(os.stat(f).st_size, os.path.realpath(f)) for f in glob.glob('*.py')])
print([(humansize.approximate_size(os.stat(f).st_size), os.path.realpath(f)) for f in glob.glob('*.py')])

metadata1 = [(f, os.stat(f).st_size) for f in glob.glob('*.py')]
print(metadata1)  # 튜플로 반환

# 값을 변환 행과 열을 대치하는데, 값이 변하지 않는 immutable일때 사용 가능
a_dict = {'a':1, 'b':2, 'c':3}
print({value:key for key, value in a_dict.items()})


#
a_set = set(range(10))
print({(x ** 2, x) for x in a_set})
