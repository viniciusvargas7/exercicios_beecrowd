A, B, C = map(float, input().split(" "))
iso = False

# Ordena em ordem decrescente
if (A > B and A > C):
    dA = A
    if (B > C):
        dB = B
        dC = C
    if (B < C):
        dB = C
        dC = B
if (B > A and B > C):
    dA = B
    if (A > C):
        dB = A
        dC = C
    if (A < C):
        dB = C
        dC = A
if (C > A and C > B):
    dA = C
    if (A > B):
        dB = A
        dC = B
    if (A < B):
        dB = B
        dC = A
if (A == B == C):
    dA = A
    dB = A
    dC = A
else:
    if (A == B and A > C) or (A == C and A > B):
        if (A == B):
            dA = A
            dB = A
            dC = C
            iso = True
        if (A == C):
            dA = A
            dB = A
            dC = B
            iso = True
    if (B == A and B > C) or (B == C and B > A):
        if (B == A):
            dA = B
            dB = B
            dC = C
            iso = True
        if (B == C):
            dA = B
            dB = B
            dC = A
            iso = True
    if (C == A and C > B) or (C == B and C > A):
        if (C == A):
            dA = C
            dB = C
            dC = B
            iso = True
        if (C == B):
            dA = C
            dB = C
            dC = A
            iso = True
#==================================================================
    if (A == B and A < C) or (A == C and A < B):
        if (A == B):
            dA = C
            dB = A
            dC = A
            iso = True
        if (A == C):
            dA = B
            dB = A
            dC = A
            iso = True
    if (B == A and B < C) or (B == C and B < A):
        if (B == A):
            dA = C
            dB = B
            dC = B
            iso = True
        if (B == C):
            dA = A
            dB = B
            dC = B
            iso = True
    if (C == A and C < B) or (C == B and C < A):
        if (C == A):
            dA = B
            dB = C
            dC = C
            iso = True
        if (C == B):
            dA = A
            dB = C
            dC = C
            iso = True

# Define tipo de triângulo
if (dA >= (dB + dC)):
    print("NAO FORMA TRIANGULO")
else:
    if ((dA * dA) == (dB * dB) + (dC * dC)):
        print("TRIANGULO RETANGULO")
    if ((dA * dA) > (dB * dB) + (dC * dC)):
        print("TRIANGULO OBTUSANGULO")
    if ((dA * dA) < (dB * dB) + (dC * dC)):
        print("TRIANGULO ACUTANGULO")
    if (dA == dB == dC):
        print("TRIANGULO EQUILATERO")
    if (iso == True):
        print("TRIANGULO ISOSCELES")
