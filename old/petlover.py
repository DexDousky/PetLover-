from funcoes.funcoescool import *

usuario_logado = None
tipo = None

def variavel():
    global tipo

def logout():
    global usuario_logado, tipo
    usuario_logado = None
    tipo = None
    print("Logout realizado com sucesso.")

erase()
while True:

    print('--\t🐶\tPet Lover\t🐶\t--')

    op = int(input('(1) Cadastro\n(2) Clientes\n(3) Pets\n(4) Serviços\n(5) Atendimento\n(6) Consultas ou Relatorio\n(7) Sair\n(\u2605 ) Digite: '))
    erase()

    if op == 1:
        while True:
            print('--\t🐶\tCadastro\t🐶\t--')
            print('vale lembrar que estamos em fase de testes, alguns bugs podem ocorrer.')
            userop = int(input('(1) Funcionários (adm)\n(2) Clientes\n(3) Pets\n(4) Serviços (adm)\n(5) Voltar para a pagina anterior"\n(\u2605 ) Digite: '))
            erase()
            if userop == 1:
                userop = int(input("Escolha a opção de Funciónario: "))
                if userop == 1:
                    if tipo == 'A':
                        erase()
                        cadastro_usuarios()
                    else:
                        erase()
                        print(' Faça login para usar essa função.')
                        login_usuario()
                elif userop == 2:
                    tipo = login_usuario()
                    if tipo:
                        print(f"Tipo de usuário logado: {tipo}")
                    else:
                        print("Falha no login.")
                elif userop == 3 and tipo == 'A':
                    usuario_atualizar()
                elif userop == 4 and tipo == 'A':
                    apagar_usuario()
                elif userop == 5 and tipo == 'A':
                    consultar_usuarios()
                elif userop == 6:
                    break
                else:
                    print("Opção inválida!")
                
    elif op == 2:

        while True:
            print('--\t🐶\tClientes\t🐶\t--')
            userop = int(input('\n(1) Cadastrar novo Cliente\n(2) Fazer Login\n(3) Atualizar\n(4) Apagar (adm)\n(5) Consultar\n(6) Voltar ao Menu Cadastro\n(\u2605 ) Digite: '))
            erase()

            if userop == 1:
                cadastro_clientes()
            elif userop == 2:
                    tipo = login_clientes()
                    if tipo:
                        print(f"Tipo de usuário logado: {tipo}")
                    else:
                        print("Falha no login.")
            elif userop == 3:
                clientes_atualizar()
            elif userop == 4 and tipo == 'A':
                apagar_cliente()
            elif userop == 5:
                consultar_cliente()
            elif userop == 6:
                break
            else: 
                print("Opção inválida!")

    elif op == 3:
     
        while True:
            print('--\t🐶\tPets\t🐶\t--')
            userop = int(input('\n(1) Cadastrar novo Pet\n(2) Atualizar\n(3) Apagar (adm)\n(4) Consultar\n(5) Voltar ao Menu Cadastro\n(\u2605 ) Digite: '))
            erase()
            opcao_pets = int(input("Escolha a opção de Pets: "))
            if opcao_pets == 1:
                cadastrar_pet()
            elif opcao_pets == 2:
                atualizar_pet()
            elif opcao_pets == 3 and tipo == 'A':
                apagar_pet()
            elif opcao_pets == 4:
                consultar_pet()
            elif opcao_pets == 5:
                break
            else: 
                print("Opção inválida!")
    
    elif op == 4:
 
        while True:
            print('--\t🐶\tServiços\t🐶\t--')
            userop = int(input('\n(1) Cadastrar novo Serviço (adm)\n(2) Atualizar (adm)\n(3) Apagar (adm)\n(4) Consultar (adm)\n(5) Voltar ao Menu Cadastro\n(\u2605 ) Digite: '))
            erase()

    elif op == 5:

        while True:
            print('--\t🐶\tAtendimento\t🐶\t--')
            userop = int(input('\n(1) Iniciar\n(2) Agendar\n(3) Remarcar\n(4) Voltar ao Menu Principal\n(\u2605 ) Digite: '))
            erase()

    elif op == 6:
            print('--\t🐶\tConsultas - Relatorios\t🐶\t--')

    elif op == 7:
        break
    
    else:
        erase()
        print('Opção invalida!\n')

# inacabado, não conta kk