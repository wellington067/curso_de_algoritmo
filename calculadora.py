"""Faça uma função calculadora de dois números com três parâmetros: 
os dois primeiros serão os números da operação e o terceiro será a
entrada que definirá a operação a ser executada. Considera a seguinte definição:

1. Soma
2. Subtração
3. Multiplicação
4. Divisão

Caso seja inserido um número de operação que não exista, o resultado deverá ser 0."""




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
    else:
        res = 0
        return res

num1=int(input("digite o primeiro numero: "))
num2= int(input("digite outro numero: "))


print("=======================================================")
print("          qual operação voce quer realizar? ")
print("=======================================================")
print("+ - para adição")
print("- - para subtração")
print("* - para multiplicação")
print("/ - para divisão")
print("=======================================================")
op=input("")

print("o resultado foi: ", calcular(num1, num2, op))


