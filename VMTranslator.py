import sys
import os
from PushPopHandler import PushPopHandler
from ArithmeticHandler import ArithmeticHandler
from BranchingHandler import BranchingHandler
from FunctionHandler import FunctionHandler



class VmTranslator:
    def __init__(self,vmFile_name):
        self.base_name = vmFile_name.rsplit('.', 1)[0] 
        self.cmd = []
        self.list_of_translated_commands=[]
        self.function_name=""
        with open(vmFile_name, "r") as f:
            for line in f:
                if line.startswith("//") or line.startswith("\n"):
                    continue
                else:
                    self.cmd.append(line.split("//")[0].strip())

    def Translate(self)->list:
        for singlecommand in self.cmd:
            if singlecommand.startswith(("push", "pop")):
                translation = PushPopHandler(singlecommand, self.base_name).handle_command()
                """**self.base_name is used for static variable naming(eg. fibonaciSeries.5) in static segment"""
                self.list_of_translated_commands.append("\n//" + singlecommand + "\n" + str(translation))

            elif singlecommand.startswith(("add", "sub", "neg", "eq", "gt", "lt", "and", "or", "not")):
                translation = ArithmeticHandler(singlecommand).handle_command()
                self.list_of_translated_commands.append("\n//" + singlecommand + "\n" + str(translation))

            elif singlecommand.startswith(("label", "goto", "if-goto")):
                translation = BranchingHandler(singlecommand,self.base_name,self.function_name).handle_command()
                self.list_of_translated_commands.append("\n//" + singlecommand + "\n" + str(translation))

            elif singlecommand.startswith(("function", "call", "return")):
                if singlecommand.startswith("function"):
                    function_name = singlecommand.split()[1]
                    self.function_name=function_name
                
                translation = FunctionHandler(singlecommand, self.base_name).handle_command()
                self.list_of_translated_commands.append("\n//" + singlecommand + "\n" + str(translation))

            else:
                print("Invalid command:", singlecommand)
                sys.exit(1) 

        return self.list_of_translated_commands
            
        

if __name__ == "__main__":

    all_translations = []
    vmFiles = []
    #check if the argumet is a .vm file or a directory
    input=sys.argv[1]
    if input.endswith(".vm"):
        vmFiles.append(input)
        output_file_path=sys.argv[1].rsplit(".",1)[0]+".asm" #if only one file is given then the name of the file is as of vm file
    else:
        for i in os.listdir(input):
            if i.endswith(".vm"):
                vmFiles.append(input+"/"+i)
        #output_file_path is inside the directory 
        output_file_path= os.path.join(input,f"{input}.asm")


    #if Sys.vm is present then it is added to the list of vm files/ #bootstrap code()
    all_translations.append("@256\nD=A\n@SP\nM=D\n")
    for filePath in vmFiles:
        if filePath.endswith('Sys.vm'):
            print(f"Yes, {filePath} is present")
            all_translations.append(FunctionHandler("call Sys.init 0", "Sys").handle_command())


    if len(vmFiles) == 0:
        print("No vm files found")
    else:
        for vmFile in vmFiles:
            vmTranslator = VmTranslator(vmFile)
            translation_list=vmTranslator.Translate() #gives back a list of translated commands
            all_translations.extend(translation_list)

    with open(output_file_path, "w") as f:
        for line in all_translations:
            f.write(f"{line}") 
    print("Translation completed successfully")



        

    
        