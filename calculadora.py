from function import *

print("=======================")
print("Bem vindo a Calculadora")
print("=======================")

num1 = menux()
num2 = menuy()

operacao = op()
if operacao == 1:
  soma(num1, num2)
elif operacao == 2:
  subtracao(num1, num2)
elif operacao == 3:
  multiplicacao(num1, num2)
elif operacao == 4:
  divisao(num1, num2)
elif operacao == 5:
  potencia(num1, num2)
elif operacao == 6:
  raiz(num1, num2)
else:
  print("\nDigite uma operação válida!")