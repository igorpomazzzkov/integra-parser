import queries as q
from database import connection


def get_crosses_oe():
    cursor = connection.cursor()
    cursor.execute(q.select_crosses)
    result = cursor.fetchall()
    cursor.close()
    connection.commit()
    if result is not None:
        return result


def save_cross_exception(cross_id, response_code):
    cursor = connection.cursor()
    cursor.execute(q.insert_cross_laximo_not_found, [cross_id, response_code])
    cursor.close()
    connection.commit()
