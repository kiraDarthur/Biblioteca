import csv
import os

def cadastrar_usuario():
    print("\n--- CADASTRO DE USUÁRIO ---")
    nome = input("Escolha um login: ")
    senha = input("Escolha uma senha: ")
    with open('usuarios.csv', mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([nome, senha])
        f.flush()
    print("Conta criada com sucesso!")
    input("Pressione ENTER para voltar...")

def fazer_login():
    if not os.path.exists('usuarios.csv'):
        print("Nenhum usuário cadastrado.")
        return None
    print("\n--- LOGIN ---")
    nome = input("Login: ")
    senha = input("Senha: ")
    with open('usuarios.csv', mode='r', encoding='utf-8') as f:
        leitor = csv.reader(f)
        for linha in leitor:
            if len(linha) >= 2 and linha[0] == nome and linha[1] == senha:
                return nome
    print("Login ou senha incorretos.")
    return None