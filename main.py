from lexico import *
from sintatico import *
import sys

def main():
    print("CompiladorCito")
    
    if len(sys.argv) != 2:
        sys.exit("Error: Se necesita un archivo fuente para poder compilar.")
    with open(sys.argv[1], 'r') as archivo:
        fuente = archivo.read()


    lexico = Lexico(fuente) #Analizador lexico
    sintatico = Sintatico(lexico) #Analizador sintatico
    
    sintatico.programa() #Empezar el analizador sintatico
    print("Analisis completo.")
    
    
main()



#codigo = "<= == + * != - / >= #Comentario\n 12.3 \"pepe\" IF var = 0 "
#codigo = "LET var = 1\n var = var + 2\n PRINT \"Var: \" + var "
#token = lexico.getToken()
#Siempre y cuando no sea EOF, continuar leyendo tokens
#while token.token != TipoToken.EOF:
    #print(token.token)
    #token = lexico.getToken()
    