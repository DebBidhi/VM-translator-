
class BranchingHandler:
    def __init__(self, command,base_name,function_name):
        self.command = command
        self.base_name=base_name
        self.function_name=function_name


    def handle_command(self):
        out=self.handle_command()
        return out

    def handle_command(self):
        if self.command.startswith("label"):
            self.label = self.command.split()[1]
            return f"({self.function_name}${self.label})\n"
        elif self.command.startswith("goto"):
            self.label = self.command.split()[1]
            return f"@{self.function_name}${self.label}\n0;JMP \n"
        elif self.command.startswith("if-goto"):
            self.label = self.command.split()[1]
            return f"@SP \nAM=M-1 \nD=M \n@{self.function_name}${self.label} \nD;JNE\n"
        else:
            print("Invalid command. Please check again")
            
