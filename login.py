import sqlite3
from insertService import insertService
from clearDisplay import clear
from listServices import listServices
from savePassword import recoverPassword

def menu():
    clear()
    print('='*50)
    print(f'{"MENU":>25}')
    print('='*50)

    print("\nI: INSERIR NOVA SENHA")
    print("L: LISTAR SERVIÇOS CADASTRADOS")
    print("R: RECUPERAR UMA SENHA")
    print("S: SAIR")

def loginSystem():
    conn = sqlite3.connect('passwords.db')
    cur = conn.execute("SELECT * FROM master")

    masterPassword = input("Digite sua senha master: ")

    for i in cur:
        if i[0] == masterPassword:
            while True:
                menu()
                try:
                    option = str(input("Opção: "))

                    if option in "Rr":
                        recoverPassword()

                    if option in 'Ii':
                        clear()
                        insertService()

                    elif option in "Ll":
                        clear()
                        listServices()
                    elif option in "Ss":
                        print("\nDesconectando...")
                        break

                except:
                    print('ERRO! OPÇÃO INVÁLIDA\n')
        
        else:
            print("ERRO!\nDESCONECTANDO...")