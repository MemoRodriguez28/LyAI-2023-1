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
        self.saltarEspacios()
        self.saltarComentarios()
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
        elif self.carActual == '=':
            #Asomar nos regresa un caracter
            if self.asomar() == '=': #==
                carAnterior = self.carActual #=1 carAnterior = '='1
                self.siguiente() #
                token = Token(carAnterior + self.carActual, TipoToken.EQEQ)
            else:
                token = Token(self.carActual, TipoToken.EQ)
        elif self.carActual == '<':
            #Asomar nos regresa un caracter
            if self.asomar() == '=': #==
                carAnterior = self.carActual #=1 carAnterior = '='1
                self.siguiente() #
                token = Token(carAnterior + self.carActual, TipoToken.LTEQ)
            else:
                token = Token(self.carActual, TipoToken.LT)
        elif self.carActual == '>':
            #Asomar nos regresa un caracter
            if self.asomar() == '=': #==
                carAnterior = self.carActual #=1 carAnterior = '='1
                self.siguiente() #
                token = Token(carAnterior + self.carActual, TipoToken.GTEQ)
            else:
                token = Token(self.carActual, TipoToken.GT)
        elif self.carActual == '!':
            if self.asomar() == '=': #!=
                carAnterior = self.carActual
                self.siguiente() 
                token = Token(carAnterior + self.carActual, TipoToken.NOTEQ)
            else:
                self.abortar("Se esperaba '!=' y se detuvo '!'.")
        elif self.carActual.isdigit(): 
            posNumInicial = self.posActual 
            while self.asomar().isdigit():
                self.siguiente()
            if self.asomar() == '.': #Punto decimal
                self.siguiente()
                if not self.asomar().isdigit(): #Si no es digito
                    self.abortar("Caracter ilegal en numero")
                while self.asomar().isdigit():
                    self.siguiente()
            #Regresa el lexema completo posNumInicial hast posActual
            #Obtener la subcadena del codigo fuente
            lexema = self.fuente[posNumInicial : self.posActual+1]
            token = Token(lexema, TipoToken.NUMERO)
        elif self.carActual.isalpha():
            pospalInicial = self.posActual
            while self.asomar().isalpha():
                self.siguiente()
            lexema = self.fuente[pospalInicial : self.posActual+1]
            token = Token(lexema, TipoToken.STRING)
              
        #Token desconocido        
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
    NUMERO = 1 #si
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
    EQ = 201 #= 2
    PLUS = 202 #+ 
    MINUS = 203 #- 
    ASTERISK = 204 #* 
    SLASH = 205 #/ 
    EQEQ = 206 #== 2
    NOTEQ = 207 #!= 2
    LT = 208 #< 2
    LTEQ = 209 #<= 2
    GT = 210 #> 2
    GTEQ = 211 #>= 2
    

def test():
    return print("import lexer.py :)")