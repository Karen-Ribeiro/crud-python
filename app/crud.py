def insert_acoes(cursor, ticker, nome_empresa, setor, preco, data_cotacao):
    query = """
        INSERT INTO acoes_b3 (ticker, nome_empresa, setor, preco, data_cotacao)
        VALUES (%s, %s, %s, %s, %s)
    """
    values = (ticker, nome_empresa, setor, preco, data_cotacao)
    cursor.execute(query, values)

def seleciona(cursor):
    query = "SELECT ticker, nome_empresa, setor, preco, data_cotacao FROM acoes_b3"
    cursor.execute(query)
    return cursor.fetchall()

def atualiza(cursor, novo_preco, ticker):
    query = "UPDATE acoes_b3 SET preco = %s WHERE ticker = %s"
    cursor.execute(query, (novo_preco, ticker))

def deleta(cursor, id_acao):
    query = "DELETE FROM acoes_b3 WHERE id = %s"
    cursor.execute(query, (id_acao,))
