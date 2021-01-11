import json


class Progression(object):

    def __init__(self):
        self.chapter = 0
        self.action = (0, 0)

    def get_current_chapter(self):
        return self.chapter

    def get_current_action(self):
        return self.action[1]

    def set_current_action(self, action):
        self.action = action

    def set_current_chapter(self, chapter):
        self.chapter = chapter


progression = Progression()


def get_progression():
    return progression


def load_progression() -> Progression:
    global progression
    progression = json.load(open('./resources/saves.json'))
    return progression


def save_progression():
    with open('./resources/saves.json', 'w') as outfile:
        json.dump(progression, outfile, indent=4)
