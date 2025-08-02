"""
[x] Tahap ke-1: menggunakan sistem paling dasar
[v] Tahap ke-2: tambahkan header => tidak perlu pakai selenium
"""
import requests

url = 'https://projects.co.id/public/browse_projects/listing'
headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": url
    }

respons = requests.get(url, headers=headers)
status = respons.status_code
if status == 200:
    print('masuk')
else:
    print('tidak masuk:', status)
content = respons.content
print(len(content))