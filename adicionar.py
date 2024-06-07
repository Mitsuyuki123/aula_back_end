def cadastrar_tarefa(tarefas):
    titulo = input('Título: ')
    descricao = input('descrição: ')
    status = 'pendente'

    tarefa = {
        'titulo': titulo,
        'descricao': descricao,
        'status': status,
    }

    tarefas.append(tarefa)
    print(f"Tarefa {titulo} cadastrada com sucesso! O status da tarefa é {status}")