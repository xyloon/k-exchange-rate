import pytest

from kexr.utils import db_session_string_definition, DBType, NotEnoughParameter


def test_db_session_string_definition_memory():
    assert "sqlite://" == db_session_string_definition(DBType.memory)


def test_db_session_string_definition_sqlite():
    assert "sqlite:///a.db" == db_session_string_definition(DBType.sqlite3, file_path="a.db")


@pytest.mark.xfail(raises=NotEnoughParameter)
def test_db_session_string_definition_sqlite_error():
    db_session_string_definition(DBType.sqlite3)


@pytest.mark.xfail(raises=NotEnoughParameter)
def test_db_session_string_definition_psql_error1():
    db_session_string_definition(DBType.postgres)


@pytest.mark.xfail(raises=NotEnoughParameter)
def test_db_session_string_definition_psql_error2():
    db_session_string_definition(DBType.postgres, username="u")


@pytest.mark.xfail(raises=NotEnoughParameter)
def test_db_session_string_definition_psql_error3():
    db_session_string_definition(DBType.postgres, username="u", password="p")


@pytest.mark.xfail(raises=NotEnoughParameter)
def test_db_session_string_definition_psql_error4():
    db_session_string_definition(DBType.postgres, username="u", password="p", ipaddr="127.0.0.1")


@pytest.mark.xfail(raises=NotEnoughParameter)
def test_db_session_string_definition_psql_error5():
    db_session_string_definition(DBType.postgres, username="u", password="p", ipaddr="127.0.0.1", port=5000)


def test_db_session_string_definition_psql():
    assert "postgres://u:p@127.0.0.1:5000/dbn" == db_session_string_definition(DBType.postgres, username="u", password="p", ipaddr="127.0.0.1", port=5000, dbname="dbn")




