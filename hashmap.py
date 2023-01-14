# understans scenarios where hashmap works
#for any problem where you need to parse thru a list use dict
lista = [1,1,2,3,4,3,5,6,5,4,3,7,6,5,4]
mapa = {}
for i in lista:
    if i not in mapa:
        #assign the key a value of 1 if it doesn't exist
        mapa[i] = 1
    else:
        #if the key exist, just add 1 to the previos value
        mapa[i] += 1
#this way you will have a dict with each element of the list x the amout
#of times it appears in the list
print(mapa)
