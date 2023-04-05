import os

my_file = open('CheckList.txt', "r")


if not os.path.isdir("List of characters"):#Проверка наличия каталога
    os.mkdir("List of characters")#Создание каталога

os.chdir("List of characters") #Смена директория

for i in range(0,43):
    for line in my_file:
        if not os.path.isdir('{}'.format(str(line.strip()))):
             os.mkdir('{}'.format(str(line.strip())))
        break