import datetime
import mongoengine


class Owner(mongoengine.Document):
    registered_date = mongoengine.DateTimeField(default=datetime.datetime.now)
    name = mongoengine.StringField(required=True)
    email = mongoengine.StringField(required=True)

    snake_ids = mongoengine.ListField()  # Store list of ID's
    cage_ids = mongoengine.ListField()  # Store a list of cage ID's

    #  Database connection to use
    meta = {
        'db_alias': 'core',
        'collection': 'owners'
    }
