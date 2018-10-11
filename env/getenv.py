"""
 OS의 환경설정을 구함

"""

import os

for item in os.environ:
    print("%s = %s" % (item, os.environ[item]))
