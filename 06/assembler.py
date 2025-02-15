import tkinter
from tkinter import filedialog
'''
any new variables/labels are added to this, done in 2 ways
1: in the first pass when (labelname) appears, it is given the value of the current index of command (1*)
2: in the second pass if @somevariable is called and retriving its value from variable_dict returns an error , it simply creates a new variable using varcount as value
'''
varcount=16

variable_dict={
    'R0': '0',
    'R1': '1',
    'R2': '2',
    'R3': '3',
    'R4': '4',
    'R5': '5',
    'R6': '6',
    'R7': '7',
    'R8': '8',
    'R9': '9',
    'R10': '10',
    'R11': '11',
    'R12': '12',
    'R13': '13',
    'R14': '14',
    'R15': '15',
    'SCREEN': '16384',
    'KBD': '24576',
    'SP':'0',
    'LCL':'1',
    'ARG':'2',
    'THIS':'3',
    'THAT':'4'
}


comp_dict = {
    '0': '0101010',
    '1': '0111111',
    '-1': '0111010',
    'D': '0001100',
    'A': '0110000',
    '!D': '0001101',
    '!A': '0110001',
    '-D': '0001111',
    '-A': '0110011',
    'D+1': '0011111',
    'A+1': '0110111',
    'D-1': '0001110',
    'A-1': '0110010',
    'D+A': '0000010',
    'D-A': '0010011',
    'A-D': '0000111',
    'D&A': '0000000',
    'D|A': '0010101',
    
    'M': '1110000',
    '!M': '1110001',
    '-M': '1110011',
    'D+M': '1000010',
    'M+1': '1110111',
    'D-M': '1010011',
    'M-D': '1000111',
    'D&M': '1000000',
    'D|M': '1010101',
    'M-1': '1110010',
}

dest_dict = {
    'M': '001',
    'D': '010',
    'MD': '011',
    'A': '100',
    'AM': '101',
    'AD': '110',
    'AMD': '111'
}

jump_dict = {
    'JMP': '111',
    'JGT': '001',
    'JEQ': '010',
    'JGE': '011',
    'JLT': '100',
    'JNE': '101',
    'JLE': '110'
}

'''
used for the second pass when all the labels were already defined, and the code was cleaned of spaces and comments


'''
def parseline(instruction):
    global varcount
    #check for A instruction
    if instruction.startswith('@'):
        try:
            #if converting it to int didnt work that means its alphanumeric . if it did work, return the A instruction in binary
            string_before_completion= bin(int(instruction[1:])).replace("0b", "") 
        except:
            try:
                #checking if its a premade label (should be in variable_dict) or a pre made variable if this returns an error this means it can only be a new variable
                string_before_completion= bin(int(variable_dict[instruction[1:]])).replace("0b", "") 
                
            except:
                #the new variable is defined in the variable_dict (1*)
                variable_dict[instruction[1:]]=varcount
                varcount+=1
                string_before_completion= bin(int(variable_dict[instruction[1:]])).replace("0b", "") 
                

        out= ('0'*(16-len(string_before_completion)))+string_before_completion
        

    #noW it is a C instruction 
    else:
        #check for dest
        if instruction.count('='):
            dest=instruction[0:(instruction.rindex('='))]
            dest=dest_dict[dest]
            instruction=instruction[instruction.rindex('=')+1:]
        else:
            dest='000'

        #now the instruction looks kinda like 'COMP' or 'COMP;JUMP' or 'COMP;'
        

        #check for jump
        #also, checks for the condition where ; is given and no jump statement is given 
        if instruction.count(';'):
            if instruction[instruction.rindex(';')+1:]:
                jump = instruction[instruction.rindex(';')+1:]
                jump=jump_dict[jump]
                instruction=instruction[:(instruction.rindex(';'))]
            else:
                instruction=instruction[:(instruction.rindex(';'))]
        else:
            jump='000'

        #by now , the instruction looks like 'COMP'
            

        comp=comp_dict[instruction]

        out= f'111{comp}{dest}{jump}'

    return out




def parse(contents_list):
    machine_code=''
    i=0

    '''first pass
    1. removes all spaces
    2. removes all \n characters
    3. pops all elements containing just comments and empty lines (element is popped)
    4. if a (label) appears (1*) (element is popped)

    when an element is non popped , the value of i increments by 1 and then the loop continues

    when an element is popped , the value of i is not increased and the loop is continued , when the element had popped , the element after that took its place 
    , hence  the element at the index has to be checked again , so the index isnt incremented
    '''
    while True:
  
        try:
            contents_list[i]=contents_list[i].replace(' ', '')
            contents_list[i]=contents_list[i].replace('\n', '')
            if contents_list[i].startswith("//") or contents_list[i].startswith("\\") or contents_list[i]=='' :
                contents_list.pop(i)
                continue
            
            if contents_list[i].startswith('('):
                variable_dict[contents_list[i][1:-1]]= i 
                contents_list.pop(i)
                continue
            i+=1
        except Exception as e:
            break


    '''SECOND PASS
    repetitively calls the parseline function for each element of the 'contents_list'  and gets a return value of the converted machine code '''
    for i in range(len(contents_list)):
        machine_code += (parseline(contents_list[i]) + '\n')

    print(machine_code)
    return machine_code
        
    
        

    
#open the file using a tkinter dialog
asm_file = tkinter.filedialog.askopenfile(mode='r', filetypes =[('Assembler Source (.asm)', '*.asm')])
path = asm_file.name
path = path[:-3]
path+= "hack"
contents_list = asm_file.readlines()    
asm_file.close()
machine_code_final= parse(contents_list)[:-1]
hack_file= open(path, 'w')
hack_file.write(machine_code_final)
hack_file.close()



      
        
