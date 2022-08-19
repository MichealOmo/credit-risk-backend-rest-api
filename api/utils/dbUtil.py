import databases
import sqlalchemy
from functools import lru_cache
from api import config
from api.models import metadata
# import config
# from models import metadata
from starlette.config import Config

# 1. Using Pydantic to load .env configuration file
@lru_cache()
def setting():
    return config.Settings()

def database_mysql_url_config():
    conf = Config('./.env')
    # return str(conf("DB_CONNECTION") + "://" + conf("DB_USER") + ":" + conf("DB_PASSWORD") +
    #            "@"  + conf("DB_HOST") + ":" + conf("DB_PORT") + "/" + conf("DB_DATABASE") )
    return str(conf("DB_CONNECTION") + "://" + conf("DB_USER") + ":" + conf("DB_PASSWORD") +
               "@"  + conf("DB_DATABASE") + "/" + conf("DB_DATABASE") )


database = databases.Database(database_mysql_url_config())
engine = sqlalchemy.create_engine(database_mysql_url_config())
metadata.create_all(engine)

# POSTGRES_USER: 'postgres'
# POSTGRES_PASSWORD: 'dbpw'
# POSTGRES_DATABASE: 'partnerup'
# POSTGRES_HOST: 'localhost'
# POSTGRES_PORT: '5432'