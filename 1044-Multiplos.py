A,B = map(int, input().split(" "))

#treinando o uso de funções
def validaMultiplo (A,B):
    resto1 = B%A
    resto2 = A%B
    if ((resto1 != 0) and (resto2 !=0)):
        result = False
        print ("Nao sao Multiplos")
    else:
        result = True
        print ("Sao Multiplos")
    return result

validaMultiplo(A,B)



