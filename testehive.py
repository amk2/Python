from sqlalchemy import *
from sqlalchemy.engine import create_engine
from sqlalchemy.schema import *
# Presto
engine = create_engine('presto://localhost:10000/hive/teste')
# Hive
engine = create_engine('hive://localhost:10000/teste')
logs = Table('employee', MetaData(bind=engine), autoload=True)
print (select([func.count('*')], from_obj=logs).scalar())