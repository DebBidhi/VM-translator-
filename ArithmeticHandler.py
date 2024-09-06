class ArithmeticHandler:
    label_counters = {}

    def __init__(self, command):
        self.command = command
        self.operation = {
            "add": "@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nM=M+D\n@SP\nM=M+1\n",
            "sub": "@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nM=M-D\n@SP\nM=M+1\n",
            "neg": "@SP\nM=M-1\nA=M\nM=-M\n@SP\nM=M+1\n",
            "and": "@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nM=D&M\n@SP\nM=M+1\n",
            "or": "@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nM=D|M\n@SP\nM=M+1\n",
            "not": "@SP\nM=M-1\nA=M\nM=!M\n@SP\nM=M+1\n",
            "eq": self.generate_operation("EQUAL"),
            "lt": self.generate_operation("LESS_THAN"),
            "gt": self.generate_operation("GREATER_THAN")
        }
    def handle_command(self):
        out = self.operation[self.command]
        return out

    def generate_operation(self, operation):
        if operation=="EQUAL":
            comparasion="JEQ"
        elif operation=="LESS_THAN":
            comparasion="JLT"
        elif operation=="GREATER_THAN":
            comparasion="JGT"
        if operation not in self.label_counters:
            self.label_counters[operation] = 1
        else:
            self.label_counters[operation] += 1

        operation_label = f"{operation}.{self.label_counters[operation]}"
        end_label = f"END_{operation}.{self.label_counters[operation]}"

        operation_code = f"@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nD=M-D\n@{operation_label}\nD;{comparasion}\n" \
                         f"@SP\nA=M\nM=0\n@{end_label}\n0;JMP\n({operation_label})\n@SP\nA=M\nM=-1\n" \
                         f"({end_label})\n@SP\nM=M+1\n"
        return operation_code
