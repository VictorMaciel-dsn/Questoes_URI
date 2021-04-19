def corte_bin (C,a):
    ini = 0
    fim = C[-1]
    h = 0
    while True:
        t=0.0000000001 
        corte = (ini + fim) / 2
        if abs(corte - fim) < t:
            return h
        r = sum([c - corte for c in C if c > corte])
        if round(r, 4) == a:
            h =round(corte,4)
            ini = corte
        elif round(r, 4) < a:
            fim = corte
        elif round(r,4) > a:
            ini = corte
while True:
    n, a = [int(x) for x in input().split()]
    if n == 0 and a == 0:
        break
    C = [int(x) for x in input().split()]
    C.sort()
    soma = sum([c for c in C])
    if soma < a:
        print('-.-')
    elif soma == a:
        print(':D')
    else:
        h = corte_bin(C,a)
        print(f'{h:.4f}')