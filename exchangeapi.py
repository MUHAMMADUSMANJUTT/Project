import requests
to = str(input("INSERT TO"))
frm = str(input("INSERT FROM"))
ammount = int(input("INSERT AMMOUNT"))

url = "https://api.apilayer.com/exchangerates_data/convert?to=to&from=frm&amount=amount"

payload = {}
headers = {
    "apikey": "1ZQ2Z97ilYgyw6vR5QIYDDaXb2CkK7xi"
}

response = requests.request("GET", url, headers=headers, data=payload)

status_code = response.status_code
result = response.text
print(result)
