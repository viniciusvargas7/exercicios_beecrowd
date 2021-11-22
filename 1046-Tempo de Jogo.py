inicio, fim = map(int, input().split(" "))

if (inicio < fim):
    duracao = fim-inicio

if (inicio > fim):
    duracao = (24-inicio)+fim

if (inicio == fim):
    duracao = 24

print (f"O JOGO DUROU {duracao} HORA(S)")
