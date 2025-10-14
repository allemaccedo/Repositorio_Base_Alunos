import sqlite3
con = sqlite3.connect("meu_banco.db")

try:
    con = sqlite3.connect("meu_banco.db")

    cur = con.cursor()

    cur.execute("CREATE TABLE pessoa(id, nome, idade, cpf)")

    con.commit()

except ConnectionRefusedError as c:
    print("erro de conexão com o banco")