def exibir_livro(livros):
    if not livros: #se a lista 'livros' estiver vazia, a função dará um early return
        print("Não há livros cadastrados.")
        return
    for idx, livro in enumerate(livros): #para cada index e obj livro dentro da lista livros, executar os comandos abaixo
        print(f"\nLivro{idx + 1}")
        print(f"Titulo: {livro['titulo']}")
        print(f"Autor: {livro['autor']}")
        print(f"Ano: {livro['ano']}")
        print(f"Status: {livro['status']}")
