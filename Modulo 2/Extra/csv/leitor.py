import csv

num = 0
# objeto = input('digite ')


try:
    with open("OCORRENCIAS_2025.csv", newline='', encoding='utf-8') as arquivo_exe:
        leitor = csv.reader(arquivo_exe, delimiter=',', dialect='excel')
        
        for linha in leitor:
            if any("Espingarda" in leitor):
                num += 1

    print(f"Quantidade de ocorrências: {num}")

except FileNotFoundError:
    print('Arquivo não encontrado')