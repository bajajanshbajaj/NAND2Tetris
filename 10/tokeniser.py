import re

class tokeniser():

    
    
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

        try:
            while True:

                if content[content_index] + content[content_index +1 ] == '/*':
                    while (content[content_index] + content[content_index +1 ]) != '*/':
                        content_index+=1
                    content_index+=2

                elif content[content_index] + content[content_index +1 ] == '//':
                    while content[content_index]  != '\n':
                        content_index+=1
                    content_index+=1
            
                elif content[content_index] == '"':
                    content_index+=1
                    while content[content_index] != '"':
                        tempstr+=content[content_index]
                        content_index+=1
                    self.token_list.append('"'+tempstr+'"')


                    content_index += 1
                    tempstr=''
            
                elif content[content_index] in self.symbols :
                    if tempstr != '':
                        self.token_list.append(tempstr)
                        tempstr = '' 
                    
                    self.token_list.append(content[content_index])
                    content_index +=1
                    

                elif content[content_index] in spacing_chars :
                    if tempstr != '':
                        self.token_list.append(tempstr)
                        tempstr = '' 
                    content_index +=1

                else:
                    tempstr+= content[content_index]
                    content_index +=1
                pass
        except:
            pass
        self.total_tokens= len(self.token_list)


        #print(self.token_list)

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
            print('ERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR')

    def current_token(self):
        return self.token_list[self.current_token_number]
    def next_token(self):
        return self.token_list[self.current_token_number +1]
    
    def advance(self):
        if self.hasMoreTokens():
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
            


    