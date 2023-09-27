from RPN import RPN

infija = "x=(a+b)*c-(d+e)"
postfija = RPN(infija)

def TAC(postfija):
    operadores = ['+', '-', '*', '/', '=']
    stack = []
    tac = []
    for i in postfija:
    return TAC