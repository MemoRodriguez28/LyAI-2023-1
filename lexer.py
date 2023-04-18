class Lexer:
    def __init__(self, fuente):
        #Se pasa el código fuente como cadena. Se le agrega newline para simplificar el análisis para el último token/sentencia.
        self.fuente = fuente + '\n' 
        self.carActual = ''     #Caracter actual en la cadena.
        self.posActual = -1     #Posición actual en la cadena.
        self.siguiente()

    #Leer el siguiente caracter.
    def siguiente(self):
        pass

    #Regresar el caracter adelante (lookahead).
    def asomar(self):
        pass
    
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