from datetime import date, timedelta

from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class EnvStore:
    env = {}

    @classmethod
    def initialize(cls):
        cls.env = {}

    @classmethod
    def set_env(cls, **kv):
        cls.env.update(kv)

    @classmethod
    def set_env_one(cls, keyname, value):
        cls.env[keyname] = value

    @classmethod
    def get_env(cls, env_name):
        return cls.env.get(env_name, None)

    @classmethod
    def rm_env(cls, env_name):
        if env_name in cls.env:
            cls.env.pop(env_name)


one_day = timedelta(days=1)


def date_iterator(start_date, end_date=None):
    sd = start_date
    while end_date is None or sd <= end_date:
        yield sd
        sd = sd + one_day


def date_creater_from_string(string):
    return date(*map(int, string.split("-")))


db_session = "db_session"
db_session_tables = "db_session_tables"


class DBType:
    memory = "memory"
    sqlite3 = "sqlite3"
    postgres = "postgres"


class NotEnoughParameter(Exception):
    @classmethod
    def make_exception(cls, *items):
        return NotEnoughParameter("This parameter does not exists : " +
                                  ", ".join(('"' + str(item) + '"' for item in items)))


def db_session_string_definition(dbtype, username=None, password=None, file_path=None, ipaddr=None, port=None,
                                 dbname=None):
    if dbtype == DBType.memory:
        return 'sqlite://'
    if dbtype == DBType.sqlite3:
        if file_path is None:
            raise NotEnoughParameter.make_exception('file_path')
        return 'sqlite:///' + file_path
    if dbtype == DBType.postgres:
        item_does_not_provided = tuple(name for name, param in (
        ('username', username), ('password', password), ('ipaddr', ipaddr), ('port', port), ('dbname', dbname)) if
                                       param is None)
        if item_does_not_provided:
            raise NotEnoughParameter.make_exception(*item_does_not_provided)
        return "postgres://{username}:{password}@{ipaddr}:{port}/{dbname}".format(
            username=username, password=password, ipaddr=ipaddr, port=port, dbname=dbname
        )
    raise Exception("Not supported")


def db_session_open(db_session_string, db_definition_method_table, sql_logging=False, autoflush=False,
                    dropable_before_create=False):
    if not EnvStore.get_env(db_session):
        base = declarative_base()
        db_table_definitions = {}
        for name, def_method in db_definition_method_table.items():
            db_table_definitions[name] = def_method(base=base, table_name=name)
        engine = create_engine(db_session_string, echo=sql_logging)
        session = sessionmaker(bind=engine, autoflush=autoflush)()
        if dropable_before_create:
            base.metadata.drop_all(engine)
        base.metadata.create_all(engine)
        db_connection = engine.connect()
        db_meta = MetaData(engine, reflect=True)
        EnvStore.set_env(db_connection=db_connection, db_meta=db_meta, db_session_tables=(
            session,
            db_table_definitions
        ))


def db_session_close(dummy=None):
    s_tables = EnvStore.get_env(db_session_tables)
    if s_tables is not None:
        s_tables[0].close()
        EnvStore.rm_env('db_connection')
        EnvStore.rm_env('db_meta')
        EnvStore.rm_env('db_session_tables')
