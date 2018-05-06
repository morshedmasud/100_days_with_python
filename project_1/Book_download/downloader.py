import requests
import sys

base_url = "http://subeen.com/download/"
info_dic = {"name": "Masud", "email": "masudraj6@gmail.com", "country": "Bangladesh"}
url = base_url + "process.php"
response = requests.post(url, data=info_dic)

if response.ok is False:
    sys.exit("Error downloading the file")

with open("Book_download/cpbook.pdf", 'wb') as f:
    f.write(response.content)

print("Book download complete!")