from package.config import folders_rules_dict
import os

folders = list(os.walk(os.path.join(os.getcwd(), 'Исходники')))[0][1]


print(folders)
for k in folders_rules_dict.keys():
    print(k)
