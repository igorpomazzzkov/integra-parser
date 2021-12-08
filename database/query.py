select_article_id_by_name = """SELECT article_id FROM art_articles WHERE article = %s"""
set_ozon_id_to_article = """UPDATE art_articles SET ozon_id = %s WHERE article = %s"""
set_is_ozon_to_article = """UPDATE art_articles SET is_ozon = true WHERE article = %s"""

select_brand_id_by_name = """SELECT id FROM brands_article WHERE UPPER(brand) = %s"""
set_focus_crosses_by_brand_id = """UPDATE brands_article SET focus = true WHERE id = %s AND brand = %s"""

select_cross = """SELECT article_id FROM cross_articles WHERE brand_art = %s"""

select_normal_cross = """SELECT id, article_id, brand_art, brand FROM cross_articles WHERE direction = 'OE' AND normalized_article = %s and UPPER(brand) LIKE UPPER(%s)"""

insert_cross_articles = """INSERT INTO cross_articles(cid, article_id, brand_art, brand, brand_id, direction, edit_user, edit_date, focus, normalized_article, supplier) VALUES(%s, %s, %s, %s, %s, %s, 'admin@fenox', NOW(), false, %s, 0)"""
