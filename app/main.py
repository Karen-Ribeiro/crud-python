from app.database import conecta, encerra_conexao
from app import crud

def main():
    conn = conecta()
    cursor = conn.cursor()

    crud.insert_acoes(cursor, 'CMIG4', 'CEMIG', 'Utilidade Pública', 11.06, '2025-07-21')
    conn.commit()

    acoes = crud.seleciona(cursor)
    for acao in acoes:
        print(acao)

    crud.atualiza(cursor, 11.76, 'CMIG4')
    conn.commit()

    crud.deleta(cursor, 1)
    conn.commit()

    encerra_conexao(conn)

if __name__ == "__main__":
    main()
