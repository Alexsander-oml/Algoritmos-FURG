N = int(input('Digite um número inteiro entre 1000 e 9999: '))


while N < 1000 or N > 9999:
    N = int(input('Digite um número VÁLIDO inteiro entre 1000 e 9999: '))

A = N // 1000            
B = (N // 100) % 10      
C = (N // 10) % 10       
D = N % 10               

V = 0
V += D * 1000            
V += C * 100             
V += B * 10              
V += A * 1               

# Exibindo o número invertido
print(f'{V}')
