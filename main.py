
from colorama import Fore, init
import pandas as pd
import os, sys

#sys.path.append(os.getcwd())
from package.fns import file_processor
from package.fns import check_file


folders_check_list = []

try:
    folders = list(os.walk('Исходники'))[0][1]

    for folder in folders:
        print(Fore.MAGENTA, folder, Fore.RESET)
        files = list(os.walk(os.path.join('Исходники', folder)))[0][2]

        res_dfs = []
        if files:
            folders_check_list.append([folder, len(files)])
            for file in files:           
                file_processor_res = file_processor(folder, file)

                if file_processor_res[0]:
                    res_dfs.append(file_processor_res[1])

                print(file_processor_res)

            if res_dfs:
                res_df = pd.concat(res_dfs)
                res_df.to_excel(os.path.join(os.getcwd(), 'Подготовленные', f'{ folder }.xlsx'))

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

