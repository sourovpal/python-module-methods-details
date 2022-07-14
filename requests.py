import requests

res = requests.get('https://jsonplaceholder.typicode.com/todos')

res.status_code
res.json() 

res.headers['content-type'] = ?

res.encoding = ?

res.text
