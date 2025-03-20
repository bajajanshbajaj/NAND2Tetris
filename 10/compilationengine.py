from tokeniser import tokeniser

#token is advanced to next token before calling another function , this gives tokens access to both current class and the next class
class CompileEngine():
    
    def __init__(self,  filestream):
        self.parsed = ''
        self.tok = tokeniser(filestream)
        #self.tok.printokenwtype()
        self.classvarsList = ['static', 'field']
        self.subroutineDecList= ['constructor', 'function', 'method']
        self.typeList= ['int', 'char', 'boolean']
        self.opList = ['+', '-', '*', '/', '&', '|', '<', '>', '=']
        self.unaryOpList = ['-', '~']
        self.keywordConstantList = ['true', 'false', 'null', 'this'] 
        self.compileClass()

        
    
    def appendnonterminalstart(self, name):
        self.parsed+= f"<{name}>\n"
    def appendnonterminalend(self, name):
        self.parsed+= f"</{name}>\n"
    def appendCurrentTokenAsTerminal(self):
        name = self.tok.current_token()
        self.parsed+= f"<{self.tok.tokentype(name)}> {self.tok.escape_xml(name)} </{self.tok.tokentype(name)}>\n"

    def compileClass(self):
        print('compileClass')
        self.appendnonterminalstart("class")
        self.appendCurrentTokenAsTerminal()
        self.tok.advance()
        self.appendCurrentTokenAsTerminal()
        self.tok.advance()
        self.appendCurrentTokenAsTerminal()
        self.tok.advance()

        if self.tok.current_token() in self.classvarsList:
            self.compileClassVarDec()
        else:  #elif self.tok.current_token() in self.subroutineDecList:
            self.compileSubroutine()
        
        if self.tok.current_token() == '}':
            self.appendCurrentTokenAsTerminal()

        self.appendnonterminalend("class")

        pass

    def compileClassVarDec(self):
        print('compileClassVarDec')

        self.appendnonterminalstart("classVarDec")
        self.appendCurrentTokenAsTerminal()
        while True:
            self.tok.advance() #add a condition to check (, varname) later
            self.appendCurrentTokenAsTerminal()
            if self.tok.current_token() == ";":
                break

        self.appendnonterminalend("classVarDec")

        self.tok.advance()

        if self.tok.current_token() in self.classvarsList:
            self.compileClassVarDec()
        else:  #elif self.tok.current_token() in self.subroutineDecList:
            self.compileSubroutine()

        pass

    def compileSubroutine(self):
        print("compileSubroutine")
        self.appendnonterminalstart("subroutineDec")
        self.appendCurrentTokenAsTerminal()
        self.tok.advance()
        if True: # self.tok.current_token() in self.subroutineDecList or self.tok.current_token() == 'void':
            self.appendCurrentTokenAsTerminal()
            if self.tok.tokentype(self.tok.advance()) == 'identifier':
                self.appendCurrentTokenAsTerminal()
                if self.tok.advance() == '(':
                    self.appendCurrentTokenAsTerminal()
                    self.tok.advance()
                    self.compileParameterList()
                    print('current token = "'+(self.tok.current_token())+'"')
                    if self.tok.current_token()== ")":
                        self.appendCurrentTokenAsTerminal()
                        self.tok.advance()
                        self.compileSubroutineBody()
                    else : print('expected ) ' )
  
        self.appendnonterminalend("subroutineDec")

        if self.tok.current_token() != '}':
            self.compileSubroutine()

        
        pass

    def compileParameterList(self):
        print('compileparameterlist')
        self.appendnonterminalstart("parameterList")
        if self.tok.current_token() != ')':
            while True:
                print(self.tok.current_token())
                if True: #self.tok.current_token() in self.typeList:
                    self.appendCurrentTokenAsTerminal()
                    self.tok.advance()
                    if self.tok.tokentype(self.tok.current_token()) == "identifier":
                        print(self.tok.current_token())
                        self.appendCurrentTokenAsTerminal()
                        self.tok.advance()
                if self.tok.current_token() == ',':
                    print(self.tok.current_token())
                    self.appendCurrentTokenAsTerminal()
                    self.tok.advance()
                else:
                    print('exiting')
                    print(self.tok.current_token())
                    break
        else : 
            print('empty param list')

            

        self.appendnonterminalend("parameterList")
        pass

    def compileSubroutineBody(self):
        print('compilesubroutinebody')
        self.appendnonterminalstart("subroutineBody")
        if self.tok.current_token() == '{':
            self.appendCurrentTokenAsTerminal()
            self.tok.advance()
        
            if self.tok.current_token()== 'var':
                self.compileVarDec()

            self.compileStatements()

            if self.tok.current_token() == '}':
                self.appendCurrentTokenAsTerminal()
                self.tok.advance()

        else : print('expected { ')
        
        self.appendnonterminalend("subroutineBody")
        pass

    def compileVarDec(self):
        print('compilevardec')

        self.appendnonterminalstart("varDec")
        self.appendCurrentTokenAsTerminal()
        while True:
            self.tok.advance() #add a condition to check (, varname) later
            self.appendCurrentTokenAsTerminal()
            if self.tok.current_token() == ";":
                break

        self.tok.advance()

        self.appendnonterminalend("varDec")

        if self.tok.current_token() == 'var':
            self.compileVarDec()

        
        pass

    def compileStatements(self):
        print("compileStatements")
        self.appendnonterminalstart("statements")
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
            
        self.appendnonterminalend("statements")
        pass

    def compileLet(self):
        print('let')
        self.appendnonterminalstart("letStatement")
        self.appendCurrentTokenAsTerminal()
        self.tok.advance()
        if self.tok.tokentype(self.tok.current_token() ) == "identifier":
            self.appendCurrentTokenAsTerminal()
            self.tok.advance()
            if self.tok.current_token() == '[':
                self.appendCurrentTokenAsTerminal()
                self.tok.advance()
                self.compileExpression()
                if self.tok.current_token() == ']':
                    self.appendCurrentTokenAsTerminal()
                    self.tok.advance()
            if self.tok.current_token() == '=':
                self.appendCurrentTokenAsTerminal()
                self.tok.advance()
                
                self.compileExpression()
                if self.tok.current_token() == ';':
                    self.appendCurrentTokenAsTerminal()
                    self.tok.advance()

        self.appendnonterminalend("letStatement")
        pass

    def compileIf(self):
        print('if')
        self.appendnonterminalstart("ifStatement")

        self.appendCurrentTokenAsTerminal()
        self.tok.advance()
        if self.tok.current_token() == '(':
            self.appendCurrentTokenAsTerminal()
            self.tok.advance()
            self.compileExpression()
            if self.tok.current_token() == ')':
                self.appendCurrentTokenAsTerminal()
                self.tok.advance()
                if self.tok.current_token()=='{':
                    self.appendCurrentTokenAsTerminal()
                    self.tok.advance()
                    self.compileStatements()
                    if self.tok.current_token() == '}':
                        self.appendCurrentTokenAsTerminal()
                        self.tok.advance()
                        if self.tok.current_token()== 'else':
                            self.appendCurrentTokenAsTerminal()
                            self.tok.advance()
                            if self.tok.current_token()== '{':
                                self.appendCurrentTokenAsTerminal()
                                self.tok.advance()
                                self.compileStatements()
                                if self.tok.current_token() == '}':
                                    self.appendCurrentTokenAsTerminal()
                                    self.tok.advance()



        self.appendnonterminalend("ifStatement")
        pass

    def compileWhile(self):
        print('while')
        self.appendnonterminalstart("whileStatement")
        self.appendCurrentTokenAsTerminal()
        self.tok.advance()
        if self.tok.current_token() == '(':
            self.appendCurrentTokenAsTerminal()
            self.tok.advance()
            self.compileExpression()
            if self.tok.current_token() == ')':
                self.appendCurrentTokenAsTerminal()
                self.tok.advance()
                if self.tok.current_token()=='{':
                    self.appendCurrentTokenAsTerminal()
                    self.tok.advance()
                    self.compileStatements()
                    if self.tok.current_token() == '}':
                        self.appendCurrentTokenAsTerminal()
                        self.tok.advance()


        self.appendnonterminalend("whileStatement")
        pass

    def compileDo(self):
        print('do')
        self.appendnonterminalstart("doStatement")
        self.appendCurrentTokenAsTerminal()
        self.tok.advance()
        if self.tok.tokentype(self.tok.current_token()) == "identifier":
            self.subroutineCall()
            if self.tok.current_token() == ';':
                self.appendCurrentTokenAsTerminal()
                self.tok.advance()

        self.appendnonterminalend("doStatement")
        pass

    def compileReturn(self):
        print('return')
        self.appendnonterminalstart("returnStatement")
        self.appendCurrentTokenAsTerminal()
        self.tok.advance()

        if self.tok.current_token() != ';':
            self.compileExpression()
        if self.tok.current_token() == ';':
            self.appendCurrentTokenAsTerminal()
            self.tok.advance()

        self.appendnonterminalend("returnStatement")
        pass

    def compileExpression(self):
        self.appendnonterminalstart('expression')
        print("compileExpression")
        
        self.compileTerm()
        while True:
            if self.tok.current_token() in self.opList:
                self.appendCurrentTokenAsTerminal()
                self.tok.advance()
                self.compileTerm()
            else:
                break


        
        self.appendnonterminalend("expression")
        pass

    def compileTerm(self):
        print("compileterm")
        self.appendnonterminalstart("term")
        if self.tok.current_token() in self.unaryOpList:
            self.appendCurrentTokenAsTerminal()
            self.tok.advance()
            self.compileTerm()
        elif self.tok.current_token() == '(':
            self.appendCurrentTokenAsTerminal()
            self.tok.advance()
            self.compileExpression()
            if self.tok.current_token()==')':
                self.appendCurrentTokenAsTerminal()
                self.tok.advance()
        elif self.tok.tokentype(self.tok.current_token()) == "identifier" and self.tok.next_token() == '[':
            self.appendCurrentTokenAsTerminal()
            self.tok.advance()
            self.appendCurrentTokenAsTerminal()
            self.tok.advance()
            self.compileExpression()
            if self.tok.current_token()==']':
                self.appendCurrentTokenAsTerminal()
                self.tok.advance()
        elif self.tok.tokentype(self.tok.current_token()) == "identifier" and (self.tok.next_token() == '(' or self.tok.next_token() == '.'):
            self.subroutineCall()
        elif self.tok.tokentype(self.tok.current_token()) != "symbol":
                self.appendCurrentTokenAsTerminal()
                self.tok.advance()

        self.appendnonterminalend("term")
        pass

    def compileExpressionList(self):
        print("compileExpressionList")
        self.appendnonterminalstart("expressionList")
        if self.tok.current_token() != ')':
            while True:
                self.compileExpression()
                if self.tok.current_token() == ',':
                    self.appendCurrentTokenAsTerminal()
                    self.tok.advance()
                else:
                    print('exitingEXPLIST')
                    break
        else : 
            print('empty exp list')
        self.appendnonterminalend("expressionList")
        pass

    def subroutineCall(self):
        print("subroutineCall")
        if self.tok.tokentype(self.tok.current_token()) == "identifier":
            self.appendCurrentTokenAsTerminal()
            self.tok.advance()
            if self.tok.current_token()== '.':
                self.appendCurrentTokenAsTerminal()
                self.tok.advance()
                if self.tok.tokentype(self.tok.current_token()) == "identifier":
                    self.appendCurrentTokenAsTerminal()
                    self.tok.advance()
                    if self.tok.current_token() == "(":
                        self.appendCurrentTokenAsTerminal()
                        self.tok.advance()
                        self.compileExpressionList()
                        if self.tok.current_token() == ')':
                            self.appendCurrentTokenAsTerminal()
                            self.tok.advance()
            elif self.tok.current_token() == "(":
                        self.appendCurrentTokenAsTerminal()
                        self.tok.advance()
                        self.compileExpressionList()
                        if self.tok.current_token() == ')':
                            self.appendCurrentTokenAsTerminal()
                            self.tok.advance()  
        pass


