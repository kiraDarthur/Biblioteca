import csv
import os


# Função responsável por cadastrar novos usuários no sistema
def cadastrar_usuario():
    print("\n--- CADASTRO DE USUÁRIO ---")
    nome = input("Escolha um login: ")
    senha = input("Escolha uma senha: ")

    # Abre o arquivo CSV em modo 'append' (adicionar) para não apagar os já existentes
    with open('usuarios.csv', mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([nome, senha])  # Salva o novo usuário como uma nova linha
        f.flush()  # Garante que os dados sejam gravados no disco imediatamente

    print("Conta criada com sucesso!")
    input("Pressione ENTER para voltar...")  # Pausa para o usuário ler a confirmação


# Função que verifica as credenciais do usuário
def fazer_login():
    # Verifica se o arquivo de usuários existe antes de tentar abrir
    if not os.path.exists('usuarios.csv'):
        print("Nenhum usuário cadastrado.")
        return None

    print("\n--- LOGIN ---")
    nome = input("Login: ")
    senha = input("Senha: ")

    # Lê o arquivo CSV linha por linha para comparar o login e senha
    with open('usuarios.csv', mode='r', encoding='utf-8') as f:
        leitor = csv.reader(f)
        for linha in leitor:
            # Verifica se a linha tem dados e se coincidem com a entrada
            if len(linha) >= 2 and linha[0] == nome and linha[1] == senha:
                return nome  # Retorna o nome do usuário se o login for bem-sucedido

    print("Login ou senha incorretos.")
    return None  # Retorna None se não encontrar o usuário