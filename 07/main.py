from tkinter import filedialog
import os
from parser import parse
from codewriter import *
from classes import *


ini = initialise()
instruction= ''
instruction+= ini.start()
asmpath = ''

vm_dir = filedialog.askdirectory()
print(vm_dir)
vm_files = os.listdir(vm_dir)
if 'Sys.vm' in vm_files:
    instruction+= ini.callsysinit()

for i in range (len(vm_files)):
    base_name = vm_files[i]
    path = vm_dir + '/'+ base_name
    filename, ext_name = os.path.splitext(base_name)
    if ext_name == '.vm':
        print(path)
        vm_file = open(path, 'r')
        contents_list = vm_file.readlines()    
        vm_file.close()
        contents_list = parse(contents_list)
        instruction += codewrite(contents_list, filename)

instruction += ini.end()

asmpath = vm_dir + '/'+ vm_dir.split(sep='/')[-1] + '.asm'
print(asmpath)
asm_file= open(asmpath, 'w')
asm_file.write(instruction)
asm_file.close() 
