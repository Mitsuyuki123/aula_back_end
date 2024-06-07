def mudar_status(livros):
    if not livros: #se a lista 'livros' estiver vazia, a função dará um early return
        print("Não há livros cadastrados.")
        return

    print("\nLivros:")
    for livro in livros: #imprime os titulos dos livros dentro da lista 'livros'
        print(f"Titulo: {livro['titulo']}")
    mudar_livro_sts = input("Informe o titulo do livro para mudar o status: ")
    livro_encontrado = [busca for busca in livros if busca['titulo'] == mudar_livro_sts]
    """no momento, caso tenha mais de um livro com o mesmo nome, a função irá pedir para 
    trocar o status de todos os livros"""
    if livro_encontrado:
        for busca in livro_encontrado:
            busca['status'] = input("Digite o novo status do livro (disponível|emprestado): ")
            print(f"O livro '{busca["titulo"]}' foi marcado como '{busca['status']}'")
            """mudar a forma como o livro é buscado para trocar o status ou criar uma 
            forma de confirmação de qual livro mudar o status"""
    else:
        print(f"livro '{mudar_livro_sts}' nao encontrado")
