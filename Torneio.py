import lib.cadastro_e_chaveamento

times = dict()

# Determinando a quantidade de equipes

num_de_equipes = (input('Quantas equipes participarão do torneio?').strip())
if num_de_equipes.isnumeric():
    num_de_equipes = int(num_de_equipes)

# Determinando os nomes das equipes

for c in range(1, num_de_equipes+1): 
    nome_da_equipe = str(input(f'Qual o nome da {c}ª equipe? ').strip().lower())
    # Cadastro de atletas
    times[nome_da_equipe] = lib.cadastro_e_chaveamento.cadastro_de_atletas()

print(times)
