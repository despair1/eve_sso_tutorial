import models


def save(character_id, character_name, token):
    try:
        t_token = models.Tokens.get(models.Tokens.CharacterID == character_id)
        t_token.CharacterName = character_name
        t_token.access_token = token["access_token"]
        t_token.refresh_token = token["refresh_token"]
    except models.Tokens.DoesNotExist:
        t_token = models.Tokens.create(CharacterID=character_id, CharacterName=character_name,
                                       access_token=token["access_token"],
                                       refresh_token=token["refresh_token"]
                                       )
    t_token.save()
