import auth

# 1. Primeiro, vamos cadastrar um usuário de teste
print("--- Iniciando Cadastro ---")
auth.cadastrar_usuario()

# 2. Agora, vamos tentar fazer o login
print("\n--- Iniciando Login ---")
usuario = auth.fazer_login()

if usuario:
    print(f"Sucesso! Bem-vindo, {usuario}")
else:
    print("Falha no login.")