while True:
    print("""
        ===== ASSISTENTE FINANCEIRO =====
        1. Adicionar despesa
        2. Ver Extrato
        """)
    opcao = input("Escolha uma opção: ")
    

    if opcao == "1":
        despesa = float(input('Digite o valor Gasto:'))
        despesa_descricao = input('Digite o Tipo de Gasto:')
    
        # add em arq txt(ganho.txt)
        with open('despesa.txt','a') as arquivo:
            arquivo.write('Gastos: ' +  str(despesa) + '\n')

        # add em arq txt (descr_despesa.txt)
        with open('descr_despesa.txt','a') as arquivo:
            arquivo.write('Descricao: '+ despesa_descricao + '\n')

        print("Despesa Armazenada com sucesso")

    elif opcao == "2":
        print("Gastos:")

        with open('despesa.txt', 'r') as arquivo:
                despesa_extrato = arquivo.readlines()

            # Mostrar todas as despesas
        for numero, linha in enumerate(despesa_extrato, start=1):
                print(f"{numero}. {linha.strip()}")

            # Somar as despesas
        total_despesas = sum(float(linha.strip().split(': ')[1]) for linha in despesa_extrato)
        print(f'Total de despesas: R$ {total_despesas:.2f}')
