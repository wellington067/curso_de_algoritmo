"""
PROBLEMA:

Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou,
ou completará, no ano atual (2022).

Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o 
erro e continuará perguntando até que um valor correto seja preenchido.
"""


print("========================================")
print("    forneça seus dados corretamente")
print("========================================")
print("")
print("")

nome_completo = input("nome completo: ")
ano_nascimento = int(input("ano de nascimento: "))

while ano_nascimento < 1922 or ano_nascimento > 2021 :
    print("por favor, digite um ano de nascimento válido.")
    print("")
    ano_nascimento= int(input("ano de nascimento: "))

idade = 2022 - ano_nascimento

print("")
print("")
print("------------------------------------------------------------------")
print("     ",nome_completo, "você fez ou fará", idade, "anos em 2022.")
print("------------------------------------------------------------------")
