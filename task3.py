# Откройте текстовый файл task3.txt для чтения.
# Извлеките все уникальные слова из файла (слова разделяются пробелами и знаками пунктуации).
# Подсчитайте, сколько раз каждое уникальное слово встречается в тексте.
# Запишите результаты в новый файл в формате:
# слово1: количество
# слово2: количество
#
# Убедитесь, что слова записаны в алфавитном порядке.
with open('task3.txt', encoding="utf-8") as f:
    e = e = f.read()
    e = e.replace('.', '')
    e = e.replace(',', '')
    e = e.replace('?', '')
    e = e.replace('!', '')
    e = e.replace('—', '')
    e = e.replace(':', '')
    e = e.replace('-', '')
    s = e.split()
new = open("New_file3.txt", "w+")
j = 0
p = []
for i in range(len(s)):
    s[i] = s[i].lower()
    if(s.index(s[i]) == i):
        p.append(s[i])
p = sorted(p)
for i in p:
    new.write(str(i) + ': ' + str(s.count(i)))
    j += 1
    new.write('\n')
new.close()