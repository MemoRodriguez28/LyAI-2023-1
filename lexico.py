import enum, sys
class Lexico:
    def __init__(self, fuente):
        #Se pasa el código fuente como cadena. Se le agrega newline para simplificar el análisis para el último token/sentencia.
        self.fuente = fuente + '\n' 
        self.carActual = ''     #Caracter actual en la cadena.
        self.posActual = -1     #Posición actual en la cadena.
        self.siguiente()

    #Leer el siguiente caracter.
    def siguiente(self): #Guarda los cambios en posActual y carActual
        self.posActual += 1 #Posición actual = 7 (8)
        if self.posActual >= len(self.fuente):
            self.carActual = '\0' #End of file EOP
        else:
            self.carActual = self.fuente[self.posActual] 

    #Regresar el caracter adelante (lookahead).
    def asomar(self): #No guarda los cambios
        #self.posActual += 1
        if self.posActual + 1 >= len(self.fuente):
            return '\0'
        return self.fuente[self.posActual + 1]
    
    #Token inválido, imprimir error y salir.
    def abortar(self, mensaje):
        sys.exit("Error lexico: " + mensaje)

    #Saltar espacios excepto \n, estas se utilizarán para indicar el final de una sentencia.
    def saltarEspacios(self):
        #Saltar los caracteres si no son espacios
        if self.carActual == ' ' or  self.carActual == '\t' or self.carActual == '\r':
            self.siguiente()

    #Saltar comentarios en el código.	
    def saltarComentarios(self):
        #Saltar caracter si es '#' comentarios de linea (\n)
        if self.carActual == '#':
            while self.carActual != '\n':  #Siempre y cuando no sea \n
                self.siguiente()
    
    #Regresar el siguiente token.
    def getToken(self):
        token = None #var Auxiliar
        #Revisar si los caracteres sencillos coinciden
        if self.carActual == '+':
            token = Token(self.carActual, TipoToken.PLUS)
        elif self.carActual == '-':
            token = Token(self.carActual, TipoToken.MINUS)
        elif self.carActual == '*':
            token = Token(self.carActual, TipoToken.ASTERISK)   
        elif self.carActual == '/':
            token = Token(self.carActual, TipoToken.SLASH)
        elif self.carActual == '\0':
            token = Token(self.carActual, TipoToken.EOF)
        elif self.carActual == '\n':
            token = Token(self.carActual, TipoToken.NEWLINE)
        else:
            self.abortar("El token '" + self.carActual + "' es desconocido")  
             
        #Si ya se identifico el token, debemos leer el siguiente caracter
        self.siguiente()
        return token
               
class Token:
    def __init__(self, lexema, token):
        self.lexema = lexema
        self.token = token #TipoToken ENUM     
    
class TipoToken(enum.Enum):
    #Escribir todos los tokens
    EOF = -1 #End of file #\n
    NEWLINE = 0 #\n
    NUMERO = 1
    ID = 2
    STRING = 3
    #Keywords
    LABEL = 101
    GOTO = 102
    PRINT = 103
    INPUT = 104
    LET = 105
    IF = 106
    THEN = 107
    ENDIF = 108
    WHILE = 109
    REPEAT = 110
    ENDWHILE = 111
    #Operadores
    EQ = 201 #=
    PLUS = 202 #+ 1
    MINUS = 203 #- 1
    ASTERISK = 204 #* 1
    SLASH = 205 #/ 1
    EQEQ = 206 #==
    NOTEQ = 207 #!= 1
    LT = 208 #<
    LTEQ = 209 #<= 
    GT = 210 #>
    GTEQ = 211 #>=
    

def test():
    return print("import lexer.py :)")