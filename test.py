import os
from pathlib import Path

s1 = 'C:\\Users\\tsvetkovds\\Documents\\.PROJECTS\\AS\\Исходники\\Ингосстрах_Прикрепление\\ИГС_ПРИКР_21-04-2026_15-18-20_1730196_ГП № 220_KDP4.XLS'
s2 = 'C:\\Users\\tsvetkovds\\Documents\\.PROJECTS\\AS\\Исходники\\Ингосстрах_Прикрепление\\ИГС_ПРИКР_21-04-2026_15-18-20_1730196_ГП № 220_KDP4.XLS'

print(os.path.exists(s1))
print(os.path.exists(s2))

#for ss1, ss2 in zip(s1,s2):
 #   print(ss1, ss2, ss1==ss2)

l = list(os.walk('C:\\Users\\tsvetkovds\\Documents\\.PROJECTS\\AS\\Исходники\\Ингосстрах_Прикрепление\\'))
print(l)