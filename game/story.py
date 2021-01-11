from pykson import JsonObject, ObjectListField

from game.chapter import Chapter


class Story(JsonObject):

    chapters = ObjectListField(Chapter)

    def __init__(self, chapters):
        super(Story, self).__init__()
        self.chapters = chapters
