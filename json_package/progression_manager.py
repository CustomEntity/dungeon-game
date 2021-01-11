import json

import pykson
from pykson import JsonObject, IntegerField, ListField


class Progression(JsonObject):
    chapter = IntegerField()
    action = ListField(int)

    def __init__(self):
        super(Progression, self).__init__()
        self.previous_action = [0, 0]
        self.action = [0, 0]

    def get_previous_action(self):
        return self.action

    def get_current_action(self):
        return self.action

    def set_current_action(self, action):
        self.set_previous_action(self.get_current_action())
        self.action = action

    def set_previous_action(self, action):
        self.action = action


progression = Progression()


def get_progression():
    return progression


def load_progression() -> Progression:
    global progression
    story = pykson.Pykson().from_json(json.load(open('./resources/saves.json')), Progression)
    return story


def save_progression():
    with open('./resources/saves.json', 'w') as outfile:
        pykson.Pykson().to_json_file(progression, outfile)
