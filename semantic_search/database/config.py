from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Configure the URI of the Data base:
DATABASE_URI = r'sqlite:///C:\Users\João Fonseca Antunes\OneDrive\Ambiente de Trabalho\Mestrado 1 ano\Gestao de ' \
               r'projetos\projeto DRE\data_set\2024-10-27-DRE.sqlite3'

# Create the connection engine and the session
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)


def get_session():
    return Session()