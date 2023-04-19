class Lexico:
    def __init__(self, fuente):
        #Se pasa el código fuente como cadena. Se le agrega newline para simplificar el análisis para el último token/sentencia.
        self.fuente = fuente + '\n' 
        self.carActual = ''     #Caracter actual en la cadena.
        self.posActual = -1     #Posición actual en la cadena.
        self.siguiente()

    #Leer el siguiente caracter.
    def siguiente(self):
        self.posActual += 1 #Posición actual = 7 (8)
        if self.posActual >= len(self.fuente):
            self.carActual = '\0' #End of file EOP
        else:
            self.carActual = self.fuente[self.posActual] 

    #Regresar el caracter adelante (lookahead).
    def asomar(self):
        #self.posActual += 1
        if self.posActual + 1 >= len(self.fuente):
            return '\0'
        return self.fuente[self.posActual + 1]
    
    #Token inválido, imprimir error y salir.
    def abortar(self, message):
        pass

    #Saltar espacios excepto \n, estas se utilizarán para indicar el final de una sentencia.
    def saltarEspacio(self):
        pass

    #Saltar comentarios en el código.	
    def saltarComentarios(self):
        pass
    
    #Regresar el siguiente token.
    def getToken(self):
        pass

def test():
    return print("import lexer.py :)")