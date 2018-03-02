import xlrd
import MySQLdb
import time


db = MySQLdb.connect(host="localhost",  # your host, usually localhost
                         user="root",  # your username
                         passwd="secret",  # your password
                         db="abhivasu")  # name of the data base
cur = db.cursor()
db.autocommit(True)
cur.execute("delete from sensors;")
def open_file(path):

    book = xlrd.open_workbook(path)

    # print number of sheets
    #print(book.nsheets)

    # print sheet names
    #print(book.sheet_names())

    # get the first worksheet
    sheet = book.sheet_by_index(0)


    query = ("""insert into sensors values(%s, %s)""")

    for r in range(1, sheet.nrows):
        t = sheet.cell(r,0 ).value
        valu = sheet.cell(r, 1).value
        values = (t,valu)
        cur.execute(query, values)
        db.commit()
        time.sleep(6.0 / 1000.0)


path = "C:\\Users\\pc\\Desktop\\a.xlsx"
open_file(path)

cur.close()
db.commit()
db.close()