@17
D=A
@SP
A=M
M=D
@SP
M=M+1
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@eqtrue1
D;JEQ
@eqfalse1
0;JMP
(eqtrue1)
@SP
A=M
M=-1
@ENDEQ1
0;JMP
(eqfalse1)
@SP
A=M
M=0
(ENDEQ1)
@SP
M=M+1
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@eqtrue2
D;JEQ
@eqfalse2
0;JMP
(eqtrue2)
@SP
A=M
M=-1
@ENDEQ2
0;JMP
(eqfalse2)
@SP
A=M
M=0
(ENDEQ2)
@SP
M=M+1
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@eqtrue3
D;JEQ
@eqfalse3
0;JMP
(eqtrue3)
@SP
A=M
M=-1
@ENDEQ3
0;JMP
(eqfalse3)
@SP
A=M
M=0
(ENDEQ3)
@SP
M=M+1
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@lttrue1
D;JLT
@ltfalse1
0;JMP
(lttrue1)
@SP
A=M
M=-1
@ENDlt1
0;JMP
(ltfalse1)
@SP
A=M
M=0
(ENDlt1)
@SP
M=M+1
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@lttrue2
D;JLT
@ltfalse2
0;JMP
(lttrue2)
@SP
A=M
M=-1
@ENDlt2
0;JMP
(ltfalse2)
@SP
A=M
M=0
(ENDlt2)
@SP
M=M+1
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@lttrue3
D;JLT
@ltfalse3
0;JMP
(lttrue3)
@SP
A=M
M=-1
@ENDlt3
0;JMP
(ltfalse3)
@SP
A=M
M=0
(ENDlt3)
@SP
M=M+1
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@gttrue1
D;JGT
@gtfalse1
0;JMP
(gttrue1)
@SP
A=M
M=-1
@ENDgt1
0;JMP
(gtfalse1)
@SP
A=M
M=0
(ENDgt1)
@SP
M=M+1
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@gttrue2
D;JGT
@gtfalse2
0;JMP
(gttrue2)
@SP
A=M
M=-1
@ENDgt2
0;JMP
(gtfalse2)
@SP
A=M
M=0
(ENDgt2)
@SP
M=M+1
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@gttrue3
D;JGT
@gtfalse3
0;JMP
(gttrue3)
@SP
A=M
M=-1
@ENDgt3
0;JMP
(gtfalse3)
@SP
A=M
M=0
(ENDgt3)
@SP
M=M+1
@57
D=A
@SP
A=M
M=D
@SP
M=M+1
@31
D=A
@SP
A=M
M=D
@SP
M=M+1
@53
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
AM=M-1
D=M
@SP
AM=M-1
M=D+M
@SP
M=M+1
@112
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
AM=M-1
D=M
@SP
AM=M-1
M=M-D
@SP
M=M+1
@SP
A=M-1
M=-M
@SP
AM=M-1
D=M
@SP
AM=M-1
M=D&M
@SP
M=M+1
@82
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
AM=M-1
D=M
@SP
AM=M-1
M=D|M
@SP
M=M+1
@SP
A=M-1
M=!M
