import requests

url = input('Give JSON url:')
res = requests.get(url)
if res.status_code == 200:
    [print(i) for i in list(dict(res.json().get('paths')).keys())]
else:
    print('URL is wrong')