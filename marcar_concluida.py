def concluida(tarefas):
    print("\nTarefas:")
    for idx, tarefa in enumerate(tarefas):
        print(f"Titulo: {tarefa['titulo']}")
    tarefa_concluida = input("Informe a tarefa concluida: ")
    tarefa_encontrada = [obj for obj in tarefas if obj['titulo'] == tarefa_concluida]
    if tarefa_encontrada:
        for obj in tarefa_encontrada:
            obj['status'] = "concluida"
            print(f'A tarefa {obj["titulo"]} foi marcada como {obj['status']}')
    else:
        print(f"tarefa {tarefa_concluida} nao encontrada")