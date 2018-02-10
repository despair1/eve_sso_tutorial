import peewee
import config_init_full_path
configuration = config_init_full_path.config_init
db = peewee.SqliteDatabase(configuration.get("oauth_database_path"))


class Tokens(peewee.Model):
    CharacterID = peewee.BigIntegerField(unique=True)
    CharacterName = peewee.CharField()
    access_token = peewee.CharField()
    refresh_token = peewee.CharField()

    class Meta:
        database = db


db.connect()
db.create_tables([Tokens, ])
