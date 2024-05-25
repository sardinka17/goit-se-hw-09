from mongoengine import Document, StringField, ReferenceField, ListField, CASCADE


class Author(Document):
    name = StringField(required=True, unique=True)
    born_date = StringField(max_length=50)
    born_location = StringField(max_length=100)
    description = StringField()
    meta = {'collection': 'authors'}


class Quote(Document):
    author = ReferenceField(Author, reverse_delete_rule=CASCADE)
    tags = ListField(StringField(max_length=100))
    quote = StringField()
    meta = {'collection': 'quotes'}
