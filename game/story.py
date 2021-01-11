from pykson import JsonObject


class Story(JsonObject):
    # actions = ObjectListField(Action)

    def __init__(self, actions):
        super(Story, self).__init__()
        self.actions = actions
