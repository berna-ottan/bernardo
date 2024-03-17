def eq_seg_grau(a, b, c):
    delta = b**2 - 4*a*c
    x1 = ((-b + delta**0.5) / (2*a))
    x2 = ((-b - delta**0.5) / (2*a))
    print("o valor de x1 é", x1)
    print("o valor de x2 é", x2)

eq_seg_grau(-1, -5, 6)

# parte 2 do trabalho

def bissexto(ano):
    print ((ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0)

bissexto(1600)
bissexto(1900)

# exercício 2

def calcula_salario(valor_hora, num_horas, irpf=0.275):
    valorbruto = valor_hora * num_horas
    impostoderenda = valorbruto * irpf
    print (valorbruto - impostoderenda)