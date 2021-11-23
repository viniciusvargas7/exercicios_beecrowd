hora_ini, min_ini, hora_fim, min_fim = map(int, input().split(" "))

conv_min_ini = (hora_ini*60) + min_ini
conv_min_fim = (hora_fim*60) + min_fim

if (conv_min_ini < conv_min_fim):
    dif_min = conv_min_fim - conv_min_ini
    if (dif_min < 60):
        duracao_hora = 0
        duracao_min = dif_min
    if (dif_min > 60):
        duracao_hora = dif_min/60
        duracao_hora = int(duracao_hora)
        duracao_min = dif_min-(duracao_hora*60)
        duracao_min = int(duracao_min)

if (conv_min_ini > conv_min_fim):
    dif_min = (1440 - conv_min_ini)+conv_min_fim
    if (dif_min < 60):
        duracao_hora = 0
        duracao_min = dif_min
    if (dif_min > 60):
        duracao_hora = dif_min/60
        duracao_hora = int(duracao_hora)
        duracao_min = dif_min-(duracao_hora*60)
        duracao_min = int(duracao_min)

if (hora_ini == min_ini == hora_fim == min_fim):
    duracao_hora = 24
    duracao_min = 0

print (f"O JOGO DUROU {duracao_hora} HORA(S) E {duracao_min} MINUTO(S)")