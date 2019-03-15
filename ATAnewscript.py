import psycopg2

#connect to db
con = psycopg2.connect(
PGHOST ='localhost',
PGDATABASE ='ATAtestdb',
PGUSER ='postgres',
PGPASSWORD ='L!oness8')

print("Connected!")


# Create a cursor object
cur = con.cursor()


def load_data(schema, table):
#execute query
    cur.execute ( "SELECT firstname, lastsname FROM People.staff")
    print("I met some nice people at ATA.  They are:")
    rows = cur.fetchall() 
    for r in rows:
        print(row[0], r[1])
    
    con.commit
      
  
#close the connection
con.close()
