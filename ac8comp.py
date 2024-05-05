def mdc(a, b):
    while b:
        a, b = b, a % b
    return a

def max_figurinhas(f1, f2):
    return mdc(f1, f2)

n = int(input())

for _ in range(n):
    f1, f2 = map(int, input().split())
    print(max_figurinhas(f1, f2))
    
    
    
    

def menor_numero_movimentos_dama(x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        return 0  
    elif x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
        return 1 
    else:
        return 2  


while True:
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0:
        break  
    print(menor_numero_movimentos_dama(x1, y1, x2, y2))
    
    
    
    
    
    
    

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

while True:
    try:
        M, N = map(int, input().split())
        soma = fatorial(M) + fatorial(N)
        print(soma)
    except EOFError:
        break
    
    
    
    
    
    
    
    
def calcular_dias_comida(C):
    dias = 0
    while C > 1:
        C = C / 2
        dias += 1
    return dias

N = int(input())

for _ in range(N):
    C = float(input())
    
    dias = calcular_dias_comida(C)
    print(f"{dias} dias")
    
    
    
    
    
def main():
    n = int(input())

    frequencia = {}

    for _ in range(n):
        num = int(input())
        if num in frequencia:
            frequencia[num] += 1
        else:
            frequencia[num] = 1

    for num in sorted(frequencia.keys()):
        print(f"{num} aparece {frequencia[num]} vez(es)")


if __name__ == "__main__":
    main()










def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    n = int(input()) 
    for _ in range(n):
        x = int(input()) 
        if is_prime(x):
            print("Prime")
        else:
            print("Not Prime")

if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    
while True:
    N = int(input())
    if N == 0:
        break
    
    results = list(map(int, input().split()))
    mary_wins = results.count(0)
    john_wins = results.count(1)
    
    print("Mary won", mary_wins, "times and John won", john_wins, "times")
    
    
    
    
    
    
    
    
    
    
def r(x, y):
    return (3*x)**2 + y**2

def b(x, y):
    return 2*(x**2) + (5*y)**2

def c(x, y):
    return -100*x + y**3

def competicao(x, y):
    resultados = {"Rafael": r(x, y), "Beto": b(x, y), "Carlos": c(x, y)}
    vencedor = max(resultados, key=resultados.get)
    print(vencedor, "ganhou")

# Entrada de dados
N = int(input())
for _ in range(N):
    x, y = map(int, input().split())
    competicao(x, y)   