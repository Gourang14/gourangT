'''# case 1
a =
b =

temp = a
a = b
b = temp

#case 2
a =
b =
a,b = b,a

#case 3
a =
b ='''

#
'''a = int(input("Enter the number:"))
m = int(input("Enter the number in whose base to convert"))

l= []
while a > 1:
    b = a % m
    l.append(b)
    a = a//m
    

l.append(1)
rev = l.reverse()
print(rev)'''

#
def an(i,l):
    m = 0
    t = i
    for j in range(len(str(i))):
        n = i % 10
        m += n ** 3
        i = i // 10

    if t == m:
        l.append(t)
        return l
a = int(input("Enter the number:"))
b = int(input("Enter the ending number:"))

l = []
for i in range(a,b):
    an(i,l)
print(l)
