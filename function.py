import math

def menux():
    x = float(input("\nDigite o primeiro número: "))
    return x

def menuy():
    y = float(input("\nDigite o segundo número: "))
    return y

def op():
    print("\n<1> Soma ")
    print("<2> Subtração ")
    print("<3> Multiplicação ")
    print("<4> Divisão ")
    print("<5> Potencialização ")
    print("<6> Raiz quadrada ")

    operacao = int(input("\nDigite qual operação deseja realizar: "))
    return operacao

def soma(x, y):
    print("\nO valor da soma é de {}" .format(x+y))
    return

def subtracao(x, y):
    sub = x-y
    print("\nO valor da subtração é de {:.1f}" .format(sub))
    return

def multiplicacao(x, y):
    multi = x*y
    print("\nO valor da multiplicação é de {:.1f}" .format(multi))
    return

def divisao(x, y):
    divi = x/y
    print("\nO valor da divisão é de {:.1f}" .format(divi))
    return

def potencia(x, y):
    pot = (pow(x, y))
    print("\nO valor da potencialização é de {:.1f} ".format(pot))
    return

def raiz(x, y):
    rq1 = (math.sqrt(x))
    rq2 = (math.sqrt(y))
    print("\nO valor da Radiciação é de {:.1f} e {:.1f}".format(rq1, rq2))
    return


