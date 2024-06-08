def concluida(tarefas):
    if not tarefas:
        print("Não há tarefas cadastradas")
        return

    try:  # código que pode gerar exceção
        tarefa_idx = int(input("Informe o número da tarefa a ser excluida: "))-1
        if 0 <= tarefa_idx < len(tarefas):
            tarefas[tarefa_idx]['concluida'] = True
            print(f"A tarefa '{tarefas[tarefa_idx]["titulo"]}' foi marcada como 'concluida'")
        else:
            print(f"tarefa '{tarefa_idx+1}' nao encontrada")
    except ValueError:  # tratamento da exceção
        print("Entrada inválida. Tente novamente")
