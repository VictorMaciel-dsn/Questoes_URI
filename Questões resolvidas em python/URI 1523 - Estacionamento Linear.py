while True:
    N, K = [int(x) for x in input().split()]  
    if N == K == 0: break
    C = [0] * N
    S = [0] * N
    for i in range(N):
        C[i], S[i] = [int(x) for x in input().split()]
    pilha = []
    resp = 'Sim'
    for i in range(N):
        while len(pilha) > 0 and pilha[-1] <= C[i]:
            pilha.pop()
        if len(pilha) == K or (len(pilha) > 0 and pilha[-1] < S[i]):
            resp = 'Nao' 
            break
        else:
            pilha.append(S[i])    
    print(resp)