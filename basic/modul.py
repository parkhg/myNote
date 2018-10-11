"""
모듈은 .py 파일 하나를 의미하고,
패키지는 .py 가 모여진 디렉토리의 모듈 집합을 의미한다.
패키지는 서브 패키지를 포함할 수 있다.
즉, 디렉토리.패키지.서브패키지와 같이 액세스가 가능하다.
예)
import models.account.bill
bill.charge(1,50)

Class : 객체지향프로그래밍(OOP, Object Oriented Programming)의 기본단위인 클래스
        method, property, class variable, instance variable, initializer, destructor
        class에 새로운 attribute 추가 가능
"""

# 수학모듈
import math
f = math.factorial(5)
print(f)

# 모듈내 특정함수만
from math import factorial
f = factorial(5) / factorial(3)
print(f)

# 모듈을 Alias
from math import factorial as fac
f = fac(20)
print(f)

# 사용자 모듈 호출
from ujuLib import *
prnline()
