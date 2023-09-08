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
        self.labelsDeclaradas.add(etiqueta) #Agregando las labels declaradas
    
    def revisarLabelsGoto(self):
       for etiqueta in self.labelsGoto:
            if etiqueta not in self.labelsDeclaradas:
                self.abortar("Se intenta saltar a una etiqueta que no esta declarada " + etiqueta)
    
    def agregarLabelGoto(self, etiqueta):
        self.labelsGoto.add(etiqueta) #Agregando el salto