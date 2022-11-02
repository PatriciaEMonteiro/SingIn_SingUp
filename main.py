# NÃO PERMITIR CADASTRO COM EMAIL'S REPETIDOS
# NÃO PERMITIR CADASTRO COM CPF REPETIDOS
# VALIDAR EMAIL, CPF, TELEFONE
# VALIDAR NOME E SOBRENOME - NÃO CONTER NUMEROS

import json
from funcoes import sing_up, save, get_users, validate_access

while True:
    
    print(" Escolha a opção desejada: ")
    acess = int(input("1 - Sing In (Entrar)  2- Sing Up (Cadastrar) 3- Close (Sair) "))

    #Main

    if acess == 1:

        #conteúdo do arquivo
        users = get_users()
                
        login_email = input("E-mail: ")
        login_password = input("Senha: ")

        resp_user = validate_access(login_email, login_password)         

        if resp_user:
            print("Login realizado com sucesso: ")
        else:
            print("Acesso negado!")
   
    elif acess == 2:
        dice = sing_up()
        
        print("Salvar Cadastro: ")
        registration = input(" S- Sim / N- Não ")

        if registration == 's':
            save(content=dice)

        elif registration == 'n':
            print("Cadastro Cancelado!")

        else:
            print("Erro!")

    
    elif acess == 3:
        break

    
    else:
        print("Opção Inválida. Tente novamente.")
        continue

