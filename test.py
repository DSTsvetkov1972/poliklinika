from package.config import folders_rules_dict
import os

folders = list(os.walk('Исходники'))[0][1]
print(folders)
downloaded_folders = [folder for folder in folders if '_Скачано' in folder]
folders_len = [len((download_folder + folders_rules_dict[download_folder]['email_folder'])) for download_folder in downloaded_folders]


print(max(folders_len))