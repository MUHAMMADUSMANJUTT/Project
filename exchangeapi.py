import psycopg2
from datetime import date
from turtle import rt
import requests
import re
"""to = str(input("INSERT TO"))
frm = str(input("INSERT FROM"))
ammount = int(input("INSERT AMMOUNT"))"""

url = "https://api.apilayer.com/exchangerates_data/convert?to=PKR&from=USD&amount=4000"

payload = {}
headers = {
    "apikey": "1ZQ2Z97ilYgyw6vR5QIYDDaXb2CkK7xi"
}

response = requests.request("GET", url, headers=headers, data=payload)

status_code = response.status_code
result = response.text
print(result)

# Extracting data from result

a = '"from": '
frm = result[result.find(a)+len(a):].split()[0]
print(frm)

a = '"to": '
to = result[result.find(a)+len(a):].split()[0]
print(to)

a = '"amount": '
amm = result[result.find(a)+len(a):].split()[0]
print(amm)

a = '"rate": '
rate = result[result.find(a)+len(a):].split()[0]
print(rate)

a = '"date": '
dat = result[result.find(a)+len(a):].split()[0]
print(dat)

a = '"result": '
rs = result[result.find(a)+len(a):].split()[0]
print(rs)


con = psycopg2.connect(
    host="localhost",
    database="exchangerates",
    user="postgres",
    password="pA6@AKbD")

# cursor
cur = con.cursor()

cur.execute("insert into excgangerate (from, to, ammount, rt, dt, result) values (%s, %s, %s, %s, %s, %s)",
            (frm, to, amm, rate, dat, rs))

# execute query
cur.execute("select from, to, ammount, rt, dt, result")

rows = cur.fetchall()

for r in rows:
    print(f"from {r[0]}  to {r[1]}  ammount {r[2]  rt {r[3]} dt {r[4]}} result {r[5]}")

# commit the transcation
con.commit()

# close the cursor
cur.close()

# close the connection
con.close()
