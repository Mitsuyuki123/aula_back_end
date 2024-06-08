def exibir_tarefa(tarefas):
    if not tarefas:
        print("nenhuma tarefa cadastrada.")
        return
    for idx, tarefa in enumerate(tarefas):
        status = "Concluida" if tarefa['concluida'] else "Pendente"
        print(f"\nTarefa{idx + 1}")
        print(f"Titulo: {tarefa['titulo']}")
        print(f"Descrição: {tarefa['descricao']}")
        print(f"Status: {status}")
