def RPN(infija): #Se recibe un string
    operadores = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0, ')': 0}
    stack = [] #Stack de operadores
    postfija = ""
    
    for i in infija: #Cada i es un caracter
        if i not in operadores.keys():
            postfija += i #Concatencion de strings
            #Agregamos los operandos
        elif i == '(':
            stack.append(i)
        elif i == ')':
            operador_stack = stack.pop() #Sacamos el operador
            while operador_stack != '(': #Revisamos si es (
                postfija += operador_stack #Se agrega el operador a postfija
                operador_stack = stack.pop() #Se repite el ciclo
        else:
            while (len(stack) != 0) and (operadores[i] <= operadores[stack[-1]]): 
                postfija += stack.pop()
            stack.append(i)
    while len(stack) != 0:
        postfija += stack.pop()
            
    return postfija


print(RPN("a+b*c"))
