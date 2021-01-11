from pykson import JsonObject


class Chapter(JsonObject):
   # name = StringField()

    def __init__(self, name):
        super(Chapter, self).__init__()
        self.name = name
