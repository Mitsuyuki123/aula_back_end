def excluir_tarefa(tarefas):
    if not tarefas:
        print("Não há tarefas no momento.")
        return

    print("\nTarefas:")
    for tarefa in tarefas:
        print(f"Titulo: {tarefa['titulo']}")

    tarefa_excluir = input("Informe a tarefa a ser excluida: ")
    tarefa_encontrada = None
    for tarefa in tarefas:
        if tarefa['titulo'] == tarefa_excluir:
            tarefa_encontrada = tarefa
            break

    if tarefa_encontrada:
        tarefas.remove(tarefa_encontrada)
        print(f"A tarefa {tarefa_excluir} foi excluída com sucesso.")
    else:
        print(f"Tarefa chamada {tarefa_excluir} nao encontrada.")