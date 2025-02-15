import tkinter
from tkinter import filedialog
import os
from variableclasses import *
from operationclasses import *



vm_file = tkinter.filedialog.askopenfile(mode='r', filetypes =[('VM file (.vm)', '*.vm')])
path = vm_file.name
base_name = os.path.basename(path)
filename, ext_name = os.path.splitext(base_name)


path = path[:-3]
contents_list = vm_file.readlines()    
vm_file.close()

instruction= ''

stack= vartype_with_predefined_variable_names( 'SP')
local= vartype_with_predefined_variable_names('LCL')
argument= vartype_with_predefined_variable_names('ARG')
this= vartype_with_predefined_variable_names('THIS')
that= vartype_with_predefined_variable_names('THAT') 
pointer = vartype_with_new_names_mapped_R3_to_R15(3)
temp= vartype_with_new_names_mapped_R3_to_R15(5)

op = operations_class()

def pop(var, num, filename):
    if var=='pointer' or var == 'temp':
        return f'''@SP
AM=M-1
D=M
@{eval(f'{var}.locate({num})')}
M=D
'''
    
    elif var=='static':
        return f'''@SP
AM=M-1
D=M
@{filename}.{num}
M=D
'''
        
    else:
        return f'''@{eval(f'{var}.name')}
D=M
@{num}
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
'''


def push(var, num, filename):
    if var=='pointer' or var == 'temp':
        return f'''@{eval(f'{var}.locate({num})')}
D=M
@SP
A=M
M=D
@SP
M=M+1
'''
    elif var=='static':
        return f'''@{filename}.{num}
D=M
@SP
M=M+1
A=M-1
M=D
'''
    elif var=='constant':
        return f'''@{num}
D=A
@SP
A=M
M=D
@SP
M=M+1
'''

        
    else:
        return f'''@{num}
D=A
@{eval(f'{var}.name')}
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
'''

def parseline(command):

    global filename

    command_list=command.split()
    print(command_list)
    global instruction
    if command_list[0]=='pop':
        command= command_list[0]
        return pop(command_list[1], int(command_list[2]), filename)

        
    elif command_list[0]=='push':
        command= command_list[0]
        return push(command_list[1], int(command_list[2]), filename)


    else:
        return eval(f'op._{command_list[0]}()')
        

def parse(contents_list):
    global instruction
    i=0
    while True:
        try:
            contents_list[i]=contents_list[i].replace('\n', '')
            if contents_list[i].startswith("//") or contents_list[i].startswith("\\") or contents_list[i]=='' :
                contents_list.pop(i)
                continue
            i+=1
        except Exception as e:
            print('loop 1 terminated')
            break


    # SECOND PASS
    for i in range(len(contents_list)):
        instruction+=f'''//{contents_list[i]}
'''
        instruction+= parseline(contents_list[i]) 


parse(contents_list)
path+= ".asm"   
asm_file= open(path, 'w')
asm_file.write(instruction)
asm_file.close()

