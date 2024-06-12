from validador_tarefa import ValidadorTarefa


class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        try:
            ValidadorTarefa.validar(tarefa)
            self.tarefas.append(tarefa)
            print(f"Tarefa '{tarefa.nome}' adicionada")
        except ValueError as e:
            print(f"Tarefa invalida. Erro: {e}")

    def exibir_tarefa(self):
        try:
            if len(self.tarefas) == 0:
                raise ValueError("Lista de tarefas vazia")
            for idx, tarefa in enumerate(self.tarefas):
                print(f"\nTarefa {idx + 1}: {tarefa.nome}")
                print(f"Descrição: {tarefa.descricao}")
                status = "concluída" if tarefa.status else "pendente"
                print(f"Status: {status}\n")
        except Exception as e:
            print(f"Erro ao exibir tarefas. Erro: {e}")

    def localizar_tarefa(self, index):
        try:
            if len(self.tarefas) == 0:
                raise ValueError("Lista de tarefas vazia")
            for tarefa in self.tarefas:
                if index == tarefa.nome:
                    return tarefa
        except Exception as e:
            print(f"Erro ao localizar tarefa. Erro: {e}")

    def atualizar_tarefa(self, tarefa):
        try:
            if len(self.tarefas) == 0:
                raise ValueError("Lista de tarefas vazia")
            ValidadorTarefa.validar(tarefa)
            tarefa.atualizar(tarefa.nome, tarefa.descricao, tarefa.status)
            status = "concluida" if tarefa.status else "pendente"
            print(f"Tarefa '{tarefa.nome}' atualizada. Novo status: {status}")
        except Exception as e:
            print(f"Erro ao atualizar tarefa. Erro: {e}")

    def remove_tarefa(self, tarefa):
        try:
            if len(self.tarefas) == 0:
                raise ValueError("Lista de tarefas vazia")
            ValidadorTarefa.validar(tarefa)
            self.tarefas.remove(tarefa)
            print(f"Tarefa '{tarefa.nome}' removida com sucesso")
        except Exception as e:
            print(f"Erro ao remover tarefa. Erro: {e}")
