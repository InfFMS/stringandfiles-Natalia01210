# Откройте текстовый файл для чтения task1.txt.
# Подсчитайте:
# Общее количество строк в файле.
# Общее количество слов во всем тексте файла.
# Общее количество символов (включая пробелы).
# Выведите полученную статистику на экран.
punctation = ".,!?^"
with open('task1.txt', encoding="utf-8") as f:
    e = f.read()
    cnt = len(e)
    e = e.replace('.', '')
    e = e.replace(',', '')
    e = e.replace('?', '')
    e = e.replace('!', '')
    e = e.replace('—', '')
    e = e.replace(':', '')
    e = e.replace('-', '')
    s = e.split()
print(e.count('\n') + 1)
print(len(s))
print(cnt)