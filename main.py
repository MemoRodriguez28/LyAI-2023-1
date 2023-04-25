from lexico import *

codigo = "<= == + * != - / >= 12.3 pedro"

lexico = Lexico(codigo)
token = lexico.getToken()
#Siempre y cuando no sea EOF, continuar leyendo tokens
while token.token != TipoToken.EOF:
    print(token.token)
    token = lexico.getToken()
    