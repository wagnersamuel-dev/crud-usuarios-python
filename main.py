while True:
    opcao = input('''
================================
      CRUD DE USUARIOS
================================

[ 1 ] CADASTRAR USUARIO
[ 2 ] LISTAR USUARIOS
[ 3 ] BUSCAR USUARIO
[ 4 ] ALTERAR USUARIO
[ 5 ] EXCLUIR USUARIO
[ 6 ] SAIR

Escolha uma opção: ''')

    if opcao == '1':
        print('\n--- CADASTRAR USUARIO ---')

        nome = input('Digite o nome: ').strip()
        idade = input('Digite a idade: ').strip()
        cidade = input('Digite a cidade: ').strip()

        with open('usuario.txt', 'a') as arquivo:
            arquivo.write(
                nome + ' | ' + idade + ' | ' + cidade + '\n'
            )

        print('Usuario cadastrado com sucesso!')


    elif opcao == '2':
        print('\n--- USUARIOS CADASTRADOS ---')

        encontrou_usuario = False

        with open('usuario.txt', 'r') as arquivo:
            for linha in arquivo:

                if linha.strip():
                    print(linha.strip())
                    encontrou_usuario = True

        if not encontrou_usuario:
            print('Nenhum usuario cadastrado.')


    elif opcao == '3':
        print('\n--- BUSCAR USUARIO ---')

        nome_busca = input(
            'Digite o nome do usuario que deseja buscar: '
        ).strip()

        encontrado = False

        with open('usuario.txt', 'r') as arquivo:
            for linha in arquivo:

                if not linha.strip():
                    continue

                nome, idade, cidade = linha.strip().split(' | ')

                if nome.lower() == nome_busca.lower():
                    encontrado = True

                    print('\nUsuario encontrado!')
                    print(f'Nome: {nome}')
                    print(f'Idade: {idade}')
                    print(f'Cidade: {cidade}')

                    break

        if not encontrado:
            print('Usuario não localizado.')


    elif opcao == '4':
        print('\n--- ALTERAR USUARIO ---')

        usuarios = []

        nome_alterar = input(
            'Digite o nome do usuario que deseja alterar: '
        ).strip()

        encontrado = False

        with open('usuario.txt', 'r') as arquivo:
            for linha in arquivo:

                if not linha.strip():
                    continue

                nome, idade, cidade = linha.strip().split(' | ')

                usuario = {
                    'nome': nome,
                    'idade': idade,
                    'cidade': cidade
                }

                usuarios.append(usuario)

        for usuario in usuarios:
            if usuario['nome'].lower() == nome_alterar.lower():

                encontrado = True

                print('Usuario encontrado!')

                nova_cidade = input(
                    'Digite a nova cidade: '
                ).strip()

                usuario['cidade'] = nova_cidade

                break

        if encontrado:

            with open('usuario.txt', 'w') as arquivo:
                for usuario in usuarios:
                    arquivo.write(
                        f"{usuario['nome']} | "
                        f"{usuario['idade']} | "
                        f"{usuario['cidade']}\n"
                    )

            print('Usuario alterado com sucesso!')

        else:
            print('Usuario não encontrado.')


    elif opcao == '5':
        print('\n--- EXCLUIR USUARIO ---')

        usuarios = []

        nome_excluir = input(
            'Digite o nome do usuario que deseja excluir: '
        ).strip()

        encontrado = False

        with open('usuario.txt', 'r') as arquivo:
            for linha in arquivo:

                if not linha.strip():
                    continue

                nome, idade, cidade = linha.strip().split(' | ')

                usuario = {
                    'nome': nome,
                    'idade': idade,
                    'cidade': cidade
                }

                usuarios.append(usuario)

        for usuario in usuarios:
            if usuario['nome'].lower() == nome_excluir.lower():

                encontrado = True
                usuarios.remove(usuario)

                break

        if encontrado:

            with open('usuario.txt', 'w') as arquivo:
                for usuario in usuarios:
                    arquivo.write(
                        f"{usuario['nome']} | "
                        f"{usuario['idade']} | "
                        f"{usuario['cidade']}\n"
                    )

            print('Usuario excluido com sucesso!')

        else:
            print('Usuario não encontrado.')


    elif opcao == '6':
        print('\nEncerrando o sistema...')
        break


    else:
        print('\nOpção invalida. Tente novamente.')