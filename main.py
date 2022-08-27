
import sqlalchemy
from sqlalchemy.orm import sessionmaker

from Homework06 import create_tables, Publisher, Book, Shop, Stock, Sale, login, DB_name, password

DNS = f'postgresql://{login}:{password}@localhost:5432/{DB_name}'
engine = sqlalchemy.create_engine(DNS)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

pub1 = Publisher(name='Anton')
pub2 = Publisher(name='Vladimir')
pub3 = Publisher(name='Nina')
session.add_all([pub1, pub2, pub3])
session.commit()
for c in session.query(Publisher).all():
    print(c)

bu1 = Book(title='My Adventury', publisher=pub1)
bu2 = Book(title='His Adventury', publisher=pub2)
bu3 = Book(title='Her Adventury', publisher=pub3)
session.add_all([bu1, bu2, bu3])
session.commit()
for c in session.query(Book).all():
    print(c)

sh1 = Shop(name='Book world')
sh2 = Shop(name='Book store')
session.add_all([sh1, sh2])
session.commit()
for c in session.query(Shop).all():
    print(c)

st1 = Stock(book=bu1, shop=sh2, count=3)
st2 = Stock(book=bu1, shop=sh1, count=2)
st3 = Stock(book=bu2, shop=sh2, count=4)
st4 = Stock(book=bu2, shop=sh1, count=1)
st5 = Stock(book=bu3, shop=sh1, count=5)
session.add_all([st1, st2, st3, st4, st5])
session.commit()
for c in session.query(Stock).all():
    print(c)

sl1 = Sale(price=150, date_sale='2022-03-01', stock=st1, sale_count=2)
sl2 = Sale(price=170, date_sale='2022-04-05', stock=st2, sale_count=3)
sl3 = Sale(price=340, date_sale='2022-05-09', stock=st3, sale_count=1)
sl4 = Sale(price=380, date_sale='2022-06-12', stock=st4, sale_count=4)
session.add_all([sl1, sl2, sl3, sl4])
session.commit()
for c in session.query(Sale).all():
    print(c)


def get_shop(d='None'):
    for c in session.query(Shop).join(Stock.shop).join(Stock.book).join(Book.publisher).filter(Publisher.name == f'{d}'):
        print('Книги можете найти в', c)

get_shop(d='Nina')

def get_publisher():
    while True:
        command = input('Введите id издателя: ')
        if id == 1:
            print(session.query(Publisher).filter(Publisher.id == f'{id}'))
        if id == 2:
            print(session.query(Publisher).filter(Publisher.id == f'{id}'))
        if id == 3:
            print(session.query(Publisher).filter(Publisher.id == f'{id}'))
        else:
            break

get_publisher()

session.close()
