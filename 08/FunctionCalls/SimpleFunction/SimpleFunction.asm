@256
D=A
@SP
M=D
//['function', 'SimpleFunction.test', '2']
(SimpleFunction.test)
@2
D=A
(SimpleFunction.test$LOCALZEROLOOP.1)
@SimpleFunction.test$LOCALZEROLOOPEND.1
D;JEQ
@SP
A=M
M=0
@SP
M=M+1
D=D-1
@SimpleFunction.test$LOCALZEROLOOP.1
0;JMP
(SimpleFunction.test$LOCALZEROLOOPEND.1)
//['push', 'local', '0']
@0
D=A
@LCL
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
//['push', 'local', '1']
@1
D=A
@LCL
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
//['not']
@SP
A=M-1
M=!M
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
//['add']
@SP
AM=M-1
D=M
@SP
AM=M-1
M=D+M
@SP
M=M+1
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
//['sub']
@SP
AM=M-1
D=M
@SP
AM=M-1
M=M-D
@SP
M=M+1
//['return']
@LCL
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
