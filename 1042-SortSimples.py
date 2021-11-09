n1, n2, n3 = map(int, input().split(" "))

#N1 maior
if (n1>n2 and n1>n3):
    v3 = n1
    if (n2>n3):
        v2 = n2
        v1 = n3
    if (n2<n3):
        v2 = n3
        v1 = n2
# N2 maior
if (n2>n1 and n2>n3):
    v3 = n2
    if (n1>n3):
        v2 = n1
        v1 = n3
    if (n1<n3):
        v2 = n3
        v1 = n1
# N3 maior
if (n3>n1 and n3>n2):
    v3 = n3
    if (n1>n2):
        v2 = n1
        v1 = n2
    if (n1<n2):
        v2 = n2
        v1 = n1
print (v1)
print (v2)
print (v3)
print ()
print (n1)
print (n2)
print (n3)