# Откройте текстовый файл task2.txt для чтения.
# Считайте его содержимое в строку.
# Найдите и замените все вхождения слова "Python" на слово "Питон" (регистр учитывать).
# Запишите обновленный текст в новый файл с другим именем.
# Выведите на экран сообщение о количестве произведённых замен.
with open('task2.txt', encoding="utf-8") as f:
    s = f.read()
    cnt = 0
    while(s.find('Python') != -1):
        s = s[:s.find('Python')] + 'Питон' + s[s.find('Python') + 6:]
        cnt += 1
new = open("New_file2.txt", "w+")
new.write(s)
new.close()
print(cnt)