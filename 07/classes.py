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
