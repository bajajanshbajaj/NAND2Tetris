@256
D=A
@SP
M=D
//['push', 'argument', '1']
@1
D=A
@ARG
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
//['pop', 'pointer', '1']
@SP
AM=M-1
D=M
@R4
M=D
//['push', 'constant', '0']
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
//['pop', 'that', '0']
@THAT
D=M
@0
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
//['push', 'constant', '1']
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
//['pop', 'that', '1']
@THAT
D=M
@1
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
//['push', 'argument', '0']
@0
D=A
@ARG
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
//['push', 'constant', '2']
@2
D=A
@SP
A=M
M=D
@SP
M=M+1
//['sub']
@SP
AM=M-1
D=M
@SP
AM=M-1
M=M-D
@SP
M=M+1
//['pop', 'argument', '0']
@ARG
D=M
@0
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
//['label', 'LOOP']
(LOOP)
//['push', 'argument', '0']
@0
D=A
@ARG
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
//['if-goto', 'COMPUTE_ELEMENT']
@SP
AM=M-1
D=M
@COMPUTE_ELEMENT   
D;JNE
//['goto', 'END']
@END
0;JMP
//['label', 'COMPUTE_ELEMENT']
(COMPUTE_ELEMENT)
//['push', 'that', '0']
@0
D=A
@THAT
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
//['push', 'that', '1']
@1
D=A
@THAT
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
//['add']
@SP
AM=M-1
D=M
@SP
AM=M-1
M=D+M
@SP
M=M+1
//['pop', 'that', '2']
@THAT
D=M
@2
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
//['push', 'pointer', '1']
@R4
D=M
@SP
A=M
M=D
@SP
M=M+1
//['push', 'constant', '1']
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
//['add']
@SP
AM=M-1
D=M
@SP
AM=M-1
M=D+M
@SP
M=M+1
//['pop', 'pointer', '1']
@SP
AM=M-1
D=M
@R4
M=D
//['push', 'argument', '0']
@0
D=A
@ARG
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
//['push', 'constant', '1']
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
//['sub']
@SP
AM=M-1
D=M
@SP
AM=M-1
M=M-D
@SP
M=M+1
//['pop', 'argument', '0']
@ARG
D=M
@0
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
//['goto', 'LOOP']
@LOOP
0;JMP
//['label', 'END']
(END)
