from classes import *

op = operations_class()
fn = functions_class()
pp = pushpop()
br = branching()

def parseline(command, filename):

    command_list=command
    print(command_list)
    global instruction
    if command_list[0]=='function':
        return fn.makefunction(command_list[1], command_list[2])
    
    if command_list[0]=='call':
        return fn.callfunction(command_list[1], command_list[2])
    
    if command_list[0]== 'return':
        return fn.returnfunction()

    if command_list[0]=='pop':
        return pp.pop(command_list[1], int(command_list[2]), filename)

    elif command_list[0]=='push':
        return pp.push(command_list[1], int(command_list[2]), filename)
    
    elif command_list[0]== 'label':
        return br.label(command_list[1])
    
    elif command_list[0] == 'goto':
        return br.goto(command_list[1])
    
    elif command_list[0] == 'if-goto':
        return br.if_goto(command_list[1])
    
    else:
        return eval(f'op._{command_list[0]}()')

def codewrite(contents_list, filename):
    instruction = ''
    for i in range(len(contents_list)):
        instruction+=f'''//{contents_list[i]}
'''
        instruction+= parseline(contents_list[i], filename) 
    return instruction