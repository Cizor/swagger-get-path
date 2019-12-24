import requests

url = input('Give N url:')
res = requests.get(url)
if res.status_code == 200:
    [print(i) for i in list(dict(res.json().get('paths')).keys())]
else:
    print('Everhing is wrong')

