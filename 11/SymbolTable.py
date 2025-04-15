class SymbolTable:
    def __init__(self):
        self.classTable = {}
        self.subroutineTable= {}

        self.countTable= {'static': 0, 'this': 0 , 'argument': 0 ,'local': 0 }
        self.classTypes= ['static', 'this']
        self.subroutineTypes = ['argument','local']
        #maybe seperate the dictionary and use its keys instead of the seperate list ??

        self.dataTypes = ['int', 'char', 'boolean']
        #ADD TYPE CHECKS WHILE DECLARATION OR CALLS ??????????????

        # self.className= ''
        # self.subroutineName = ''


    def reset(self):
        self.subroutineTable.clear()
        self.countTable['argument'] = 0
        self.countTable['local'] = 0


    def define(self, v_name, v_type , v_kind):

        # name : [type, kind, hash]
        if v_kind in self.classTypes:
            self.classTable[v_name] = [v_type, v_kind.replace("field","this"), self.countTable[v_kind]]
            self.countTable[v_kind] += 1
        elif v_kind.replace('var', 'local') in self.subroutineTypes:
            self.subroutineTable[v_name] = [v_type, v_kind.replace('var', 'local'), self.countTable[v_kind]]
            self.countTable[v_kind] += 1
        else:
            #err?
            pass

    def varCount(self, v_kind):
        return self.countTable[v_kind]


    def _Of(self, v_name, num):
        if v_name in self.subroutineTable.keys(): # prioritise subroutine over class
            return self.subroutineTable[v_name][num]
        elif v_name in self.classTable.keys():
            return self.classTable[v_name][num]
        else: 
            #error?
            pass

    def typeOf(self, v_name):
        return self._Of(v_name, 0)

    def kindOf(self, v_name):
        return self._Of(v_name, 1)

    def indexOf(self, v_name):
        return self._Of(v_name, 2)

