# # Trabalho AC1
# # Exercício 1 

a = float(input("informe o coeficiente de a: "))
b = float(input("informe o coeficiente de b: "))
c = float(input("informe o coeficiente de c: "))

delta = b**2 - 4*a*c

x1 = ((-b + delta**0.5) / (2*a))
x2 = ((-b - delta**0.5) / (2*a))
print("o valor de x1 é", x1)
print("o valor de x2 é", x2)

# Exercício 2

ano = int(input("Informe um ano: "))

print(ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0)