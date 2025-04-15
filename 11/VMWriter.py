class VMWriter:
    def __init__(self, VMpath):
        VMfile= open(VMpath, 'w')
        VMfile.close()
        self.VMfile= open(VMpath, 'a')
        pass

    def write(self, stuff):
        self.VMfile.write(stuff)
        #print(stuff, sep= '')

    def writePush(self, segment, index): #segment (CONSTANT,ARGUMENT, LOCAL, STATIC, THIS, THAT, POINTER, TEMP)
        self.write(f'push {segment} {index}\n')
        pass

    def writePop(self, segment, index):
        self.write(f'pop {segment} {index}\n')
        pass

    def writeArithmetic(self, command): #(ADD, SUB, NEG, EQ, GT, L T, AND, OR, NOT)
        self.write(f'{command}\n')
        pass

    def writeLabel(self, label):
        self.write(f'label {label}\n')
        pass

    def writeGoto(self, label):
        self.write(f'goto {label}\n')
        pass

    def writeIf(self, label):
        self.write(f'if-goto {label}\n')
        pass

    def writeCall(self, name, nArgs):
        self.write(f'call {name} {nArgs}\n')
        pass

    def writeFunction(self, name, nVars):
        self.write(f'function {name} {nVars}\n')        
        pass

    def writeReturn(self):
        self.write(f'return\n')
        pass

    def writeComment(self, comment):
        #self.write(f'\n//{comment}\n\n')
        pass

    def close(self):
        self.VMfile.close()
        pass