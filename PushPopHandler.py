class PushPopHandler:
    def __init__(self, command, base_name):
        self.command=command
        self.base_name=base_name.split("/")[-1].split(".")[0]
        
        self.push_actions = {
            "local": self.push_common4,
            "argument": self.push_common4,
            "this": self.push_common4,
            "that": self.push_common4,
            "constant": self.push_constant,
            "static": self.push_static,
            "temp": self.push_temp,
            "pointer": self.push_pointer,
        }

        self.pop_actions = {
            "local": self.pop_common4,
            "argument": self.pop_common4,
            "this": self.pop_common4,
            "that": self.pop_common4,
            "constant": self.pop_constant,
            "static": self.pop_static,
            "temp": self.pop_temp,
            "pointer": self.pop_pointer,
        }

        self.segment_memory_name={
            "local":"1",
            "argument":"2",
            "this":"3",
            "that":"4"
        }

        
    def handle_command(self):
        action_type, segment, value = self.command.split()[0:3]
        self.segment=segment
        if action_type == "push":
            out=self.execute_push_action(segment, value)
        elif action_type == "pop":
            out=self.execute_pop_action(segment, value)
        else:
            raise ValueError("Invalid command type. Please use 'push' or 'pop'")
            
        return out
    

    def execute_push_action(self, segment, value):
        if segment in self.push_actions:
            return self.push_actions[segment](value)
        else:
            raise ValueError("Invalid push command. Please check again")

    def execute_pop_action(self, segment, value):
        if segment in self.pop_actions:
            return self.pop_actions[segment](value)
        else:
            raise ValueError("Invalid pop command. Please check again")

    # Push methods
    def push_common4(self, value):
        ##4 all methods..condition for memory overflow can be done also like if value is over 256  the overflowing etc..
        segment_pointer=self.segment_memory_name[self.segment]
        out=f"@{value} \nD=A \n@{segment_pointer} \nA=M \nA=D+A \nD=M \n@SP \nA=M \nM=D \n@SP \nM=M+1 \n"

        return out

    def push_constant(self, value):
        out = f"@{value} \nD=A \n@SP \nA=M \nM=D \n@SP \nM=M+1 \n"
        return out
    
    def push_static(self, value):
        out = f"@{self.base_name}.{value} \nD=M \n@SP \nA=M \nM=D \n@SP \nM=M+1 \n"
        return out
    
    def push_temp(self, value):
        out = f"@{int(value) + 5} \nD=M \n@SP \nA=M \nM=D \n@SP \nM=M+1 \n"
        return out
    
    def push_pointer(self, value):
        value = int(value)
        if value == 0:
            out = "@THIS \nD=M \n@SP \nA=M \nM=D \n@SP \nM=M+1 \n"
            return out
        elif value == 1:

            out = "@THAT \nD=M \n@SP \nA=M \nM=D \n@SP \nM=M+1 \n"
            return out
        else:

            print("push pointer takes 0 or 1")
            raise ValueError("Invalid push command. Please check again")

    # Pop methods
    def pop_common4(self, value):
        segment_pointer=self.segment_memory_name[self.segment]
        out=f"@{value} \nD=A \n@{segment_pointer} \nD=D+M \n@R13 \nM=D \n@SP \nM=M-1 \nA=M \nD=M \n@R13 \nA=M \nM=D \n"
        return out
    def pop_constant(self, value):
        raise ValueError("pop constant does not exist. Please check VM code")
    
    def pop_static(self, value):
        out = f"@SP \nM=M-1 \nA=M \nD=M \n@{self.base_name}.{value} \nM=D \n"
        return  out
    
    def pop_temp(self, value):
        out = f"@{value} \nD=A \n@5 \nD=D+A \n@R13 \nM=D \n@SP \nM=M-1 \nA=M \nD=M \n@R13 \nA=M \nM=D \n"
        return  out
    
    def pop_pointer(self, value):
        value = int(value)
        if value == 0:
            out = "@SP \nM=M-1 \nA=M \nD=M \n@THIS \nM=D \n"
            return  out
        elif value == 1:
            out = "@SP \nM=M-1 \nA=M \nD=M \n@THAT \nM=D \n"
            return  out
        else:
            print("pop pointer takes 0 or 1")
            raise ValueError("Invalid pop command. Please check again")

