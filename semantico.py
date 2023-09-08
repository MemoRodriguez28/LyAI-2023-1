import sys
from lexico import *

class Semantico:
    def __init__(self):
        self.variables = set() #Variables
        self.labelsDeclaradas = set() #Labels
        self.labelsGoto = set() #Labels a las que se a saltado (GOTO)
        
        def abortar(self, mensaje):
            sys.exit("Error: " + mensaje)
        #def revisarLabel(TipoToken.LABEL):
            #if self.tokenActual.lexema in self.labelsDeclaradas: #ID
                #self.abortar("Ese Label (Etiqueta) ya existe: " + self.tokenActual.lexema)
        #def agregarlabel():
            #self.labelsDeclaradas.add(self.tokenActual.lexema) #Agregando las labels declaradas
            #self.match(TipoToken.ID)
        
        
        
        
        def revisarVariable(self, variable):
            pass
        def agregarVariable(self, variable):
            pass