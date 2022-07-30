import requests
url = "https://note.nkmk.me/python-requests-usage/"
res = requests.get(url)
print(res.text)