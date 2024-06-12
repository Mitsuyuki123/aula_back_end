class ValidadorTarefa:
    @staticmethod
    def validar(tarefa):
        if tarefa is None:
            raise ValueError("tarefa não pode ser nulo")
        if tarefa.nome == "":
            raise ValueError("Nome do tarefa não pode ser vazio")
        if tarefa.descricao == "":
            tarefa.descricao = "'sem descrição'"
        if tarefa.status not in [True, False]:
            raise ValueError("Status inválido")
