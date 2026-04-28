import zipfile
import os
import xml.etree.ElementTree as ET

file_path = '26.04.27 Лебедев Ю890(010).xlsx'  # Файл, который открывается, но листы защищены
password = 'rgs2023'     # Пароль на защиту листа (если есть)
output_path = 'unlocked_by_xml.xlsx'

# 1. Распаковываем Excel как ZIP-архив
with zipfile.ZipFile(file_path, 'r') as z:
    z.extractall('temp_excel_folder')

# 2. Чистим защиту в workbook.xml (снимаем структуру книги)
wb_xml = 'temp_excel_folder/xl/workbook.xml'
tree = ET.parse(wb_xml)
root = tree.getroot()
# Ищем пространство имен
ns = {'default': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
# Удаляем атрибуты защиты
for elem in root.findall('.//default:workbookProtection', ns):
    root.remove(elem)

# 3. Чистим защиту в каждом листе (снимаем защиту листа)
sheets_dir = 'temp_excel_folder/xl/worksheets'
for sheet_file in os.listdir(sheets_dir):
    if sheet_file.endswith('.xml'):
        sheet_path = os.path.join(sheets_dir, sheet_file)
        sheet_tree = ET.parse(sheet_path)
        sheet_root = sheet_tree.getroot()
        for elem in sheet_root.findall('.//default:sheetProtection', ns):
            sheet_root.remove(elem)
        sheet_tree.write(sheet_path, encoding='utf-8', xml_declaration=True)

tree.write(wb_xml, encoding='utf-8', xml_declaration=True)

# 4. Собираем обратно в XLSX
with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as z:
    for foldername, subfolders, filenames in os.walk('temp_excel_folder'):
        for filename in filenames:
            filepath = os.path.join(foldername, filename)
            z.write(filepath, arcname=filepath.replace('temp_excel_folder/', ''))

# Удаляем временную папку
import shutil
shutil.rmtree('temp_excel_folder')
print(f"Готово: {output_path}")