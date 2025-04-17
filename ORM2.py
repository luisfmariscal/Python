from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from ORM import Pessoa

def RetornaSession():
    HOST='localhost'
    USUARIO ="root"
    SENHA =""
    PORT=3306
    BANCO='pythonfull'      
    CONN = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}"
    
    engine = create_engine(CONN, echo=True)
    Session = sessionmaker(bind=engine)
    return Session()
    
session = RetornaSession()

x = Pessoa(nome='Luis Mariscal', usuario='LuisM', senha='123')
y = Pessoa(nome='Luis Fernando', usuario='LuisF', senha='123')
session.add_all([x,y])
session.rollback()
session.commit()
print('Adicionado com sucesso')