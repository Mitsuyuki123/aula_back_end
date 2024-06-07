def exibir_tarefa(tarefas):
    if not tarefas:
        print("nenhuma tarefa cadastrada.")
        return
    for idx, tarefa in enumerate(tarefas):
        print(f"\nTarefa{idx + 1}")
        print(f"Titulo: {tarefa['titulo']}")
        print(f"Descrição: {tarefa['descricao']}")
        print(f"Status: {tarefa['status']}")
