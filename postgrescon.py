import psycopg2

con = psycopg2.connect(
    host="localhost",
    database="supplier",
    user="postgres",
    password="pA6@AKbD")

# cursor
cur = con.cursor()

cur.execute("insert into employees (id, name) values (%s, %s)",
            ("2", "saleem"))

# execute query
cur.execute("select id, name from employees")

rows = cur.fetchall()

for r in rows:
    print(f"id {r[0]} name {r[1]}")

# commit the transcation
con.commit()

# close the cursor
cur.close()

# close the connection
con.close()
