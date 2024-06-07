def cadastrar_livro(livros):
    titulo = input('Título do livro: ')
    autor = input('Autor do livro: ')
    ano = input('Ano de publicação: ')
    status = input('Status (disponível|emprestado):')

    livro = {  #cria objeto chamado livro com os atributos titulo, autor, etc...
        'titulo': titulo,
        'autor': autor,
        'ano': ano,
        'status': status,
    }

    livros.append(livro)  #o objeto 'livro' criado é acrescentado à lista 'livros'
    print(f"Livro '{titulo}' cadastrado com sucesso. O status do livro é '{status}'")
