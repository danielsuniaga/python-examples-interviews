# n = int(input()) 

tupla = tuple(map(int, input().split()))

tupla_cifrada = hash(tupla)

print(tupla_cifrada)


