class initialise():
    def __init__(self):
        pass

    def start(self):
        return '''// START
@256
D=A
@SP
M=D
'''
    
    def end(self):
        return '''// END
@endofprogram
(endofprogram)
0;JMP
'''
    
    def callsysinit(self):
        return '''// call Sys.init
@Sys.init$RETURN.0
D=A
@SP
A=M
M=D
@LCL
D=M
@SP
AM=M+1
M=D
@ARG
D=M
@SP
AM=M+1
M=D
@THIS
D=M
@SP
AM=M+1
M=D
@THAT
D=M
@SP
AM=M+1
M=D
@SP
MD=M+1
@ARG
M=D
@0
D=A
@ARG
M=M-D
@5
D=A
@ARG
M=M-D
@SP
D=M
@LCL
M=D
@Sys.init
0;JMP
(Sys.init$RETURN.0)
'''


variable_dict = {
    'stack': 'SP',
    'local': 'LCL',
    'argument': 'ARG',
    'this': 'THIS',
    'that': 'THAT',
    'pointer': 3,
    'temp': 5
}

class pushpop():
    def __init__(self):
        pass

    def pop(self, var, num, filename):
        if var=='pointer' or var == 'temp':
            return f'''@SP
AM=M-1
D=M
@{f'R{variable_dict[var]+num}'}
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
            return f'''@{variable_dict[var]}
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

    def push(self, var, num, filename):
        if var=='pointer' or var == 'temp':
            return f'''@{f'R{variable_dict[var]+num}'}
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
@{variable_dict[var]}
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
'''


class operations_class():

    def __init__(self):
        pass
        self.eqcounter=0
        self.gtcounter=0
        self.ltcounter=0

    def _add(self):
        return '''@SP
AM=M-1
D=M
@SP
AM=M-1
M=D+M
@SP
M=M+1
'''

    def _sub(self):
        return '''@SP
AM=M-1
D=M
@SP
AM=M-1
M=M-D
@SP
M=M+1
'''

    def _neg(self):
        return '''@SP
A=M-1
M=-M
'''

    def _eq(self):
        self.eqcounter=self.eqcounter+1
        return f'''@SP
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@eqtrue{self.eqcounter}
D;JEQ
@eqfalse{self.eqcounter}
0;JMP
(eqtrue{self.eqcounter})
@SP
A=M
M=-1
@ENDEQ{self.eqcounter}
0;JMP
(eqfalse{self.eqcounter})
@SP
A=M
M=0
(ENDEQ{self.eqcounter})
@SP
M=M+1
'''

    def _gt(self):
        self.gtcounter=self.gtcounter+1
        return f'''@SP
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@gttrue{self.gtcounter}
D;JGT
@gtfalse{self.gtcounter}
0;JMP
(gttrue{self.gtcounter})
@SP
A=M
M=-1
@ENDgt{self.gtcounter}
0;JMP
(gtfalse{self.gtcounter})
@SP
A=M
M=0
(ENDgt{self.gtcounter})
@SP
M=M+1
'''

    def _lt(self):
        self.ltcounter+=1
        return f'''@SP
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@lttrue{self.ltcounter}
D;JLT
@ltfalse{self.ltcounter}
0;JMP
(lttrue{self.ltcounter})
@SP
A=M
M=-1
@ENDlt{self.ltcounter}
0;JMP
(ltfalse{self.ltcounter})
@SP
A=M
M=0
(ENDlt{self.ltcounter})
@SP
M=M+1
'''
    
    def _and(self):
        return '''@SP
AM=M-1
D=M
@SP
AM=M-1
M=D&M
@SP
M=M+1
'''

    def _or(self):
        return '''@SP
AM=M-1
D=M
@SP
AM=M-1
M=D|M
@SP
M=M+1
'''

    def _not(self):
        return '''@SP
A=M-1
M=!M
'''


class branching():
    def __init__(self):
        pass
    def label(self, where):
        return f'''({where})
'''
    def goto(self, where):
        return f'''@{where}
0;JMP
'''
    def if_goto(self, where):
        return f'''@SP
AM=M-1
D=M
@{where}   
D;JNE
'''


class functions_class():
    def __init__(self):
        self.i = 0 
        self.j = 0
    def makefunction(self, name, locals):
        self.j += 1

        return f'''({name})
@{locals}
D=A
({name}$LOCALZEROLOOP.{self.j})
@{name}$LOCALZEROLOOPEND.{self.j}
D;JEQ
@SP
A=M
M=0
@SP
M=M+1
D=D-1
@{name}$LOCALZEROLOOP.{self.j}
0;JMP
({name}$LOCALZEROLOOPEND.{self.j})
'''

    def callfunction(self, name, nargs):
        self.i += 1
    
        return f'''@{name}$RETURN.{self.i}
D=A
@SP
A=M
M=D
@LCL
D=M
@SP
AM=M+1
M=D
@ARG
D=M
@SP
AM=M+1
M=D
@THIS
D=M
@SP
AM=M+1
M=D
@THAT
D=M
@SP
AM=M+1
M=D
@SP
MD=M+1
@ARG
M=D
@{nargs}
D=A
@ARG
M=M-D
@5
D=A
@ARG
M=M-D
@SP
D=M
@LCL
M=D
@{name}
0;JMP
({name}$RETURN.{self.i})
'''

    def returnfunction(self):

        return f'''@LCL
D=M
@$ENDFRAME
M=D
@5
D=D-A
A=D
D=M
@$RETADDR
M=D
@SP
AM=M-1
D=M
@ARG
A=M
M=D
@ARG
D=M
@SP
M=D+1
@$ENDFRAME
D=M-1
A=D
D=M
@THAT
M=D
@$ENDFRAME
D=M-1
D=D-1
A=D
D=M
@THIS
M=D
@$ENDFRAME
D=M-1
D=D-1
D=D-1
A=D
D=M
@ARG
M=D
@$ENDFRAME
D=M-1
D=D-1
D=D-1
D=D-1
A=D
D=M
@LCL
M=D
@$RETADDR
A=M
0;JMP
''' 