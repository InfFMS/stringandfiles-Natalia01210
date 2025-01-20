# Откройте текстовый файл task5.txt для чтения.
# Найдите самое длинное слово в тексте. Если таких слов несколько, выберите первое из них.
# Запишите это слово и его длину в новый файл в формате:
# Самое длинное слово: слово
# Его длина: длина
#
# Выведите это слово и длину в консоль.
with open('task5.txt', encoding="utf-8") as f:
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
mxlen = 0
for i in s:
    if(len(i) > mxlen):
        mxlen = len(i)
        mxw = i
new = open("New_file5.txt", "w+")
new.write('Самое длинное слово: ')
new.write(mxw)
new.write('\n' + 'Его длина: ')
new.write(str(mxlen))
new.close()