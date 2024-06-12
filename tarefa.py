class Tarefas:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao
        self.status = False

    def __str__(self):
        status = "concluida" if self.status else "pendende"
        return f"Nome: {self.nome}, Descrição: {self.descricao}, Status: {status}"

    def atualizar(self, nome, descricao, status):
        self.nome = nome
        self.descricao = descricao
        try:
            if not status:
                self.status = True
            elif status:
                self.status = False
        except ValueError as e:
            print(f"Erro ao atualiza tarefa. Erro: {e}")
