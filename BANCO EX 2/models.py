from sqlalchemy import create_engine, Column, Integer, String, Float, select
from sqlalchemy.orm import scoped_session, declarative_base, sessionmaker

engine = create_engine('sqlite:///base_flet')
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()


class Livro(Base):
    __tablename__ = 'Livro'
    id = Column(Integer, primary_key=True)
    titulo = Column(String, nullable=False, index=True)
    autor = Column(String, nullable=False, index=True)
    descricao = Column(String, nullable=False, index=True)
    categoria = Column(String, nullable=False, index=True)

    def __repr__(self):
        return '<Livro: {} {} {} {}'.format(self.id, self.titulo, self.autor, self.descricao)


    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def seralize_livro(self):
        dados_livro = {
            'id_livro': self.id,
            'titulo': self.titulo,
            'autor': self.autor,
            'descricao': self.descricao,
            'categoria': self.categoria,
        }
        return dados_livro




def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_db()