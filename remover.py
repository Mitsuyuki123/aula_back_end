def remover_livro(livros):
    if not livros:
        print("Não há livros cadastrados.")
        return

    livro_excluir = input("Informe o titulo do livro a ser excluido: ")
    livro_encontrado = None
    for livro in livros:
        if livro['titulo'] == livro_excluir:  #outra forma de buscar um objeto a partir de um atributo dentro do objeto
            livro_encontrado = livro
            break

    """no caso acima, apenas o primeiro objeto encontrado será o escolhido. pesquisar como escolher dentro de uma 
    seleção de livros com mesmo nome"""

    if livro_encontrado:
        livros.remove(livro_encontrado)
        print(f"O livro '{livro_excluir}' foi removido do catálogo com sucesso.")
        """to-do buscar forma de remover todos livros com mesmo nome, ou selecionar
         um livro especifico e não apenas o primeiro"""
    else:
        print(f"livro com titulo '{livro_excluir}' não foi encontrado.")
