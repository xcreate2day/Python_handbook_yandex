""" 3.5. Потоковый ввод/вывод. Работа с текстовыми файлами. JSON """
""" Без комментариев 2.0
    Формат ввода: Вводятся строки программы.
    Формат вывода: Каждую строку нужно очистить от комментариев. А если комментарий — вся строка, то выводить её не нужно.
    """

from sys import stdin

for line in stdin.readlines():
    if line[0] != '#':
        print(line.split('#')[0].rstrip('\n'))


""" Найдётся всё 2.0
    Формат ввода: Вводятся заголовки страниц. В последней строке записан поисковый запрос.
    Формат вывода: Вывести все заголовки страниц, в которых присутствует поисковый запрос (регистр не имеет значения).
    Порядок заголовков должен сохраниться. 
    """

from sys import stdin
*headers, target = [header.strip('\n') for header in stdin.readlines()]
print(*[header.strip() for header in headers if header.lower().find(target.lower()) + 1], sep='\n')

""" А роза упала на лапу Азора 6.0
    Формат ввода: Вводятся слова.
    Формат вывода: Список слов-палиндромов в алфавитном порядке без повторений.
    """

from sys import stdin
strings = [word.strip() for string in stdin.readlines() for word in string.split() if word.lower() == word[::-1].lower()]
print(*[header.strip() for header in sorted(set(strings))], sep='\n')

""" Транслитерация 2.0
    Формат ввода: В одной папке с вашей программой лежит файл cyrillic.txt. В нём, в числе прочих, 
    содержится некоторое количество кириллических символов.
    Формат вывода: В файл transliteration.txt записать результат транслитерации исходного файла.
    """
alphabet = {
    'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E',
    'Ж': 'ZH', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M',
    'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U',
    'Ф': 'F', 'Х': 'KH', 'Ц': 'TC', 'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH',
    'Ы': 'Y', 'Э': 'E', 'Ю': 'IU', 'Я': 'IA', 'Ь': '', 'Ъ': ''
}

encoded = ''

with open('cyrillic.txt', encoding="UTF-8") as file_in:
    data = file_in.readlines()

for s in data:
    for ch in s:
        if ch.upper() in alphabet:
            encoded += alphabet[ch.upper()].lower() if ch.islower() else alphabet[ch].capitalize()
        else:
            encoded += ch

with open('transliteration.txt', 'w', encoding="UTF-8") as file_out:
    file_out.writelines(encoded)
