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
