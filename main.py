
import json
from funcoes import init, sing_up, save, get_users, validate_access, validate_registration

while True:
    
    start = init()

    #Main

    if start == 1:

        #conteúdo do arquivo
        users = get_users()
                
        login_email = input("E-mail: ")
        login_password = input("Senha: ")

        resp_user = validate_access(login_email, login_password)         

        if resp_user:
            print("Login realizado com sucesso: ")
        else:
            print("Acesso negado!")
   

    elif start == 2:

        dice = sing_up()
        
        print("Salvar Cadastro: ")
        registration = input(" S- Sim / N- Não ")

        if registration == 's':
            save(content=dice)

        elif registration == 'n':
            print("Cadastro Cancelado!")

        else:
            print("Erro!")

    
    elif start == 3:
        break

    
    else:
        print("Opção Inválida. Tente novamente.")
        continue

