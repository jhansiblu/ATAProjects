import psycopg2

#connect to db
con = psycopg2.connect(
host ='35.174.168.138',
database ='ATAtestdb',
user ='postgres',
password ='L!oness8')

print("I met some nice people at ATA. They are:")

# Create a cursor object
cur = con.cursor()

#execute query
cur.execute(""" SELECT firstname, lastsname FROM "People"."staff" ORDER BY lastsname; """)

rows = cur.fetchall() 

for r in rows:
    print(r[0], r[1])
    
cur.close()
      
  
#close the connection
con.close()
