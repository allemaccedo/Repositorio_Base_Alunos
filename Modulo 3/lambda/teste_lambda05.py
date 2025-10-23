jogadores = [
    
    {'nome': 'Samuel', 'score': 1200, 'level': 15},
    {'nome': 'Lazaro', 'score': 950, 'level': 12},
    {'nome': 'Kety', 'score': 200, 'level': 3},
    {'nome': 'Afonso', 'score': 1500, 'level': 18},
    {'nome': 'Vitoria', 'score': 400, 'level': 5}

]

ranking = sorted(jogadores, key=lambda jogador: jogador['score'], reverse=True)
for jogador in ranking:
    print(jogador)