from db.components.db_config import DbConfig
from db.components.db_conn import DbConn
from db.components.db_init import DbInit
from db.components.push_to_db import PushToDb


db_conn = DbConn(DbConfig.get_host(),int(DbConfig.get_port()),DbConfig.get_user(),DbConfig.get_password())
db_init = DbInit(db_conn.get_conn())
db_init.create_tables()
push_to_db = PushToDb(db_conn.get_conn())
