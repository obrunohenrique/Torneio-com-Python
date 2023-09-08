import lib.interface

def cadastro_de_atletas():
    try:
        atletas = []
        while True:
            nome = str(input('Digite o nome do atleta: '))
            atletas.append(nome)
            resp = str(input('Deseja continuar o cadastro de atletas? [S/N]: ')).strip().upper()[0]
            if resp == 'N':
                return atletas 
    except Exception as Erro:
        print(f'O erro foi no cadastro de atletas - {Erro}')


def sorteio(times):
    from random import shuffle
    shuffle(times)
    return times


def mostrar_sorteio(times):
    jogos = {}
    cont_de_jogos = 1
    indice = i = 0
    indice_reverso = -1
    while True:
        if i == len(times) / 2:
            break
        else: 
            lib.interface.linha(f'Jogo {cont_de_jogos}:')
            print(times[indice], 'X', times [indice_reverso])
            cont_de_jogos += 1
            indice += 1
            indice_reverso -= 1
            i += 1