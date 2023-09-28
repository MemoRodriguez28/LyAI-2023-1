from RPN import RPN

infija = "x=(a+b)*c-(d+e)"
postfija = RPN(infija)

def TAC(postfija):
    operadores = ['+', '-', '*', '/', '=']
    stack = []
    tac = []
    cont = 1
    
    for i in postfija:
        if i not in operadores:
            stack.append(i)
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            temp = "t" + str(cont)
            cont += 1
            if i == '=':
                tac.append(op1 + ":= " + op2)
            else:
                tac.append(temp + " := " + op1 + i + op2)
                stack.append(temp)
    return tac

print(TAC(postfija))