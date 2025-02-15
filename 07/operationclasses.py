class operations_class():
    def __init__(self):
        pass
        self.i=0
        self.j=0
        self.k=0
        self.l=0
        self.m=0
        self.n=0
        self.o=0
        self.p=0
        self.q=0
    def _add(self):
        self.i=self.i+1
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
        self.j=self.j+1
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
        self.k=self.k+1
        return '''@SP
A=M-1
M=-M
'''

    def _eq(self):
        self.l=self.l+1
        return f'''@SP
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@eqtrue{self.l}
D;JEQ
@eqfalse{self.l}
0;JMP
(eqtrue{self.l})
@SP
A=M
M=-1
@ENDEQ{self.l}
0;JMP
(eqfalse{self.l})
@SP
A=M
M=0
(ENDEQ{self.l})
@SP
M=M+1
'''

    def _gt(self):
        self.m=self.m+1
        return f'''@SP
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@gttrue{self.m}
D;JGT
@gtfalse{self.m}
0;JMP
(gttrue{self.m})
@SP
A=M
M=-1
@ENDgt{self.m}
0;JMP
(gtfalse{self.m})
@SP
A=M
M=0
(ENDgt{self.m})
@SP
M=M+1
'''

    def _lt(self):
        self.n+=1
        return f'''@SP
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@lttrue{self.n}
D;JLT
@ltfalse{self.n}
0;JMP
(lttrue{self.n})
@SP
A=M
M=-1
@ENDlt{self.n}
0;JMP
(ltfalse{self.n})
@SP
A=M
M=0
(ENDlt{self.n})
@SP
M=M+1
'''
    def _and(self):
        self.o+=1
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
        self.p+=1
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
        self.q+=1
        return '''@SP
A=M-1
M=!M
'''

