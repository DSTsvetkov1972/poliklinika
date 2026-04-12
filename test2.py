import imapclient

# Автоматическое преобразование UTF-8 в UTF-7
folder_name_utf8 = "Отправл енные"
folder_name_utf7 = imapclient.imap_utf7.encode(folder_name_utf8)
print(folder_name_utf7)  # '&BBkEQQQ/BDo-'