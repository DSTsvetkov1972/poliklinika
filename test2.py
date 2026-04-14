file_path = "aaa.abc.xlsx"


file_path_parts = file_path.split('.')
file_path_short = '.'.join(file_path_parts[0:-1])
file_path_extension = file_path_parts[-1]

print(file_path_parts,file_path_short+'.'+file_path_extension )