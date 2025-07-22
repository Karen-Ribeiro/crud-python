import pytest
from app import crud
from unittest.mock import MagicMock

@pytest.fixture
def cursor():
    return MagicMock()

def test_insert_acoes(cursor):
    crud.insert_acoes(cursor, 'PETR4', 'Petrobras', 'Energia', 33.25, '2025-07-21')
    cursor.execute.assert_called_once()

def test_seleciona(cursor):
    cursor.fetchall.return_value = [('PETR4', 'Petrobras', 'Energia', 33.25, '2025-07-21')]
    result = crud.seleciona(cursor)
    assert result[0][0] == 'PETR4'

def test_atualiza(cursor):
    crud.atualiza(cursor, 35.00, 'PETR4')
    cursor.execute.assert_called_once()

def test_deleta(cursor):
    crud.deleta(cursor, 1)
    cursor.execute.assert_called_once()
