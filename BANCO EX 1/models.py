from sqlalchemy import create_engine, Column, Integer, String, Float, select
from sqlalchemy.orm import scoped_session, declarative_base, sessionmaker

engine = create_engine('sqlite:///base_flet_usuario')
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()


class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    profissao = Column(String, nullable=False)
    salario = Column(Float, nullable=False)

    def __repr__(self):
        return '<Usuario: {} {} {} {}'.format (self.nome, self.id, self.salario, self.salario)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize_usuario(self):
        dados_usuario = {
            'id': self.id,
            'nome': self.nome,
            'profissao': self.profissao,
            'salario': self.salario,
        }
        return dados_usuario


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_db()