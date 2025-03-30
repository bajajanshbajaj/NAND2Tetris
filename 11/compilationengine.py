from tokeniser import tokeniser
import logging 



#token is advanced to next token before calling another function , this gives tokens access to both current class and the next class
class CompileEngine():
    
    def __init__(self,  filestream, logfile):
        self.parsed = ''
        self.tok = tokeniser(filestream)
        #self.tok.printokenwtype()
        self.classvarsList = ['static', 'field']
        self.subroutineDecList= ['constructor', 'function', 'method']
        self.typeList= ['int', 'char', 'boolean']
        self.opList = ['+', '-', '*', '/', '&', '|', '<', '>', '=']
        self.unaryOpList = ['-', '~']
        self.keywordConstantList = ['true', 'false', 'null', 'this'] 
        logging.basicConfig(
    filename=logfile,  # Log file name
    level=logging.DEBUG,  # Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Log format
    datefmt='%Y-%m-%d %H:%M:%S'  # Date format
)
        self.compileClass()

        
    
    def appendnonterminalstart(self, name):
        self.parsed+= f"<{name}>\n"
    def appendnonterminalend(self, name):
        self.parsed+= f"</{name}>\n"
    def appendCurrentTokenAsTerminal(self):
        name = self.tok.current_token()
        self.parsed+= f"<{self.tok.tokentypecurrent()}> {self.tok.escape_xml(name)} </{self.tok.tokentypecurrent()}>\n"

    def compileClass(self):
        logging.debug('compileClass') 
        self.appendnonterminalstart("class")

        if self.tok.tokentypecurrent() == 'keyword':
            self.appendCurrentTokenAsTerminal()
            self.tok.advance()
            if self.tok.tokentypecurrent() =='identifier':
                self.appendCurrentTokenAsTerminal()
                self.tok.advance()
                if self.tok.current_token() == '{':
                    self.appendCurrentTokenAsTerminal()
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
                self.appendCurrentTokenAsTerminal()
                break
            else:self.tok.errorhandler()

        self.appendnonterminalend("class")

        pass

    def compileClassVarDec(self):
        logging.debug('compileClassVarDec')

        self.appendnonterminalstart("classVarDec")
        self.appendCurrentTokenAsTerminal()
        while True:
            self.tok.advance() #add a condition to check (, varname) later
            self.appendCurrentTokenAsTerminal()
            if self.tok.current_token() == ";":
                break

        self.appendnonterminalend("classVarDec")

        self.tok.advance()
        pass

    def compileSubroutine(self):
        logging.debug("compileSubroutine")
        self.appendnonterminalstart("subroutineDec")
        # self.appendCurrentTokenAsTerminal()
        # self.tok.advance()
        if self.tok.current_token() in self.subroutineDecList :
            self.appendCurrentTokenAsTerminal()
            self.tok.advance()
            if True:# self.tok.current_token() == 'void' or self.tok.tokentypecurrent() == ?
                self.appendCurrentTokenAsTerminal()
                # self.tok.advance()
                if self.tok.tokentype(self.tok.advance()) == 'identifier':

                    self.appendCurrentTokenAsTerminal()
                    if self.tok.advance() == '(':
                        self.appendCurrentTokenAsTerminal()
                        self.tok.advance()
                        self.compileParameterList()
                        logging.debug('current token = "'+(self.tok.current_token())+'"')
                        if self.tok.current_token()== ")":
                            self.appendCurrentTokenAsTerminal()
                            self.tok.advance()
                            self.compileSubroutineBody()
                        else:self.tok.errorhandler()
                    else:self.tok.errorhandler()
                else:self.tok.errorhandler()

  
        self.appendnonterminalend("subroutineDec")
        
        pass

    def compileParameterList(self):
        logging.debug('compileparameterlist')
        self.appendnonterminalstart("parameterList")
        if self.tok.current_token() != ')':
            while True:
                logging.debug(self.tok.current_token())
                if True: #self.tok.current_token() in self.typeList:
                    self.appendCurrentTokenAsTerminal()
                    self.tok.advance()
                    if self.tok.tokentypecurrent() == "identifier":
                        logging.debug(self.tok.current_token())
                        self.appendCurrentTokenAsTerminal()
                        self.tok.advance()
                    else:self.tok.errorhandler()
                if self.tok.current_token() == ',':
                    logging.debug(self.tok.current_token())
                    self.appendCurrentTokenAsTerminal()
                    self.tok.advance()
                else:
                    logging.debug('exiting')
                    logging.debug(self.tok.current_token())
                    break
        else : 
            logging.debug('empty param list')

            

        self.appendnonterminalend("parameterList")
        pass

    def compileSubroutineBody(self):
        logging.debug('compilesubroutinebody')
        self.appendnonterminalstart("subroutineBody")
        if self.tok.current_token() == '{':
            self.appendCurrentTokenAsTerminal()
            self.tok.advance()

            while True:
                if self.tok.current_token()== 'var':
                    self.compileVarDec()
                else:break

            self.compileStatements()

            if self.tok.current_token() == '}':
                self.appendCurrentTokenAsTerminal()
                self.tok.advance()
            else:self.tok.errorhandler()

        else:self.tok.errorhandler()
        
        self.appendnonterminalend("subroutineBody")
        pass

    def compileVarDec(self):
        logging.debug('compilevardec')

        self.appendnonterminalstart("varDec")
        self.appendCurrentTokenAsTerminal()
        while True:
            self.tok.advance() #add a condition to check (, varname) later
            self.appendCurrentTokenAsTerminal()
            if self.tok.current_token() == ";":
                break

        self.tok.advance()

        self.appendnonterminalend("varDec")

        
        pass

    def compileStatements(self):
        logging.debug("compileStatements")
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
        logging.debug('let')
        self.appendnonterminalstart("letStatement")
        self.appendCurrentTokenAsTerminal()
        self.tok.advance()
        if self.tok.tokentypecurrent() == "identifier":
            self.appendCurrentTokenAsTerminal()
            self.tok.advance()
            if self.tok.current_token() == '[':
                self.appendCurrentTokenAsTerminal()
                self.tok.advance()
                self.compileExpression()
                if self.tok.current_token() == ']':
                    self.appendCurrentTokenAsTerminal()
                    self.tok.advance()
                else:self.tok.errorhandler()
            if self.tok.current_token() == '=':
                self.appendCurrentTokenAsTerminal()
                self.tok.advance()
                
                self.compileExpression()
                if self.tok.current_token() == ';':
                    self.appendCurrentTokenAsTerminal()
                    self.tok.advance()
                else:self.tok.errorhandler()
            else:self.tok.errorhandler()

        self.appendnonterminalend("letStatement")
        pass

    def compileIf(self):
        logging.debug('if')
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
                                else:self.tok.errorhandler()
                            else:self.tok.errorhandler()
                        
                    else:self.tok.errorhandler()
                else:self.tok.errorhandler()
            else:self.tok.errorhandler()
        else:self.tok.errorhandler()



        self.appendnonterminalend("ifStatement")
        pass

    def compileWhile(self):
        logging.debug('while')
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
                    else:self.tok.errorhandler()
                else:self.tok.errorhandler()
            else:self.tok.errorhandler()
        else:self.tok.errorhandler()


        self.appendnonterminalend("whileStatement")
        pass

    def compileDo(self):
        logging.debug('do')
        self.appendnonterminalstart("doStatement")
        self.appendCurrentTokenAsTerminal()
        self.tok.advance()
        if self.tok.tokentypecurrent() == "identifier":
            self.subroutineCall()
            if self.tok.current_token() == ';':
                self.appendCurrentTokenAsTerminal()
                self.tok.advance()
            else:self.tok.errorhandler()
        else:self.tok.errorhandler()

        self.appendnonterminalend("doStatement")
        pass

    def compileReturn(self):
        logging.debug('return')
        self.appendnonterminalstart("returnStatement")
        self.appendCurrentTokenAsTerminal()
        self.tok.advance()

        if self.tok.current_token() != ';':
            self.compileExpression()
        if self.tok.current_token() == ';':
            self.appendCurrentTokenAsTerminal()
            self.tok.advance()
        else:self.tok.errorhandler()

        self.appendnonterminalend("returnStatement")
        pass

    def compileExpression(self):
        self.appendnonterminalstart('expression')
        logging.debug("compileExpression")
        
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
        logging.debug("compileterm")
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
            else:self.tok.errorhandler()
        elif self.tok.tokentypecurrent() == "identifier" and self.tok.next_token() == '[':
            self.appendCurrentTokenAsTerminal()
            self.tok.advance()
            self.appendCurrentTokenAsTerminal()
            self.tok.advance()
            self.compileExpression()
            if self.tok.current_token()==']':
                self.appendCurrentTokenAsTerminal()
                self.tok.advance()
            else:self.tok.errorhandler()
        elif self.tok.tokentypecurrent() == "identifier" and (self.tok.next_token() == '(' or self.tok.next_token() == '.'):
            self.subroutineCall()
        elif self.tok.tokentypecurrent() != "symbol":
                self.appendCurrentTokenAsTerminal()
                self.tok.advance()

        self.appendnonterminalend("term")
        pass

    def compileExpressionList(self):
        logging.debug("compileExpressionList")
        self.appendnonterminalstart("expressionList")
        if self.tok.current_token() != ')':
            while True:
                self.compileExpression()
                if self.tok.current_token() == ',':
                    self.appendCurrentTokenAsTerminal()
                    self.tok.advance()
                else:
                    logging.debug('exitingEXPLIST')
                    break
        else : 
            logging.debug('empty exp list')
        self.appendnonterminalend("expressionList")
        pass

    def subroutineCall(self):
        logging.debug("subroutineCall")
        if self.tok.tokentypecurrent() == "identifier":
            self.appendCurrentTokenAsTerminal()
            self.tok.advance()
            if self.tok.current_token()== '.':
                self.appendCurrentTokenAsTerminal()
                self.tok.advance()
                if self.tok.tokentypecurrent() == "identifier":
                    self.appendCurrentTokenAsTerminal()
                    self.tok.advance()
                    if self.tok.current_token() == "(":
                        self.appendCurrentTokenAsTerminal()
                        self.tok.advance()
                        self.compileExpressionList()
                        if self.tok.current_token() == ')':
                            self.appendCurrentTokenAsTerminal()
                            self.tok.advance()
                        else:self.tok.errorhandler()
                    else:self.tok.errorhandler()
                else:self.tok.errorhandler()
            elif self.tok.current_token() == "(":
                        self.appendCurrentTokenAsTerminal()
                        self.tok.advance()
                        self.compileExpressionList()
                        if self.tok.current_token() == ')':
                            self.appendCurrentTokenAsTerminal()
                            self.tok.advance()  
                        else:self.tok.errorhandler()
        pass


