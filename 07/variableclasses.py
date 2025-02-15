# class 1 : stack local arguement this that
# class 2 : temp , pointer 
# class 3 : static

class vartype_with_predefined_variable_names :
    
    def __init__(self,  NAME):
        global instruction
        self.name= NAME
        # instruction += f'''@{START}\nD=A\n@{NAME}\nM=D\n'''


# want temp 1 to point to R5 and so on -> OBJECT.name shall return Rx
#object's name shall still remain the same as the vm code syntax 
#object.name shall still point to some variable which is already  predefined in the assmebly instructions 
# r3 and 4 are used for the pointer which is the same as this and that 
# temp is mapped from r5 to 12
#hence r13 14 15 are available for our use 

# icnlude temp, pointer 
class vartype_with_new_names_mapped_R3_to_R15 :
    def __init__(self,  RSTART):
        self.start= RSTART
        self.name = 'R'+ str(RSTART)
    def locate(self, relative_location):
        return 'R' + str(self.start+ relative_location)