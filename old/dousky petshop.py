# essa versão é a que eu estive fazendo em sala seguindo as suas aulas mas, muita coisa mudou desde qnd eu parei de usar isso aqui 100% e estritamente como base


import time
import os

clientes = []
Pets = [('ID','Nome','Categoria','Raça','Aniversario','CPFdono')]
Serviços = [('ID','Descrição','Valor','Orientação',)]
Atendimento = [('IDServiço','IDPet','DataAtendimento','DataAgendamento','DataConclusão','Status')]

def erase():
    if os.name == 'nt': #linux
        os.system('cls')
    elif os.name == 'posix': #windows
        os.system('clear')

def onesec():
    time.sleep(1)

while True:
    erase()
    wait = 0.2
    print('\u2605   - - - - - - -  🤓 Dousky Petshop 🤓  - - - - - - -  \u2605 ')
    onesec()
    print('(1) Cliente\n(2) Pet\n(3) Serviços\n(4) Atendimento\n(5) Sair')
    
    menu = int(input ('\nDigite o numero de sua opção:  (1, 2, 3, 4...)\n\nOpção: ' ))
    
    if menu == 1: # Cliente
        erase()
        print('\u2605 - - - - - - -  Área do Cliente  - - - - - - -  \u2605 ')
        onesec()
        print('\n(1) Login\n(2) Cadastro')
        onesec()

        opcao = int(input('\nOpção: '))
        
        if opcao == 1: # Login
            erase()
            print('\u2605 - - - - - - -  Login  - - - - - - -  \u2605 ')
            onesec()
            usuario = input('\u2605 Usuario: ')
            senha = int(input('\u2605 Senha: '))
            erase()
            if usuario == ('DDousky') and senha == 1991:
                print (' Bem vindo Dousky! ')
                onesec()
            
        elif opcao == 2: # Cadastro
            erase()
            print('\u2605 - - - - - - -  Cadastro  - - - - - - -  \u2605 ')
            onesec()
            nomeC = input('\u2605 Nome: ') 
            Cpfc = int(input('\u2605 CPF: '))
            Cep = int(input('\u2605 CEP: '))
            Cell = int(input('\u2605 Celular: '))
            Email = input('\u2605 E-mail: ')
            erase()
            dados_cliente = (nomeC, Cpfc, Cep, Cell, Email)
            clientes.append(dados_cliente)
            
            print('Seus dados são: ')
            print( clientes)
            time.sleep(3)
           
                     
    elif menu == 2: # Pet
        erase()
        print('\u2605 - - - - - - -  Área do Pet  - - - - - - -  \u2605 ')
        onesec()
        print('\n(1) Cadastro\n(2) Incrições\n(3) Alguma opção')
        
        opcao = int(input('\nOpção: '))

        if opcao == 1:
            print('\u2605 - - - - - - -  Cadastro Pet  - - - - - - -  \u2605  ')
            nomeP= input('\u2605 Nome do pet: ') 
            IDP = int(input('\u2605 ID do pet: '))
            Aniversario = int(input('\u2605 Aniversario do pet: '))

