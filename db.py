from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id= Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    tel = Column(String)

    def __repr__(self):
        return "<User(name='%s', email='%s', tel='%s')>" % (self.name, self.email, self.tel)


engine = create_engine('sqlite:///bd.db', echo= True)

User.__table__
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

def new_user(name,email,tel):
    ej_user = User(name = name, email = email, tel=tel)
    session.add(ej_user)
    session.commit()

def allUsers():
    return session.query(User).all()

def delete_user(id):
    user= session.query(User).filter_by(id=id).all()[0]
    session.delete(user)
    session.commit()

def update_user(id,name,email,tel):
    user = session.query(User).filter_by(id=id).all()[0]
    user.name = name
    user.email = email
    user.tel = tel
    session.commit()




