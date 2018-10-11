# -*- coding: utf-8 -*-

s = '深入 다이빙 Python'
print(len(s), s[0])
by = s.encode('utf-8')
print(by)

query = 'user=pilgrim&database=master&password=PapayaWhip'
a_list = query.split('&')
print(a_list)
a_list_of_lists = [v.split('=',1) for v in a_list if '=' in v]
print(a_list_of_lists)
a_dict = dict(a_list_of_lists)
print(a_dict)
print(a_dict['database'])
