import sys
from urllib.parse import urlparse, parse_qs
import requests
import config_init_full_path

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


print(sys.version)

input("press enter to continue")


