from database import conecta, encerra_conexao

"""CRUD
C= CREATE
R= READ
U= UPDATE
D= DELETE
"""

def main():

    connection = conecta()
    cursor = connection.cursor()

    def insert_acoes(ticker, nome_empresa, setor, preco, data_cotacao):
        query = "INSERT INTO acoes_b3 (ticker, nome_empresa, setor, preco, data_cotacao) VALUES (%s, %s, %s, %s, %s)"
        values = ticker, nome_empresa, setor, preco, data_cotacao
        cursor.execute(query, values)
        connection.commit()
        print("Dados inseridos com sucesso!")

    def seleciona():
        query = "SELECT ticker, nome_empresa, setor, preco, data_cotacao FROM acoes_b3"
        cursor.execute(query)
        acoes = cursor.fethcall()
        for acao in acoes:
            print(acao)
        return acao
    
    def atualiza(novo_preco, ticker):
        query = "UPDATE acoes_b3 SET preco={novo_preco} WHERE ticker='{ticker}'"
        cursor.execute(query)
        connection.commit()
        print("Registro atualizado com sucesso!")

    def deleta(id):
        query = "DELETE FROM acoes_b3 WHERE id='{id}"
        cursor.execute(query)
        connection.commit()
        print("Registro deletado com sucesso!")

    insert_acoes('CMIG4', 'CEMIG', 'Utilidade Pública', 11.06, '2025-07-21')

    seleciona()

    atualiza(11.76, 'CMIG4')

    deleta(1)

    encerra_conexao(connection)

if __name__ == "__main__":
    main()