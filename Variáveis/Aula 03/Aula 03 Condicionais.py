# Modulos aula 03

import math
from operator import truediv

num = 17
raiz = math.sqrt(num)
print(f'A raiz de num é {raiz:.2f}')  #Ao adicionar :.2f, ele arrredonda para 2 casas decimais. Pode ser infinitos número

graus = 45

radiano = graus / 180 * math.pi
seno = math.sin(radiano)
print(seno)

import random

num_rand = random.random()
print(num_rand)


# Como criar essas funções?


def print_lyrics():
    print("I ain't gonna live forever")
    print("I just want to live while I'm alive")

print_lyrics()

print(type(print_lyrics))

# Condicionais

nota_final = 4

if nota_final < 4:
    print("Reprovado")

else:
    if nota_final < 6:
        print("recuperação")


print("Fim")


# Operadores lógicos

verfica_email = True
verifica_senha = True

verifica_login = verfica_email and verifica_senha
print(verifica_login)

if verifica_login:
    print("Entrar no programa")


#lógica ou (or)

logica_ou = False or True
print(logica_ou)


# Operador not

negacao = not False
print(negacao)

if not verifica_login:
    print("Loga certo ai cara")


 # Match case
 
 # 0 = sair do programa
 # 1 = entrar no programa

match escolha_usuario:
     case 0:
         print("Sair do programa")
     case 1:
         print("Entrar no programa")
     case _:
        print("Erro no programa")





