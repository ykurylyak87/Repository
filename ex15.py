# -*- coding: utf-8 -*-
from sys import argv

# Передаємо два аргумента скрипту (назава скрипта, назва файлу)
script, filename = argv
# Відкриваємо переданий вище файл і присвоюємо його змінній txt
txt = open(filename)
# Видаємо на екран назву скрипта
print "Content of files %r:" % filename
# Видаємо на екран вміст змінної txt (куди ми передали вміст файлу)
print txt.read()
# Просимо користувача ввести назву файлу ще раз і присвоюємо її змінній file_again
print "Enter the name of the file again:" 
file_again = raw_input ("> ")
# Передаємо вміст файлу у змінну txt_again
txt_again = open(file_again)
# Виводимо на екран вміст змінної txt_again
print txt_again.read()
txt_again2 = open(filename, "w")
txt_again2.write("Hello")
txt_again2.close()
