import re

def solve(x):
    return len(re.findall(r";<{\(",x)) # найти все смайлики по структуре, добавить в лист и возвращать длину листа.

address_input = "D:\ITMO\\1st Semester\Computer Science (Basics)\lab3\lab3_1\input.txt"
address_output = 'D:\ITMO\\1st Semester\Computer Science (Basics)\lab3\lab3_1\output.txt'

input_file = open(address_input,'r',encoding='utf-8')
output_file = open(address_output,'w',encoding='utf-8')

x = input_file.read().split('\n')

for i in range(len(x)):
    output_file.write(str(solve(x[i]))+'\n')

input_file.close()
output_file.close()