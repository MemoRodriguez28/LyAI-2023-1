from lexico import *

#codigo = "<= == + * != - / >= #Comentario\n 12.3 \"pepe\" IF var = 0 "
codigo = "LET var = 1\n var = var + 2\n PRINT \"Var: \" + var "

lexico = Lexico(codigo)
token = lexico.getToken()
#Siempre y cuando no sea EOF, continuar leyendo tokens
while token.token != TipoToken.EOF:
    print(token.token)
    token = lexico.getToken()
    