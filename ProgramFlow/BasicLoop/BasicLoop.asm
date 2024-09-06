
//push constant 0
@0 
D=A 
@SP 
A=M 
M=D 
@SP 
M=M+1 

//pop local 0
@0 
D=A 
@1 
D=D+M 
@R13 
M=D 
@SP 
M=M-1 
A=M 
D=M 
@R13 
A=M 
M=D 

//label LOOP_START
($LOOP_START)

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

//pop local 0
@0 
D=A 
@1 
D=D+M 
@R13 
M=D 
@SP 
M=M-1 
A=M 
D=M 
@R13 
A=M 
M=D 

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

//push constant 1
@1 
D=A 
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

//pop argument 0
@0 
D=A 
@2 
D=D+M 
@R13 
M=D 
@SP 
M=M-1 
A=M 
D=M 
@R13 
A=M 
M=D 

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

//if-goto LOOP_START
@SP 
AM=M-1 
D=M 
@$LOOP_START 
D;JNE

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
