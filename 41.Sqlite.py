import sqlite3
con=sqlite3.connect("sqlite.db")#creat database
con.execute('''
create table student(
    st_id INT AUTO_INCREMENT PRIMARY KEY,
    st_name VARCHAR(50),
    st_class VARCHAR(20),
    st_mail VARCHAR(30)
    
    
    )
    ''')
con.close()