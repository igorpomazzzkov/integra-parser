import psycopg2

local = {
    'host': 'localhost',
    'db': 'integra',
    'username': 'postgres',
    'password': '12345'
}

dev = {
    'host': '10.10.11.30',
    'db': 'postgres',
    'username': 'postgres',
    'password': 'pg2020inteGra!#'
}

prod = {
    'host': '95.216.225.187',
    'db': 'postgres',
    'username': 'postgres',
    'password': 'pg2020inteGra!#'
}

database = local

connection = psycopg2.connect(host=database['host'], database=database['db'], user=database['username'],
                              password=database['password'])
from psycopg2 import errors




def get_brands_article_with_tecdoc_id():
    cursor = connection.cursor()
    cursor.execute(
        """SELECT id, brand, tecdoc_id FROM brands_article WHERE tecdoc_id IS NOT NULL AND ID NOT IN(1, 2, 3, 4) ORDER BY brand""")
    result = cursor.fetchall()
    cursor.close()
    connection.commit()
    return result


def save_motor_id(brand_id, motor_id):
    UniqueViolation = errors.lookup('23505')
    cursor = connection.cursor()
    connection.autocommit = True
    try:
        cursor.execute("""INSERT INTO tecdoc_motor_ids(brand_id, motor_id) VALUES(%s, %s)""", [brand_id, motor_id])
    except UniqueViolation:
        print(brand_id, motor_id, 'NOT INSERTED')
    finally:
        if cursor is not None:
            cursor.close()
