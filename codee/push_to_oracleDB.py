import cx_Oracle


con = cx_Oracle.connect('pythonhol/welcome@127.0.0.1/orcl')
rows = [ (1, "First" ),
         (2, "Second" ),
         (3, "Third" ),
         (4, "Fourth" ),
         (5, "Fifth" ),
         (6, "Sixth" ),
         (7, "Seventh" ) ]
         
cur = con.cursor()
cur.bindarraysize = 7
cur.setinputsizes(int, 20)
cur.executemany("insert into mytab(id, data) values (:1, :2)", rows)
con.commit()