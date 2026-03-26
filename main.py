from fns.fns import check_file, fns_dict
from colorama import Fore, init
import pandas as pd
import os
from fns.fns import file_processor


folders_check_list = []

try:
    folders = list(os.walk('files'))[0][1]

    for folder in folders:
        print(Fore.MAGENTA, folder, Fore.RESET)
        files = list(os.walk(os.path.join('files', folder)))[0][2]
        if files:
            folders_check_list.append([folder, len(files)])
            for file in files:           
                file_processor_res = file_processor(folder, file)
                print(file_processor_res)

        else:
            folders_check_list.append([folder, 0])



    # print(folders_check_list)
except Exception as e:
    print(Fore.RED, str(e), Fore.RESET)

# print(folders_rules_dict['Согаз_изменение объёма'])

   

  


#
##if __name__ == '__main__':
#    folder = 'Согаз_изменение объёма'
#    file = 'Согаз изменение объема пример.xls'
#    file_processor_res = file_processor(folder, file)
#    print(file_processor_res)

