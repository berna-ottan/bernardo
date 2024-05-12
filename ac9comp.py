#1
def calcular_tempo(distancia):
    tempo = distancia / (90 - 60)
    tempo_minutos = tempo * 60
    return tempo_minutos

distancia = int(input())

tempo_necessario = calcular_tempo(distancia)

print(f"{int(tempo_necessario)} minutos")


#2
def calcular_fatorial(n):
    if n == 0:
        return 1
    else:
        return n * calcular_fatorial(n - 1)

n = int(input())

if 0 < n < 13:
    resultado = calcular_fatorial(n)
    print(resultado)
else:
    print("O valor de N deve estar entre 1 e 12.")
    
    
    
#3
def calcular_gasto(produtos_disponiveis, produtos_desejados):
    total = 0
    for produto, quantidade in produtos_desejados:
        for p, preco in produtos_disponiveis:
            if p == produto:
                total += preco * quantidade
                break
    return total

def main():
    casos_teste = int(input())

    for _ in range(casos_teste):
        m = int(input())
        produtos_disponiveis = []
        for _ in range(m):
            produto, preco = input().split()
            produtos_disponiveis.append((produto, float(preco)))

        p = int(input())
        produtos_desejados = []
        for _ in range(p):
            produto, quantidade = input().split()
            produtos_desejados.append((produto, int(quantidade)))

        gasto_total = calcular_gasto(produtos_disponiveis, produtos_desejados)
        print("R$ {:.2f}".format(gasto_total))

if __name__ == "__main__":
    main()
    
    
    
    
    
#4
def contar_respostas_corretas(tipo_cha, respostas):
    corretas = respostas.count(tipo_cha)
    return corretas

tipo_cha = int(input())
respostas = list(map(int, input().split()))

print(contar_respostas_corretas(tipo_cha, respostas))




#5
C, P, F = map(int, input().split())

total_folhas_necessarias = C * F

if total_folhas_necessarias <= P:
    print('S')
else:
    print('N')
    
    
    
#6
def calcular_distancia(tempo, velocidade):
    return tempo * velocidade

N = int(input())

distancia_total = 0

for _ in range(N):
    tempo, velocidade = map(int, input().split())
    distancia_total += calcular_distancia(tempo, velocidade)
print(distancia_total)



#7 
t =int(input())

print(4 * t)





#8
N = int(input())

sequencia = []
for _ in range(N):
    sequencia.append(int(input()))

numeros_marcados = 1   

for i in range(1, N):
    if sequencia[i] != sequencia[i - 1]:
        numeros_marcados += 1
print(numeros_marcados)