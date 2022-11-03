import json

#Função Inicio
def init ():
    print(" Escolha a opção desejada: ")
    acess = int(input("1 - Sing In (Entrar)  2- Sing Up (Cadastrar) 3- Close (Sair) "))
    return acess

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
        if validated:
            return True
    
    return validated


#Função validação Email e CPF
def validate_registration(email, CPF):
    validated = False
    users = get_users()
    for line in users:
        r_users = json.loads(line)
        validated = email in r_users.values() or CPF in r_users.values()
        if validated:
            return True
    
    return validated


#Função Cadastro
def sing_up ():

    users = get_users()

    #Rebendo Nome e Telefone
    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")

    #validando email e cpf
    email = input("Email: ")
    CPF = input("CPF: ")

    registration = validate_registration(email, CPF)
    
    if registration:
        print ("Email e Cpf já cadastrados!")
        return init()
        
    #Rebendo telefone
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
