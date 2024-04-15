"""
Criar de duas tabelas relacionadas, Produto e Fornecedor, utilizando SQLAlchemy. Cada produto terá um fornecedor associado, 
demonstrando o uso de chaves estrangeiras para estabelecer relações entre tabelas. Além disso, você realizará inserções nessas tabelas 
para praticar a manipulação de dados.
"""

from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Fornecedor(Base):
    """
    Class representing a supplier in the database.

    Attributes:
        __tablename__ (str): The name of the table in the database.
        id (int): The primary key of the supplier.
        name (str): The name of the supplier.
        telefone (str): The phone number of the supplier.
        email (str): The email address of the supplier.
        endereco (str): The address of the supplier.

    """

    __tablename__ = "fornecedores"
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    telefone = Column(String(20))
    email = Column(String(50))
    endereco = Column(String(100))


class Produto(Base):
    """
    Class representing a product in the database.

    Attributes:
        __tablename__ (str): The name of the table in the database.
        id (int): The primary key of the product.
        name (str): The name of the product.
        preco (float): The price of the product.
        fornecedor_id (int): The foreign key of the supplier.

    """

    __tablename__ = "produtos"
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    descricao = Column(String(200))
    preco = Column(Integer, nullable=False)
    fornecedor_id = Column(Integer, ForeignKey("fornecedores.id"), nullable=False)

    fornecedor = relationship("Fornecedor", backref="produtos")


def create_tables(engine):
    """
    Create the tables in the database.

    Args:
        engine (sqlalchemy.engine.Engine): The engine to connect to the database.

    """
    Base.metadata.create_all(engine)
