from database.connection import connection
import database.query as q

def get_article_id_by_name(article: str):
    cursor = connection.cursor()
    cursor.execute(q.select_article_id_by_name, [article])
    result = cursor.fetchone()
    cursor.close()
    connection.commit()
    if result is not None:
        return result[0]


def set_ozon_id_to_article(ozon_id: int, article: str):
    cursor = connection.cursor()
    cursor.execute(q.set_ozon_id_to_article, [ozon_id, article])
    cursor.close()
    connection.commit()


def set_is_ozon_to_article(article: str):
    cursor = connection.cursor()
    cursor.execute(q.set_is_ozon_to_article, [article])
    cursor.close()
    connection.commit()


def get_brand_id_by_name(brand: str):
    cursor = connection.cursor()
    cursor.execute(q.select_brand_id_by_name, [brand])
    result = cursor.fetchone()
    cursor.close()
    connection.commit()
    if result is not None:
        return result[0]


def set_focus_crosses_by_brand_id_ana_brand(brand_id: str, brand: str):
    cursor = connection.cursor()
    cursor.execute(q.set_focus_crosses_by_brand_id, [brand_id, brand])
    cursor.close()
    connection.commit()


def add_cross(cid, article_id, brand_art, brand, brand_id, direction, normalized_article):
    cursor = connection.cursor()
    cursor.execute(q.insert_cross_articles,
                   [cid, article_id, brand_art, brand, brand_id, direction, normalized_article])
    cursor.close()
    connection.commit()


def get_cross(brand_art):
    cursor = connection.cursor()
    cursor.execute(q.select_cross,
                   [brand_art])
    result = cursor.fetchone()
    cursor.close()
    connection.commit()
    if result is not None:
        return result[0]

def get_cross(brand_art_norm, brand):
    cursor = connection.cursor()
    cursor.execute(q.select_normal_cross,
                   [brand_art_norm, brand])
    result = cursor.fetchall()
    cursor.close()
    connection.commit()
    return result
