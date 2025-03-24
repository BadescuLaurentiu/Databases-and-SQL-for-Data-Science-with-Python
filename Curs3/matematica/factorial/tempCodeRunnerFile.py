n = 6
lista_factorial = [] # (6!, 720), (5!, 120), (4!, 24)    
for i in range(n, -1, -1):
    lista_factorial.append((i, factorial(i)))

print(lista_factorial)