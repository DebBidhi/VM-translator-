class FunctionHandler:
    label_counter = 1  
    def __init__(self, command, base_name):
        self.command = command
        self.base_name = base_name
        # FunctionHandler.label_counter += 1  
        self.current_label_counter = FunctionHandler.label_counter  # Store the current label counter for this instance

    def handle_command(self):
        if self.command.startswith("function"):
            return self.handle_function()
        elif self.command.startswith("call"):
            return self.handle_call()
        elif self.command.startswith("return"):
            return self.handle_return()

    def handle_function(self):
        function_name = self.command.split()[1]
        local_variables = self.command.split()[2]
        function_code = f"({function_name})\n"
        # Initialization local variables to 0
        for i in range(int(local_variables)):
            function_code += "@SP\nA=M\nM=0\n@SP\nM=M+1\n"
        return function_code

    def handle_return(self):
        return_code = f"@LCL\nD=M\n@R13\nM=D\n@5\nA=D-A\nD=M\n@R14\nM=D\n@SP\nAM=M-1\nD=M\n@ARG\nA=M\nM=D\n@ARG\nD=M+1\n@SP\nM=D\n"
        # returning the previous state of the caller
        return_code += "@R13\nAM=M-1\nD=M\n@THAT\nM=D\n@R13\nAM=M-1\nD=M\n@THIS\nM=D\n@R13\nAM=M-1\nD=M\n@ARG\nM=D\n@R13\nAM=M-1\nD=M\n@LCL\nM=D\n"
        return_code += "@R14\nA=M\n0;JMP\n"
        return return_code

    def handle_call(self):
        FunctionHandler.label_counter += 1 
        function_name = self.command.split()[1]
        arguments = self.command.split()[2]
        return_code = f"@{function_name}$ret.{self.current_label_counter}\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
        return_code += "@LCL\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
        return_code += "@ARG\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
        return_code += "@THIS\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
        return_code += "@THAT\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
        return_code += f"@SP\nD=M\n@5\nD=D-A\n@{arguments}\nD=D-A\n@ARG\nM=D\n"
        return_code += "@SP\nD=M\n@LCL\nM=D\n"
        return_code += f"@{function_name}\n0;JMP\n"
        return_code += f"({function_name}$ret.{self.current_label_counter})\n"
        return return_code

