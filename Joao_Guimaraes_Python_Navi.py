# Exemplo 1
import math
print("Exercicio 1:\n")
i = 2*49*37
Resultado = math.floor(5000000/i)
print("O numero de valores que obedecem as tres condições e", Resultado)

# Exemplo 2
print("\n\nExercicio 2:\n")


def Fatorial(num):
    if num < 0:
        print("Numero negativo nao tem fatorial")

    elif num == 0:
        return 1

    else:
        fact = 1
        while(num > 1):
            fact *= num
            num -= 1
        return fact


Lista = []
i = 0
while(i < 10):
    if(i % 2 == 0):
        Lista.append(3+7*Fatorial(i))
    else:
        Lista.append(2**i + 4*math.log(i))
    i += 1

indice = Lista.index(max(Lista))
media = sum(Lista)/10

print("O indice do maior termo e", indice,
      '\nA media dos valores dessa lista e de %.2f' % media)

# Exemplo 3
print("\n\nExercicio 3:\n")
Dicionario = {}
i = 0
while(i < 5):
    i += 1
    key = input("Qual o nome do aluno {}: ".format(i))
    nota = float(input("Qual a nota do aluno {}: ".format(i)))
    Dicionario.update({key: nota})
print(Dicionario)
alunomax = max(Dicionario, key=Dicionario.get)
print("A nota maxima foi alcancada por", alunomax,
      "e essa nota foi de %.2f" % Dicionario[alunomax])
