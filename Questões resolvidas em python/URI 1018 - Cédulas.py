valor = int(input())
print(valor)

cedulas = [100, 50, 20, 10, 5, 2, 1]
for cedula in cedulas:
    qtd_cedulas = int(valor / cedula)
    
    print('{} nota(s) de R$ {},00'.format(qtd_cedulas,cedula))
    valor -= qtd_cedulas * cedula