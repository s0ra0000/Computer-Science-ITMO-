import re
def solve(x):
    string = ''
    a = re.split(r'\W+',x) #разделить по любой не-буква, не-цифра и не подчёркивание и добавить в лист, (+) значит может более синоним
    for i in range(len(a)):
        if(i<len(a)-1): #если это не последный элемент листа
            match = re.search(r'\w*[УуЕеЫыАаОоЭэЯяИиЮю]{2}\w*',a[i]) #проверить это слово,в которых две гласные стоят подряд
            if(match and len(re.findall(r'[йЦцКкНнГгШшЩщЗзХхФфВвПпРрЛлДдЖжБбТтМмСсЧч]',a[i+1]))<4): #проверить после этого слово идет ли слово, в котором не больше 3 согласных
                string += a[i] + ' '
    return string

address_input = "D:\ITMO\\1st Semester\Computer Science (Basics)\lab3\lab3_2\input.txt"
address_output = 'D:\ITMO\\1st Semester\Computer Science (Basics)\lab3\lab3_2\output.txt'
input_file = open(address_input,'r',encoding='utf-8')
output_file = open(address_output,'w',encoding='utf-8')

x = input_file.read().split('\n')

for i in range(len(x)):
    output_file.write(str(solve(x[i]))+'\n')

input_file.close()
output_file.close()