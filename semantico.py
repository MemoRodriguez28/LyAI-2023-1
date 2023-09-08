import sys
from lexico import *

class Semantico:
    def __init__(self):
        self.variables = set() #Variables
        self.labelsDeclaradas = set() #Labels
        self.labelsGoto = set() #Labels a las que se a saltado (GOTO)
        
    def abortar(self, mensaje):
        sys.exit("Error: " + mensaje)

    def revisarVariable(self, variable):
        if variable not in self.variables:
            self.abortar("La variable no ha sido declarada: " + variable)
            
    def agregarVariable(self, variable):
        if variable not in self.variables:
             self.variables.add(variable)
    
    def revisarLabelDeclarada(self, etiqueta):
        if etiqueta in self.labelsDeclaradas: 
            self.abortar("Ese Label (Etiqueta) ya existe: " + etiqueta)
                
    def agregarLabelDeclarada(self, etiqueta):
        if etiqueta not in self.labelsDeclaradas:
            self.variables.add(etiqueta)
    
    def revisarLabelGoto(self, etiqueta):
        if etiqueta in self.labelsGoto: 
            self.abortar("Ese Label (Etiqueta) ya existe: " + etiqueta)