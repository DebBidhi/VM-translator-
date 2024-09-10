
//function Main.fibonacci 0
(Main.fibonacci)

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
//push constant 2
@2 
D=A 
@SP 
A=M 
M=D 
@SP 
M=M+1 

//lt
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=M-D
@LESS_THAN.1
D;JLT
@SP
A=M
M=0
@END_LESS_THAN.1
0;JMP
(LESS_THAN.1)
@SP
A=M
M=-1
(END_LESS_THAN.1)
@SP
M=M+1

//if-goto IF_TRUE
@SP 
AM=M-1 
D=M 
@Main.fibonacci$IF_TRUE 
D;JNE

//goto IF_FALSE
@Main.fibonacci$IF_FALSE
0;JMP 

//label IF_TRUE
(Main.fibonacci$IF_TRUE)

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

//label IF_FALSE
(Main.fibonacci$IF_FALSE)

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

//push constant 2
@2 
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

//call Main.fibonacci 1
@Main.fibonacci$ret.1
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@5
D=D-A
@1
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(Main.fibonacci$ret.1)

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

//call Main.fibonacci 1
@Main.fibonacci$ret.2
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@5
D=D-A
@1
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(Main.fibonacci$ret.2)

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

//function Sys.init 0
(Sys.init)

//push constant 4
@4 
D=A 
@SP 
A=M 
M=D 
@SP 
M=M+1 

//call Main.fibonacci 1
@Main.fibonacci$ret.3
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@5
D=D-A
@1
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(Main.fibonacci$ret.3)

//label WHILE
(Sys.init$WHILE)

//goto WHILE
@Sys.init$WHILE
0;JMP 
