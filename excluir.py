def excluir_tarefa(tarefas):
    if not tarefas:
        print("Não há tarefas no momento.")
        return

    try:
        tarefa_idx = int(input("Informe o número da tarefa a ser excluida: ")) - 1
        if 0 <= tarefa_idx < len(tarefas):
            tarefa_excluida = tarefas.pop(tarefa_idx)
            print(f"Tarefa '{tarefa_excluida['titulo']}' excluida com sucesso!")
        else:
            print(f"Tarefa '{tarefa_idx+1}' nao encontrada.")

    except ValueError:
        print("Entrada inválida. Tente novamente.")
