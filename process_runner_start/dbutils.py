import os
import sqlite3
from exceptions import FileDBError as DBerr

query = "SELECT * FROM fileassociations WHERE fn1 = ? OR fn2 = ? OR fn3 = ? OR fn4 = ? OR fn5 = ? OR fn6 = ? OR fn7 = ? OR fn8 = ?"

def __checkDB__():
    # db checks
    if not os.path.isfile(dbpath):
        raise DBerr("missing dbfile")
    else:
        # check to make sure it is a db
        con = sqlite3.connect(dbpath)
        cur = con.cursor()
        try:
            cur.execute("PRAGMA integrety_check")
        except sqlite3.DatabaseError:
            raise DBerr("dbfile init error")

# CREATE TABLE fileassociations(languageName text primary key, filenames int, fn1 text, fn2 text, fn3 text, fn4 text, fn5 text, fn6 text, fn7 text, fn8 text)s
def findEntry(fileOrExt: str):
    # connect to db
    con = sqlite3.connect("fileassociations.db")
    cur = con.cursor()

    # find the file through the worst means ever lol
    result = cur.execute(query,fileOrExt)

    # close the db
    cur.close()
    # con.commit()
    con.close()
    return result