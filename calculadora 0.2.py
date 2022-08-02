"""Faça uma função calculadora que os números e as operações serão feitas pelo usuário.
O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair.
No início, o programa mostrará a seguinte lista de operações:

1: Soma
2: Subtração
3: Multiplicação
4: Divisão
0: Sair

Digite o número para a operação correspondente e caso o usuário introduza qualquer outro,
o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.

Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada.
Depois precisa executar a operação e mostrar o resultado na tela.
Quando o usuário escolher a opção “Sair”, o sistema irá parar. 

É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado. 
"""




print("--------------------------------------------------------")
print("                     calculadora")
print("--------------------------------------------------------")
print("")
print("")


def calcular(num1, num2, op):
    if op == "+" : 
        res = num1+num2 
        return res
    elif op == "-" :
        res = num1-num2 
        return res
    elif op == "*" : 
        res = num1*num2 
        return res
    elif op == "/" : 
        res = num1/num2 
        return res
    elif op == "0" :
        res=0
        print("sistema finalizado")
        return res
    else:
        res = "essa opção não existe"
        return res

sair=0
while sair==0 :
    
     print("")
     print("------------------------------------------------------")
     print("")
     
     num1=int(input("digite o primeiro número: "))
     num2= int(input("digite o segundo número: "))

     print("=======================================================")
     print("          qual operação você quer realizar? ")
     print("=======================================================")
     print("+ - para adição")
     print("- - para subtração")
     print("* - para multiplicação")
     print("/ - para divisão")
     print("0 - para Sair")
     print("=======================================================")
     op=input("")
    
     if op=="0":
        sair=1
    
     print("o resultado foi: ", calcular(num1, num2, op))

