
//function SimpleFunction.test 2
(SimpleFunction.test)
@SP
A=M
M=0
@SP
M=M+1
@SP
A=M
M=0
@SP
M=M+1

//push local 0
@0 
D=A 
@1 
A=M 
A=D+A 
D=M 
@SP 
A=M 
M=D 
@SP 
M=M+1 

//push local 1
@1 
D=A 
@1 
A=M 
A=D+A 
D=M 
@SP 
A=M 
M=D 
@SP 
M=M+1 

//add
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
M=M+D
@SP
M=M+1

//not
@SP
M=M-1
A=M
M=!M
@SP
M=M+1

//push argument 0
@0 
D=A 
@2 
A=M 
A=D+A 
D=M 
@SP 
A=M 
M=D 
@SP 
M=M+1 

//add
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
M=M+D
@SP
M=M+1

//push argument 1
@1 
D=A 
@2 
A=M 
A=D+A 
D=M 
@SP 
A=M 
M=D 
@SP 
M=M+1 

//sub
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
M=M-D
@SP
M=M+1

//return
@LCL
D=M
@R13
M=D
@5
A=D-A
D=M
@R14
M=D
@SP
AM=M-1
D=M
@ARG
A=M
M=D
@ARG
D=M+1
@SP
M=D
@R13
AM=M-1
D=M
@THAT
M=D
@R13
AM=M-1
D=M
@THIS
M=D
@R13
AM=M-1
D=M
@ARG
M=D
@R13
AM=M-1
D=M
@LCL
M=D
@R14
A=M
0;JMP
