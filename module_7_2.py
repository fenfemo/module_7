def custom_write(file_name, strings):
    file = open(file_name, 'a', encoding = 'utf-8')
    strings_positions = {}
    i = 0
    for line in strings:
        byte = file.tell()
        i += 1
        file.write(f'{line}\n')
        strings_positions[(i, byte)] = line
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():

  print(elem)