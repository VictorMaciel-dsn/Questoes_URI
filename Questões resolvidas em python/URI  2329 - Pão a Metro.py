def busca(m,n):
    ini = 1
    fim = max(m)
    h = 0
    while True:
        l = []
        corte = (ini + fim) // 2
        for i in range (k):
            l.append(m[i] // corte)
        if fim - ini == 1:
            if h == 0:
                return corte
            else:
                return h
        elif sum(l) == n:
            h = corte
            ini = corte
        elif sum(l) > n:
            ini = corte
        elif sum(l) < n:
            fim = corte
n = int(input())
k = int(input())
m = [int(x) for x in input().split()]
print(busca(m,n))