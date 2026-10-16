
import pymysql

def connect_to_db():
    connection = pymysql.connect(
        host='localhost',
        port=1111,
        user='root',
        password='123456',
        database='book_keeping',
    )
    return connection