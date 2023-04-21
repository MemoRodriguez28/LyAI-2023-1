from lexico import *

codigo = "+*-/"

lexico = Lexico(codigo)
token = lexico.getToken()
#Siempre y cuando no sea EOF, continuar leyendo tokens
while token.token != TipoToken.EOF:
    print(token.token)
    token = lexico.getToken()