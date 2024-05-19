import sys

while True:
    N = int(sys.stdin.readline().strip())
    if N == 0:
        break

    shirts = []
    for _ in range(N):
        name = sys.stdin.readline().strip()
        color, size = sys.stdin.readline().strip().split()
        shirts.append((name, color, size))

    shirts.sort(key=lambda x: (x[1], x[2], x[0]))

    for name, color, size in shirts:
        print(name)
        print(color, size)
    print()
    
    
    
    
    
    
    
    
    
from collections import Counter
import sys

def calcular_fracao_populacao(arvores):
    
    total_arvores = len(arvores)
    contagem_arvores = Counter(arvores)
    especies_unicas = sorted(contagem_arvores.keys())
    
    for especie in especies_unicas:
        fracao = contagem_arvores[especie] / total_arvores * 100
        
        print(f"{especie} {fracao:.4f}")

def processar_casos_teste():
    num_casos = int(input())
    input()
    
    for i in range(num_casos):
        arvores = []
        while True:
            try:
                arvore = input().strip()
                if not arvore:
                    break
                arvores.append(arvore)
            except EOFError:
                break
        
        calcular_fracao_populacao(arvores)
        if i != num_casos - 1:
            print()

try:
    processar_casos_teste()
except EOFError:
    sys.exit(0)
    
    
    
    
    
    
    
    
    
import math

while True:
    try:
        N = int(input())
        H, C, L = map(int, input().split())

        area_total = N * math.sqrt(H**2 + C**2) * L / 10000

        print('{:.4f}'.format(area_total))
    except EOFError:
        break