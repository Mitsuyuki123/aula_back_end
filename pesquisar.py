def pesquisar_livro(livros):
    if not livros: #se a lista 'livros' estiver vazia, a função dará um early return
        print("Não há livros cadastrados.")
        return

    forma_busca = input("\nDigite a forma de busca desejada (titulo|autor):")
    if forma_busca == 'titulo':
        busca_titulo = input("Informe o titulo do livro: ")
        livro_encontrado = [busca for busca in livros if busca['titulo'] == busca_titulo]
        """a palavra 'busca' vai ser substituida por cada objeto da lista 'livros' 
        e se o atributo 'titulo' desse objeto for igual ao 'busca_titulo', retorna o objeto inteiro"""
        if livro_encontrado: #se a busca nao retornar vazia, executar o comando abaixo
            print(f"\nLivros com título '{busca_titulo}'")
            for busca in livro_encontrado: #printar todos os objetos que possuem atributos 'titulo' solicitado
                print(f'{busca}')
        else:
            print(f"livro {busca_titulo} nao encontrado")
    elif forma_busca == 'autor':
        busca_autor = input("Informe o autor do livro: ")
        livro_encontrado = [busca for busca in livros if busca['autor'] == busca_autor]
        """#a palavra 'busca' vai ser substituida por cada objeto da lista 'livros' e 
        se o atributo 'autor' desse objeto for igual ao 'busca_autor', retorna o objeto inteiro"""
        if livro_encontrado:
            print(f"\nLivros do autor '{busca_autor}'")
            for busca in livro_encontrado: #printar todos os objetos que possuem atributos 'autor' solicitado
                print(f"{busca}")
        else:
            print(f"livros com autor {busca_autor} nao encontrado")
    else:
        print("Opção inválida.") #opção inválida caso a variavel forma_busca não seja nem 'titulo' nem 'autor'
