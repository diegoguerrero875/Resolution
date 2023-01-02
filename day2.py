#In this python file I will list the problems that come to my mind when thinking on my journey as well as things that in the begging where very difficult to me and now I can do without thinking much, this is day 2 of my challenge to do something code related everyday for a year and uploaded to github via Git commands.

#get the biggest number from a list
def biggest_num():
    example_list = [1,2,3,4,5,6,7,8,9]
    c = 0
    for i in example_list:
        if  i > c:
            c = i
    print(f'The biggest number in the list is {c}')


#prime number
def prime_num(x):
    isPrime = True
    for i in range(2,x):
        if i % x == 0:
            isPrime = False
    print(f'The number {x} is prime ? {isPrime}')

#fibbonacci
def fibb(n):
    a = 0
    b = 1
    c = 0
    for i in range(1,n):
        c = a + b
        a = b
        b = c
    print(c)

fibb(8)
