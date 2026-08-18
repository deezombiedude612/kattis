"""
Kattis Problem also in IT5003 PS0
https://nus.kattis.com/courses/IT5003/IT5003_S1_AY2627/assignments/hkm5gk/problems/heimasida
"""


processed_input = map(
    lambda c: {'Á': 'a', 'á': 'a', 'Ð': 'd', 'ð': 'd',
               'É': 'e', 'é': 'e', 'Í': 'i', 'í': 'i',
               'Ó': 'o', 'ó': 'o', 'Ú': 'u', 'ú': 'u',
               'Ý': 'y', 'ý': 'y', 'Þ': 'th', 'þ': 'th',
               'Æ': 'ae', 'æ': 'ae', 'Ö': 'o', 'ö': 'o'}.get(c, c), input())
print(''.join(x for x in processed_input if x.isalnum()).lower() + ".is")
