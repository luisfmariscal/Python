import pymysql.cursors

con = pymysql.connect(
    host='localhost',
    user="root",
    password="",
    port=3306,
    db='pythonfull',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor)


def criar_tabela(nomeTabela):
    try:
        with con.cursor() as cursor:
            cursor.execute(f"CREATE TABLE {nomeTabela} (nome VARCHAR(50))")
        con.close()
        print("Tabela criada com sucesso")
    except Exception as e:
        print(f"Erro ao criar tabela {e}")

def removeTabela(nomeTabela):
    try:
        with con.cursor() as cursor:
            cursor.execute(f"DROP TABLE {nomeTabela}")
        con.close()
        print("Tabela removida com sucesso")
    except Exception as e:
        print(f"Erro ao remover tabela {e}")

try:
    with con.cursor() as cursor:
        cursor.execute(f"DELETE FROM teste WHERE nome = 'Luis'")
        print('Remoção efetuado com suvesso')
except Exception as e:
    print(f"Ocorreu um erro {e}")