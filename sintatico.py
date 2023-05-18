import sys
from lexico import *


class Sintatico:
    def __init__(self, lexico):
        self.lexico = lexico
        self.tokenActual = None #Este es el token actual
        self.asomarToken = None #Este es el token que sigue (pero sin que se guarde)
        self.siguienteToken()
        #Se tiene que llamar dos veces para inicializar actual y asomar
        self.siguienteToken() 
    
    #Regresar true si el token actual es igual (del mismo tipo)    
    def revisarToken(self, tipo):
        if (tipo == self.tokenActual.tipo):
            return True
        #return tipo == self.tokenActual.tipo
        
    #Regresar true si el token siguiente es igual (del mismo tipo)
    def revisarAsomar(self, tipo):
        if (tipo == self.asomarToken.tipo):
            return True
        
    #Revisar si el tipo de token es el esperado     
    def match(self, tipo):
        if not self.revisarToken(tipo): #Si no es el tipo que se estaba esperando
            self.abortar("Se esperaba: " + tipo.name + ", se obtuvo " + self.tokenActual.tipo.name)
        #Si esñ el tipo que se esperaba
        self.siguienteToken()
    
    #Pasar al siguiente token
    def siguienteToken(self, tipo):
        #Remplazara el token actual por el siguiente
        self.tokenActual = self.asomarToken(tipo)
        #Obtiene el token que sigue en el codigo
        self.asomarToken = self.lexico.getToken()
    
    def abortar(self, mensaje):
        sys.exit("Error: " + mensaje)