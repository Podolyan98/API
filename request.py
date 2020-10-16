import requests
from loguru import logger


url = 'https://auth-api.rabota.ua/Login'
payload = {'username': 'email',
           'password': 'password'}
headers = {'accept': 'text/plain',
           'Accept': 'application/json'}

response = requests.post(url, data = payload, headers = headers)
logger.debug(response)

token = 'Bearer %s' % response.text.replace('"', '')
logger.debug('Token received')
logger.debug(token)

url = 'https://employer-api.rabota.ua/apply/list'
payload = {'vacancyId': 0, 
           'folderId': 1,
           'page': 2,
           'Authorization': token}
headers = {'accept': 'text/plain',
           'Content-Type': 'application/json'}

response = requests.post(url, data = payload, headers = headers)
logger.debug(response)
logger.debug(response.text)
