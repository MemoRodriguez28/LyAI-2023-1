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
    
    #------Reglas de producccion (Son 9 en total)--------
    #programa ::= sentencia* (Cero o mas veces)
    def programa(self):
        #Checar que no sea un EOF
        while not self.revisarToken(Token(TipoToken.EOF)):
            self.sentencia()
    
    #sentencia ::= (‘IF’ comparación ‘THEN’ nl (sentencia)* ‘ENDIF’ ) 
    # | (‘PRINT’ (expr | STRING) ) | (
    # ‘WHILE’ comparacion ‘REPEAT’ nl (sentencia)* ‘ENDWHILE’ ) 
    # | (‘LABEL’ ID )
    # | (‘GOTO’ ID ) 
    # | (‘LET’ ID ‘=’ expr )
    # | (‘INPUT’ ID )
    def sentencia(self):
        # ‘IF’ comparación ‘THEN’ nl (sentencia)* ‘ENDIF’ 
        if self.revisarToken(Token(TipoToken.IF)): #revisarToken (If/While) y regresa true
            self.siguienteToken()
            self.comparacion()
            
            self.match(Token(TipoToken.THEN)) #Si es pasa al siguiente; si no es, error
            self.nl()
            
            #(sentencia)*
            while not self.revisarToken(Token(TipoToken.EOF)):
                self.sentencia()
            
            self.match(Token(TipoToken.ENDIF))
            
        #Newline final
        self.nl()
            
    
    #comparacion::= expr (opComp expr)+
    def comparacion(self):
        pass
    
    #expr::= termino ((‘+’ | ‘-‘ ) termino)*
    def expr(self):
        pass
    
    #termino::= unario ((‘*’ | ‘/‘ ) unario)+
    def termino(self):
        pass
    
    #unario::= ( ‘+’ | ‘-‘)? primario
    def unario(self):
        pass
    
    #primario::= NUMERO | ID
    def primario(self):
        pass
    
    #opComp::= ‘==’ | ‘!=’ | ‘>’ | ‘>=’ | ‘<’ | ‘<=’
    def opComp(self):
        pass
    
    #nl::= ‘\n’+
    def nl(self):
        pass