operadores = ['+','-','*','/','|','&']








soma = lambda lista : int(lista[0]) if (len(lista) == 1) else int(lista[0]) + int(soma(lista[1:]))

subtrair = lambda lista: int(lista[0]) if (len(lista) == 1) else  int(subtrair(lista[0:-1]))-int(lista[-1])

multiplicasao = lambda lista: int(lista[0]) if(len(lista)==1) else int(lista[0])*int(multiplicasao(lista[1:]))

divisao = lambda lista: int(lista[0]) if (len(lista)==1) else int(divisao(lista[0:-1]))/int(lista[-1])

exponenciasao = lambda lista: int(lista[0]) if (len(lista)==1) else int(exponenciasao(lista[0:-1]))**int(lista[-1])




def calcula(Formula):
    analisador = []
    while (Formula != []):
        if(Formula[0] == '('):
            analisador.append(calcula(Formula[1:]))
            for i in range(0,Formula.index(')')+1):
                Formula.pop(0)                          #(a ( b c +)+) -> ( a d +)
        elif(Formula[0] == ')'):
            return analisador[-1]
        elif(Formula[0].isnumeric()):            #0~...
            analisador.append(Formula[0])
            Formula.pop(0)
        else:
            if(Formula[0] == '+'):  #soma
                x = soma(analisador)
            elif(Formula[0] == '-'):  #subtrair
                x = subtrair(analisador)
            elif(Formula[0] == '*'):  #multiplicar
                x = multiplicasao(analisador)
            elif(Formula[0] == '/'):  #dividir
                x = divisao(analisador)
            elif(Formula[0] == '|'):  #exponenciação
                x = exponenciasao(analisador)
            elif(Formula[0] == '&'):  #raiz quadrada
                x = int(analisador[0])**0.5 # a diferença dele e sqrt só aparece após 971
            analisador.clear()
            analisador.append(x)
            Formula.pop(0)




def preparar(calculo):
    calculo = calculo.replace('('," ( ")
    calculo = calculo.replace(')'," ) ")
    return calculo.split( )

def verifica(calculo):
    conta = []
    if(calculo[0]!='('): return False    # 1 2 +
    for i in calculo:
        if( not(i.isnumeric()) and (i not in operadores) and ('('!= i !=')') and i!=' '):   # 1 a +
            return False
        elif(i == '('):
            conta.append('(')
        elif(i == ')'):
            if(len(conta)!= 0):
                conta.pop(0)
            else:
                return False              # ( 1 2 + ))
    if(len(conta)!=0):                    # (( 1 2 + )
        return False
    return True                           # ((1 2 +))


def menu():
    calcular = input('Digite a formula:')
    if(verifica(calcular)):
        Novo = preparar(calcular)
        Resposta = calcula(Novo[1:])
        print(Resposta)
    else:
        print('Syntax error')
menu()
