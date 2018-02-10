import sys
from urllib.parse import urlparse, parse_qs
import requests
import config_init_full_path
import save_token

configuration = config_init_full_path.config_init
for i in sys.argv:
    print(i)
url = urlparse(sys.argv[1])
"""print(url.scheme)
print(url.netloc)
print(url.path)
print(url.params)
print(parse_qs(url.query))"""
""" по окончанию авторизации браузер получает редирект
    от сервера ССР в это приложение, получив URL 
    парсим его до кода авторизации
    """
code = parse_qs(url.query)["code"]
r = requests.post(configuration.get("verify_authorization_code_url"),
                  auth=(
                      configuration.get("ClientID"),
                      configuration.get("SecretKey")
                  ),
                  data={"grant_type": "authorization_code",
                        "code": code}
                  )
print(r.status_code)
print(r.text)
token_from_redirect = r.json()
authorization = token_from_redirect["token_type"] + " " + token_from_redirect["access_token"]
""" проверяем полученный токен и получаем идентефикатор перса"""
url = configuration.get("obtaining_character_id_url")
headers = {"user-agent": "test_esi_api",
           "authorization": authorization,
           "host": "login.eveonline.com"
           }
r = requests.get(url, headers=headers)
print("char id ")
print(r.status_code)
print(r.text)
character_id = r.json()
dir(character_id)
print(character_id["CharacterID"])
input("press enter to continue")
save_token.save(character_id["CharacterID"], character_id["CharacterName"],
                token_from_redirect)

print(sys.version)

input("press enter to continue")


