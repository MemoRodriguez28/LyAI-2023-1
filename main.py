from lexico import *

fuente = "PRINT a" #Longitud es 7
lexico = Lexico(fuente)

#while len(fuente) != None:
#    lexico.siguiente()

while lexico.asomar() != '\0':
    print(lexico.carActual)
    lexico.siguiente()