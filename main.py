import re

import xlrd

from database.article import get_oe_laximo_replacement_and_part_of_the_whole, get_masks_by_brand_count, save_none_masks_cross


book = xlrd.open_workbook("./files/update-integra.xlsx")
sheet = book.sheet_by_name("list")
cid = '54ad9a693070426b9aebe23d26ff0b39'


def normalized_article(article: str) -> str:
    return re.sub("[^a-zA-Z\d]", "", article)


for row in range(1, sheet.nrows):
    article = str(sheet.cell(row, 0).value).strip()
    pg = str(sheet.cell(row, 1).value).strip()
    name = str(sheet.cell(row, 2).value).strip()
    applic = str(sheet.cell(row, 3).value).strip()
    comment = str(sheet.cell(row, 4).value).strip()
    print(article, pg, name, applic, comment)

# for cross in get_oe_laximo_replacement_and_part_of_the_whole():
#     article_id = cross[0]
#     article = cross[1]
#     brand = cross[2]
#     brand_art = str(cross[3]).strip()
#     brand_id = cross[4]
#     cross_id = cross[5]
#     masks = get_masks_by_brand_count(brand_id, len(brand_art))
#     for mask in masks:
#         number = mask[0]
#         regex = mask[1]
#         char = brand_art[number - 1]
#         result = char in regex
#         if not result:
#             save_none_masks_cross(article, article_id, brand, brand_art, False, cross_id)
#             print(cross_id, article_id, brand, brand_art)
#             break

