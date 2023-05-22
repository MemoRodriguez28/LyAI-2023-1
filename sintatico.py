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
        while not self.revisarToken(TipoToken.EOF):
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
        if self.revisarToken(TipoToken.IF): #revisarToken (If/While) y regresa true
            self.siguienteToken()
            self.comparacion()
            
            self.match(TipoToken.THEN) #Si es pasa al siguiente; si no es, error
            self.nl()

            #(sentencia)*
            while not self.revisarToken(TipoToken.EOF):
                self.sentencia()
            
            self.match(TipoToken.ENDIF)

        #‘PRINT’  (expr | STRING) == 'PRINT' expr | 'PRINT' STRING
        elif self.revisarToken(TipoToken.PRINT):
            self.siguienteToken()
            if self.revisarToken(TipoToken.STRING):
                self.siguienteToken()
            else:
                self.expr()
    
        #‘WHILE’ comparación ‘REPEAT’ nl (sentencia)* ‘ENDWHILE’
        elif self.revisarToken(TipoToken.WHILE):
            self.siguienteToken()
            self.comparacion()
            self.match(TipoToken.REPEAT)
            self.nl()
            while not self.revisarToken(TipoToken.EOF): #sentencia*
                self.sentencia()
            self.match(TipoToken.ENDWHILE)
            
        #'LABEL' ID
        elif self.revisarToken(TipoToken.LABEL):
            self.siguienteToken()
            self.match(TipoToken.ID)
            
        #'GOTO' ID
        elif self.revisarToken(TipoToken.GOTO):
            self.siguienteToken()
            self.match(TipoToken.ID)
        
        #'LET' ID '=' expr == ['LET' ID EQ expr]
        elif self.revisarToken(TipoToken.LET):
            self.siguienteToken()
            self.match(TipoToken.ID)
            self.match(TipoToken.EQ)
            self.expr()
        
        #'INPUT' ID
        elif self.revisarToken(TipoToken.INPUT):
            self.siguienteToken()
            self.match(TipoToken.ID)
        
        else:
            self.abortar("Sentencia no válida en " + self.tokenActual.text + "(" + self.tokenActual.tipo.name + ")")
               
        #Newline final
        self.nl()
            
    
    #comparacion::= expr (opComp expr)+
    def comparacion(self):
         self.expr()
         if self.opComp(): #if True [1 vez]
            self.siguienteToken()
            self.expr()
         else: #si no es un operador de comparación, entonces está mal
            self.abortar("Se esperaba un operador de comparación en: " + self.tokenActual.text)
        
         while self.opComp(): #if True [más veces]
            self.siguienteToken()
            self.expr()
    
    #expr::= termino ((‘+’ | ‘-‘ ) termino)*
    def expr(self):
        self.termino()
        while self.revisarToken(TipoToken.PLUS) or self.revisarToken(TipoToken.MINUS): #*
            self.siguienteToken()
            self.termino()
    
    #termino::= unario ((‘*’ | ‘/‘ ) unario)+
    def termino(self):
        self.unario()
        while self.revisarToken(TipoToken.ASTERISK) or self.revisarToken(TipoToken.SLASH):
            self.siguienteToken()
            self.unario()
    
    #unario::= ( ‘+’ | ‘-‘)? primario
    def unario(self):
        pass
    
    #primario::= NUMERO | ID
    def primario(self):
        pass
    
    #opComp::= ‘==’ | ‘!=’ | ‘>’ | ‘>=’ | ‘<’ | ‘<=’
    def opComp(self):
         if (self.revisarToken(TipoToken.EQEQ) or self.revisarToken(TipoToken.NOTEQ)
            or self.revisarToken(TipoToken.GT) or self.revisarToken(TipoToken.GTEQ) 
            or self.revisarToken(TipoToken.LT) or self.revisarToken(TipoToken.LTEQ)):
            return True
        #return self.revisarToken(TipoToken.EQEQ) or ...
    
    #nl::= ‘\n’+
    def nl(self):
        pass