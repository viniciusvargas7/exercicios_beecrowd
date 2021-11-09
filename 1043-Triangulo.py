A, B, C = map(float, input().split(" "))

if (((A + B) > C) and ((A + C) > B) and ((C + B) > A)):
    r = A + B + C
    print (f"Perimetro = {r:.1f}")
else:
    r = ((A + B) * C) / 2
    print (f"Area = {r:.1f}")