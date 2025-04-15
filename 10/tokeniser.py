import sys
class tokeniser():


    token_list = []
    line_number = 1
    character_number = 0 


    def tokentype(self, token):
        if token[0] == '"' and token[-1] == '"':
            return "stringConstant"
        
        elif token in self.keywords:
            return "keyword"
        
        elif token in self.symbols:
            return "symbol"
        
        elif token.isnumeric():
            return "integerConstant"
        
        elif token[0].isalpha() or token[0] == '_':
            return "identifier"
        else:
            print('ERR')
       
    
    def token_list_append(self, token):
        self.current_line_token_number +=1 
        self.token_list.append([token, self.tokentype(token), self.line_number, self.current_line_token_number])

    
    def __init__(self, filestream):

        self.keywords = [
        "class", "constructor", "function", "method", "field", "static", 
        "var", "int", "char", "boolean", "void", "true", "false", "null", 
        "this", "let", "do", "if", "else", "while", "return"]

        self.symbols = [
        "(", ")", "{", "}", "[", "]", ".", ",", ";", "+", "-", "*", "/", 
        "&", "|", ">", "<", "=", "~"]

        spacing_chars= ['\n', ' ', '\t']
        
        
        tempstr= ''
        content = list(filestream.read())

        content_index = 0

        self.token_list = []
        self.current_token_number=0

        while content_index < len(content):
            if content[content_index] == '\n' :
                self.line_number += 1 
                self.current_line_token_number = 0 

            if content_index + 1 < len(content) and content[content_index] + content[content_index + 1] == '/*':
                while content_index + 1 < len(content) and content[content_index] + content[content_index + 1] != '*/':

                    if content[content_index] == '\n' :
                        self.line_number += 1 
                        self.current_line_token_number = 0 

                    
                    content_index+=1
                content_index+=2

            elif content_index + 1 < len(content) and content[content_index] + content[content_index + 1] == '//':
                while content[content_index]  != '\n':
                    content_index+=1
                content_index+=1
                self.line_number += 1 
                self.current_line_token_number = 0 
        
            elif content[content_index] == '"':
                content_index+=1
                while content[content_index] != '"':
                    tempstr+=content[content_index]
                    content_index+=1
                self.token_list_append('"'+tempstr+'"')


                content_index += 1
                tempstr=''
        
            elif content[content_index] in self.symbols :
                if tempstr != '':
                    self.token_list_append(tempstr)
                    tempstr = '' 
                
                self.token_list_append(content[content_index])
                content_index +=1
                

            elif content[content_index] in spacing_chars :
                if tempstr != '':
                    self.token_list_append(tempstr)
                    tempstr = '' 
                content_index +=1

            else:
                tempstr+= content[content_index]
                content_index +=1
            pass
        
        if tempstr:
            self.token_list_append(tempstr)
        
        self.total_tokens = len(self.token_list)

        


        #print(self.token_list)
    
    def tokentypecurrent(self):
        return self.token_list[self.current_token_number][1]

    def current_token(self):
        return self.token_list[self.current_token_number][0]
    
    def next_token(self):
        return self.token_list[self.current_token_number +1][0]
    
    def advance(self):

        if self.hasMoreTokens(): 
            #print(self.current_token())
            self.current_token_number+=1
            return self.current_token()
    
    def hasMoreTokens(self):
        return self.current_token_number < self.total_tokens

    def keyWord(self):
        return self.current_token()
    def symbol(self):
        return self.current_token()
    def identifier(self):
        return self.current_token()
    def intVa1(self):
        return int(self.current_token())
    def stringVa1(self):
        return self.current_token()[1:-2]
    
    def escape_xml(self, st):
        result=r''
        escape_dict = {
            '&': '&amp;',
            '<': '&lt;',
            '>': '&gt;',
            '"': '&quot;',
            "'": '&apos;'
        }
        for c in st:
            result += escape_dict.get(c, c)  # Concatenation using '+'
        return result
    

    def printokenwtype(self):
        tempstr = ''
        for tkn in self.token_list:
            tempstr += (f"<{self.tokentype(tkn)}>{self.escape_xml(tkn)}</{self.tokentype(tkn)}>\n")
        print(tempstr)

    def errorhandler(self):
        print (f'''Compilation error in line: {self.token_list[self.current_token_number][2]} | token number: {self.token_list[self.current_token_number][3]}
after token : "{self.token_list[self.current_token_number-1][0]}"  | tokentype : {self.token_list[self.current_token_number-1][1]}
before token : "{self.token_list[self.current_token_number][0]}"  | tokentype : {self.token_list[self.current_token_number][1]}''')
        sys.exit(1)
            


    
