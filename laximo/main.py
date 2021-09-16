from time import sleep
import xlrd

import requests

import article

def get_crosses_from_file() -> list:
    book = xlrd.open_workbook("../files/crosses_laximo_not_found.xlsx")
    sheet = book.sheet_by_name("list")
    crosses = []
    for row in range(1, sheet.nrows):
        cid = sheet.cell(row, 0).value
        article_id = str(sheet.cell(row, 1).value).replace('.0', '')
        brand = sheet.cell(row, 2).value
        brand_art = sheet.cell(row, 4).value
        id = str(sheet.cell(row, 9).value).replace('.0', '')
        cross = (id, cid, article_id, brand, brand_art)
        print(cross)
        crosses.append(cross)
    return crosses


def get_cross():
    count = 0
    file = open('error-crosses.txt', 'a')
    print('function starts')
    crosses = get_crosses_from_file()
    print(len(crosses))
    for cross in crosses:
        sleep(0.1)
        count += 1
        cid = cross[1]
        id = cross[0]
        brand_art = cross[4]
        brand = cross[3]
        data = {
            "functionName": "FindOEM",
            "params": {
                "Locale": "ru_RU",
                "Brand": brand,
                "OEM": brand_art
            },
            "replacementTypes": ["PartOfTheWhole", "Replacement", "Duplicate"],
            "options": ["crosses"],
            "hard": False
        }
        response = requests.post('https://integra.fenox.com/backend/laximo/' + cid + '/' + str(id), json=data, headers={
            'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMyIsImlhdCI6MTYzMTY5OTAwNSwiZXhwIjoxNjMyMTc5MDA1LCJyb2xlIjoiQURNSU4iLCJjb21wYW55IjoiRkVOT1giLCJ1c2VybmFtZSI6ImFkbWluIiwiY2lkIjoiNTRhZDlhNjkzMDcwNDI2YjlhZWJlMjNkMjZmZjBiMzkiLCJzdGF0dXMiOiJVTkJMT0NLRUQifQ.46cKJpU2YyL2Klqf3DhNfwEHJwnex4EtpNJLVmKuzCN3sKLOWQpUq605wdrLBkTR_DjUyKfg2RiX9epbfoJU_w',
        })
        if response.status_code != 200:
            file.write(str(id) + '\n')
        article.save_cross_exception(id, response.status_code)
        print(count, id, brand, brand_art, response.status_code)
    file.write("THE END")
    file.close()


if __name__ == '__main__':
    get_cross()
