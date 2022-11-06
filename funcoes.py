import json
import re


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
        d_users = json.loads(line) 
        validated = login_email in d_users.values() and login_password in d_users.values()
        if validated:
            return True
    
    return validated


#Função para validar o email e garantir que seja inserido corretamente
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
def validated_email (email):
    result_validated = re.search(regex,email)
    return result_validated


#Função verificar se Email e CPF já estão cadastrados
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

    #Recebe e Valida email
    while True:
        email = input("Email: ")
        if validated_email(email):
            break
        else:
            print("Email Inválido")
            continue

    #Recebe e Verifica se CPF contém apenas numeros
    while True:
        CPF = input("CPF: ")
        if CPF.isdigit() and len(CPF)==11:
            break
        else:
            print("CPF não é valido!")
            continue

    #Validando email e cpf para garantir que não haja cadastros repetidos
    registration = validate_registration(email, CPF)
    if registration:
        print ("Email e Cpf já cadastrados!")
        return init()
        
    #Recebe e Valida telefone para garantir que o mesmo tenha apenas numeros
    while True:
        telefone = input("Telefone: ")
        if telefone.isdigit() and len(telefone)==11:
            break
        else:
            print("Telefone não é valido!")
            continue
    
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
