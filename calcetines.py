#indeepth explination of the socks problem
ar = [1,2,3,4,2,2,1,1,3]
#we innicilized a dict or hashmap to store the number of ocurrenses
canasto = {}
pares = 0
for i in ar:
    if i not in canasto:
        #if  the value is not in the dict it will created and assig 1
        canasto[i] = 1
    else:
        #if it is it will add +1
        canasto[i] += 1
# so at this point our dict looks like this
# canasto = {1:3,2:3,3:2,4:1}
for i in canasto:
    #now it will check the value of each and divided by 2 and floor the result
    pares += canasto[i] // 2
#pares = 3 
print(pares)
