A, B, C = map(float, input().split(" "))

# Ordena em ordem decrescente
if (A > B and A > C):
    dA = A
    if (B > C):
        dB = B
        dC = C
    if (B < C):
        dB = C
        dC = B
    else:
        dB = B
        dC = B
if (B > A and B > C):
    dA = B
    if (A > C):
        dB = A
        dC = C
    if (A < C):
        dB = C
        dC = A
    else:
        dB = A
        dC = A
if (C > A and C > B):
    dA = C
    if (A > B):
        dB = A
        dC = B
    if (A < B):
        dB = B
        dC = A
    else:
        dB = A
        dC = A
if (A == B == C):
    dA = A
    dB = A
    dC = A

# print (dA)
# print (dB)
# print (dC)

# Define tipo de triângulo
if (dA >= (dB + dC)):
    print("NAO FORMA TRIANGULO")
if ((dA * dA) == (dB * dB) + (dC * dC)):
    print("TRIANGULO RETANGULO")
if ((dA * dA) > (dB * dB) + (dC * dC)):
    print("TRIANGULO OBTUSANGULO")
if ((dA * dA) < (dB * dB) + (dC * dC)):
    print("TRIANGULO ACUTANGULO")
if (dA == dB == dC):
    print("TRIANGULO EQUILATERO")
