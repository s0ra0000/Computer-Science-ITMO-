import re

def solve(x):
    string = ''
    a = re.split(r'\W+',x) #разделить по любой не-буква, не-цифра и не подчёркивание и добавить в лист, (+) значит может более синоним
    if(a[-1] == 'P3111'): #проверить номер группы
        b = re.findall(r'[А-ЯЁ]',x) #найти всю большаую букву и добавить в лист 
        if(b[0] != b[1] or b[1] != b[2] or b[0] != b[2]): #если они не равны друг с другом, то записать в файл
            string += x
            output_file.write(string+'\n')
    else: #если номер группы отличается от "P3111", то записать в файл
        string += x
        output_file.write(string+'\n')

address_input = "D:\ITMO\\1st Semester\Computer Science (Basics)\lab3\lab3_3\input.txt"
address_output = 'D:\ITMO\\1st Semester\Computer Science (Basics)\lab3\lab3_3\output.txt'

input_file = open(address_input,'r',encoding='utf-8')
output_file = open(address_output,'w',encoding='utf-8')

x = input_file.read().split('\n')

for i in range(len(x)):
    solve(x[i])

input_file.close()
output_file.close()