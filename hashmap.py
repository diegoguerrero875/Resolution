# understans scenarios where hashmap works

lista = [1,1,2,3,4,3,5,6,5,4,3,7,6,5,4]
mapa = {}
for i in lista:
    if i not in mapa:
        mapa[i] = 1
    else:
        mapa[i] += 1

print(mapa)
