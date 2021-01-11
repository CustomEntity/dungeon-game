from pykson import JsonObject, StringField, ObjectListField

from game.actions.action import Action


class Chapter(JsonObject):

    name = StringField()
    actions = ObjectListField(Action)

    def __init__(self, name, actions):
        super(Chapter, self).__init__()
        self.name = name
        self.actions = actions



