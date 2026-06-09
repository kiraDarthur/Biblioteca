import csv
from datetime import datetime, timedelta


class Livro:
    def __init__(self, isbn, titulo, autor, ano, categoria, total, disponiveis):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.categoria = categoria
        self.total = int(total)
        self.disponiveis = int(disponiveis)
        self.prazo_dias = 14


class Usuario:
    def __init__(self, nome, id_usuario):
        self.nome = nome
        self.id_usuario = id_usuario
        self.emprestimos = []


acervo = []
usuario_logado = Usuario("João", "001")


def carregar_livros():
    try:
        with open('acervo.csv', mode='r', encoding='utf-8') as f:
            leitor = csv.reader(f)
            next(leitor)  # Pula o cabeçalho
            for linha in leitor:
                if len(linha) < 7: continue
                acervo.append(Livro(linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6]))
    except Exception as e:
        print(f"Erro ao carregar CSV: {e}")


def selecionar_livro_por_busca():
    while True:
        print("\n--- FILTROS DE BUSCA ---")
        print("1. Título \n 2. Autor \n 3. Ano \n 4. Categoria \n 0. Voltar")
        tipo = input("Escolha o filtro: ")
        if tipo == '0': return None

        termo = input("Digite o termo de busca: ").lower()

        if tipo == '1':
            resultados = [l for l in acervo if termo in l.titulo.lower()]
        elif tipo == '2':
            resultados = [l for l in acervo if termo in l.autor.lower()]
        elif tipo == '3':
            resultados = [l for l in acervo if termo == l.ano]
        elif tipo == '4':
            resultados = [l for l in acervo if termo in l.categoria.lower()]
        else:
            continue

        if not resultados:
            print("Nenhum livro encontrado.")
            continue

        for i, l in enumerate(resultados):
            status = "Disponível" if l.disponiveis > 0 else "Indisponível"
            print(f"{i + 1} - {l.titulo} | {l.autor} ({status})")

        escolha = int(input("\nDigite o número (ou 0 para voltar): "))
        if escolha == 0: continue
        return resultados[escolha - 1]


def menu():
    carregar_livros()
    while True:
        print("\n--- MENU BIBLIOTECA ---")
        print("1. Listar Acervo \n 2. Consultar/Reservar \n 3. Empréstimo \n 4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            for l in acervo: print(f"{l.titulo} - Estoque: {l.disponiveis}/{l.total}")

        elif opcao in ['2', '3']:
            livro = selecionar_livro_por_busca()
            if livro and opcao == '2':
                entrega = datetime.now() + timedelta(days=livro.prazo_dias)
                print(f"Disponível: {livro.disponiveis}. Entrega sugerida: {entrega.strftime('%d/%m/%Y')}")
            elif livro and opcao == '3':
                if livro.disponiveis > 0 and len(usuario_logado.emprestimos) < 2:
                    livro.disponiveis -= 1
                    usuario_logado.emprestimos.append(livro)
                    print(f"Empréstimo de '{livro.titulo}' realizado!")
                else:
                    print("Erro: Livro indisponível ou limite de 2 livros atingido.")

        elif opcao == '4':
            break


if __name__ == "__main__":
    menu()