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
    
    rows = cur.fetchall() 
    for r in rows:
        print(f"firstname {r[0]} lastsname {r[1]}")
    
    cur.close()
    
    # Load the data
    data = pd.read_sql(sql_command, conn)

    print(data.shape)
    return (data)
#close the connection
con.close()
