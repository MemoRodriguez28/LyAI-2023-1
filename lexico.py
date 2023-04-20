import enum
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
    def abortar(self, message):
        pass #Todavia no

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
        pass
    
class TipoToken(enum.Enum):
    #Escribir todos los tokens
    EOF = -1 #End of file
    NEWLINE = 0 
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
    EQ = 201
    PLUS = 202
    MINUS = 203
    ASTERISK = 204
    SLASH = 205
    EQEQ = 206
    NOTEQ = 207
    LT = 208
    LTEQ = 209
    GT = 210
    GTEQ = 211
    

def test():
    return print("import lexer.py :)")