from menu import menu
from adicionar import cadastrar_livro
from exibir import exibir_livro
from pesquisar import pesquisar_livro
from marcar_emprestado import mudar_status
from remover import remover_livro


def main():
    livros = []
    while True:
        escolha = menu()
        if escolha == "1":
            cadastrar_livro(livros)
        elif escolha == "2":
            exibir_livro(livros)
        elif escolha == "3":
            pesquisar_livro(livros)
        elif escolha == "4":
            mudar_status(livros)
        elif escolha == "5":
            remover_livro(livros)
        elif escolha == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")


if __name__ == '__main__':
    main()
