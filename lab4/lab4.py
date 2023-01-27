import xmlplain
import re
import time

def parser():
    address_input = "D:\ITMO\\1st Semester\Computer Science (Basics)\lab4\Timetable_xml.xml"
    address_output = "D:\ITMO\\1st Semester\Computer Science (Basics)\lab4\Timetable_yaml.yml"
    input_file = open(address_input,'r',encoding='utf-8')
    output_file = open(address_output,'w',encoding='utf-8')
    lines = input_file.readlines()
    countTab = 0
    for line in lines:
        line = line.strip()
        if "<?" in line[:2]:
            continue
        elif "</" in line[:2]:
            countTab -= 1
        elif "<" in line[0]:
            start = line.index("<")
            end = line.index(">")
            cline = line[end+1:]
            if len(cline)<1:
                output_file.write(countTab * '  ' + line[start+1:end] + ":\n" )
                countTab += 1
            else:
                if cline.find("<") > -1:
                    close_tag = cline.index("<")
                    output_file.write(countTab * '  ' + line[start+1:end] + ': "' + cline[:close_tag] + '"\n')
                else:  
                    output_file.write(countTab * '  ' + line[start+1:end] + ": " + cline + "\n")
                    countTab += 1
        else:
            if "<" in line:
                end = line.index("<")
                output_file.write(countTab * '  ' + line[:end] + '\n')
                countTab -= 1
            else:
                output_file.write(countTab * '  ' + line + '\n')
    input_file.close()
    output_file.close()

def parser_with_library():
    address_input = "D:\ITMO\\1st Semester\Computer Science (Basics)\lab4\Timetable_xml.xml"
    address_output = "D:\ITMO\\1st Semester\Computer Science (Basics)\lab4\Timetable_with_library_yaml.yml"
    input_file = open(address_input,'r',encoding='utf-8')
    output_file = open(address_output,'w',encoding='utf-8')
    root = xmlplain.xml_to_obj(input_file, strip_space=True, fold_dict=True)
    xmlplain.obj_to_yaml(root, output_file)
    input_file.close()
    output_file.close()

def parser_with_re():
    address_input = "D:\ITMO\\1st Semester\Computer Science (Basics)\lab4\Timetable_xml.xml"
    address_output = "D:\ITMO\\1st Semester\Computer Science (Basics)\lab4\Timetable_with_re_yaml.yml"
    input_file = open(address_input,'r',encoding='utf-8')
    output_file = open(address_output,'w',encoding='utf-8')
    xml_lines = input_file.readlines()
    countTab = 0
    for xml_line in xml_lines:
        line = xml_line.strip()
        if re.search(r'<\w*>[\W\w]*<\/\w*>',line,re.I):
            str = ' '.join(re.findall(r'<[а-я\w\d]*>',line))[1:-1]
            str = str + ': "'+ ' '.join(re.findall(r'>[а-я\W\w\d]*<\/',line))[1:-2]
            output_file.write(countTab * '  ' + str + '"\n')
        elif re.search(r'<[а-я\w\d]*>',line,re.I):
            str_1 = ''.join(re.findall(r'<[а-я\w\d]*>',line))[1:-1] + ':'
            output_file.write(countTab * '  ' + str_1 + '\n')
            countTab += 1
        else:
            if re.search(r'^[а-я\w\d]+',line,re.I):
                str_2 = ''.join(re.findall(r'[а-я\w\d\D]+',line,re.I))
                print(str_2)
                output_file.write(countTab * '  ' + str_2 + '\n')
                if re.search(r'<\/[а-я\w\d]*>',line):
                    countTab -=1
            elif re.search(r'<\?',line):
                continue
            else:
                countTab -=1
    input_file.close()
    output_file.close()

parser_time = time.time()
for i in range(10):
    parser()
parser_time = time.time() - parser_time

parser_with_library_time = time.time()
for i in range(10):
    parser_with_library()
parser_with_library_time = time.time() - parser_with_library_time

parser_with_re_time = time.time()
for i in range(10):
    parser_with_re()
parser_with_re_time = time.time() - parser_with_re_time

print('Parser time: ' + str(parser_time))
print('Parser time with library: ' + str(parser_with_library_time))
print('Parser time with re: ' + str(parser_with_re_time)) 
