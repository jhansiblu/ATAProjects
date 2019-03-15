pip install psycopg2-binary

#connect to db
con = psycopg2.connect(
host ='localhost',
database ='ATAtestdb',
user ='postgres',
password ='L!oness8')

print("I met some nice people at ATA. They are:")


# Create a cursor object
cur = con.cursor()


def load_data(schema, table):
#execute query
    cur.execute ( "select firstname, lastsname FROM staff")
    rows = cur.fetchall() 
    for r in rows:
        print(row[0], r[1])
    
    con.commit
      
  
#close the connection
con.close()
