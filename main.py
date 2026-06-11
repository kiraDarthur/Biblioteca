import csv
from datetime import datetime, timedelta
import auth
import os


# Classe que define a estrutura de um Livro no sistema
class Livro:
    def __init__(self, isbn, titulo, autor, ano, categoria, total, disponiveis):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.categoria = categoria
        self.total = int(total)
        self.disponiveis = int(disponiveis)
        self.prazo_dias = 14  # Prazo padrão de empréstimo


acervo = []  # Lista global que armazena os objetos Livro


# Carrega os dados do arquivo CSV para a lista acervo na memória
def carregar_livros():
    acervo.clear()
    with open('acervo.csv', mode='r', encoding='utf-8') as f:
        leitor = csv.reader(f)
        next(leitor)  # Pula o cabeçalho do arquivo
        for linha in leitor:
            acervo.append(Livro(*linha))


# Atualiza o arquivo CSV com o estado atual da lista acervo (estoque)
def salvar_acervo():
    with open('acervo.csv', mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['ISBN', 'Titulo', 'Autor', 'Ano', 'Categoria', 'Total', 'Disponiveis'])
        for l in acervo:
            writer.writerow([l.isbn, l.titulo, l.autor, l.ano, l.categoria, l.total, l.disponiveis])


# Registra o empréstimo em um arquivo de texto, associando ao usuário
def salvar_emprestimo(usuario, livro, data_pegou, data_dev):
    with open('emprestimos.txt', 'a', encoding='utf-8') as f:
        f.write(f"{usuario},{livro.titulo},{data_pegou},{data_dev}\n")


# Lê o arquivo de texto e filtra apenas os empréstimos do usuário logado
def carregar_meus_livros(usuario):
    meus_livros = []
    if os.path.exists('emprestimos.txt'):
        with open('emprestimos.txt', 'r', encoding='utf-8') as f:
            for linha in f:
                linha = linha.strip()
                if not linha: continue
                dados = linha.split(',')
                # Validação para garantir que a linha está correta antes de ler
                if len(dados) == 4 and dados[0] == usuario:
                    meus_livros.append(f"Livro: {dados[1]} | Pegou: {dados[2]} | Devolver: {dados[3]}")
                elif len(dados) < 4:
                    print(f"Aviso: Linha corrompida ignorada: {linha}")
    return meus_livros


# Menu principal após o login realizado
def menu_biblioteca(nome_usuario):
    while True:
        print(f"\n--- MENU BIBLIOTECA (Logado: {nome_usuario}) ---")
        print("1. Listar Acervo \n2. Consultar/Reservar \n3. Empréstimo \n4. Meus Livros \n0. Sair")
        opcao = input("Escolha uma opção: ")

        # Função interna para reutilizar a lógica de filtros de busca
        def buscar_livros():
            print("\n--- FILTROS DE BUSCA ---")
            print("1. Título \n2. Autor \n3. Ano \n4. Categoria \n0. Voltar")
            filtro = input("Escolha o filtro: ")
            termo = input("Digite o termo: ").lower()
            if filtro == '1': return [l for l in acervo if termo in l.titulo.lower()]
            if filtro == '2': return [l for l in acervo if termo in l.autor.lower()]
            if filtro == '3': return [l for l in acervo if termo == l.ano]
            if filtro == '4': return [l for l in acervo if termo in l.categoria.lower()]
            return []

        if opcao == '1':  # Exibe todos os livros
            for l in acervo: print(f"{l.titulo} | Disp: {l.disponiveis}")

        elif opcao == '2':  # Busca e exibe apenas resultados filtrados
            encontrados = buscar_livros()
            for i, l in enumerate(encontrados): print(f"{i + 1} - {l.titulo} por {l.autor} ({l.disponiveis} disp.)")

        elif opcao == '3':  # Processa o empréstimo de um livro selecionado
            encontrados = buscar_livros()
            for i, l in enumerate(encontrados): print(f"{i + 1} - {l.titulo} por {l.autor}")

            sel = int(input("Digite o número do livro: ")) - 1
            if 0 <= sel < len(encontrados):
                livro = encontrados[sel]
                if livro.disponiveis > 0:
                    livro.disponiveis -= 1  # Atualiza estoque na memória
                    data_hoje = datetime.now().strftime('%d/%m/%Y')
                    data_dev = (datetime.now() + timedelta(days=14)).strftime('%d/%m/%Y')
                    salvar_emprestimo(nome_usuario, livro, data_hoje, data_dev)
                    salvar_acervo()  # Salva mudança no CSV
                    print(f"\nEmpréstimo de '{livro.titulo}' realizado!")
                    print(f"Data: {data_hoje} | Devolução: {data_dev}")
                else:
                    print("Livro indisponível.")

        elif opcao == '4':  # Exibe histórico do usuário
            print("\n--- MEUS LIVROS EMPRESTADOS ---")
            for item in carregar_meus_livros(nome_usuario): print(item)

        elif opcao == '0':  # Sai do menu da biblioteca
            break


# Fluxo inicial que controla Login, Cadastro e Sair
def sistema_inicial():
    carregar_livros()
    while True:
        print("\n--- BEM-VINDO ---")
        print("1. Login \n2. Cadastrar \n3. Sair")
        opcao = input("Escolha: ")
        if opcao == '1':
            user = auth.fazer_login()
            if user: menu_biblioteca(user)
        elif opcao == '2':
            auth.cadastrar_usuario()
        elif opcao == '3':
            break


# Ponto de entrada do script
if __name__ == "__main__":
    sistema_inicial()