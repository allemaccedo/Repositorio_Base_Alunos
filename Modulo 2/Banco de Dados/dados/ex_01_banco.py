import sqlite3
con = sqlite3.connect("meu_banco_ex01.db")

try:
    con = sqlite3.connect("meu_banco_ex01.db")

    cur = con.cursor()

    # cur.execute("CREATE TABLE pessoa(id_funcionario,nome, chave)")

    cur.execute("INSERT INTO pessoa VALUES('1', 'ana', 'recepçao')")
    cur.execute("INSERT INTO pessoa VALUES('2', 'bruno', 'financeiro')")
    cur.execute("INSERT INTO pessoa VALUES('3', 'carla', 'deposito')")
    

    cur.execute("SELECT * FROM pessoa WHERE chave = 'deposito'")
    result = cur.fetchone()
    print(result)

    con.commit()
except ConnectionRefusedError as c:
    print("erro de conexão com o banco")