def soma(x, y):
    return x + y
def subtracao(x, y):
    return x - y
def multiplicacao(x, y):
    return x * y
def divisao(x, y):
    if y == 0:
        return 'error'
    else:
        return x/y
    
def calculadora():
    x = float(input("insira o numero: "))
    y = float(input("insira o numero: "))
    op = (input("operação: "))
    if op == "divisão":
        print (divisao(x, y))
    elif op == "soma":
        print (soma(x, y))
    elif op == "subtração":
        print (subtracao(x, y))
    elif op == "multiplicação":
        print (multiplicacao(x, y))
    else: 
        print("operacao nao correta")

calculadora()


def dia_semana(d):
    if d == 7:
        return "sabado"
    elif d == 6:
        return "sexta"
    elif d == 5:
        return "quinta"
    elif d == 4:
        return "quarta"
    elif d == 3:
        return "terça"
    elif d == 2:
        return "segunda"
    elif d == 1:
        return "domingo"
    else:
        return ''
    
print(dia_semana(2)) # segunda-feira
print(dia_semana(6)) # sexta-feira
print(dia_semana(7)) # sábado
print(dia_semana(9)) # string vazia


def determina_tipo_triangulo(x, y, z):
    if x >= y + z or y >= x + z or z >= x + y:
        return 'nao existe'
    elif x == y == z:
        return 'equilatero'
    elif y == x or y == z or x == z:
        return 'isósceles'
    else:
        return 'escaleno'
print(determina_tipo_triangulo(4, 4, 4)) # Equilátero
print(determina_tipo_triangulo(2, 4, 4)) # Isósceles
print(determina_tipo_triangulo(3, 4, 5)) # Escaleno
print(determina_tipo_triangulo(1, 1, 4)) # Não é um triângulo