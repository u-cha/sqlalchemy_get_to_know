from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, DateTime, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

DeclarativeBase = declarative_base()


class Post(DeclarativeBase):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    name = Column('name', String)
    url = Column('url', String)

    def __repr__(self):
        return ' '.join((str(self.id), self.name, self.url))


class Currency(DeclarativeBase):
    __tablename__ = 'currencies'
    id = Column(Integer, primary_key=True)
    code = Column('code', VARCHAR)

    def __repr__(self):
        return ' '.join((str(self.id), self.code))


def main():
    # Создаем объект Engine, который будет использоваться объектами ниже для связи с БД
    engine = create_engine('postgresql+psycopg2://postgres:admin@localhost:5432/postgres')

    # Метод create_all создает таблицы в БД , определенные с помощью  DeclarativeBase, если они не существуют
    # DeclarativeBase.metadata.create_all(engine)

    # Создаем фабрику для создания экземпляров session_factory. При создании фабрики в аргументе
    # bind передаем объект engine
    session_factory = sessionmaker(bind=engine)

    # Создаем объект сессии из вышесозданной фабрики Session
    session = session_factory()

    # Создаем новую запись.
    # new_post = Post(name='Two record', url="http://testsite.ru/first_record")

    # # Добавляем запись
    # session.add(new_post)
    #
    # # Благодаря этой строчке мы добавляем данные а таблицу
    # session.commit()
    # session.add(Currency(id=32, code='USD'))
    # session.commit()

    # А теперь попробуем вывести все посты , которые есть в нашей таблице
    for currency in session.query(Currency):
        print(currency)


if __name__ == "__main__":
    main()
