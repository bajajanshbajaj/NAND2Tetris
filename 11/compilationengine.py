from tokeniser import tokeniser
import logging 
from SymbolTable import SymbolTable
from VMWriter import VMWriter

#token is advanced to next token before calling another function , this gives token's access to both current method and the next method
class CompileEngine():
    
    def __init__(self,  filestream, logpath, VMpath):

        self.tok = tokeniser(filestream)
        self.ST= SymbolTable()
        self.VMW = VMWriter(VMpath)

        self.classvarsList = ['static', 'field']
        self.subroutineDecList= ['constructor', 'function', 'method']
        self.typeList= ['int', 'char', 'boolean']
        self.opList = ['+', '-', '*', '/', '&', '|', '<', '>', '=']
        self.unaryOpList = ['-', '~']
        self.unaryDict = {
                                '-': 'neg',
                                '~': 'not'

        }

        self.keywordConstantList = ['true', 'false', 'null', 'this'] #maybe change toktypeCURRENT to IF(token in keywordconstantlist) ? add errhandler?
        self.opLookup = {
                                '+': 'add',
                                '-': 'sub',
                                'neg': 'neg',
                                '=': 'eq',
                                '>': 'gt',
                                '<': 'lt',
                                '&': 'and',
                                '|': 'or',
                                '~': 'not',
                                '/': 'call Math.divide 2',
                                '*': 'call Math.multiply 2'
                            }
        

        
        logging.basicConfig(
            filename=logpath,  
            level=logging.DEBUG,  
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  datefmt='%Y-%m-%d %H:%M:%S'  
        )

        self.ifcount = -1
        self.labelcount = 0
        self.whilecount = 0  

        self.numberOfFieldVars = 0

        self.compileClass()

        self.VMW.close()

        

    def compileClass(self): #DONE
        
        logging.debug('compileClass') 

        self.VMW.writeComment('compileClass')
 
        # 'class' className '{' classVarDec* subroutineDec* '}'
        if self.tok.tokentypecurrent() == 'keyword': 
            self.tok.advance()
            if self.tok.tokentypecurrent() =='identifier':
                self.className = self.tok.current_token()
                self.tok.advance()
                if self.tok.current_token() == '{':
                    self.tok.advance()
                else:self.tok.errorhandler()
            else:self.tok.errorhandler()
        else:self.tok.errorhandler()

        while True:
            if self.tok.current_token() in self.classvarsList:
                self.compileClassVarDec()
            elif self.tok.current_token() in self.subroutineDecList:
                self.compileSubroutine()
            elif self.tok.current_token() == '}':
                break
            else:self.tok.errorhandler()

        pass

    # ('static' I 'field' ) type varName (,' varName)*
    
    def compileClassVarDec(self):# DONE
        logging.debug('compileClassVarDec')
        self.VMW.writeComment('compileClassVarDec')

        if self.tok.current_token() in self.classvarsList:
            _kind = self.tok.current_token()
             
            self.tok.advance()
            _type = self.tok.current_token()
            self.tok.advance()
            while True:
                if self.tok.tokentypecurrent() == 'identifier':
                    if _kind == 'field':
                        self.numberOfFieldVars +=1 

                    self.ST.define(v_name= self.tok.current_token() , v_kind=_kind.replace('field', 'this'), v_type=_type)
                    print( self.tok.current_token() , _kind.replace('field', 'this'), _type)
                    self.tok.advance()
                    if self.tok.current_token() == ',':
                        self.tok.advance()
                    else: break
            if self.tok.current_token() == ';':
                self.tok.advance()

        pass

    def compileSubroutine(self): # DONE #NVARS COULDNT BE DEFINED -> WILL BE DONE AFTER VARIABLE DECLARATION IS COMPLETED, (SELF.CURRENTSUBROUTINENAME)
        logging.debug("compileSubroutine")
        self.VMW.writeComment('compileSubroutine')
        
        # ('constructor' I 'function' I 'method') ('void' I type) subroutineName '(' parameterList subroutineBody
        if self.tok.current_token() in self.subroutineDecList :

            self.ST.reset()
            #self.ifcount = -1
            self.subroutineTypeCurrent = self.tok.current_token()
            self.tok.advance()
            if self.subroutineTypeCurrent == 'method':    
                self.ST.define(v_kind='argument',v_name='this',v_type=self.className)
            if True:# self.tok.current_token() == 'void' or self.tok.tokentypecurrent() == ?
                # subroutine_return_type = self.tok.current_token()
                self.tok.advance()

                if self.tok.tokentypecurrent() == 'identifier':
                    self.currentSubroutineName = self.tok.current_token()
                    # subroutine_name = self.tok.current_token()
                    
                    if self.tok.advance() == '(':
                        #
                        self.tok.advance()
                        logging.debug('current token = "'+(self.tok.current_token())+'"')
                        self.compileParameterList()
                        if self.tok.current_token()== ")":
                            self.tok.advance()
                            self.compileSubroutineBody()
                            # print('x')
                        else:
                            # print('z')
                            self.tok.errorhandler()
                        # print('y')
                    else:self.tok.errorhandler()
                else:self.tok.errorhandler()
            else:self.tok.errorhandler() 
        pass


    def compileParameterList(self): #DONE
        self.VMW.writeComment('compileParameterList')
        
        # ( (type varName) (' , ' type varName)*)? 
        
        logging.debug('compileparameterlist')
        
        if self.tok.current_token() != ')':
            while True:
                logging.debug(self.tok.current_token())
                
                if True: #self.tok.current_token() in self.typeList:
                    _type= self.tok.current_token()
                    self.tok.advance()
                    if self.tok.tokentypecurrent() == "identifier":
                        logging.debug(self.tok.current_token())
                        self.ST.define(v_name=self.tok.current_token(), v_kind= 'argument', v_type=_type)
                        self.tok.advance()
                    else:self.tok.errorhandler()
                if self.tok.current_token() == ',':
                    logging.debug(self.tok.current_token())
                    
                    self.tok.advance()
                else:
                    logging.debug('exiting')
                    logging.debug(self.tok.current_token())
                    break
        else : 
            logging.debug('empty param list')

        pass

    def compileSubroutineBody(self): #DONE
        self.VMW.writeComment('compileSubroutineBody')
        logging.debug('compilesubroutinebody')
        _nvarstotal= 0
        if self.tok.current_token() == '{':
            # if self.subroutineTypeCurrent == 'method':    
            #     self.ST.define(v_kind='argument',v_name='this',v_type=self.className)
            self.tok.advance()
            while True:
                if self.tok.current_token()== 'var':
                    _nvarstotal += self.compileVarDec()
                else:break

            self.VMW.writeFunction(name= self.className + '.' + self.currentSubroutineName , nVars= _nvarstotal )

            if self.subroutineTypeCurrent == 'constructor':
                self.VMW.writePush(segment= 'constant', index= self.numberOfFieldVars)
                self.VMW.writeCall(name = 'Memory.alloc', nArgs= 1)
                self.VMW.writePop(segment= 'pointer', index = 0)
            if self.subroutineTypeCurrent == 'method':    
                #self.ST.define(v_kind='argument',v_name='this',v_type=self.className)
                self.VMW.writePush(segment= 'argument', index = 0)
                self.VMW.writePop(segment= 'pointer', index = 0)
            




            self.compileStatements()

            if self.tok.current_token() == '}':
                self.tok.advance()
            else:self.tok.errorhandler()

        else:self.tok.errorhandler()
        
        pass

    # varDec: 'var' type varName (' , ' varName)* ' ; '

    def compileVarDec(self): #DONE
        self.VMW.writeComment('compileVarDec')
        logging.debug('compilevardec')
        _nVars = 0
        if self.tok.current_token() == 'var':
            self.tok.advance()
            _type = self.tok.current_token()
            self.tok.advance()
            while True:
                _nVars+=1
                if self.tok.tokentypecurrent() == 'identifier':
                    self.ST.define(v_kind='local',v_name=self.tok.current_token(),v_type=_type)
                    self.tok.advance()
                    if self.tok.current_token() == ',':
                        self.tok.advance()
                    else: break
            if self.tok.current_token() == ';':
                
                self.tok.advance()
            

        
        return _nVars

    def compileStatements(self): #DONE
        self.VMW.writeComment('compileStatements')
        logging.debug("compileStatements")
        while True:
            if self.tok.current_token() == 'let':
                self.compileLet()
            elif self.tok.current_token() == 'if':
                self.compileIf()
            elif self.tok.current_token() == 'while':
                self.compileWhile()
            elif self.tok.current_token() == 'do':
                self.compileDo()
            elif self.tok.current_token() == 'return':
                self.compileReturn()
            else: 
                break

        
        self.VMW.writeComment('compileLetEND')
        pass

    def compileLet(self): #'let' varName t' expression 'l ')? '=' expression ' #DONE
        self.VMW.writeComment('compileLet')
        logging.debug('let')
        #'let'      
        self.tok.advance()
        #varname
        if self.tok.tokentypecurrent() == "identifier":
            _var_name = self.tok.current_token() 
            self.tok.advance()

            #current variable is some array[index]
            if self.tok.current_token() == '[':
                self.VMW.writePush(segment=self.ST.kindOf(_var_name),  index= self.ST.indexOf(_var_name))
                self.tok.advance()
                self.compileExpression()
                if self.tok.current_token() == ']':
                    self.VMW.writeArithmetic('add')
                    self.tok.advance()
                    self.tok.advance() #PASSES '=' 
                    self.compileExpression()
                    if self.tok.current_token() == ';':
                        self.VMW.writePop(segment= 'temp', index = 0)
                        self.VMW.writePop(segment= 'pointer', index= 1)
                        self.VMW.writePush(segment= 'temp', index = 0)
                        self.VMW.writePop(segment= 'that', index= 0)

                        self.tok.advance()
                    else:self.tok.errorhandler()
                else:self.tok.errorhandler()

            
            elif self.tok.current_token() == '=': 
                self.tok.advance()
                self.compileExpression()
                if self.tok.current_token() == ';':
                    self.VMW.writePop(segment= self.ST.kindOf(_var_name), index= self.ST.indexOf(_var_name))
                    self.tok.advance()
                else:self.tok.errorhandler()
            else:self.tok.errorhandler()
        self.VMW.writeComment('compileLetEND')

        pass

    def compileIf(self):    #DONE
        self.VMW.writeComment('compileIf')
        logging.debug('if')
        self.ifcount +=1 
        ifcount = self.ifcount
        self.tok.advance()
        if self.tok.current_token() == '(':
            self.tok.advance()
            self.compileExpression()
            if self.tok.current_token() == ')':
                
                self.VMW.writeIf(label = f'class{self.className}ifLabelExecuteIf{ifcount}')
                self.VMW.writeGoto(label = f'class{self.className}ifLabelExecuteElse{ifcount}')
                self.VMW.writeLabel(label = f'class{self.className}ifLabelExecuteIf{ifcount}')
                self.tok.advance()
                if self.tok.current_token()=='{':
                    self.tok.advance()
                    self.compileStatements()
                    if self.tok.current_token() == '}':
                        
                        
                        self.tok.advance()
                        
                        if self.tok.current_token()== 'else':
                            self.VMW.writeGoto(label = f'class{self.className}ifLabelEND{ifcount}')
                            self.VMW.writeLabel(label = f'class{self.className}ifLabelExecuteElse{ifcount}')
                            self.tok.advance()
                            
                            if self.tok.current_token()== '{':
                                
                                self.tok.advance()
                                self.compileStatements()
                                if self.tok.current_token() == '}':
                                    self.tok.advance()
                                else:self.tok.errorhandler()
                            else:self.tok.errorhandler()
                            self.VMW.writeLabel(label = f'class{self.className}ifLabelEND{ifcount}')
                        else:self.VMW.writeLabel(label = f'class{self.className}ifLabelExecuteElse{ifcount}')
                    
                    else:self.tok.errorhandler()
                else:self.tok.errorhandler()
            else:self.tok.errorhandler()
        else:self.tok.errorhandler()
        
        pass

    def compileWhile(self): #DONE
        self.VMW.writeComment('compileWhile')
        logging.debug('while')
        self.whilecount +=1 
        whilecount = self.whilecount

        self.VMW.writeLabel(label = f'class{self.className}whileLabelStart{whilecount}')
        self.tok.advance()
        if self.tok.current_token() == '(':
            self.tok.advance()
            self.compileExpression()
            if self.tok.current_token() == ')':
                self.VMW.writeArithmetic('not')
                self.tok.advance()
                self.VMW.writeIf(label = f'class{self.className}whileLabelEXIT{whilecount}')
                if self.tok.current_token()=='{':
                    self.tok.advance()
                    self.compileStatements()
                    if self.tok.current_token() == '}':
                        self.VMW.writeGoto(label = f'class{self.className}whileLabelStart{whilecount}')
                        self.tok.advance()
                    else:self.tok.errorhandler()
                else:self.tok.errorhandler()
            else:self.tok.errorhandler()
        else:self.tok.errorhandler()

        self.VMW.writeLabel(label = f'class{self.className}whileLabelEXIT{whilecount}')



        pass

    def compileDo(self): #DONE
        self.VMW.writeComment('compileDo')
        logging.debug('do')
    
        self.tok.advance()
        if self.tok.tokentypecurrent() == "identifier":
            self.subroutineCall()
            if self.tok.current_token() == ';':
                self.VMW.writePop(segment='temp', index=0)
                self.tok.advance()
            else:self.tok.errorhandler()
        else:self.tok.errorhandler()
        pass

    def compileReturn(self): #DONE
        self.VMW.writeComment('compileReturn')
        logging.debug('return')

        self.tok.advance()

        if self.tok.current_token() != ';':
            self.compileExpression()
            self.VMW.writeReturn()
            self.tok.advance()

        elif self.tok.current_token() == ';':
            self.VMW.writePush(segment='constant', index= 0)
            self.VMW.writeReturn()
            self.tok.advance()
        else:self.tok.errorhandler()

        pass

    def compileExpression(self): # term (op term)*  #DONE
        self.VMW.writeComment('compileExpression')

        logging.debug("compileExpression")
        
        self.compileTerm()
        while True:
            if self.tok.current_token() in self.opList:
                _currentOp = self.opLookup[self.tok.current_token()]
                self.tok.advance()
                self.compileTerm()
                self.VMW.writeArithmetic(_currentOp)
            else:
                break
        pass

    def compileTerm(self):# integerConstant I stringConstant I keywordConstant I varName I varName '[' expression ']' I subroutineCall I ' expression ' I unaryOp term
        logging.debug("compileterm")
        self.VMW.writeComment('compileTerm')
        
        #DONE
        if self.tok.current_token() in self.unaryOpList:
            # print(1)
            _unary= self.tok.current_token()
            self.tok.advance() 
            self.compileTerm()
            self.VMW.writeArithmetic(self.unaryDict[_unary])

        #DONE
        elif self.tok.current_token() == '(': #  expression
            # print(2)
            self.tok.advance()
            self.compileExpression()
            if self.tok.current_token()==')':
                self.tok.advance()
            else:self.tok.errorhandler()




        ####### IMPLEMENT LATER ? ->   varName '[' expression ']'

        #DONE!!!!!!!!!!

        elif self.tok.tokentypecurrent() == "identifier" and self.tok.next_token() == '[': # varName '[' expression ']' 
            # print(3)
            self.VMW.writePush(segment=self.ST.kindOf(self.tok.current_token()), index = self.ST.indexOf(self.tok.current_token()))
            self.tok.advance()
            self.tok.advance()
            self.compileExpression()
            if self.tok.current_token()==']':
                self.VMW.writeArithmetic('add')
                self.tok.advance()
                self.VMW.writePop(segment= 'pointer', index = 1)
                self.VMW.writePush(segment= 'that', index= 0)
            else:self.tok.errorhandler()

        elif self.tok.tokentypecurrent() == "identifier" and (self.tok.next_token() == '(' or self.tok.next_token() == '.'): # subroutineCall
            # print(4)
            self.subroutineCall()

        elif self.tok.tokentypecurrent() == "keyword": #keywordConstant
            # print(5)
            if self.tok.current_token() == 'true':
                self.VMW.writePush(segment= 'constant', index= '0')
                self.VMW.writeArithmetic('not')

            elif self.tok.current_token() == 'false':
                self.VMW.writePush(segment= 'constant', index= '0')

            elif self.tok.current_token() == 'null':
                self.VMW.writePush(segment= 'constant', index= '0')

            elif self.tok.current_token() == 'this':
                self.VMW.writePush(segment= 'pointer', index= '0')
            self.tok.advance()

        elif self.tok.tokentypecurrent() == "integerConstant":
            # print(6)
            self.VMW.writePush(segment= 'constant', index= self.tok.current_token())
            self.tok.advance()

        #STRING DO LATER
        elif self.tok.tokentypecurrent() == "stringConstant":
            _string = self.tok.current_token()[1:-1]
            self.VMW.writePush(segment='constant', index=len(_string)) 
            self.VMW.writeCall('String.new', 1)  

            
            for char in _string:
                self.VMW.writePush(segment='constant', index=ord(char))  
                self.VMW.writeCall('String.appendChar', 2) 
        
            self.tok.advance()



        elif self.tok.tokentypecurrent() == "identifier": # varName
            # print(8) 
            self.VMW.writePush(segment= self.ST.kindOf(self.tok.current_token()), index=self.ST.indexOf(self.tok.current_token()))
            self.tok.advance()
        pass

    def compileExpressionList(self): #DONE
        logging.debug("compileExpressionList")
        self.VMW.writeComment('compileExpressionList')
        _argsNumber = 0
        if self.tok.current_token() != ')': 
            while True:
                _argsNumber +=1 
                self.compileExpression()
                if self.tok.current_token() == ',':
                    self.tok.advance()
                else:
                    logging.debug('exitingEXPLIST')
                    break
        else : 
            logging.debug('empty exp list')
        
        return _argsNumber

    # def subroutineCall(self):
    #     logging.debug("subroutineCall")
    #     self.VMW.writeComment('subroutineCall')
    #     if self.tok.tokentypecurrent() == "identifier":

    #         #_calledSubroutineClass  might be the class name when external subroutine is called but may be the subroutine name itself when internal subroutine is called
    #         _calledSubroutineClass = self.tok.current_token()
    #         self.tok.advance()
    #         if self.tok.current_token()== '.':
                
    #             self.tok.advance()
    #             if self.tok.tokentypecurrent() == "identifier":
    #                 _calledSubroutineName = self.tok.current_token()
    #                 self.tok.advance()
    #                 if self.tok.current_token() == "(":
    #                     self.tok.advance()
    #                     _argsNumber = self.compileExpressionList()
    #                     if self.tok.current_token() == ')':
    #                         self.VMW.writeCall(name=_calledSubroutineClass+'.'+ _calledSubroutineName, nArgs= _argsNumber)
    #                         self.tok.advance()
    #                     else:self.tok.errorhandler()
    #                 else:self.tok.errorhandler()
    #             else:self.tok.errorhandler()
    #         elif self.tok.current_token() == "(":
        
    #             self.tok.advance()
    #             _argsNumber = self.compileExpressionList()
    #             if self.tok.current_token() == ')':
    #                 self.VMW.writeCall(name=self.className + '.'+ _calledSubroutineClass, nArgs= _argsNumber)

    #                 self.tok.advance()  
    #             else:self.tok.errorhandler()
    #     
    
    def subroutineCall(self):
        logging.debug("subroutineCall")
        self.VMW.writeComment("subroutineCall")

        if self.tok.tokentypecurrent() == "identifier":
            name = self.tok.current_token()  # could be className, varName, or subroutineName
            self.tok.advance()

            # External call: either var.method() or Class.func()
            if self.tok.current_token() == '.':
                self.tok.advance()
                subroutineName = self.tok.current_token()
                self.tok.advance()

                # Is 'name' a variable (i.e., method call on an object)?
                if self.ST.kindOf(name) is not None:
                    kind = self.ST.kindOf(name)
                    index = self.ST.indexOf(name)
                    type_ = self.ST.typeOf(name)

                    self.VMW.writePush(kind, index)  # push object reference
                    fullName = type_ + '.' + subroutineName
                    nArgs = 1  # account for 'this'
                else:
                    # It's a class name: static call
                    fullName = name + '.' + subroutineName
                    nArgs = 0

            # Internal method call: just subroutineName(...)
            elif self.tok.current_token() == '(':
                fullName = self.className + '.' + name
                self.VMW.writePush('pointer', 0)  # push this
                nArgs = 1

            else:
                self.tok.errorhandler()
                return

            self.tok.advance()  # skip '('
            nArgs += self.compileExpressionList()
            if self.tok.current_token() == ')':
                self.VMW.writeCall(fullName, nArgs)
                self.tok.advance()
            else:
                self.tok.errorhandler()

