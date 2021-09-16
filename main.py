import re

import xlrd

from database.article import get_cross, get_article_id_by_name, add_cross

book = xlrd.open_workbook("./files/trialli.xlsx")
sheet = book.sheet_by_name("list")

cid = '54ad9a693070426b9aebe23d26ff0b39'
brand_trialli = 3005


def normalized_article(article: str) -> str:
    return re.sub("[^a-zA-Z\d]", "", article)


for row in range(20651, sheet.nrows):
    article = sheet.cell(row, 0).value
    article_id = get_article_id_by_name(article)
    cross = sheet.cell(row, 1).value
    if article_id is not None:
        add_cross(cid, article_id, cross, 'TRIALLI', brand_trialli, 'CM', normalized_article(article))
        print(row.real, article, article_id, cross)


