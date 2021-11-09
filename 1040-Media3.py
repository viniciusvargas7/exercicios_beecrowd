N1, N2, N3, N4 = input().split(" ")
N1 = eval(N1)
N2 = eval(N2)
N3 = eval(N3)
N4 = eval(N4)
media = ((N1*2)+(N2*3)+(N3*4)+(N4*1))/10
print (f"Media: {media:.1f}")

if (media >= 7.0):
    print ("Aluno aprovado.")

if (media < 5.0):
    print ("Aluno reprovado.")

if (media >= 5.0 and media <= 6.9):
    print ("Aluno em exame.")
    n_exame = eval(input())
    print(f"Nota do exame: {n_exame:.1f}")
    m_final = (media + n_exame)/2
    if (m_final >= 5.0):
        print("Aluno aprovado.")
        print(f"Media final: {m_final:.1f}")
    else:
        print("Aluno reprovado.")
        print(f"Media final: {m_final:.1f}")

