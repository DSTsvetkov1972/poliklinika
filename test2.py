def fio_splitter(fio):

    whitespace_qty = fio.count(' ')
    if whitespace_qty != 2:
        raise ValueError(f'Строка ФИО должна содержать 2 пробела, по факту { whitespace_qty }')
    fio_parts = fio.split(' ')
    return {
        'surname': fio_parts[0],
        'name': fio_parts[1],
        'patronymic': fio_parts[2]
    }


if __name__ == '__main__':
    fio = 'Цветков Дмитрий Сергеевич'

    print(fio_splitter(fio))