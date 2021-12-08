import database.query as q
from database.connection import connection


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


def delete_by_brand_name_and_oe_cross(brand: str, oe: str):
    cursor = connection.cursor()
    cursor.execute("""DELETE FROM cross_articles WHERE UPPER(brand) = UPPER(%s) AND normalized_article = %s""",
                   [brand, oe])
    cursor.close()
    connection.commit()


def find_brand_by_name(brand: str):
    cursor = connection.cursor()
    cursor.execute("""SELECT id FROM brands_article WHERE UPPER(brand) = UPPER(%s)""",
                   [brand])
    result = cursor.fetchall()
    cursor.close()
    connection.commit()
    return result


def add_mask_to_crosses(brand_id, count):
    cursor = connection.cursor()
    cursor.execute("""INSERT INTO cross_masks(brand_id, count) VALUES(%s, %s) RETURNING ID""",
                   [brand_id, count])
    result = cursor.fetchone()
    cursor.close()
    connection.commit()
    return result


def add_mask_regex_to_crosses(mask_id, number, regex):
    cursor = connection.cursor()
    cursor.execute("""INSERT INTO cross_masks_regex(mask_id, number, regex) VALUES(%s, %s, %s)""",
                   [mask_id, number, regex])
    cursor.close()
    connection.commit()


def get_oe_laximo_replacement_and_part_of_the_whole():
    cursor = connection.cursor()
    cursor.execute(
        """SELECT aa.article_id, aa.article, cl.brand, cl.brand_art, cl.brand_id, cl.cross_id FROM cross_articles ca INNER JOIN check_masks cm on ca.id = cm.cross_id INNER JOIN cross_laximo cl on ca.id = cl.cross_id INNER JOIN art_articles aa on ca.article_id = aa.article_id WHERE ca.direction = 'OE' AND (cl.type = 'REPLACEMENT' OR cl.type = 'PARTOFTHEWHOLE') AND cl.brand != 'FENOX'""")
    result = cursor.fetchall()
    cursor.close()
    connection.commit()
    return result


def get_masks_by_brand_count(brand_id: int, count: int):
    cursor = connection.cursor()
    cursor.execute(
        """SELECT number, regex FROM cross_masks_regex cmr INNER JOIN cross_masks cm ON cm.id = cmr.mask_id WHERE cm.brand_id = %s AND cm.count = %s""",
        [brand_id, count])
    result = cursor.fetchall()
    cursor.close()
    connection.commit()
    return result


def save_none_masks_cross(article, article_id, brand, brand_art, status, cross_id):
    cursor = connection.cursor()
    cursor.execute(
        """INSERT INTO check_masks(article, article_id, brand, brand_article, status, cross_id) VALUES(%s, %s, %s, %s, %s, %s)""",
        [article, article_id, brand, brand_art, status, cross_id])
    cursor.close()
    connection.commit()


def update_article_integra(article, name, applic, comment):
    cursor = connection.cursor()
    cursor.execute(
        """UPDATE art_articles SET name = %s AND comment_applic = %s AND comment_second = %s WHERE article = %s""",
        [name, applic, comment, name])
    cursor.close()
    connection.commit()
