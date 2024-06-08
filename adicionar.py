def cadastrar_tarefa(tarefas):
    titulo = input('Título: ')
    descricao = input('descrição: ')

    tarefa = {
        'titulo': titulo,
        'descricao': descricao,
        'concluida': False
    }

    tarefas.append(tarefa)
    print(f"Tarefa '{titulo}' cadastrada com sucesso!")
