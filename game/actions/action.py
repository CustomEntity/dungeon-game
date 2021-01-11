from pykson import JsonObject, StringField


class Action(JsonObject):

    type = StringField()
    content = StringField()

    def __init__(self, type, content):
        super(Action, self).__init__()
        self.type = type
        self.content = content