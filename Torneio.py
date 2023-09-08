import lib.cadastro_e_chaveamento
import lib.interface

torneio = dict()
times = list()

# Determinando a quantidade de equipes
while True:
    num_de_equipes = (input('Quantas equipes participarão do torneio?').strip())
    if num_de_equipes.isnumeric():
        num_de_equipes = int(num_de_equipes)
        break
    else:
        lib.interface.titulo('ERRO! por favor, digite a quantidade de equipes pelo teclado numérico.')

lib.interface.titulo(f'O Torneio Terá {num_de_equipes} Equipes!')

# Determinando os nomes das equipes

for c in range(1, num_de_equipes+1): 
    lib.interface.titulo(f'Equipe {c}...')
    nome_da_equipe = str(input(f'Qual o nome da {c}ª equipe? ').strip().lower())
    times.append(nome_da_equipe)
    lib.interface.titulo(f'Nome da {c}ª equipe definido: {nome_da_equipe}.')
    
    # Cadastro de atletas
    
    torneio[nome_da_equipe] = lib.cadastro_e_chaveamento.cadastro_de_atletas()

# Mostrando Times cadastrados na tela

for i, k in enumerate(times):
    print()
    lib.interface.titulo(k)
    for j in torneio[times[i]]:
        print(j)
        
# Sorteando os confrontos

lib.cadastro_e_chaveamento.sorteio(times)
lib.interface.titulo('Jogos Sorteados!')

# Mostrando os confrontos

print(lib.cadastro_e_chaveamento.mostrar_sorteio(times))