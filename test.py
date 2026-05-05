from openpyxl.utils.cell import coordinate_from_string, column_index_from_string

cell_coord = 'AA4'
col_letter, row_num = coordinate_from_string(cell_coord)  # ('D', 4)
col_num = column_index_from_string(col_letter)            # 4

print(f"Строка: {row_num}, Столбец: {col_num}")