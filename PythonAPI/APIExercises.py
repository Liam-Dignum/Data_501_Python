import requests
from requests.auth import HTTPBasicAuth

#r =requests.get('https://eodx8a2l1yg4ioo.m.pipedream.net')
'''
r =requests.get('https://reqres.in/api/users/2')
print(r.text)
jsonData = r.json()
print(jsonData['data']['first_name'])
'''

#r =requests.get('https://eodx8a2l1yg4ioo.m.pipedream.net?key1=value1&key2=value2')
#payload = {'first' : 'one', 'second' : 'two'}
#r =requests.get('https://eodx8a2l1yg4ioo.m.pipedream.net', params=payload)
#headers = {'myToken' : 'j2134hj21he3bjdbnxj1231sxa'}
#r =requests.get('https://eodx8a2l1yg4ioo.m.pipedream.net', headers=headers)


'''
r = requests.post('https://eodx8a2l1yg4ioo.m.pipedream.net')
r = requests.delete('https://eodx8a2l1yg4ioo.m.pipedream.net')
r= requests.put('https://eodx8a2l1yg4ioo.m.pipedream.net')
r= requests.patch('https://eodx8a2l1yg4ioo.m.pipedream.net')
'''
'''
payload = {'name' : 'Liam', 'job' : 'Data_Engineer' }
r= requests.post('https://reqres.in/api/users', json=payload)

print(r.text)
'''
'''
payload = {'name':'Liam','location':'Manchester'}
r = requests.post('https://eodx8a2l1yg4ioo.m.pipedream.net', data=payload)
r= requests.post('https://httpbin.org/post',data=payload)
print(r.text)
'''
'''
r = requests.get('https://httpbin.org/image/jpeg')
print(r.headers)
with open('image.jpg','wb') as f:
    for chunk in r.iter_content(chunk_size=500):
        f.write(chunk)
'''
'''
r = requests.get('https://httpbin.org/status/500')

try:
    r.raise_for_status()
except requests.exceptions.HTTPError:
    print('ERROR')

print(r)
'''

'''
try:
    r = requests.get('https://dasdasdasfasfdasdsa')
except requests.exceptions.ConnectionError:
    print('Connection Error')
'''
'''
try:
    r = requests.get('https://httpbin.org/delay/10',timeout=5)
except requests.exceptions.Timeout:
    print('Timeout')
'''


'''
r = requests.get('https://httpbin.org/basic-auth/user/password',auth=HTTPBasicAuth('user','password'))
print(r)
'''
base_url = 'https://restcountries.com/v3.1/'
r = requests.get(base_url+'all?fields=name,region,capital')
print(r.text)
json_resp = r.json()
print(json_resp[0])