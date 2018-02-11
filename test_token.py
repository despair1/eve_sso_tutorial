import models
import requests
import peewee


def test_token(character_id):
    t = models.Tokens.get(CharacterID=character_id)
    url = "https://esi.tech.ccp.is/latest/characters/%s/wallet/journal/" % character_id
    params = dict()
    params["datasource"] = "tranquility"
    params["token"] = t.access_token
    r = requests.get(url, params=params)
    print("response status code ", r.status_code)
    print("response text: ", r.text)


for i in models.Tokens.select():
    test_token(i.CharacterID)



