print('-='*20)
print('Analisador de triângulos')
print('-='*20)
r1=int('Primeiro segmento')
r2=float('Segundo segmento')
r3=float('Terceiro segmento')
if r1 < r2+r3 and r3 < r1+r2 and r2 < r1+r3:
    print('Os segmentos acima pdem formar triângulo')
else:
    print('Os segmentos acima não podem formar um triângulo')
