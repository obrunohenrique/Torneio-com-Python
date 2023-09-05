import lib.cadastro_e_chaveamento

times = dict()

nome_da_equipe = str(input('Qual o nome da equipe? ').strip().lower())
times[nome_da_equipe] = lib.cadastro_e_chaveamento.cadastro_de_atletas()
print(times)
