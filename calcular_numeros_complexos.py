"""Crie um tipo abstrato de dado (TAD) para manipular números
complexos na linguagem Python.
O método deve:

- calcular três números complexos;
- realizar todas as operações básicas;
- e imprimir as propriedades real e img do números. 
"""

a = complex(3,7)
b = complex(8,9)
c = complex(2,5)

print(a+b)
print(b-c)
print(a*b)
print(c/b)

print(a.imag)
print(a.real)
print(b.imag)
print(b.real)
print(c.imag)
print(c.real)
