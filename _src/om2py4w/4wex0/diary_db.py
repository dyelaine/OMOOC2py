import sqlite3
con = sqlite3.connect('diary.db')
con.execute("CREATE TABLE diary (id INTEGER PRIMARY KEY, time char(100) NOT NULL, content char(100) NOT NULL)")
con.execute("INSERT INTO diary (time, content) VALUES ('15/11/03', 'I bought a new bike')")
con.execute("INSERT INTO diary (time, content) VALUES ('15/11/04','Nice day!')")
con.execute("INSERT INTO diary (time, content) VALUES ('15/11/05','love coding~')")
con.commit()
