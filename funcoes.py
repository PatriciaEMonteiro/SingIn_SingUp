import json

#Função Arquivo
def save (content):
    file = open("usuarios.txt",'a')
    file.write(json.dumps(content))
    file.write("\n")
    file.close()

#Função para ler um arquivo
def get_users ():
    file = open("usuarios.txt", "r")
    return file.readlines()

#Função validação Login e Senha
def validate_access(login_email, login_password):
    validated = False
    users = get_users()
    for line in users:
        d_users = json.loads(line) #transforma string em dicionário
        validated = login_email in d_users.values() and login_password in d_users.values()
        return validated
    
    return validated

#Função Cadastro
def sing_up ():

    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")
    email = input("email: ")
    CPF = input("CPF: ")
    telefone = input("Telefone: ")
    
    #validando senha
    while True:
        senha = str(input("Senha: "))
        confirmar_senha = input("Confirmar Senha: ")
        if senha != confirmar_senha:
            print("Senhas não conferem. Digite novamente. ")
            continue
        else:
            break

    #Criando Dicionário - De nome dados
    dice = {
        "Nome": nome,
        "Sobrenome": sobrenome,
        "E-mail": email,
        "CPF": CPF,
        "Telefone": telefone,
        "Senha": senha
    }

    return dice
